#!/usr/bin/env python3
"""
The one content model every output renders (DECISIONS.md #74, #75).

    python3 model/document.py DE        # print one country's document as JSON
    python3 model/document.py --check   # exit 1 if any fact in any document lacks a resolvable source

Why this file exists
--------------------
One country used to be written seven times: GOAL.md, the book entry, the report (pandoc over GOAL.md),
the web page, the Chrome PDF, the poster and the mobile screen, each with its own section list. This
module writes it once, as data, and every renderer walks the same structure:

    document = {iso, name, sections: [{id, title, blocks: [...]}]}

A block is one of `p`, `table`, `callout`, `list`, `stats`. Text is a list of spans. Every piece of
text has a role:

    label    a heading, column name or row label -- not a claim
    method   this project's own reasoning or instructions, stated as such
    fact     a statement about the world; carries claim ids that resolve to a cited source
    gap      where a fact would go, stated as not yet sourced -- the value is withheld

The rule the `--check` gate enforces (#75): a `fact` must carry at least one claim id, every claim id
must have a citation in `sources/citations.csv`, and every citation's source must be in the registry
and actually support the claim (`provenance.supported`). An unsourced value is never printed as a
fact: it becomes a `gap`. That is what "unimpeachable" means operationally -- a reader can follow
every fact to a document, a hash and a quote, and every gap is visible rather than papered over.

No country is described relative to another (#72). Nothing here reads a baseline country.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import evidence  # noqa: E402
import national_data as nd  # noqa: E402
import provenance  # noqa: E402
import sovereignty as sv  # noqa: E402

# The Eurostat fundamentals, in display order: (column, label, unit, decimals).
FUNDAMENTALS = [
    ("population_m", "Population", "million", 2),
    ("gdp_eur_bn", "GDP, current prices", "EUR bn", 1),
    ("gov_employment_k", "Public administration employment (NACE O)", "thousand", 1),
    ("elec_price_eur_mwh", "Non-household electricity price", "EUR/MWh", 1),
    ("renewables_pct", "Renewables share of electricity", "%", 1),
    ("land_km2", "Land area", "km²", 0),
]

# Legal and institutional posture: shown only where a source supports the cell (#75).
POSTURE = [
    ("legal_instrument", "Governing instrument"),
    ("sovereign_cloud_initiative", "Sovereign or government cloud"),
    ("certification_scheme", "Cloud certification"),
    ("data_classification", "Data classification"),
    ("procurement_vehicle", "Procurement route"),
    ("digital_id", "National digital identity"),
    ("ixp", "Internet exchange"),
    ("hyperscaler_regions_live", "Hyperscaler regions in country"),
]

# Priority of a holding for sovereign hosting: a declared formula, never a judgement about a
# country (#10, #73). Consequence of loss by tier, how hard the data is to rebuild, and what is
# known about its current dependency on non-EU providers.
TIER_POINTS = {0: 3, 1: 2, 2: 1, 3: 0}
RECOVERY_POINTS = {"low": 2, "medium": 1, "high": 0}
EXPOSURE_POINTS = {"non_eu_provider": 2, "mixed": 2, "unknown": 1, "": 1, "eu_provider": 1, "national": 0}
PRIORITY_BANDS = [(6, "Critical"), (4, "High"), (0, "Standard")]
PRIORITY_RULE = (
    "Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of "
    "rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers "
    "(non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). "
    "Critical is 6 or more, High is 4 or 5."
)

DEPENDENCY_LABEL = {
    "national": "National infrastructure", "eu_provider": "EU provider",
    "non_eu_provider": "Non-EU provider", "mixed": "Mixed", "unknown": "Not stated in sources",
}


# --------------------------------------------------------------------------- #
# Spans and cells
# --------------------------------------------------------------------------- #

def label(t: str) -> dict:
    return {"t": t, "role": "label"}


def method(t: str) -> dict:
    return {"t": t, "role": "method"}


def gap(t: str = "Not yet sourced") -> dict:
    return {"t": t, "role": "gap"}


class Sources:
    """The citations and registry, with the one test that matters: does a claim have support?"""

    def __init__(self) -> None:
        self.reg = provenance.registry()
        self.cites = provenance.citations()
        self.params = provenance.parameters()
        self.by_claim: dict[str, list[dict]] = {}
        for c in self.cites:
            self.by_claim.setdefault(c["claim"], []).append(c)

    def supported(self, claim: str) -> bool:
        return any(provenance.supported(c, self.reg, self.params) for c in self.by_claim.get(claim, []))

    def backing(self, claim: str, text: str, categorical: bool = False) -> list[dict]:
        """The citations that support `claim` *as printed*. A free-text value must also pass the
        value-in-quote rule against the citation (#82); a categorical value comes from a closed
        vocabulary and is admitted by review (#79), and a dataset value by reproduction."""
        out = []
        for c in self.by_claim.get(claim, []):
            if not provenance.supported(c, self.reg, self.params):
                continue
            src = self.reg[c["source_id"]]
            if categorical or src["doc_type"] == "dataset":
                out.append(c)
            elif evidence.value_in_quote(text, c["quote"], src["title"])["ok"]:
                out.append(c)
        return out

    def fact(self, claim: str, text: str, missing: str = "Not yet sourced", *,
             categorical: bool = False) -> dict:
        """A fact span if a citation supports the value as printed, otherwise a gap. The value is
        never shown unsourced."""
        if text and self.backing(claim, text, categorical):
            span = {"t": text, "role": "fact", "c": [claim]}
            if categorical:
                span["k"] = "categorical"
            return span
        return gap(missing)


def num(value, places: int) -> str:
    return f"{float(value):,.{places}f}".replace(",", " ")


# --------------------------------------------------------------------------- #
# Sections
# --------------------------------------------------------------------------- #

def priority(entry: dict) -> tuple[int, str]:
    score = (TIER_POINTS[entry["tier"]] + RECOVERY_POINTS[entry["recoverability"]]
             + EXPOSURE_POINTS.get(entry.get("foreign_dependency", ""), 1))
    band = next(name for floor, name in PRIORITY_BANDS if score >= floor)
    return score, band


def fundamentals(c: dict, src: Sources) -> dict:
    iso, p = c["iso2"], c["params"]
    rows = []
    for col, name, unit, places in FUNDAMENTALS:
        claim = f"param:{iso}:{col}"
        value = f"{num(p[col], places)} {unit}" if p.get(col) not in (None, "") else ""
        missing = ("Under review: the pinned source does not reproduce this value"
                   if col == "gov_employment_k" else "Not yet sourced")
        rows.append([label(name), src.fact(claim, value, missing)])
    return {
        "id": "fundamentals", "title": "Fundamentals",
        "blocks": [
            {"type": "p", "spans": [method(
                f"{c['name']} described on its own measured characteristics. Each figure is the "
                "published value of a pinned Eurostat series; the footnote names the series, "
                "the dimensions and the retrieval date.")]},
            {"type": "table", "columns": [label("Indicator"), label("Value")], "align": ["left", "right"],
             "rows": rows},
        ],
    }


def holdings_section(c: dict, src: Sources, entries: list[dict]) -> dict:
    iso = c["iso2"]
    ranked = sorted(entries, key=lambda e: (-priority(e)[0], nd.RECORD_CLASSES.index(e["record_class"])))
    rows = []
    for e in ranked:
        cls = e["record_class"]
        base = f"record:{iso}:{cls}"
        score, band = priority(e)
        if e["status"] == "held":
            name = src.fact(f"{base}:register", e["register"])
            operator = src.fact(f"{base}:operator", e["holder"]) if e["holder"] else gap()
            dep = e.get("foreign_dependency", "")
            dependency = (src.fact(f"{base}:foreign_dependency", DEPENDENCY_LABEL[dep], categorical=True)
                          if dep and dep != "unknown" else gap("Not stated in sources"))
            size_bits = []
            if e.get("record_count"):
                size_bits.append(src.fact(f"{base}:count", e["record_count"]))
            if e.get("data_size"):
                size_bits.append(src.fact(f"{base}:size", e["data_size"]))
            size = size_bits[0] if size_bits else gap("Not yet measured")
        elif e["status"] == "not_held":
            name = src.fact(f"{base}:register", "No central register", "Not yet sourced", categorical=True)
            operator, dependency, size = method("—"), method("—"), method("—")
        else:
            name = gap("Not yet verified")
            operator, dependency, size = gap("—"), gap("—"), gap("—")
        rows.append([
            label(band), label(f"{e['label']} (tier {e['tier']})"), name, operator, dependency, size,
        ])

    verified = sum(1 for e in entries if e["status"] != "unrecorded")
    measured = sum(1 for e in entries if e.get("record_count") or e.get("data_size"))
    return {
        "id": "holdings", "title": "Critical data holdings, by priority",
        "blocks": [
            {"type": "p", "spans": [method(
                f"The holdings {c['name']} cannot let depend on infrastructure a foreign state can "
                f"compel or switch off, ranked by a declared rule. {verified} of {len(entries)} "
                f"holding classes have a verified source; {measured} have a sourced record count "
                "or data size.")]},
            {"type": "callout", "tone": "method", "spans": [method(PRIORITY_RULE)]},
            {"type": "table",
             "columns": [label("Priority"), label("Holding"), label("Register or system"),
                         label("Operator"), label("Infrastructure dependency"), label("Records / size")],
             "align": ["left"] * 6, "rows": rows},
        ],
    }


def exposure_section(c: dict, entries: list[dict]) -> dict:
    held = [e for e in entries if e["status"] == "held"]
    counts: dict[str, int] = {}
    for e in held:
        k = e.get("foreign_dependency") or "unknown"
        counts[k] = counts.get(k, 0) + 1
    rows = [[label(DEPENDENCY_LABEL[k]), method(str(counts.get(k, 0)))]
            for k in ("national", "eu_provider", "mixed", "non_eu_provider", "unknown")]
    return {
        "id": "exposure", "title": "Foreign-dependency exposure",
        "blocks": [
            {"type": "p", "spans": [method(
                f"Of the {len(held)} verified holdings, how many sources state where the "
                "infrastructure is operated. A holding counts as dependent only when a cited "
                "document says so; silence is counted as not stated, never as national.")]},
            {"type": "table", "columns": [label("Infrastructure"), label("Holdings")],
             "align": ["left", "right"], "rows": rows},
        ],
    }


def posture_section(c: dict, src: Sources) -> dict:
    iso, p = c["iso2"], c["params"]
    rows = [[label(name), src.fact(f"param:{iso}:{col}", str(p.get(col, "")).strip())]
            for col, name in POSTURE]
    shown = sum(1 for r in rows if r[1]["role"] == "fact")
    return {
        "id": "posture", "title": "Legal and institutional posture",
        "blocks": [
            {"type": "p", "spans": [method(
                f"{shown} of {len(rows)} posture entries have a verified source. The others were "
                "researched from public policy documents but are withheld here until each is "
                "checked against the governing instrument.")]},
            {"type": "table", "columns": [label("Dimension"), label("Position")],
             "align": ["left", "left"], "rows": rows},
        ],
    }


def sizing_section(c: dict, entries: list[dict]) -> dict:
    measured = sum(1 for e in entries if e.get("record_count") or e.get("data_size"))
    return {
        "id": "sizing", "title": "Capacity",
        "blocks": [
            {"type": "callout", "tone": "gap", "spans": [method(
                f"Not yet sized. Capacity for {c['name']} will be derived from its own measured "
                f"holdings (record counts and data sizes), not scaled from another country. "
                f"{measured} of {len(entries)} holding classes have a sourced measurement so far.")]},
        ],
    }


def gaps_section(c: dict, entries: list[dict]) -> dict:
    missing = [e for e in entries if e["status"] == "unrecorded" and e["tier"] <= 1]
    items = [[method(f"{e['label']} (tier {e['tier']})")] for e in missing]
    return {
        "id": "gaps", "title": "Research still open",
        "blocks": [
            {"type": "p", "spans": [method(
                f"Tier 0 and 1 holdings for {c['name']} without a verified source yet. "
                "Corrections and sources are welcome through the repository's issue template.")]},
            {"type": "list", "items": items} if items else
            {"type": "p", "spans": [method("None: every tier 0 and 1 class has a verified source.")]},
        ],
    }


INDICATOR_DEFS = {r["id"]: r for r in sv.indicator_defs()}
VALUE_LABEL = {"yes": "Yes", "partial": "Partly", "no": "No", "unknown": "Not yet sourced"}


def indicators_for(iso: str, src: Sources) -> dict[str, str]:
    """The state's indicator values that a checked citation supports; the rest are unknown."""
    raw = sv.load_values().get(iso, {})
    supported = sv.supported_values(iso, raw, src.supported)
    return {i: supported.get(i, "unknown") for i in sv.INDICATOR_IDS}


def placement(c: dict, src: Sources) -> dict:
    ind = indicators_for(c["iso2"], src)
    return {**sv.place(ind, c["national_data"]), "indicators": ind}


def move_text(m: dict) -> str:
    if m["input"] == "holdings":
        return (f"If any of the {m['count']} tier 0/1 holdings whose hosting is not yet sourced turns "
                f"out to run on non-EU infrastructure: {sv.LABELS[m['group']]}.")
    name = INDICATOR_DEFS[m["input"]]["label"]
    return f"If {name.lower()} is found to be {m['if']}: {sv.LABELS[m['group']]}."


def placement_section(c: dict, src: Sources, p: dict) -> dict:
    iso = c["iso2"]
    rows = []
    for i in sv.INDICATOR_IDS:
        d = INDICATOR_DEFS[i]
        v = p["indicators"][i]
        cell = (src.fact(f"indicator:{iso}:{i}", VALUE_LABEL[v], categorical=True)
                if v != "unknown" else gap())
        rows.append([label(d["label"]), cell])
    moves = [[method(move_text(m))] for m in p["could_move"]]
    rng = p["range"]
    return {
        "id": "placement", "title": "Data-sovereignty placement",
        "blocks": [
            {"type": "callout", "tone": "notice", "spans": [method(
                f"{sv.LABELS[p['group']]}. Confidence: {p['confidence']}. With the evidence still "
                f"open, {c['name']} could be anywhere from '{sv.LABELS[rng[0]]}' to "
                f"'{sv.LABELS[rng[-1]]}'.")]},
            {"type": "p", "spans": [method(sv.GUARDRAIL)]},
            {"type": "table", "columns": [label("Indicator"), label("Finding")],
             "align": ["left", "left"], "rows": rows},
            {"type": "p", "spans": [method("What could move this placement:")]},
            {"type": "list", "items": moves} if moves else
            {"type": "p", "spans": [method("Nothing: every input the rule reads is settled by a source.")]},
        ],
    }


def country(c: dict, src: Sources | None = None) -> dict:
    """One country's document. `c` is a bundle country (country_data.build output)."""
    src = src or Sources()
    entries = c["national_data"]
    return {
        "iso": c["iso2"], "name": c["name"],
        "sections": [
            placement_section(c, src, placement(c, src)),
            fundamentals(c, src),
            holdings_section(c, src, entries),
            exposure_section(c, entries),
            posture_section(c, src),
            sizing_section(c, entries),
            gaps_section(c, entries),
        ],
    }


# --------------------------------------------------------------------------- #
# Sources used, and the gate
# --------------------------------------------------------------------------- #

def walk_spans(doc: dict):
    for s in doc["sections"]:
        for b in s["blocks"]:
            if b["type"] in ("p", "callout"):
                yield from b["spans"]
            elif b["type"] == "list":
                for item in b["items"]:
                    yield from item
            elif b["type"] == "table":
                yield from b["columns"]
                for row in b["rows"]:
                    yield from row


def claims_used(doc: dict) -> list[str]:
    seen: list[str] = []
    for span in walk_spans(doc):
        for claim in span.get("c", []):
            if claim not in seen:
                seen.append(claim)
    return seen


def check(doc: dict, src: Sources) -> list[str]:
    errors = []
    for span in walk_spans(doc):
        role = span.get("role")
        if role not in ("label", "method", "fact", "gap"):
            errors.append(f"{doc['iso']}: span without a role: {span.get('t', '')[:60]!r}")
        if role == "fact":
            if not span.get("c"):
                errors.append(f"{doc['iso']}: fact without a claim: {span['t'][:60]!r}")
            for claim in span.get("c", []):
                if not src.backing(claim, span["t"], span.get("k") == "categorical"):
                    errors.append(f"{doc['iso']}: {claim} is shown as {span['t'][:40]!r} but no "
                                  "citation supports that value")
    return errors


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("iso", nargs="?")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args(argv)
    import export_json  # noqa: PLC0415

    bundle = export_json.build_bundle()
    src = Sources()
    if args.check:
        errors = [e for iso in sorted(bundle["countries"])
                  for e in check(country(bundle["countries"][iso], src), src)]
        for e in errors:
            print(e, file=sys.stderr)
        print(f"{len(bundle['countries'])} documents checked, {len(errors)} unsourced facts")
        return 1 if errors else 0
    print(json.dumps(country(bundle["countries"][args.iso.upper()], src), indent=1, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
