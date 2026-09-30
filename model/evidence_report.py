#!/usr/bin/env python3
"""
Write docs/evidence.md: the state of the evidence behind every printed fact, with charts.

    python3 model/evidence_report.py        # regenerate docs/evidence.md from the bundle

Why this file exists
--------------------
A description of the evidence written by hand drifts from the evidence, which is how "every fact was
fetched, hashed and checked" came to be printed over figures that were never hashed (#82). This page is
generated from web/public/data/eu27.json on every `./run.sh data`, and ./test.sh fails when the
committed copy differs from a fresh one. Its charts are Mermaid, so GitHub renders them from text and a
diff shows exactly what moved.
"""
from __future__ import annotations

import collections
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "model"))
import document  # noqa: E402
import evidence  # noqa: E402

BUNDLE = ROOT / "web" / "public" / "data" / "eu27.json"
OUT = ROOT / "docs" / "evidence.md"

KIND = {"register": "Register or system", "operator": "Operator", "count": "Record count",
        "size": "Data size", "foreign_dependency": "Infrastructure dependency",
        "legal_basis": "Legal basis", "hosting": "Hosting"}

# Why a fact is Standard rather than Strong: each Strong condition it misses (a fact can miss several).
SHORTFALLS = [
    ("Best source below T2 (e.g. an unofficial law mirror)", lambda c: c["tier"] > 2),
    ("Machine summary of a non-English quote, no figure to match",
     lambda c: c["language"] != "english" and c.get("value") in ("summary", "verbatim_gloss")
     and not c.get("figures_matched")),
    ("No archived copy of exactly this URL", lambda c: not c["archived"]),
    ("Categorical: review agreed but was not blind", lambda c: "review" in c),
    ("A name in the value is not in the quote", lambda c: bool(c.get("names_not_in_quote"))),
    ("Dataset response not yet hashed", lambda c: not c["document_hashed"]),
    ("Secondary source or statement of absence", lambda c: c["source"] not in ("primary", "official")),
    ("Quote matched loosely (punctuation)", lambda c: c.get("quote_match") == "loose"),
]


def kind_of(claim: str) -> str:
    ns = claim.split(":")[0]
    if ns == "record":
        return KIND.get(claim.split(":")[-1], claim.split(":")[-1])
    return {"param": "Eurostat fundamental or posture", "indicator": "Sovereignty indicator"}.get(ns, ns)


def facts(b: dict):
    """(iso, span, best citation) for every printed fact."""
    for iso, doc in sorted(b["documents"].items()):
        for span in document.walk_spans(doc):
            if span.get("role") == "fact":
                yield iso, span, b["claims"][span["c"][0]][0]


