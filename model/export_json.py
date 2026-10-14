#!/usr/bin/env python3
"""
Export every fact about all 27 member states as one JSON bundle for the web app.

    python3 model/export_json.py [-o web/public/data/eu27.json] [--split [DIR]]
    python3 model/export_json.py --from web/public/data/eu27.json [--split [DIR]]

Reads the same country_data.build() dict and content model (document.py) the markdown
briefs and the PDFs are rendered from, so no output can disagree with another. The bundle is about
930 KB gzipped (7.5 MB raw); the web app ships the entire model client-side and needs no API.

`--split` also writes the *edition* the mobile reader ships (#110): the same content as 28 parts,
`eu27.core.json` plus one `eu27.<ISO>.json` per member state, each self-contained, and a
`manifest.json` naming the sha256 of every part and of the single file (the edition id). The parts are
a pure function of the single file, so they are generated, never tracked; the manifest is tracked, in
`mobile/assets/data/` and in `web/public/data/`, so the site publishes its edition id too. `--from`
splits an existing bundle without rebuilding the model. tests/test_export_split.py proves the parts
merge back to the single file byte for byte.

Keys prefixed with "_" are dropped: they carry Python objects (the raw Summary
dataclass) that exist only so the markdown renderer can format unrounded values.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import capacity_model as cm  # noqa: E402
import country_data  # noqa: E402
import national_data as nd  # noqa: E402
import generate_countries as gc  # noqa: E402
import document  # noqa: E402
import evidence  # noqa: E402

SCHEMA_VERSION = 2
DEFAULT_OUT = cm.ROOT / "web" / "public" / "data" / "eu27.json"
# The split edition (#110): the parts next to the app that bundles them, the manifest also next to the site's
# single file. Part names are fixed so the app's static requires and the manifest's keys cannot drift.
SPLIT_DIR = cm.ROOT / "mobile" / "assets" / "data"
SITE_MANIFEST = DEFAULT_OUT.parent / "manifest.json"
CORE_PART = "eu27.core.json"
MANIFEST = "manifest.json"
# The record maps a country part carries; everything else in the bundle is core.
PER_COUNTRY = ("documents", "countries")


def dumps(obj) -> str:
    """The one serialisation every file here uses: sorted keys, so bytes are reproducible and diffs readable."""
    return json.dumps(obj, indent=1, sort_keys=True, ensure_ascii=False)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def cited(docs: list[dict], claims: dict) -> tuple[dict, list[str]]:
    """The claims a list of documents cites (any span carrying ids, so a disputed span's trace resolves
    too), restricted to what the bundle records, and the source ids behind them."""
    ids = sorted({c for d in docs for s in document.walk_spans(d) for c in s.get("c", []) if c in claims})
    sub = {c: claims[c] for c in ids}
    return sub, sorted({cite["source_id"] for cs in sub.values() for cite in cs})


def index_entry(doc: dict, country: dict) -> dict:
    """What the country list shows without opening a part: the same counts the web's Countries page
    derives (web/src/data/sources.ts coverage() and factCounts(), web/src/pages/Countries.tsx)."""
    spans = list(document.walk_spans(doc))
    held = country["national_data"]
    return {
        "name": country["name"],
        "facts": sum(1 for s in spans if s["role"] == "fact"),
        "gaps": sum(1 for s in spans if s["role"] in ("gap", "disputed") and s["t"] != "—"),
        "withheld": sum(1 for s in spans if s["role"] == "disputed"),
        "holdings_verified": sum(1 for e in held if e["status"] != "unrecorded"),
        "holdings_total": len(held),
        "tier0_verified": sum(1 for e in held if e["status"] != "unrecorded" and e["tier"] == 0),
        "tier0_total": sum(1 for e in held if e["tier"] == 0),
    }


def split_bundle(bundle: dict) -> dict[str, bytes]:
    """The edition: the bundle as self-contained parts plus a manifest, as bytes keyed by file name.

    `eu27.<ISO>.json` holds one state's document, data, fact-check appendix and line, with exactly the claims
    its spans cite and the sources behind them. `eu27.core.json` holds everything else (notice, sovereignty,
    methodology, infrastructure, the EU fact-check appendix, ...) with the claims *those* cite, plus `index`,
    the one key the single file lacks. Duplicates across parts (a source two states cite, the infrastructure
    overview's copies of country spans) are byte-identical, which merge_parts() asserts."""
    single = dumps(bundle).encode("utf-8")
    claims, sources, fc = bundle["claims"], bundle["sources"], bundle["factcheck"]
    isos = sorted(bundle["documents"])
    files: dict[str, bytes] = {}

    core = {k: v for k, v in bundle.items() if k not in PER_COUNTRY + ("claims", "sources", "factcheck")}
    core["factcheck"] = {"eu": fc["eu"]}
    core["claims"], sids = cited([bundle["infrastructure"], bundle["methodology"], fc["eu"]], claims)
    core["sources"] = {s: sources[s] for s in sids}
    core["index"] = {iso: index_entry(bundle["documents"][iso], bundle["countries"][iso]) for iso in isos}
    files[CORE_PART] = dumps(core).encode("utf-8")

    for iso in isos:
        docs = [bundle["documents"][iso], fc["countries"][iso]]
        part_claims, sids = cited(docs, claims)
        part = {"schema_version": bundle["schema_version"], "generated": bundle["generated"],
                "documents": {iso: bundle["documents"][iso]}, "countries": {iso: bundle["countries"][iso]},
                "factcheck": {"countries": {iso: fc["countries"][iso]}, "lines": {iso: fc["lines"][iso]}},
                "claims": part_claims, "sources": {s: sources[s] for s in sids}}
        files[f"eu27.{iso}.json"] = dumps(part).encode("utf-8")

    manifest = {"schema_version": bundle["schema_version"], "generated": bundle["generated"],
                "edition": sha256(single),
                "parts": {name: {"sha256": sha256(data), "bytes": len(data)} for name, data in files.items()}}
    files[MANIFEST] = dumps(manifest).encode("utf-8")
    return files


def merge_parts(parts: dict[str, dict]) -> dict:
    """The single bundle from loaded parts (name -> dict). Inverse of split_bundle(): a duplicate record
    that differs between parts is a corrupt edition, not a merge to resolve."""
    core = dict(parts[CORE_PART])
    core.pop("index")
    merged = {**core, "documents": {}, "countries": {}, "claims": dict(core["claims"]),
              "sources": dict(core["sources"]), "factcheck": {"eu": core["factcheck"]["eu"], "countries": {}, "lines": {}}}
    for name, part in sorted(parts.items()):
        if name in (CORE_PART, MANIFEST):
            continue
        for key in PER_COUNTRY:
            merged[key].update(part[key])
        merged["factcheck"]["countries"].update(part["factcheck"]["countries"])
        merged["factcheck"]["lines"].update(part["factcheck"]["lines"])
        for key in ("claims", "sources"):
            for k, v in part[key].items():
                if k in merged[key] and merged[key][k] != v:
                    raise ValueError(f"{name}: {key} {k} differs from another part")
                merged[key][k] = v
    for key in ("documents", "countries", "claims", "sources"):
        merged[key] = dict(sorted(merged[key].items()))
    merged["factcheck"]["countries"] = dict(sorted(merged["factcheck"]["countries"].items()))
    merged["factcheck"]["lines"] = dict(sorted(merged["factcheck"]["lines"].items()))
    return merged


def write_split(bundle: dict, out_dir: Path, site_manifest: Path | None = SITE_MANIFEST) -> dict:
    """Write the edition into out_dir, removing any part that is no longer in it, and the manifest also
    beside the site's single file. Returns the manifest."""
    files = split_bundle(bundle)
    out_dir.mkdir(parents=True, exist_ok=True)
    for stale in out_dir.glob("eu27.*.json"):
        if stale.name not in files:
            stale.unlink()
    for name, data in files.items():
        (out_dir / name).write_bytes(data)
    if site_manifest:
        site_manifest.parent.mkdir(parents=True, exist_ok=True)
        site_manifest.write_bytes(files[MANIFEST])
    return json.loads(files[MANIFEST])


def strip_private(obj):
    """Drop "_"-prefixed keys recursively; they hold Python objects, not data."""
    if isinstance(obj, dict):
        return {k: strip_private(v) for k, v in obj.items() if not k.startswith("_")}
    if isinstance(obj, list):
        return [strip_private(v) for v in obj]
    return obj


def build_bundle() -> dict:
    params = {r["iso2"]: r for r in cm.read_csv(gc.PARAMS)}
    # Read once, outside the loop: country_data.build() does no file I/O of its own.
    register = nd.load()
    # Each country from its own parameter row and register only (#72). No capacity: withdrawn
    # until a country is sized from its own measured holdings (#73).
    countries = {iso: strip_private(country_data.build(c, nd.for_country(register, iso)))
                 for iso, c in sorted(params.items())}

    # The content model (#74) and everything its facts cite (#75): renderers look sources up here
    # rather than carrying their own copies, so a footnote cannot drift from the register.
    src = document.Sources()
    documents = {iso: document.country(c, src) for iso, c in countries.items()}
    # Each claim lists only the citations that back its value as printed (#82), with the checklist
    # and grade evidence.assess() gives each. A claim id is printed once, in its own country.
    claims = {}
    for d in documents.values():
        for span in document.walk_spans(d):
            if span.get("role") != "fact":
                continue
            for claim in span["c"]:
                claims[claim] = [
                    {**{k: c[k] for k in ("source_id", "locator", "quote", "value_as_found",
                                          "confidence", "retrieved", "checked_by")}, **a,
                     # For renderers, so none re-derives a rule: the quote as found, the machine
                     # gloss apart from it, and the checks as phrases.
                     "original": evidence.split_quote(c["quote"])[0],
                     "gloss": evidence.split_quote(c["quote"])[1],
                     "checklist": evidence.checklist(a["checks"])}
                    for c, a in src.evidence(claim, span["t"], span.get("k") == "categorical")]
    claims = dict(sorted(claims.items()))
    source_ids = sorted({c["source_id"] for cs in claims.values() for c in cs})
    sources = {sid: {**src.reg[sid], "label": document.provenance.label(sid, src.reg)}
               for sid in source_ids}

    import contrib  # noqa: PLC0415
    import factcheck_appendix  # noqa: PLC0415
    import methodology  # noqa: PLC0415
    facts = [s for d in documents.values() for s in document.walk_spans(d) if s.get("role") == "fact"]
    n_facts, n_verified = len(facts), sum(1 for s in facts if s.get("g") == evidence.VERIFIED)
    return {
        "schema_version": SCHEMA_VERSION,
        "documents": documents,
        # How every fact was sourced and every figure calculated, generated (#84).
        "methodology": methodology.build(documents, claims, sources),
        # How every printed fact was checked by the model that did not write it, for the EU-27 report
        # and for each country, generated from the fact-check ledger (#87).
        "factcheck": factcheck_appendix.build(documents, claims, sources),
        # Key infrastructure and hosting across the 27 (#95): copies of the country documents' spans, so it
        # prints no fact of its own and needs no fact check of its own.
        "infrastructure": document.infrastructure(documents),
        "claims": claims,
        "sources": sources,
        "holding_classes": [{"class_id": c, "label": nd.LABELS[c], "tier": nd.TIER_OF[c],
                             "domain": nd.DOMAIN_OF[c]} for c in nd.RECORD_CLASSES],
        "priority_rule": document.PRIORITY_RULE,
        # #77: groups by a published rule, with computed range and confidence. Ids and labels only;
        # there is no score anywhere in the bundle.
        "sovereignty": {
            "groups": [{"id": g, "label": document.sv.LABELS[g]} for g in document.sv.GROUPS],
            "guardrail": document.sv.GUARDRAIL,
            "rule": [{"group": g, "label": document.sv.LABELS[g], "condition": t}
                     for g, t in document.sv.RULE],
            "unknown_rule": document.sv.UNKNOWN_RULE,
            "confidence_rule": document.sv.CONFIDENCE_RULE,
            "indicators": [{k: d[k] for k in ("id", "dimension", "label", "question")}
                           for d in document.sv.indicator_defs()],
            "placements": {iso: document.placement(c, src) for iso, c in countries.items()},
        },
        "generated": gc.gen_date(),
        # One wording, from evidence.py, so no surface claims a check that did not run.
        "provenance": f"{evidence.disclaimer(n_verified, n_facts)} {evidence.WITHHELD} Capacity is not yet sized.",
        # Where a reader checks a fact or submits a source (#85).
        "contribute": {"review": contrib.REVIEW_TEMPLATE, "submit": contrib.SUBMIT_TEMPLATE},
        "notice": {"disclaimer": evidence.disclaimer(n_verified, n_facts), "withheld": evidence.WITHHELD,
                   "grade_rule": evidence.GRADE_RULE,
                   "checks": [{"name": n, "what": w} for n, w in evidence.CHECKS]},
        # One disclaimer, in the bundle, so the markdown brief, the web page, the book and the
        # mobile reader hedge identically instead of growing four different wordings.
        "national_data_note": nd.NOTE,
        "countries": countries,
    }


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("-o", "--out", type=Path, default=DEFAULT_OUT)
    p.add_argument("--split", nargs="?", const=SPLIT_DIR, default=None, type=Path, metavar="DIR",
                   help=f"also write the split edition and its manifest (default DIR {SPLIT_DIR.relative_to(cm.ROOT)})")
    p.add_argument("--from", dest="source", type=Path, metavar="FILE",
                   help="split this existing bundle instead of rebuilding the model (implies --split)")
    args = p.parse_args(argv)

    if args.source:
        bundle = json.loads(args.source.read_text(encoding="utf-8"))
        split_dir = args.split or SPLIT_DIR
    else:
        bundle = build_bundle()
        args.out.parent.mkdir(parents=True, exist_ok=True)
        # sort_keys so the bundle is byte-reproducible and diffs stay readable.
        args.out.write_text(dumps(bundle), encoding="utf-8")
        size = args.out.stat().st_size
        print(f"{args.out}: {len(bundle['countries'])} countries, {size:,} bytes")
        split_dir = args.split

    if split_dir:
        manifest = write_split(bundle, split_dir)
        total = sum(p["bytes"] for p in manifest["parts"].values())
        print(f"{split_dir}: edition {manifest['edition'][:16]}…, {len(manifest['parts'])} parts, {total:,} bytes; "
              f"manifest also at {SITE_MANIFEST.relative_to(cm.ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
