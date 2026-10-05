#!/usr/bin/env python3
"""
Write each country's readable brief, countries/<ISO>/GOAL.md, and the index countries/SUMMARY.md.

    python3 model/generate_countries.py

Every brief is a markdown rendering of the content model (`document.py`, DECISIONS.md #74): the
same sections, the same facts and the same gaps as the PDF and the web page, with the sources as
markdown footnotes. All 27 are generated the same way, the Netherlands included -- no country is
a baseline for another (#72). The hand-written Dutch plan the model used to scale from is kept as
a note at countries/NL/REFERENCE-CASE.md and is not an input to anything.

Byte-reproducible: the date comes from SOURCE_DATE_EPOCH when set, so regenerating on a
different day is not a 27-file diff.
"""
from __future__ import annotations

import os
import re
import sys
from datetime import date, datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import emoji  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
COUNTRIES = ROOT / "countries"
PARAMS = ROOT / "model" / "eu27_parameters.csv"


def gen_date() -> str:
    """The date stamped into generated files (SOURCE_DATE_EPOCH if set, #34)."""
    epoch = os.environ.get("SOURCE_DATE_EPOCH")
    if epoch:
        return datetime.fromtimestamp(int(epoch), tz=timezone.utc).date().isoformat()
    return date.today().isoformat()


def slug(heading: str) -> str:
    """The GitHub anchor for a rendered `## N. Title` heading: lowercase, punctuation dropped,
    spaces to hyphens."""
    return re.sub(r"[^a-z0-9 -]", "", heading.lower()).replace(" ", "-")


def cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


# The label every how-we-know section carries, in every output (#88). Markdown has no colour; the
# PDFs and web pages also set these sections in the method teal.
METHOD_KICKER = "Method · how this was made"


class Markdown:
    """Renders one document; numbers its footnotes by source, in first-citation order."""

    def __init__(self, bundle: dict) -> None:
        self.b = bundle
        self.order: list[str] = []

    def span(self, s: dict) -> str:
        role, text = s.get("role"), s["t"]
        if role in ("gap", "disputed"):
            return f"*{text}*"
        if role == "fact":
            marks = []
            for claim in s.get("c", []):
                for cite in self.b["claims"].get(claim, []):
                    if cite["source_id"] not in self.order:
                        self.order.append(cite["source_id"])
                    marks.append(f"[^s{self.order.index(cite['source_id']) + 1}]")
            return text + "".join(dict.fromkeys(marks))
        return text

    def spans(self, spans: list[dict]) -> str:
        return " ".join(self.span(s) for s in spans)

    @staticmethod
    def walk(section: dict):
        """Every span in one section of the content model."""
        for b in section["blocks"]:
            if b["type"] in ("p", "callout"):
                yield from b["spans"]
            elif b["type"] == "list":
                for item in b["items"]:
                    yield from item
            elif b["type"] == "table":
                for row in b["rows"]:
                    yield from row

    def block(self, b: dict) -> str:
        if b["type"] == "p":
            return self.spans(b["spans"])
        if b["type"] == "callout":
            return "> " + self.spans(b["spans"])
        if b["type"] == "list":
            return "\n".join(f"- {self.spans(item)}" for item in b["items"])
        if b["type"] == "table":
            head = "| " + " | ".join(cell(self.span(c)) for c in b["columns"]) + " |"
            rule = "|" + "|".join("---:" if a == "right" else "---" for a in b.get("align", [])) + "|"
            rows = ["| " + " | ".join(cell(self.span(x)) for x in row) + " |" for row in b["rows"]]
            return "\n".join([head, rule, *rows])
        raise ValueError(b["type"])

    def document(self, doc: dict) -> str:
        titles = [f"{n}. {s['title']}" for n, s in enumerate(doc["sections"], start=1)]
        out = [
            f"# {doc['name']}: critical data holdings and sovereign hosting",
            "",
            f"> Generated {self.b['generated']} by `model/generate_countries.py` from the content model "
            "(`model/document.py`). The same document is typeset as the country PDF and rendered on the "
            f"web.\n>\n> **{self.b['notice']['disclaimer']}** {self.b['notice']['withheld']} A value in "
            "*italics* is withheld.",
            "",
            "## Contents",
            "",
            *[f"{t.split('. ', 1)[0]}. [{t.split('. ', 1)[1]}](#{slug(t)})" for t in titles],
            "",
        ]
        for t, s in zip(titles, doc["sections"]):
            out += [f"## {t}", ""]
            for b in s["blocks"]:
                out += [self.block(b), ""]
        # How this was made, generated: the methodology (#84) and how each fact above was checked by the
        # model that did not write it (#87). The same documents the PDFs and web pages carry (#88).
        for title, appendix in (("Appendix: methodology", self.b["methodology"]),
                                ("Appendix: fact check", self.b["factcheck"]["countries"][doc["iso"]])):
            out += [f"## {title}", "", f"*{METHOD_KICKER}*", ""]
            for s in appendix["sections"]:
                out += [f"### {s['title']}", ""]
                for b in s["blocks"]:
                    out += [self.block(b), ""]
        if self.order:
            out += ["---", ""]
            for n, sid in enumerate(self.order, start=1):
                src = self.b["sources"][sid]
                archived = f" ([archived]({src['archived_url']}))" if src.get("archived_url") else ""
                out.append(f"[^s{n}]: {src['label']}. {src['title']}. <{src['url']}>{archived}")
            grades = [sp.get("g") for s in doc["sections"] for sp in self.walk(s) if sp.get("role") == "fact"]
            out += ["", f"**Evidence grades:** {grades.count('Strong')} Strong, {grades.count('Standard')} "
                    f"Standard. {self.b['notice']['grade_rule']} The checks behind each fact are listed in "
                    "the country PDF and on the web page.", "",
                    "**Methodology:** how every fact was sourced, checked and calculated is in the two "
                    "appendices above, generated from the code that produced this brief; the same text is "
                    "in the country PDF and on the web pages /methodology and /fact-check.", ""]
        return "\n".join(out)


