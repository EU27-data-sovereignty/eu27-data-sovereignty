#!/usr/bin/env python3
"""
Place each member state in a data-sovereignty group, by a published rule, with its confidence.

    python3 model/sovereignty.py            # the placement of all 27, with range and confidence
    python3 model/sovereignty.py DE         # one country, with why and what could move it

Why a rule and not a score (DECISIONS.md #77, amending #10)
------------------------------------------------------------
The dimensions do not add: a statute and a data centre are not commensurable, and a weighted index
would invent a precision the evidence does not have. So a state is placed in one of five named groups
by a decision rule over sourced indicators, evaluated in order, first match wins:

    dependent           a sourced non-EU dependency for a tier 0/1 holding, or a non-EU / uncontrolled
                        national eID or trust anchor (K1 or K2 = no). Checked first: an evidenced
                        dependency outweighs any protection on paper.
    law_and_practice    L1 = yes, and practice: H1 (>= 75% of verified tier 0/1 holdings on national or
                        EU infrastructure, per sources), K1 = yes, K2 = yes, and C1 or C2 = yes
    practice_only       practice as above, but L1 is not yes
    law_only            L1 = yes, practice not demonstrated
    not_demonstrated    neither

Display order is best to worst: law_and_practice, practice_only, law_only, not_demonstrated,
dependent. Within a group states are alphabetical: the group is the finding.

Confidence is computed, not asserted
------------------------------------
Every input a source does not settle is *unknown*. The placement treats an unknown as not
demonstrated -- never as sovereign, never as dependent. Then the rule is run twice more: once with
every unknown resolved in the state's favour, once against it. The groups those give are the range
the state could be in once the research is finished. One group is High confidence, two Medium, three
or more Low. The unknowns that set the range are the explanation.

The rule is monotone -- improving any input never worsens the group -- so the placement always lies
inside its range. tests/test_sovereignty.py checks that on every combination.
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDICATORS = ROOT / "model" / "indicators.csv"
VALUES = ROOT / "model" / "sovereignty_indicators.csv"

GROUPS = ["law_and_practice", "practice_only", "law_only", "not_demonstrated", "dependent"]
LABELS = {
    "law_and_practice": "Sovereign in law and in practice",
    "practice_only": "Sovereign in practice, not secured in law",
    "law_only": "Secured in law, not yet in practice",
    "not_demonstrated": "Not demonstrated",
    "dependent": "Dependent on non-EU providers",
}
CONFIDENCE = {1: "High", 2: "Medium"}          # width of the range; 3 or more is Low
H1_SHARE = 0.75
VALUE = ("yes", "partial", "no")
GUARDRAIL = ("Groups describe what the sources show, not how sovereign a state is. A Low-confidence "
             "placement mostly reflects research that is not finished.")


def indicator_defs() -> list[dict[str, str]]:
    with INDICATORS.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


INDICATOR_IDS = tuple(r["id"] for r in indicator_defs())


# --------------------------------------------------------------------------- #
# The rule
# --------------------------------------------------------------------------- #

def group(v: dict) -> str:
    """The rule on fully resolved inputs. v: L1..C2 in yes/partial/no, h1: bool, h2: bool."""
    if v["h2"] or v["K1"] == "no" or v["K2"] == "no":
        return "dependent"
    law = v["L1"] == "yes"
    practice = (v["h1"] and v["K1"] == "yes" and v["K2"] == "yes"
                and (v["C1"] == "yes" or v["C2"] == "yes"))
    if law and practice:
        return "law_and_practice"
    if practice:
        return "practice_only"
    if law:
        return "law_only"
    return "not_demonstrated"


def resolve(indicators: dict[str, str], holdings: list[dict], mode: str) -> dict:
    """Turn a state's evidence into rule inputs.

    mode "evidenced": an unknown is neither yes nor no (not demonstrated, not dependent).
    mode "best": every unknown resolves in the state's favour.
    mode "worst": every unknown resolves against it.
    """
    v: dict = {}
    for i in INDICATOR_IDS:
        x = indicators.get(i, "unknown")
        if x == "unknown":
            x = {"evidenced": "unknown", "best": "yes", "worst": "no"}[mode]
        v[i] = x

    core = [h for h in holdings if h["tier"] <= 1]
    verified = [h for h in core if h["status"] == "held"]
    dep = [h.get("foreign_dependency") or "unknown" for h in verified]
    open_classes = sum(1 for h in core if h["status"] == "unrecorded")
    national = sum(1 for d in dep if d in ("national", "eu_provider"))
    non_eu = sum(1 for d in dep if d in ("non_eu_provider", "mixed"))
    unknown = sum(1 for d in dep if d == "unknown")

    if mode == "evidenced":
        v["h1"] = bool(verified) and national / len(verified) >= H1_SHARE
        v["h2"] = non_eu > 0
    elif mode == "best":
        # Unknown dependencies and unresearched classes all turn out national or EU.
        total = len(verified) + open_classes
        v["h1"] = total > 0 and (national + unknown + open_classes) / total >= H1_SHARE
        v["h2"] = non_eu > 0
    else:
        # Any unknown dependency or unresearched class could turn out to run on non-EU infrastructure.
        v["h1"] = bool(verified) and national / (len(verified) + open_classes) >= H1_SHARE
        v["h2"] = non_eu > 0 or unknown > 0 or open_classes > 0
    return v


def place(indicators: dict[str, str], holdings: list[dict]) -> dict:
    """Group, range and confidence for one state. Returns ids, never a number to quote."""
    placed = group(resolve(indicators, holdings, "evidenced"))
    best = group(resolve(indicators, holdings, "best"))
    worst = group(resolve(indicators, holdings, "worst"))
    lo, hi = sorted((GROUPS.index(best), GROUPS.index(worst)))
    lo, hi = min(lo, GROUPS.index(placed)), max(hi, GROUPS.index(placed))
    span = GROUPS[lo:hi + 1]
    return {
        "group": placed,
        "range": span,
        "confidence": CONFIDENCE.get(len(span), "Low"),
        "could_move": could_move(indicators, holdings, placed),
    }


def could_move(indicators: dict[str, str], holdings: list[dict], placed: str) -> list[dict]:
    """Each single unknown that would, alone, change the group -- and to what."""
    out = []
    for i in INDICATOR_IDS:
        if indicators.get(i, "unknown") != "unknown":
            continue
        for value in ("yes", "no"):
            g = group(resolve({**indicators, i: value}, holdings, "evidenced"))
            if g != placed:
                out.append({"input": i, "if": value, "group": g})
    core = [h for h in holdings if h["tier"] <= 1]
    unsettled = [h for h in core if h["status"] == "unrecorded"
                 or (h["status"] == "held" and (h.get("foreign_dependency") or "unknown") == "unknown")]
    if unsettled:
        g = group({**resolve(indicators, holdings, "evidenced"), "h2": True})
        if g != placed:
            out.append({"input": "holdings", "if": "non_eu_found", "group": g,
                        "count": len(unsettled)})
    return out


# --------------------------------------------------------------------------- #
# Evidence
# --------------------------------------------------------------------------- #

def load_values() -> dict[str, dict[str, str]]:
    """Indicator values per state, from sovereignty_indicators.csv. Missing file: all unknown."""
    if not VALUES.exists():
        return {}
    out: dict[str, dict[str, str]] = {}
    with VALUES.open(newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            out.setdefault(r["iso"], {})[r["indicator"]] = r["value"]
    return out


def supported_values(iso: str, values: dict[str, str], supported) -> dict[str, str]:
    """Only a value a checked citation supports counts; anything else is unknown (#75)."""
    return {i: (v if v in VALUE and supported(f"indicator:{iso}:{i}") else "unknown")
            for i, v in values.items()}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("iso", nargs="?")
    args = ap.parse_args(argv)
    import document  # noqa: PLC0415
    import national_data as nd  # noqa: PLC0415

    src = document.Sources()
    register = nd.load()
    values = load_values()
    isos = [args.iso.upper()] if args.iso else sorted(provenance_isos())
    for iso in isos:
        ind = supported_values(iso, values.get(iso, {}), src.supported)
        p = place(ind, nd.for_country(register, iso))
        if args.iso:
            print(json.dumps(p, indent=1))
        else:
            print(f"{iso}  {LABELS[p['group']]:<42} {p['confidence']:<7} "
                  f"range: {LABELS[p['range'][0]]} .. {LABELS[p['range'][-1]]}")
    return 0


def provenance_isos() -> list[str]:
    import provenance  # noqa: PLC0415
    return list(provenance.parameters())


if __name__ == "__main__":
    sys.exit(main())
