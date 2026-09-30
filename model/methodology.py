#!/usr/bin/env python3
"""
The methodology appendix: how every fact was sourced and every figure calculated, generated.

    python3 model/methodology.py        # print the document as JSON

Why this file exists
--------------------
A methodology written by hand drifts from the method. That is how "every fact was fetched, hashed and
checked" came to be printed over citations that were never checked (#82). So this appendix states
nothing of its own: every rule is the constant the code runs (`evidence`, `document`, `sovereignty`,
`fetch_eurostat`), and every number is counted from the files the build reads. It is a content-model
document like a country's, so the EU-27 report, each country PDF and the web page render the same text.

What it cannot carry is the git commit: a commit hash in a committed file changes with every commit.
The PDFs stamp the commit and the bundle's sha256 when they are built (book/report.py).
"""
from __future__ import annotations

import collections
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "model"))
import document  # noqa: E402
import evidence  # noqa: E402
import sovereignty as sv  # noqa: E402

label, method = document.label, document.method


def _rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def _p(text: str) -> dict:
    return {"type": "p", "spans": [method(text)]}


def _table(columns: list[str], rows: list[list[str]], align: list[str] | None = None) -> dict:
    return {"type": "table", "columns": [label(c) for c in columns],
            "align": align or ["left"] * len(columns),
            "rows": [[label(r[0])] + [method(str(v)) for v in r[1:]] for r in rows]}


def _list(items: list[str]) -> dict:
    return {"type": "list", "items": [[method(t)] for t in items]}


