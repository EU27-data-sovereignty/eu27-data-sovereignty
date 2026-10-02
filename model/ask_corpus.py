#!/usr/bin/env python3
"""
Build the corpus /ask answers from: api/_corpus.json (DECISIONS.md #78).

    python3 model/ask_corpus.py          # write api/_corpus.json from the bundle
    python3 model/ask_corpus.py --check  # exit 1 if the file is stale

Why this file exists
--------------------
/ask may answer only from this project's sourced data (#75, #78). The function hands the model a
set of documents with citations enabled, and every citation comes back as a block index. So the
corpus is built from the content model (`document.py`) as small, self-contained blocks, one fact
each, and each block carries the claim ids it rests on. A citation to block 17 is therefore a
citation to specific claims, which the page resolves to their quote, URL, hash and archived copy.

What goes in, and what never does:

    fact    the value, with its claim ids              -> cited answer
    gap     "not yet sourced" for that row             -> the model can say what is unknown
    method  the project's rules (priority, ranking)    -> explains, never a fact about a state

An unsourced value never enters the corpus: the content model has already withheld it as a gap,
and this file only copies spans. That is what stops /ask from saying anything the site would not.

Deterministic, sorted, standard library only.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUNDLE = ROOT / "web" / "public" / "data" / "eu27.json"
OUT = ROOT / "api" / "_corpus.json"


def row_text(country: str, section: str, cells: list[dict], columns: list[dict]) -> tuple[str, list[str], str]:
    """One table row as a sentence-like block: 'Germany - Critical holdings - Tax: X; Operator: Y'."""
    label = cells[0]["t"]
    parts, claims, kinds = [], [], set()
    for col, cell in zip(columns[1:], cells[1:]):
        if cell.get("role") == "fact":
            parts.append(f"{col['t']}: {cell['t']}")
            claims += cell.get("c", [])
            kinds.add("fact")
        elif cell.get("role") in ("gap", "disputed") and cell["t"] not in ("—", ""):
            parts.append(f"{col['t']}: {cell['t'].lower()}")
            kinds.add("gap")
        elif cell.get("role") in ("method", "label") and cell["t"] not in ("—", ""):
            parts.append(f"{col['t']}: {cell['t']}")
            kinds.add("method")
    kind = "fact" if "fact" in kinds else ("gap" if "gap" in kinds else "method")
    return f"{country} — {section} — {label}: " + "; ".join(parts), claims, kind


def country_blocks(doc: dict) -> list[dict]:
    out = []
    for s in doc["sections"]:
        for b in s["blocks"]:
            if b["type"] == "table":
                unverified = []
                for row in b["rows"]:
                    # A holding with nothing verified is one name in a list, not a row of blanks:
                    # the model needs to know it is open, not read 39 empty rows.
                    if s["id"] == "holdings" and row[2].get("t") == "Not yet verified":
                        unverified.append(row[1]["t"])
                        continue
                    text, claims, kind = row_text(doc["name"], s["title"], row, b["columns"])
                    out.append({"text": text, "claims": sorted(set(claims)), "kind": kind})
                if unverified:
                    out.append({"text": f"{doc['name']} — {s['title']} — not yet verified by any "
                                        f"checked source: " + "; ".join(unverified) + ".",
                                "claims": [], "kind": "gap"})
            elif b["type"] in ("p", "callout"):
                spans = b["spans"]
                claims = sorted({c for sp in spans for c in sp.get("c", [])})
                kind = "fact" if claims else "method"
                out.append({"text": f"{doc['name']} — {s['title']}: " + " ".join(sp["t"] for sp in spans),
                            "claims": claims, "kind": kind})
            elif b["type"] == "list":
                for item in b["items"]:
                    out.append({"text": f"{doc['name']} — {s['title']}: " + " ".join(sp["t"] for sp in item),
                                "claims": sorted({c for sp in item for c in sp.get("c", [])}),
                                "kind": "method"})
    return out


def build(bundle: dict) -> dict:
    sov = bundle["sovereignty"]
    labels = {g["id"]: g["label"] for g in sov["groups"]}
    method = [
        {"text": "About this project: an independent analysis of each EU member state's critical "
                 "government data holdings, analysed on each state's own fundamentals. It is not "
                 "affiliated with any government or EU body.", "claims": [], "kind": "method"},
        {"text": "Sourcing rule: a value is shown only when a document was fetched, its SHA-256 "
                 "recorded and the quoted text found in it. Anything else is 'not yet sourced'.",
         "claims": [], "kind": "method"},
        {"text": "How holdings are prioritised: " + bundle["priority_rule"], "claims": [], "kind": "method"},
        {"text": "How the ranking works: states are placed in five groups by a published rule, never "
                 "scored. Groups in order: " + "; ".join(g["label"] for g in sov["groups"]) + ". An input "
                 "without a checked source counts as not demonstrated. Confidence is the range of "
                 "groups a state could still reach if its open evidence resolved for or against it: "
                 "one group High, two Medium, three or more Low.", "claims": [], "kind": "method"},
        {"text": "Guardrail: " + sov["guardrail"], "claims": [], "kind": "method"},
        {"text": "Capacity (servers, power, sites, cost) is not yet sized for any state.",
         "claims": [], "kind": "method"},
    ]
    names = {iso: d["name"] for iso, d in bundle["documents"].items()}
    ranking = []
    for iso in sorted(sov["placements"], key=lambda i: names[i]):
        p = sov["placements"][iso]
        claims = sorted(f"indicator:{iso}:{i}" for i, v in p["indicators"].items()
                        if v != "unknown" and f"indicator:{iso}:{i}" in bundle["claims"])
        ranking.append({
            "text": f"{names[iso]} ({iso}) is placed in '{labels[p['group']]}', confidence {p['confidence']}; "
                    f"with its open evidence it could be anywhere from '{labels[p['range'][0]]}' to "
                    f"'{labels[p['range'][-1]]}'.",
            "claims": claims, "kind": "method"})
    # How every printed fact was checked by the model that did not write it (#87): the EU-27 appendix,
    # flattened to text. The per-fact verdicts stay in the PDFs and on the web page.
    checked = []
    for sec in bundle["factcheck"]["eu"]["sections"]:
        for b in sec["blocks"]:
            lines = ([b["spans"]] if b["type"] in ("p", "callout") else b["items"] if b["type"] == "list"
                     else [[*row] for row in b["rows"]])
            sep = " | " if b["type"] == "table" else " "
            checked += [{"text": f"{sec['title']}: " + sep.join(sp["t"] for sp in line), "claims": [],
                         "kind": "method"} for line in lines]
    documents = [
        {"title": "Method and rules", "blocks": method},
        {"title": "Fact check: how each printed fact was checked by a second model", "blocks": checked},
        {"title": "Data-sovereignty ranking (placements by rule, with confidence)", "blocks": ranking},
    ]
    for iso in sorted(bundle["documents"], key=lambda i: names[i]):
        documents.append({"title": f"{names[iso]} ({iso})", "iso": iso,
                          "blocks": country_blocks(bundle["documents"][iso])})
    return {"generated": bundle["generated"], "schema_version": 1, "documents": documents}


def render(corpus: dict) -> str:
    return json.dumps(corpus, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args(argv)
    text = render(build(json.loads(BUNDLE.read_text(encoding="utf-8"))))
    if args.check:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != text:
            print("api/_corpus.json is stale; run ./run.sh data", file=sys.stderr)
            return 1
        return 0
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(text, encoding="utf-8")
    blocks = sum(len(d["blocks"]) for d in json.loads(text)["documents"])
    print(f"{OUT.relative_to(ROOT)}: {blocks} blocks, {len(text):,} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
