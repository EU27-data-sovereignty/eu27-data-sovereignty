#!/usr/bin/env python3
"""
Build the vetting run's input: per state, every printed fact and every open gap to work on (#83).

    python3 model/research/vetting/build_input.py > input.json
    python3 model/research/vetting/build_input.py --wave hosting > input.json   # gaps only (docs/gaps.md)

Read from the bundle, so the researcher sees exactly what the report prints: the value, the source
behind it, that source's tier and date, and the evidence grade. Facts on the weakest sources come
first, because an agent that runs out of time should have spent it where it matters most.
"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "model"))
import document  # noqa: E402

KIND = {"register": "the name of the register or system", "operator": "the body that operates it",
        "count": "how many records it holds", "size": "its data size",
        "foreign_dependency": "where its infrastructure runs: national / eu_provider / non_eu_provider / mixed"}
# The questions a wave asks. Kept apart from KIND on purpose: factcheck.describe() reads KIND for each fact's
# "what", which is part of the fact's hash (#87), so changing KIND would re-open every checked fact of that kind.
WAVE_KIND = {**KIND, "hosting": "where its data is hosted and who runs that infrastructure: the data centre, "
                                "the hosting or cloud provider, or the body that operates its IT systems"}

# A wave: research only these fields of the holdings already known, no re-vetting of printed facts. Each
# gap is one docs/gaps.md calls not filled, so a wave is the gap list turned into work.
WAVES = {"hosting": ("hosting", "foreign_dependency")}


def tables() -> tuple[dict, dict]:
    """The holding classes and indicator definitions a claim id refers to."""
    with (ROOT / "model" / "holding_classes.csv").open(newline="", encoding="utf-8") as fh:
        classes = {r["class_id"]: r for r in csv.DictReader(fh)}
    with (ROOT / "model" / "indicators.csv").open(newline="", encoding="utf-8") as fh:
        indicators = {r["id"]: r for r in csv.DictReader(fh)}
    return classes, indicators


def describe(claim: str, classes: dict, indicators: dict) -> str:
    """What a printed fact answers, in words: the question its value is the answer to."""
    parts = claim.split(":")
    return (f"{classes[parts[2]]['label']}: {KIND.get(parts[3], parts[3])}" if parts[0] == "record"
            else f"indicator {parts[2]}: {indicators[parts[2]]['question']}" if parts[0] == "indicator"
            else claim)


def wave(name: str) -> list[dict]:
    """Per state, only gaps: the wave's fields of every known holding that has none yet, tier 0 first."""
    import gaps  # noqa: PLC0415
    classes, _ = tables()
    b = json.loads((ROOT / "web" / "public" / "data" / "eu27.json").read_text(encoding="utf-8"))
    field_of = {kind: field for field, kind in gaps.FIELDS.items()}
    want = {field_of[k] for k in WAVES[name]}
    todo = [c for c in gaps.cells() if c["kind"] == "holding" and c["field"] in want and c["state"] != "filled"]
    import national_data  # noqa: PLC0415
    rows = {(r["iso"], r["record_class"]): r for r in national_data.read_rows()}

    def holding(iso: str, cls: str) -> str:
        """The class, and the register the report already names for it, so the search starts from the name."""
        r = rows[(iso, cls)]
        return (f"{classes[cls]['label']} (the register: {r['register']}"
                + (f"; operated by {r['holder']}" if r["holder"] else "") + ")")

    out = []
    for iso, doc in sorted(b["documents"].items()):
        mine = sorted((c for c in todo if c["iso"] == iso), key=lambda c: (int(c["tier"]), c["item"], c["field"]))
        out.append({"iso": iso, "name": doc["name"], "facts": [], "gaps": [
            {"claim": c["claim"], "tier": int(c["tier"]),
             "what": f"{holding(iso, c['item'])}: {WAVE_KIND[gaps.FIELDS[c['field']]]}"} for c in mine]})
    return out


def main() -> int:
    if "--wave" in sys.argv:
        json.dump(wave(sys.argv[sys.argv.index("--wave") + 1]), sys.stdout, ensure_ascii=False, indent=1)
        return 0
    b = json.loads((ROOT / "web" / "public" / "data" / "eu27.json").read_text(encoding="utf-8"))
    classes, indicators = tables()
    out = []
    for iso, doc in sorted(b["documents"].items()):
        facts = []
        for span in document.walk_spans(doc):
            if span.get("role") != "fact":
                continue
            claim = span["c"][0]
            if claim.startswith("param:") and b["claims"][claim][0]["checks"].get("dataset_value_reproduced"):
                continue                    # Eurostat: vetted by fetch_eurostat.py, not by an agent
            best = min(b["claims"][claim], key=lambda c: c["checks"]["tier"])
            src = b["sources"][best["source_id"]]
            what = describe(claim, classes, indicators)
            facts.append({"claim": claim, "what": what, "printed": span["t"], "source_url": src["url"],
                          "tier": best["checks"]["tier"], "source_kind": best["checks"]["tier_kind"],
                          "published": src.get("published", ""), "grade": best["grade"]})
        facts.sort(key=lambda f: (-f["tier"], f["grade"] != "Standard", f["claim"]))
        entries = b["countries"][iso]["national_data"]
        gaps = [{"claim": f"record:{iso}:{e['record_class']}:register", "tier": e["tier"],
                 "what": f"{classes[e['record_class']]['label']}: {classes[e['record_class']]['contains']}"}
                for e in entries if e["status"] == "unrecorded" and e["tier"] <= 1]
        placed = b["sovereignty"]["placements"][iso]["indicators"]
        gaps += [{"claim": f"indicator:{iso}:{i}", "tier": None,
                  "what": f"{indicators[i]['question']} yes = {indicators[i]['yes']}; partial = "
                          f"{indicators[i]['partial']}; no = {indicators[i]['no']}"}
                 for i, v in sorted(placed.items()) if v == "unknown"]
        out.append({"iso": iso, "name": doc["name"], "facts": facts, "gaps": gaps})
    json.dump(out, sys.stdout, ensure_ascii=False, indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main())
