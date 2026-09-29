#!/usr/bin/env python3
"""
Model and data-integrity tests.

    python3 -m unittest discover -s tests -v

Stdlib unittest, no pytest, consistent with the project's stdlib-only rule.

These guard the model's inputs, the capacity engine's arithmetic, the generated briefs, and
the rule that no country is derived from another (#72).
"""
from __future__ import annotations

import csv
import hashlib
import os
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "model"))

import capacity_model as cm  # noqa: E402
import country_data  # noqa: E402
import emoji  # noqa: E402
import generate_countries as gc  # noqa: E402

# The pinned generation date, read from the one file that owns it. Hardcoding this
# has now broken twice: once in init.sh, once in the CI workflow.
PINNED_EPOCH = (ROOT / ".build-epoch").read_text().strip()


def params() -> dict[str, dict]:
    return {r["iso2"]: r for r in cm.read_csv(gc.PARAMS)}


class EngineReproducesTheSpreadsheet(unittest.TestCase):
    """The capacity engine (capacity_model.py) is kept for sizing from measured holdings (#73).
    Its arithmetic is still checked against the one spreadsheet it was built to reproduce --
    as an engine test only: the Dutch inputs size nothing and feed no other country (#72)."""

    def test_engine_reproduces_the_dutch_spreadsheet(self):
        s = cm.run_country("NL", write=False)
        self.assertEqual(s.total_servers, 5691)
        self.assertAlmostEqual(s.design_mw, 14.2, places=1)
        self.assertAlmostEqual(s.capex_total, 339.0, places=0)


class NoCountryIsDerivedFromAnother(unittest.TestCase):
    """#72: each country is analysed on its own fundamentals. Changing one country's parameter
    row must leave every other country's document byte-identical."""

    def test_changing_the_netherlands_changes_no_other_document(self):
        import document
        import national_data as nd
        rows = params()
        register = nd.load()
        src = document.Sources()

        def docs(p):
            return {iso: document.country(country_data.build(c, nd.for_country(register, iso)), src)
                    for iso, c in p.items() if iso != "NL"}

        before = docs(rows)
        mutated = {**rows, "NL": {**rows["NL"], "population_m": "99.9", "gdp_eur_bn": "9999"}}
        self.assertEqual(before, docs(mutated))

    def test_no_other_brief_mentions_the_dutch_case(self):
        for f in sorted(ROOT.glob("countries/*/GOAL.md")):
            if f.parent.name == "NL":
                continue
            with self.subTest(country=f.parent.name):
                text = f.read_text(encoding="utf-8")
                self.assertNotIn("Dutch", text)
                self.assertNotIn("Netherlands", text)

    def test_no_scaled_capacity_reaches_the_bundle(self):
        """#73: capacity is withdrawn until sized from a country's own holdings."""
        bundle = json_bundle()
        self.assertNotIn("totals", bundle)
        for iso, c in bundle["countries"].items():
            with self.subTest(iso=iso):
                self.assertNotIn("capacity", c)
                self.assertNotIn("scale", c)


def json_bundle() -> dict:
    import json
    return json.loads((ROOT / "web" / "public" / "data" / "eu27.json").read_text(encoding="utf-8"))


class CsvIntegrity(unittest.TestCase):
    """The IT/ES bug: unquoted commas shifted every later field, silently corrupting
    the generated threat notes. csv.DictReader signals it with a None key."""

    def all_csvs(self):
        return sorted(ROOT.glob("model/*.csv")) + sorted(ROOT.glob("countries/*/*.csv"))

    def test_no_row_has_stray_fields(self):
        for path in self.all_csvs():
            with self.subTest(csv=str(path.relative_to(ROOT))):
                with path.open(newline="", encoding="utf-8") as f:
                    reader = csv.DictReader(f)
                    width = len(reader.fieldnames or [])
                    for i, row in enumerate(reader, start=2):
                        self.assertNotIn(
                            None, row,
                            f"line {i} has more fields than the {width}-column header "
                            "(usually an unquoted comma)",
                        )
                        self.assertFalse(
                            any(v is None for v in row.values()),
                            f"line {i} has fewer fields than the header",
                        )

    def test_enum_columns(self):
        allowed = {
            "seismic": {"low", "moderate", "high"},
            "gov_cloud_maturity": {"none", "pilot", "operational", "federated"},
            "certification_strength": {"baseline", "national", "stringent"},
            "hyperscaler_dependency": {"low", "medium", "high", "critical"},
            "frontline": {"0", "1"},
            "grid_isolated": {"0", "1"},
        }
        for r in cm.read_csv(gc.PARAMS):
            for col, ok in allowed.items():
                with self.subTest(iso=r["iso2"], column=col):
                    self.assertIn(r[col], ok)

    def test_numeric_ranges(self):
        bounds = {
            "population_m": (0.1, 100.0),
            "gdp_eur_bn": (1.0, 6000.0),
            "elec_price_eur_mwh": (50.0, 400.0),
            "renewables_pct": (0.0, 100.0),
            "min_sites": (1, 8),
            "hyperscaler_regions_live": (0, 20),
        }
        for r in cm.read_csv(gc.PARAMS):
            for col, (lo, hi) in bounds.items():
                with self.subTest(iso=r["iso2"], column=col):
                    self.assertTrue(lo <= float(r[col]) <= hi, f"{r[col]} outside [{lo}, {hi}]")


