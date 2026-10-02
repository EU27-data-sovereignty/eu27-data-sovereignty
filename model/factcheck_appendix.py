#!/usr/bin/env python3
"""
The fact-check appendix every asset carries: how each printed fact was checked by a second model (#87).

    python3 model/factcheck_appendix.py [ISO]     # print the document as JSON

Why this file exists
--------------------
The audit file (docs/fact-check-audit.md) is for someone auditing the repository. A reader of one PDF,
one brief or one web page should not need the repository to see how the facts in front of them were
checked. So each asset carries the process in full and, for a country, the verdict on each of its own
facts. Like the methodology appendix (methodology.py), it states nothing of its own: the rule and the
steps are factcheck.py's constants, and every row is read from the ledger and the run manifests.

Its spans are `method` and `label`, never `fact`: it reports on the facts without printing their values,
so it adds nothing that would itself need checking.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "model"))
import document  # noqa: E402
import evidence  # noqa: E402
import factcheck  # noqa: E402

label, method = document.label, document.method
TITLE = "Fact check"


def _p(text: str) -> dict:
    return {"type": "p", "spans": [method(text)]}


def _table(columns: list[str], rows: list[list], align: list[str] | None = None) -> dict:
    return {"type": "table", "columns": [label(c) for c in columns],
            "align": align or ["left"] * len(columns),
            "rows": [[label(str(r[0]))] + [method(str(v)) for v in r[1:]] for r in rows]}


def _status(why: str, row: dict | None) -> str:
    if not why:
        return "supported"
    return why if row is None or why.startswith("changed") else row["verdict"].replace("_", " ")


def process(s: dict) -> list[dict]:
    """The sections every asset shares: what the check is, the rule, the steps, the runs."""
    runs = factcheck.manifests()
    return [
        {"id": "f-what", "title": "What was checked, and by whom", "blocks": [
            {"type": "callout", "tone": "notice", "spans": [method(
                f"{evidence.DISCLAIMER} The check below is made by a second model, not by a person.")]},
            _p("Every printed fact is put, exactly as printed, to a checker that is a different model from the "
               "one that wrote it. The checker fetches the cited source and decides whether it supports the "
               "statement as printed: the same value, name, unit, date, country and scope. A production "
               "deploy is refused unless every printed fact has a current verdict of supported from an "
               "eligible checker."),
            _p(f"In this build, {s['passing']} of {s['printed']} printed facts pass."),
            _table(["Fact written by", "Checked by"], factcheck.RULE),
        ]},
        {"id": "f-steps", "title": "How a check runs", "blocks": [
            {"type": "list", "items": [[method(t.replace("`", "").replace("*", ""))] for t in factcheck.STEPS]},
            _p("A verdict holds for one fact exactly as printed: a SHA-256 of the claim, the question it "
               "answers, the printed text and every citation behind it. If any of these changes, the verdict "
               "lapses and the fact must be checked again before the next deploy."),
        ]},
        {"id": "f-runs", "title": "Fact-check runs", "blocks": [
            _table(["Run", "Date", "Facts checked", "Checker models", "Verdicts"],
                   [[m["run"], m["date"], m["facts_checked"],
                     "; ".join(f"{k}: {n}" for k, n in m["checker_model"].items()),
                     "; ".join(f"{k.replace('_', ' ')}: {n}" for k, n in m["verdicts"].items() if n) or "none"]
                    for m in runs], ["left", "left", "right", "left", "left"])
            if runs else _p("No fact-check run has been recorded yet, so no printed fact has been checked."),
        ]},
    ]


def build(documents: dict, claims: dict, sources: dict) -> dict:
    """{"eu": the EU-27 appendix, "countries": {iso: that country's appendix}, "lines": {iso: the poster's
    one-line summary}} for this build."""
    bundle = {"documents": documents, "claims": claims, "sources": sources}
    ledger = factcheck.load_ledger()
    rows = factcheck.assess(bundle, ledger)
    s = factcheck.summary(bundle)
    names = {iso: d["name"] for iso, d in documents.items()}
    who = factcheck.authors(bundle)

    per_state = []
    for iso in sorted(documents, key=lambda i: names[i]):
        mine = [why for f, _, why in rows if f["iso"] == iso]
        per_state.append([names[iso], len(mine), sum(1 for w in mine if not w), sum(1 for w in mine if w)])
    eu = {"iso": "", "name": TITLE, "sections": process(s) + [
        {"id": "f-states", "title": "Facts checked, by member state", "blocks": [
            _table(["Member state", "Printed facts", "Supported", "Not passing"], per_state,
                   ["left", "right", "right", "right"]),
            _p("Each country report lists the verdict on every one of its facts in its own fact-check "
               "appendix. Every disagreement ever recorded, with the checker's reason, is in the project's "
               "audit file, docs/fact-check-audit.md."),
        ]},
    ]}

    # One line per country for the poster, which cannot carry the appendix itself.
    lines = {}
    for iso in documents:
        mine = [why for f, _, why in rows if f["iso"] == iso]
        models = sorted({ledger[f["claim"]]["checker_model"] for f, _, why in rows
                         if f["iso"] == iso and not why})
        lines[iso] = (f"Fact check: {sum(1 for w in mine if not w)} of {len(mine)} facts confirmed by a second "
                      f"model that did not write them ({', '.join(models) or 'none yet'}); not by a person. "
                      f"How: /fact-check/{iso}")

    countries = {}
    for iso in documents:
        table = [[f["claim"], f["what"], "; ".join(sorted(who[f["claim"]])),
                  ledger.get(f["claim"], {}).get("checker_model", "") or "none",
                  _status(why, ledger.get(f["claim"])), ledger.get(f["claim"], {}).get("run", "")]
                 for f, _, why in rows if f["iso"] == iso]
        countries[iso] = {"iso": iso, "name": TITLE, "sections": process(s) + [
            {"id": "f-facts", "title": f"The verdict on each fact about {names[iso]}", "blocks": [
                _p(f"{sum(1 for r in table if r[4] == 'supported')} of {len(table)} printed facts about "
                   f"{names[iso]} pass."),
                _table(["Claim", "What it answers", "Written by", "Checked by", "Verdict", "Run"], table),
            ]},
        ]}
    return {"eu": eu, "countries": countries, "lines": lines}


if __name__ == "__main__":
    b = json.loads(factcheck.BUNDLE.read_text(encoding="utf-8"))
    out = build(b["documents"], b["claims"], b["sources"])
    print(json.dumps(out["countries"][sys.argv[1]] if len(sys.argv) > 1 else out["eu"], indent=1,
                     ensure_ascii=False))
