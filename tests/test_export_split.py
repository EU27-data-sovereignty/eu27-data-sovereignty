#!/usr/bin/env python3
"""
The split edition the mobile reader ships (model/export_json.py --split, #110).

    python3 -m unittest discover -s tests -v

The 28 parts are a pure function of the committed single file, so they are generated and never tracked; what
is tracked is the manifest, which names the sha256 of every part and of the single file (the edition id).
These tests are the proof that makes that arrangement honest: the parts merge back to the single file byte
for byte, every part renders alone, the manifest on disk is the one the committed bundle produces, and the
site's copy of the manifest is the app's. No network, no model rebuild: everything is read from the tree.
"""
from __future__ import annotations

import hashlib
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "model"))

import document  # noqa: E402
import export_json as ej  # noqa: E402

SINGLE = ROOT / "web" / "public" / "data" / "eu27.json"
SINGLE_BYTES = SINGLE.read_bytes()
BUNDLE = json.loads(SINGLE_BYTES)
FILES = ej.split_bundle(BUNDLE)
PARTS = {name: json.loads(data) for name, data in FILES.items()}
MANIFEST = PARTS[ej.MANIFEST]
ISOS = sorted(BUNDLE["documents"])

# Every key of the TypeScript Bundle interface (web/src/data/types.ts), which a part may carry a subset of.
BUNDLE_KEYS = set(BUNDLE)


class RoundTrip(unittest.TestCase):
    def test_the_parts_merge_back_to_the_single_file_byte_for_byte(self):
        merged = ej.merge_parts(PARTS)
        self.assertEqual(merged, BUNDLE)
        self.assertEqual(ej.dumps(merged).encode("utf-8"), SINGLE_BYTES)

    def test_a_differing_duplicate_is_a_corrupt_edition_not_a_merge(self):
        parts = {name: json.loads(data) for name, data in FILES.items()}
        # Two parts carry the same shared source: change it in one of them.
        shared = next(s for s in parts["eu27.core.json"]["sources"]
                      if any(s in parts[f"eu27.{iso}.json"]["sources"] for iso in ISOS))
        parts["eu27.core.json"]["sources"][shared] = {**parts["eu27.core.json"]["sources"][shared], "title": "x"}
        with self.assertRaises(ValueError):
            ej.merge_parts(parts)


class Manifest(unittest.TestCase):
    def test_the_edition_id_is_the_single_file_s_sha256(self):
        self.assertEqual(MANIFEST["edition"], hashlib.sha256(SINGLE_BYTES).hexdigest())
        self.assertEqual(MANIFEST["schema_version"], ej.SCHEMA_VERSION)
        self.assertEqual(MANIFEST["generated"], BUNDLE["generated"])

    def test_every_part_s_hash_and_size_are_in_the_manifest(self):
        self.assertEqual(sorted(MANIFEST["parts"]), sorted(n for n in FILES if n != ej.MANIFEST))
        for name, entry in MANIFEST["parts"].items():
            self.assertEqual(entry["sha256"], hashlib.sha256(FILES[name]).hexdigest(), name)
            self.assertEqual(entry["bytes"], len(FILES[name]), name)

    def test_the_part_names_are_core_plus_the_27_member_states(self):
        self.assertEqual(sorted(MANIFEST["parts"]), sorted([ej.CORE_PART] + [f"eu27.{iso}.json" for iso in ISOS]))
        self.assertEqual(len(ISOS), 27)
        self.assertIn("EL", ISOS)                                  # Greece by its Eurostat code, never GR

    def test_the_tracked_manifests_are_the_ones_the_committed_bundle_produces(self):
        # The same idea as design/build_tokens.py --check: the generated file in the tree is current.
        app = (ej.SPLIT_DIR / ej.MANIFEST).read_bytes()
        site = ej.SITE_MANIFEST.read_bytes()
        self.assertEqual(app, FILES[ej.MANIFEST], "mobile/assets/data/manifest.json is stale: run ./run.sh data")
        self.assertEqual(site, FILES[ej.MANIFEST], "web/public/data/manifest.json is stale: run ./run.sh data")