class GeneratorDeterminism(unittest.TestCase):
    def test_regeneration_is_a_no_op(self):
        """With the date pinned, running the generator twice must change nothing."""
        env = {**os.environ, "SOURCE_DATE_EPOCH": PINNED_EPOCH}

        def fingerprint():
            h = hashlib.sha256()
            for f in sorted(ROOT.glob("countries/*/GOAL.md")):
                h.update(f.read_bytes())
            h.update((ROOT / "countries" / "SUMMARY.md").read_bytes())
            return h.hexdigest()

        run = lambda: subprocess.run(  # noqa: E731
            [sys.executable, str(ROOT / "model" / "generate_countries.py")],
            cwd=ROOT, env=env, capture_output=True, check=True,
        )
        run()
        before = fingerprint()
        run()
        self.assertEqual(before, fingerprint(), "generator is not byte-reproducible")


class ContentsMatchHeadings(unittest.TestCase):
    """A brief must not advertise a section it does not have.

    The contents list and the headings are both built from `generate_countries.SECTIONS`,
    so they cannot disagree by construction -- but that is exactly the kind of invariant
    that survives one refactor and quietly dies in the next. Asserted against the rendered
    files rather than against the tuple, so the test fails if the *output* drifts.
    """

    HEADING = re.compile(r"^## (\d+)\. (.+)$", re.M)
    ENTRY = re.compile(r"^(\d+)\. \[(.+)\]\(#(.+)\)$", re.M)

    def briefs(self):
        """All 27, NL included: every brief is generated the same way (#72)."""
        return sorted(ROOT.glob("countries/*/GOAL.md"))

    def test_every_generated_brief_has_a_contents_list(self):
        for f in self.briefs():
            with self.subTest(country=f.parent.name):
                self.assertIn("## Contents", f.read_text(encoding="utf-8"))

    def test_contents_matches_the_headings_exactly(self):
        for f in self.briefs():
            with self.subTest(country=f.parent.name):
                text = f.read_text(encoding="utf-8")
                headings = [(int(n), t) for n, t in self.HEADING.findall(text)]
                entries = [(int(n), t) for n, t, _ in self.ENTRY.findall(text)]
                self.assertEqual(entries, headings)

    def test_numbering_is_contiguous_from_one(self):
        for f in self.briefs():
            with self.subTest(country=f.parent.name):
                numbers = [int(n) for n, _ in self.HEADING.findall(f.read_text(encoding="utf-8"))]
                self.assertEqual(numbers, list(range(1, len(numbers) + 1)))

    def test_every_anchor_resolves_to_its_heading(self):
        """GitHub builds the anchor from the heading text; a wrong slug is a dead link."""
        for f in self.briefs():
            with self.subTest(country=f.parent.name):
                text = f.read_text(encoding="utf-8")
                expected = {gc.slug(f"{n}. {t}") for n, t in self.HEADING.findall(text)}
                anchors = {a for _, _, a in self.ENTRY.findall(text)}
                self.assertEqual(anchors, expected)


class SummaryIsAnIndex(unittest.TestCase):
    """countries/SUMMARY.md is the cross-country table of contents."""

    def setUp(self):
        self.text = (cm.COUNTRIES / "SUMMARY.md").read_text(encoding="utf-8")

    def test_every_country_links_to_its_brief(self):
        for row in cm.read_csv(ROOT / "model" / "eu27_parameters.csv"):
            iso, name = row["iso2"], row["country"]
            with self.subTest(iso=iso):
                self.assertIn(f"[{name}]({iso}/GOAL.md)", self.text)

    def test_every_country_carries_its_flag(self):
        for row in cm.read_csv(ROOT / "model" / "eu27_parameters.csv"):
            with self.subTest(iso=row["iso2"]):
                self.assertIn(emoji.flag(row["iso2"]), self.text)


if __name__ == "__main__":
    unittest.main()