def build(documents: dict, claims: dict, sources: dict) -> dict:
    """The appendix, from the finished documents and claims of this build."""
    staging = ROOT / "model" / "research"
    verification = collections.Counter(r["match"] for r in _rows(staging / "verification.csv"))
    recheck = collections.Counter(r["outcome"] for r in _rows(staging / "recheck.csv"))
    vet_outcomes = _rows(staging / "vetting" / "outcomes.csv")
    vet_results = collections.Counter(r["result"] or r["status"] for r in vet_outcomes)
    runs = sorted({json.loads(p.read_text(encoding="utf-8")).get("run", "") for p in (staging / "vetting").glob("[A-Z][A-Z].json")} - {""})
    models = sorted({json.loads(p.read_text(encoding="utf-8")).get("reviewer_model", "") for p in (staging / "vetting").glob("[A-Z][A-Z].json")} - {""})

    spans = [s for d in documents.values() for s in document.walk_spans(d)]
    roles = collections.Counter(s["role"] for s in spans)
    grades = collections.Counter(s.get("g") for s in spans if s["role"] == "fact")
    tiers = collections.Counter(min(c["checks"]["tier"] for c in cs) for cs in claims.values())

    from fetch_eurostat import SERIES  # noqa: PLC0415 -- a data table; importing it fetches nothing
    eurostat = [[col, ds, "; ".join(f"{k}={v}" for k, v in sorted(f.items())), period,
                 f"× {mult:g}", str(dec)] for col, (ds, f, mult, dec, period) in SERIES.items()]

    sections = [
        {"id": "m-status", "title": "What this is, and what it is not", "blocks": [
            {"type": "callout", "tone": "notice", "spans": [method(evidence.DISCLAIMER)]},
            _p(f"This appendix is generated from the code and data that produced this document. Every rule "
               "below is the rule the build runs, and every number is counted from the files it reads. "
               f"In this build: {roles['fact']} facts are printed, {roles['gap']} values are withheld as "
               f"gaps, and {roles['disputed']} are withheld as disputed."),
        ]},
        {"id": "m-sourcing", "title": "How sources were found", "blocks": [
            _p("Research agents, one per member state, looked for each critical holding and each "
               "indicator. Each claim needed a verbatim quote of 8 to 60 words from an exact URL. Nothing an "
               "agent returned was used until it passed the mechanical checks below. Agent output is staged "
               "separately and is never rendered."),
            _table(["Quote check of the first research runs", "Claims"],
                   [[k, verification[k]] for k in ("exact", "loose", "not_found", "fetch_failed") if verification[k]],
                   ["left", "right"]),
            _p("A vetting run then re-examined every printed fact, and after it the gaps. It looked for a "
               "better source, for newer information and for any source that disagrees. Each of its "
               "findings was judged by a blind reviewer, shown the quote and URL but never the proposed "
               f"value. Runs: {', '.join(runs) or 'none yet'}. Reviewer model: {', '.join(models) or 'n/a'}, "
               "the same model as the researcher."),
            *([_table(["Vetting outcome", "Findings or items"], sorted([[k, n] for k, n in vet_results.items()]),
                      ["left", "right"])] if vet_results else []),
            _p("Every cited source is re-fetched periodically and each quote looked for again. A fact whose "
               "quote has vanished, or whose source is gone, is withheld as disputed. A refusal to serve "
               "the page changes nothing."),
            *([_table(["Latest recheck", "Sources"], sorted([[k, n] for k, n in recheck.items()]),
                      ["left", "right"])] if recheck else []),
        ]},
        {"id": "m-checks", "title": "What must hold for a fact to be printed", "blocks": [
            _list([f"{name}: {what}" for name, what in evidence.CHECKS]),
            _p("The printed value is checked against its quote at build time. Every number and date in it "
               "must appear in the original-language quote, read in any EU number format. A number found "
               "only in the English translation does not count. An abbreviation not found in the quote is "
               "shown in the fact's checklist. A value that is not a verbatim extract is a machine summary "
               "of the quote, and is labelled as one."),
            _p(evidence.WITHHELD),
        ]},
        {"id": "m-tiers", "title": "Source tiers", "blocks": [
            _p("How good is the best source behind each fact? Each cited host is classified once. An "
               "archived copy counts as the page it archived. The classification was drawn up by an agent "
               "and has not been reviewed by a person."),
            _table(["Tier", "Printed facts"], [[evidence.TIERS[t], tiers[t]] for t in sorted(evidence.TIERS)],
                   ["left", "right"]),
        ]},
        {"id": "m-grades", "title": "Evidence grades", "blocks": [
            _p(evidence.GRADE_RULE),
            _table(["Grade", "Printed facts"], [[g, grades[g]] for g in (evidence.STRONG, evidence.STANDARD)],
                   ["left", "right"]),
            _p("There is no numeric confidence score: nothing has calibrated one."),
        ]},
        {"id": "m-calculations", "title": "Calculations", "blocks": [
            _p(f"Priority of a holding. {document.PRIORITY_RULE}"),
            _p("Infrastructure exposure counts, for each state, the verified holdings whose cited source "
               "says where the infrastructure runs. Silence counts as not stated, never as national."),
            _p(f"Data-sovereignty placement. {sv.UNKNOWN_RULE} Each state is placed by the first rule it "
               "meets, in this order:"),
            _list([f"{sv.LABELS[g]}: {t}." for g, t in sv.RULE]),
            _p(sv.CONFIDENCE_RULE),
            _p("Fundamentals are Eurostat values at a pinned period, read through the dissemination API. "
               "Each is multiplied into the unit shown and rounded, and must reproduce the published "
               "value within 0.5%:"),
            _table(["Figure", "Dataset", "Filters", "Period", "Scale", "Decimals"], eurostat),
        ]},
        {"id": "m-ask", "title": "Questions answered on the web", "blocks": [
            _p("The web page's Ask feature answers questions using only these sourced findings, with a "
               "citation for every fact. Each question is sent to Anthropic's API to generate the answer "
               "and is not stored by this site. The model is told the findings are machine-checked and to "
               "say so in every answer."),
        ]},
        {"id": "m-reproduce", "title": "Reproducing this document", "blocks": [
            _p("Everything is built from the project's repository. `./run.sh reproduce` rebuilds every "
               "output in a fresh clone and compares it with the published one. `./run.sh reproduce "
               "--evidence` also re-fetches every cited source and checks every quote again. The git "
               "commit and the data bundle's SHA-256 this document was built from are printed on its "
               "title page."),
            _p("Not reproducible byte for byte: agent research gives different findings if run again, so "
               "what is reproducible is their admission, from the recorded outputs. Also not: the posters "
               "(browser screenshots), and the hash of a page rendered in a browser."),
        ]},
        {"id": "m-limits", "title": "What this does not establish", "blocks": [
            _list([
                "No person has verified any finding. Agents found and checked everything.",
                "The blind reviewer was the same model as the researcher, so the two readings can share its "
                "blind spots.",
                "English wording of a non-English source is a machine translation or machine summary. Its "
                "figures are checked against the original; its words are not.",
                "A gap means not yet sourced. It never means the thing does not exist.",
                "Most states do not publish where their critical registers are hosted, so placements are "
                "mostly of low confidence. That is a finding about transparency, not about sovereignty.",
            ]),
        ]},
    ]
    return {"iso": "", "name": "Methodology", "sections": sections}


if __name__ == "__main__":
    b = json.loads((ROOT / "web" / "public" / "data" / "eu27.json").read_text(encoding="utf-8"))
    print(json.dumps(build(b["documents"], b["claims"], b["sources"]), indent=1, ensure_ascii=False))
