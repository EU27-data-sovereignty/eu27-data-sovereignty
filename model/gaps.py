#!/usr/bin/env python3
"""
Write docs/gaps.md: every piece of data the project does not have yet, and how hard it has been looked for.

    python3 model/gaps.py                  # regenerate docs/gaps.md
    python3 model/gaps.py --csv out.csv    # one row per gap, the input for a research wave (not committed)

Why this file exists
--------------------
"Find as much data as we can" (docs/status.md) needs to know what is missing and where to look first. Until
now an empty cell meant either "searched and not found" or "never searched", and nothing told them apart.
This page derives the difference from the research that already ran, so it is generated, never kept by hand
(the reasoning of #82):

- **Run 1** (`model/research/<ISO>.json`, 2026-09-29) asked about every field of every holding class in
  every state, so each cell has had one search. A claim it made that is not in the register failed
  verification or review: the evidence exists, but was not admitted.
- **Run 2** (`model/research/indicators/<ISO>.json`) did the same for the seven indicators.
- **The vetting run** (`model/research/vetting/<ISO>.json`), its later rounds and research waves
  (`rounds/<run>/`) searched again for the claims they reached. The outcome `not_reached` is not a search.

A cell is **dry** once two passes have found nothing (the stop rule in docs/status.md). Absence that was
*established* (a register is `not_held`, with an authoritative source) is data, not a gap.
"""
from __future__ import annotations

import argparse
import collections
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "model"))
import national_data  # noqa: E402

RESEARCH = ROOT / "model" / "research"
OUT = ROOT / "docs" / "gaps.md"
INDICATORS = ROOT / "model" / "sovereignty_indicators.csv"
INDICATOR_DEFS = ROOT / "model" / "indicators.csv"

# Register column -> claim kind (provenance.RECORD_KINDS). The register column is the holding itself.
FIELDS = {"register": "register", "holder": "operator", "legal_basis": "legal_basis", "hosting": "hosting",
          "foreign_dependency": "foreign_dependency", "record_count": "count", "data_size": "size"}
SEARCHED = ("found", "no_better_found")               # vetting outcomes that were a search
STATES = ("filled", "claimed_unverified", "not_searched", "searched_once", "dry")


def _json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def research_passes() -> tuple[dict, set]:
    """Passes per claim (record:<ISO>:<class>:<kind> or indicator:<ISO>:<id>), and the claims some run made."""
    passes: collections.Counter = collections.Counter()
    claimed: set[str] = set()
    for iso in national_data.countries():
        for h in _json(RESEARCH / f"{iso}.json").get("holdings", []):
            for kind in set(FIELDS.values()):
                passes[f"record:{iso}:{h['class_id']}:{kind}"] += 1
            for c in h.get("claims", []):
                kind = national_data.KIND_OF_FIELD.get(c.get("field", ""))
                if kind:
                    claimed.add(f"record:{iso}:{h['class_id']}:{kind}")
        for ind in _json(RESEARCH / "indicators" / f"{iso}.json").get("indicators", []):
            passes[f"indicator:{iso}:{ind['id']}"] += 1
            if ind.get("claims"):
                claimed.add(f"indicator:{iso}:{ind['id']}")
    # The vetting run, its later rounds and waves (rounds/<run>/), and citizens' submissions (#85, #93).
    import vetting  # noqa: PLC0415
    for doc in vetting.staged().values():
        for o in doc.get("outcomes", []):
            if o["status"] in SEARCHED:
                passes[o["claim"]] += 1
        for f in doc.get("findings", []):
            claimed.add(f["claim"])
    return passes, claimed


def state(claim: str, filled: bool, passes, claimed) -> str:
    if filled:
        return "filled"
    if claim in claimed:
        return "claimed_unverified"
    return {0: "not_searched", 1: "searched_once"}.get(passes[claim], "dry")


def cells() -> list[dict[str, str]]:
    """Every (state, class, field) and (state, indicator) cell, with its state. Fields of a holding that is
    not held are not cells; the fields of a holding not yet found follow its register and are not listed."""
    passes, claimed = research_passes()
    rows = {(r["iso"], r["record_class"]): r for r in national_data.read_rows()}
    out = []
    for iso in national_data.countries():
        for cls in national_data.RECORD_CLASSES:
            row = rows.get((iso, cls))
            if row and row["status"] == "not_held":
                continue
            for field, kind in FIELDS.items():
                if not row and field != "register":
                    continue
                value = (row or {}).get(field, "").strip()
                filled = bool(value) and value != "unknown"
                claim = f"record:{iso}:{cls}:{kind}"
                out.append({"iso": iso, "kind": "holding", "item": cls, "field": field,
                            "tier": str(national_data.TIER_OF[cls]), "claim": claim,
                            "state": state(claim, filled, passes, claimed), "passes": str(passes[claim])})
    with INDICATORS.open(newline="", encoding="utf-8") as fh:
        have = {(r["iso"], r["indicator"]) for r in csv.DictReader(fh) if r["value"].strip()}
    with INDICATOR_DEFS.open(newline="", encoding="utf-8") as fh:
        ids = [r["id"] for r in csv.DictReader(fh)]
    for iso in national_data.countries():
        for i in ids:
            claim = f"indicator:{iso}:{i}"
            out.append({"iso": iso, "kind": "indicator", "item": i, "field": "value", "tier": "",
                        "claim": claim, "state": state(claim, (iso, i) in have, passes, claimed),
                        "passes": str(passes[claim])})
    return out