class SelfContained(unittest.TestCase):
    """A country part renders alone: every claim its spans cite is in it, with the sources behind them."""

    def test_every_claim_and_source_a_part_cites_is_in_the_part(self):
        for name, part in PARTS.items():
            if name == ej.MANIFEST:
                continue
            docs = ([part["infrastructure"], part["methodology"], part["factcheck"]["eu"]] if name == ej.CORE_PART
                    else [*part["documents"].values(), *part["factcheck"]["countries"].values()])
            cited = {c for d in docs for s in document.walk_spans(d) for c in s.get("c", []) if c in BUNDLE["claims"]}
            self.assertEqual(cited, set(part["claims"]), name)
            needed = {cite["source_id"] for cs in part["claims"].values() for cite in cs}
            self.assertEqual(needed, set(part["sources"]), name)

    def test_a_country_part_carries_only_its_own_state(self):
        for iso in ISOS:
            part = PARTS[f"eu27.{iso}.json"]
            self.assertEqual(list(part["documents"]), [iso])
            self.assertEqual(list(part["countries"]), [iso])
            self.assertEqual(list(part["factcheck"]["countries"]), [iso])
            self.assertEqual(list(part["factcheck"]["lines"]), [iso])
            self.assertEqual(part["schema_version"], BUNDLE["schema_version"])
            self.assertEqual(part["generated"], BUNDLE["generated"])
            self.assertLessEqual(set(part), BUNDLE_KEYS)

    def test_every_claim_in_the_bundle_is_in_exactly_one_country_part(self):
        # A claim id names its state (kind:ISO:...), and only that state's document prints it (#82).
        seen: dict[str, str] = {}
        for iso in ISOS:
            for claim in PARTS[f"eu27.{iso}.json"]["claims"]:
                self.assertNotIn(claim, seen, f"{claim} in both {seen.get(claim)} and {iso}")
                seen[claim] = iso
        self.assertEqual(sorted(seen), sorted(BUNDLE["claims"]))


class Core(unittest.TestCase):
    def test_core_carries_everything_that_is_not_per_state_plus_the_index(self):
        core = PARTS[ej.CORE_PART]
        self.assertEqual(set(core) - BUNDLE_KEYS, {"index"})
        self.assertEqual(set(BUNDLE) - set(core), set(ej.PER_COUNTRY))
        self.assertEqual(list(core["factcheck"]), ["eu"])
        for key in ("notice", "provenance", "sovereignty", "methodology", "infrastructure", "holding_classes",
                    "priority_rule", "national_data_note", "contribute"):
            self.assertEqual(core[key], BUNDLE[key], key)

    def test_the_index_is_a_recount_of_the_parts(self):
        index = PARTS[ej.CORE_PART]["index"]
        self.assertEqual(sorted(index), ISOS)
        for iso in ISOS:
            part = PARTS[f"eu27.{iso}.json"]
            self.assertEqual(index[iso], ej.index_entry(part["documents"][iso], part["countries"][iso]), iso)
            self.assertEqual(index[iso]["name"], BUNDLE["countries"][iso]["name"])
            self.assertLessEqual(index[iso]["withheld"], index[iso]["gaps"])
            self.assertLessEqual(index[iso]["holdings_verified"], index[iso]["holdings_total"])

    def test_the_index_counts_what_the_web_country_list_counts(self):
        # web/src/data/sources.ts factCounts(): a fact span counts; a gap or disputed span counts unless it
        # is the empty cell "—". web/src/pages/Countries.tsx: withheld = disputed spans.
        iso = "DE"
        spans = list(document.walk_spans(BUNDLE["documents"][iso]))
        entry = PARTS[ej.CORE_PART]["index"][iso]
        self.assertEqual(entry["facts"], sum(1 for s in spans if s["role"] == "fact"))
        self.assertEqual(entry["withheld"], sum(1 for s in spans if s["role"] == "disputed"))
        self.assertEqual(entry["holdings_total"], len(BUNDLE["countries"][iso]["national_data"]))


class Writer(unittest.TestCase):
    def test_write_split_removes_a_part_that_is_no_longer_in_the_edition(self):
        import tempfile  # noqa: PLC0415
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp)
            (out / "eu27.XX.json").write_bytes(b"{}")
            manifest = ej.write_split(BUNDLE, out, site_manifest=out / "site" / ej.MANIFEST)
            self.assertFalse((out / "eu27.XX.json").exists())
            self.assertEqual(sorted(p.name for p in out.glob("eu27.*.json")), sorted(manifest["parts"]))
            self.assertEqual((out / "site" / ej.MANIFEST).read_bytes(), (out / ej.MANIFEST).read_bytes())


if __name__ == "__main__":
    unittest.main()