def build(b: dict) -> str:
    rows = list(facts(b))
    gaps = collections.Counter(iso for iso, doc in b["documents"].items()
                               for s in document.walk_spans(doc) if s.get("role") == "gap")
    by_state = collections.defaultdict(collections.Counter)
    by_kind = collections.defaultdict(collections.Counter)
    shortfall = collections.Counter()
    tiers = collections.Counter()
    tier_kinds = collections.Counter()
    mirrors = collections.Counter()
    for iso, span, best in rows:
        top = min(b["claims"][span["c"][0]], key=lambda c: c["checks"]["tier"])["checks"]
        t = top["tier"]
        tiers[t] += 1
        tier_kinds[(t, top["tier_kind"])] += 1
        if top["tier_kind"] == "unofficial_law_mirror":
            mirrors[iso] += 1
        by_state[iso][span["g"]] += 1
        by_kind[kind_of(span["c"][0])][span["g"]] += 1
        if span["g"] == evidence.STANDARD:
            for name, test in SHORTFALLS:
                if test(best["checks"]):
                    shortfall[name] += 1
    strong = sum(c[evidence.STRONG] for c in by_state.values())
    standard = sum(c[evidence.STANDARD] for c in by_state.values())
    isos = sorted(b["documents"])

    def bar(title: str, values: list[int], y: str) -> list[str]:
        top = max(values + [1])
        return ["```mermaid", "xychart-beta", f'  title "{title}"',
                f"  x-axis [{', '.join(isos)}]", f'  y-axis "{y}" 0 --> {top}',
                f"  bar [{', '.join(str(v) for v in values)}]", "```"]

    out = [
        "# The evidence behind every printed fact",
        "",
        f"> Generated {b['generated']} by `model/evidence_report.py` from the bundle. Do not edit by hand:",
        "> `./run.sh data` rewrites it and `./test.sh` fails if it is stale.",
        ">",
        f"> **{b['notice']['disclaimer']}**",
        "",
        "## At a glance",
        "",
        "| | Count |",
        "|---|---:|",
        f"| Printed facts | {len(rows)} |",
        f"| Strong | {strong} |",
        f"| Standard | {standard} |",
        f"| Gaps (values withheld) | {sum(gaps.values())} |",
        "",
        "```mermaid",
        "pie showData",
        '  title "Printed facts by evidence grade"',
        f'  "Strong" : {strong}',
        f'  "Standard" : {standard}',
        "```",
        "",
        f"**How grades are set.** {b['notice']['grade_rule']}",
        "",
        "## Source tiers",
        "",
        "How good is the best source behind each printed fact? Tiers are set per host in "
        "[`model/sources/authorities.csv`](../model/sources/authorities.csv) (#83), a classification made "
        "by an agent and not yet reviewed by a person.",
        "",
        *[f"- **{evidence.TIERS[t]}**" for t in sorted(evidence.TIERS)],
        "",
        "```mermaid",
        "pie showData",
        '  title "Printed facts by best source tier"',
        *[f'  "T{t}" : {tiers[t]}' for t in sorted(tiers)],
        "```",
        "",
        "| Tier | Kind of source | Facts |",
        "|---|---|---:|",
        *[f"| T{t} | {k.replace('_', ' ')} | {n} |" for (t, k), n in sorted(tier_kinds.items())],
        "",
        "Facts whose best source is an unofficial copy of a statute are the first target of the vetting "
        "run: the same text on the official law portal would make them T1.",
        "",
        *bar("Facts resting on an unofficial law mirror, per state", [mirrors[i] for i in isos], "facts"),
        "",
        "## Why most facts are Standard",
        "",
        "Each Strong condition a Standard fact misses. One fact can miss several, so the counts add up to "
        "more than the number of Standard facts.",
        "",
        "| Condition not met | Facts |",
        "|---|---:|",
        *[f"| {name} | {shortfall[name]} |" for name, _ in SHORTFALLS if shortfall[name]],
        "",
        "## By state",
        "",
        *bar("Printed facts per state", [sum(by_state[i].values()) for i in isos], "facts"),
        "",
        *bar("Strong facts per state", [by_state[i][evidence.STRONG] for i in isos], "facts"),
        "",
        "| State | Printed | Strong | Standard | Gaps |",
        "|---|---:|---:|---:|---:|",
        *[f"| {b['documents'][i]['name']} ({i}) | {sum(by_state[i].values())} | "
          f"{by_state[i][evidence.STRONG]} | {by_state[i][evidence.STANDARD]} | {gaps[i]} |" for i in isos],
        "",
        "## By kind of fact",
        "",
        "| Kind | Printed | Strong | Standard |",
        "|---|---:|---:|---:|",
        *[f"| {k} | {sum(c.values())} | {c[evidence.STRONG]} | {c[evidence.STANDARD]} |"
          for k, c in sorted(by_kind.items(), key=lambda kc: -sum(kc[1].values()))],
        "",
        "## How the checks run",
        "",
        *[f"- **{c['name']}:** {c['what']}" for c in b["notice"]["checks"]],
        "",
        f"{b['notice']['withheld']} The full method, with diagrams, is in [`METHOD.md`](../METHOD.md).",
        "",
    ]
    return "\n".join(out)


def main() -> int:
    b = json.loads(BUNDLE.read_text(encoding="utf-8"))
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(build(b), encoding="utf-8")
    print(f"{OUT.relative_to(ROOT)}: {sum(1 for _ in facts(b))} facts")
    return 0


if __name__ == "__main__":
    sys.exit(main())