def _row(label: str, counts: collections.Counter, total: int) -> str:
    gaps = total - counts["filled"]
    return (f"| {label} | {counts['filled']} of {total} | {gaps} | {counts['claimed_unverified']} | "
            f"{counts['not_searched']} | {counts['searched_once']} | {counts['dry']} |")


HEAD = ("| | Have | Gaps | Claimed, not verified | Never searched | Searched once | Searched twice, not found |\n"
        "|---|---|---|---|---|---|---|")


def render(cs: list[dict[str, str]]) -> str:
    holdings = [c for c in cs if c["kind"] == "holding"]
    reg = [c for c in holdings if c["field"] == "register"]
    out = ["# Gaps: what the data does not have yet",
           "",
           "Generated by `python3 model/gaps.py` from the registers and the staged research runs; `./test.sh` fails",
           "when this copy is stale. Edit the generator, never this file.",
           "",
           "**How to read it.** Each cell is a (state, holding class, field) or a (state, indicator). A gap is one",
           "of four kinds, which decide what to do next:",
           "- **Claimed, not verified.** A research run found a source, but its quote failed the fetch-and-hash",
           "  check or the review. The cheapest gap to close: a better or reachable source for something already",
           "  found.",
           "- **Never searched.** No run has looked for it yet.",
           "- **Searched once.** One pass found nothing. It needs a second, independent pass.",
           "- **Searched twice, not found.** Dry under the stop rule. A third pass needs a new kind of source",
           "  (procurement notices, audit-office reports, parliamentary answers), or the absence is the finding.",
           "",
           "A holding that a source says is not held is data, not a gap. The fields of a holding not yet found",
           "follow its register, so only the register is counted for it.",
           "",
           "## Holdings: is the register known?",
           "",
           f"{len([c for c in reg if c['state'] == 'filled'])} of {len(reg)} (state, class) pairs that are not",
           "established as absent have a known register.",
           "",
           HEAD]
    for tier in sorted({c["tier"] for c in reg}):
        sub = [c for c in reg if c["tier"] == tier]
        out.append(_row(f"Tier {tier}", collections.Counter(c["state"] for c in sub), len(sub)))
    out.append(_row("**All**", collections.Counter(c["state"] for c in reg), len(reg)))
    out += ["", "## Fields of the known holdings", "", HEAD]
    known = {(c["iso"], c["item"]) for c in reg if c["state"] == "filled"}
    for field in FIELDS:
        if field == "register":
            continue
        sub = [c for c in holdings if c["field"] == field and (c["iso"], c["item"]) in known]
        out.append(_row(f"`{field}`", collections.Counter(c["state"] for c in sub), len(sub)))
    out += ["", "## Registers not yet found, by class", "", HEAD]
    for cls in national_data.RECORD_CLASSES:
        sub = [c for c in reg if c["item"] == cls]
        counts = collections.Counter(c["state"] for c in sub)
        if counts["filled"] < len(sub):
            out.append(_row(f"`{cls}` (tier {national_data.TIER_OF[cls]})", counts, len(sub)))
    out += ["", "## By state", "",
            "| State | Registers known | Hosting known | Gaps | Claimed, not verified | Never searched | "
            "Searched once | Searched twice, not found |",
            "|---|---|---|---|---|---|---|---|"]
    for iso in national_data.countries():
        mine = [c for c in cs if c["iso"] == iso and (c["kind"] == "indicator" or c["field"] == "register"
                                                     or (c["iso"], c["item"]) in known)]
        counts = collections.Counter(c["state"] for c in mine)
        r = [c for c in reg if c["iso"] == iso]
        h = [c for c in holdings if c["iso"] == iso and c["field"] == "hosting" and (iso, c["item"]) in known]
        out.append(f"| {iso} | {sum(c['state'] == 'filled' for c in r)} of {len(r)} | "
                   f"{sum(c['state'] == 'filled' for c in h)} of {len(h)} | {len(mine) - counts['filled']} | "
                   f"{counts['claimed_unverified']} | {counts['not_searched']} | {counts['searched_once']} | "
                   f"{counts['dry']} |")
    ind = [c for c in cs if c["kind"] == "indicator"]
    out += ["", "## Indicators", "", HEAD]
    for i in sorted({c["item"] for c in ind}, key=[c["item"] for c in ind].index):
        sub = [c for c in ind if c["item"] == i]
        out.append(_row(f"`{i}`", collections.Counter(c["state"] for c in sub), len(sub)))
    out.append(_row("**All**", collections.Counter(c["state"] for c in ind), len(ind)))
    out += ["", "Country parameters are not listed here: `python3 model/provenance.py` reports their coverage.", ""]
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0].strip())
    ap.add_argument("--csv", help="also write one row per gap to this file (input for a research wave)")
    args = ap.parse_args(argv)
    cs = cells()
    OUT.write_text(render(cs), encoding="utf-8")
    gaps = [c for c in cs if c["state"] != "filled"]
    print(f"wrote {OUT.relative_to(ROOT)}: {len(gaps)} gaps in {len(cs)} cells")
    if args.csv:
        with open(args.csv, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(cs[0]), lineterminator="\n")
            w.writeheader()
            w.writerows(gaps)
        print(f"wrote {args.csv}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
