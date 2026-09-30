#!/usr/bin/env python3
"""
Build the vetting run's input: per state, every printed fact and every open gap to work on (#83).

    python3 model/research/vetting/build_input.py > input.json

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


def main() -> int:
    b = json.loads((ROOT / "web" / "public" / "data" / "eu27.json").read_text(encoding="utf-8"))
    classes = {r["class_id"]: r for r in csv.DictReader((ROOT / "model" / "holding_classes.csv").open())}
    indicators = {r["id"]: r for r in csv.DictReader((ROOT / "model" / "indicators.csv").open())}
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
            parts = claim.split(":")
            what = (f"{classes[parts[2]]['label']}: {KIND.get(parts[3], parts[3])}" if parts[0] == "record"
                    else f"indicator {parts[2]}: {indicators[parts[2]]['question']}" if parts[0] == "indicator"
                    else claim)
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
