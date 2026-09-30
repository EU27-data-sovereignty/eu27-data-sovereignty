#!/usr/bin/env python3
"""
Export every fact about all 27 member states as one JSON bundle for the web app.

    python3 model/export_json.py [-o web/public/data/eu27.json]

Reads the same country_data.build() dict and content model (document.py) the markdown
briefs and the PDFs are rendered from, so no output can disagree with another. The whole bundle is ~26 KB gzipped, which is
why the app ships the entire model client-side and needs no API.

Keys prefixed with "_" are dropped: they carry Python objects (the raw Summary
dataclass) that exist only so the markdown renderer can format unrounded values.
"""
from __future__ import annotations

import argparse
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


def strip_private(obj):
    """Drop "_"-prefixed keys recursively; they hold Python objects, not data."""
    if isinstance(obj, dict):
        return {k: strip_private(v) for k, v in obj.items() if not k.startswith("_")}
    if isinstance(obj, list):
        return [strip_private(v) for v in obj]
    return obj


def provenance_ok(c: dict, src) -> bool:
    return document.provenance.supported(c, src.reg, src.params)


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
    used = sorted({claim for d in documents.values() for claim in document.claims_used(d)})
    claims = {claim: [{k: c[k] for k in ("source_id", "locator", "quote", "value_as_found",
                                         "confidence", "retrieved", "checked_by")}
                      for c in src.by_claim[claim] if provenance_ok(c, src)]
              for claim in used}
    source_ids = sorted({c["source_id"] for cs in claims.values() for c in cs})
    sources = {sid: {**src.reg[sid], "label": document.provenance.label(sid, src.reg)}
               for sid in source_ids}

    return {
        "schema_version": SCHEMA_VERSION,
        "documents": documents,
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
        "provenance": f"{evidence.PROVENANCE} Capacity is not yet sized.",
        "notice": {"disclaimer": evidence.DISCLAIMER, "withheld": evidence.WITHHELD,
                   "checks": [{"name": n, "what": w} for n, w in evidence.CHECKS]},
        # One disclaimer, in the bundle, so the markdown brief, the web page, the book and the
        # mobile reader hedge identically instead of growing four different wordings.
        "national_data_note": nd.NOTE,
        "countries": countries,
    }


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("-o", "--out", type=Path, default=DEFAULT_OUT)
    args = p.parse_args(argv)

    bundle = build_bundle()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    # sort_keys so the bundle is byte-reproducible and diffs stay readable.
    args.out.write_text(json.dumps(bundle, indent=1, sort_keys=True, ensure_ascii=False), encoding="utf-8")

    size = args.out.stat().st_size
    print(f"{args.out}: {len(bundle['countries'])} countries, {size:,} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