def overview(bundle: dict) -> str:
    """countries/EU-INFRASTRUCTURE.md: the EU-27 key-infrastructure overview (document.infrastructure, #95)."""
    md, doc = Markdown(bundle), bundle["infrastructure"]
    out = [
        f"# EU-27: {doc['name'].lower()}",
        "",
        f"> Generated {bundle['generated']} by `model/generate_countries.py` from the content model "
        "(`model/document.py`). Every value is the one a state's own brief prints, with the same source; the "
        f"same overview is in the EU-27 report and on the web.\n>\n> **{bundle['notice']['disclaimer']}** "
        f"{bundle['notice']['withheld']} A value in *italics* is withheld.",
        "",
    ]
    for s in doc["sections"]:
        out += [f"## {s['title']}", ""]
        for b in s["blocks"]:
            out += [md.block(b), ""]
    out += ["---", ""]
    for n, sid in enumerate(md.order, start=1):
        src = bundle["sources"][sid]
        archived = f" ([archived]({src['archived_url']}))" if src.get("archived_url") else ""
        out.append(f"[^s{n}]: {src['label']}. {src['title']}. <{src['url']}>{archived}")
    return "\n".join(out + [""])


def summary(bundle: dict) -> str:
    rows = []
    for iso in sorted(bundle["documents"], key=lambda i: bundle["documents"][i]["name"]):
        d, c = bundle["documents"][iso], bundle["countries"][iso]
        entries = c["national_data"]
        verified = sum(1 for e in entries if e["status"] != "unrecorded")
        tier0 = sum(1 for e in entries if e["status"] != "unrecorded" and e["tier"] == 0)
        n0 = sum(1 for e in entries if e["tier"] == 0)
        rows.append(f"| {emoji.flag(iso)} | [{d['name']}]({iso}/GOAL.md) | {iso} | "
                    f"{verified} of {len(entries)} | {tier0} of {n0} | Not yet sized |")
    return "\n".join([
        "# EU-27 country briefs",
        "",
        f"> Generated {bundle['generated']} by `model/generate_countries.py`. Each brief analyses one "
        "member state on its own fundamentals (DECISIONS.md #72); none is scaled from another.",
        "",
        "Where each state's key registers are hosted, and by whom: [EU-INFRASTRUCTURE.md](EU-INFRASTRUCTURE.md).",
        "",
        "| | Country | ISO | Holdings verified | Tier 0 verified | Capacity |",
        "|---|---|---|---:|---:|---|",
        *rows,
        "",
    ])


def main() -> int:
    import export_json  # noqa: PLC0415 -- the bundle is the single input

    bundle = export_json.build_bundle()
    for iso, doc in sorted(bundle["documents"].items()):
        (COUNTRIES / iso).mkdir(parents=True, exist_ok=True)
        (COUNTRIES / iso / "GOAL.md").write_text(Markdown(bundle).document(doc), encoding="utf-8")
    (COUNTRIES / "SUMMARY.md").write_text(summary(bundle), encoding="utf-8")
    (COUNTRIES / "EU-INFRASTRUCTURE.md").write_text(overview(bundle), encoding="utf-8")
    print(f"countries/: {len(bundle['documents'])} briefs, SUMMARY.md and EU-INFRASTRUCTURE.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
