#!/usr/bin/env python3
"""
Render the content model (model/document.py) to typst: the EU-27 report and one PDF per country.

    python3 book/report.py                         # report -> book/build/eu27-report.pdf
    python3 book/report.py --countries             # 27 PDFs -> book/build/report/<ISO>.pdf
    python3 book/report.py --countries --iso DE    # one country
    python3 book/report.py -o web/dist             # both, into a deploy tree (eu27-report.pdf, report/)

Reads only web/public/data/eu27.json: the documents, the claims they cite and the sources those
claims rest on (DECISIONS.md #74, #75). This file decides how things look on paper, never what is
said -- a renderer that adds a sentence has become a second source of truth.

How sources are shown
---------------------
Every `fact` span gets a footnote at the foot of its page: the source's short label, the locator
and the retrieval date, with a link to its entry in the Sources appendix. The appendix lists each
source once, numbered, with its title, publisher, URL, archived copy, retrieval date and document
hash, followed by every claim that cites it and the quote that supports it. A `gap` span is set in
grey italic, so a withheld value is visible as a gap and never mistaken for a fact.

Standard library only; needs typst to compile.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

BOOK = Path(__file__).resolve().parent
ROOT = BOOK.parent
BUNDLE = ROOT / "web" / "public" / "data" / "eu27.json"
BUILD = BOOK / "build"

TITLE = "Sovereign Data Centres for the EU-27"
SUBTITLE = "Each member state's critical data holdings, analysed on its own fundamentals"

_SPECIAL = re.compile(r"([#@$\\<>*_`~\[\]])")


def esc(value) -> str:
    return _SPECIAL.sub(r"\\\1", str(value))


def string(value) -> str:
    """A typst string literal."""
    return '"' + str(value).replace("\\", "\\\\").replace('"', '\\"') + '"'


class Renderer:
    """Holds the source numbering for one output, so footnotes and appendix agree."""

    def __init__(self, bundle: dict) -> None:
        self.b = bundle
        self.order: list[str] = []          # source ids in first-citation order

    def number(self, sid: str) -> int:
        if sid not in self.order:
            self.order.append(sid)
        return self.order.index(sid) + 1

    # -- spans --------------------------------------------------------------

    def span(self, s: dict) -> str:
        role, text = s.get("role"), esc(s["t"])
        if role == "gap":
            return f"#gap[{text}]"
        if role == "fact":
            notes = []
            for claim in s.get("c", []):
                for cite in self.b["claims"].get(claim, []):
                    n = self.number(cite["source_id"])
                    src = self.b["sources"][cite["source_id"]]
                    where = f", {esc(cite['locator'])}" if cite["locator"] not in ("page text", "") else ""
                    notes.append(f"#link(<src-{n}>)[\\[S{n}\\]] {esc(src['label'])}{where}; "
                                 f"retrieved {esc(cite['retrieved'])}.")
            return text + "".join(f"#footnote[{n}]" for n in dict.fromkeys(notes))
        return text

    def spans(self, spans: list[dict]) -> str:
        return " ".join(self.span(s) for s in spans)

    # -- blocks -------------------------------------------------------------

    def block(self, b: dict) -> str:
        t = b["type"]
        if t == "p":
            return self.spans(b["spans"]) + "\n"
        if t == "callout":
            return f"#callout(tone: {string(b.get('tone', 'method'))})[{self.spans(b['spans'])}]\n"
        if t == "list":
            return "\n".join(f"- {self.spans(item)}" for item in b["items"]) + "\n"
        if t == "table":
            cols = len(b["columns"])
            align = ", ".join(b.get("align", ["left"] * cols))
            widths = "(auto, 1fr)" if cols == 2 else "(" + ", ".join(["auto"] + ["1fr"] * (cols - 1)) + ")"
            head = ", ".join(f"[{self.span(c)}]" for c in b["columns"])
            body = "\n".join("  " + ", ".join(f"[{self.span(cell)}]" for cell in row) + ","
                             for row in b["rows"])
            return (f"#table(\n  columns: {widths},\n  align: ({align},),\n"
                    f"  table.header({head}),\n{body}\n)\n")
        raise ValueError(f"unknown block type {t}")

    def chapter(self, doc: dict, level: int = 1) -> str:
        out = [f"{'=' * level} {esc(doc['name'])} ({esc(doc['iso'])})", ""]
        for s in doc["sections"]:
            out += [f"{'=' * (level + 1)} {esc(s['title'])}", ""]
            out += [self.block(b) for b in s["blocks"]]
        return "\n".join(out)

    # -- appendix -----------------------------------------------------------

    def appendix(self, heading: str = "= Sources") -> str:
        cited_by: dict[str, list[tuple[str, dict]]] = {}
        for claim, cites in self.b["claims"].items():
            for c in cites:
                cited_by.setdefault(c["source_id"], []).append((claim, c))
        out = [heading, "",
               "Each source is listed once, in order of first citation. The hash identifies the exact "
               "document that was fetched and checked; the quote under each claim is text found in it.", ""]
        for n, sid in enumerate(self.order, start=1):
            s = self.b["sources"][sid]
            archived = (f"#link({string(s['archived_url'])})[archived copy]"
                        if s.get("archived_url") else "no archived copy recorded")
            out.append(f"#source-entry({n})[*{esc(s['title'])}*. "
                       f"{esc(s['publisher'])}{', ' + esc(s['published']) if s.get('published') else ''}. "
                       f"#link({string(s['url'])})[{esc(s['url'])}]; {archived}."
                       f"{' ' + esc(s['notes']) + '.' if s.get('notes') else ''}] <src-{n}>")
            for claim, c in sorted(cited_by.get(sid, [])):
                shown = esc(c["quote"]) if c["quote"] else f"value {esc(c['value_as_found'])} at {esc(c['locator'])}"
                out.append(f"#claim-entry[{esc(claim)}][{shown}][{esc(c['confidence'])}, "
                           f"retrieved {esc(c['retrieved'])}]")
            out.append("")
        return "\n".join(out)


def document_spans(doc: dict):
    """Every span in a document, in reading order (for tests and counts)."""
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


# --------------------------------------------------------------------------- #
# Documents
# --------------------------------------------------------------------------- #

def front_matter(b: dict) -> str:
    docs = [b["documents"][iso] for iso in sorted(b["documents"], key=lambda i: b["documents"][i]["name"])]
    rows = []
    for d in docs:
        c = b["countries"][d["iso"]]
        entries = c["national_data"]
        verified = sum(1 for e in entries if e["status"] != "unrecorded")
        tier0 = sum(1 for e in entries if e["status"] != "unrecorded" and e["tier"] == 0)
        n0 = sum(1 for e in entries if e["tier"] == 0)
        measured = sum(1 for e in entries if e.get("record_count") or e.get("data_size"))
        rows.append(f"  [{esc(d['name'])}], [{esc(d['iso'])}], [{verified} of {len(entries)}], "
                    f"[{tier0} of {n0}], [{measured}], [Not yet sized],")
    return "\n".join([
        "= About this report",
        "",
        "#callout(tone: \"notice\")[*Read this first.* Every statement of fact in this report carries a "
        "footnote to a document that was fetched, hashed and checked to contain the quoted text. Where no "
        "such document has been found yet, the value is withheld and the gap is shown in grey italics. "
        "Nothing here is legal advice or an official position of any government or EU body.]",
        "",
        "Each member state is analysed strictly on its own fundamentals: its measured characteristics, "
        "the critical data holdings it cannot let depend on foreign-controlled infrastructure, and the "
        "legal instruments that govern them. No country is scaled from or compared against another.",
        "",
        "== How a source is checked",
        "",
        "A researched claim is admitted only after the cited page or PDF is downloaded, its SHA-256 "
        "recorded, and the quoted text found in the extracted document. An archived copy is looked up "
        "on the Internet Archive. Claims that fail stay out of this report, with the reason recorded "
        "in the repository.",
        "",
        "== How holdings are prioritised",
        "",
        esc(b["priority_rule"]),
        "",
        "== The EU-27 at a glance",
        "",
        "#table(",
        "  columns: (1fr, auto, auto, auto, auto, auto),",
        "  align: (left, left, right, right, right, left),",
        "  table.header([Country], [ISO], [Holdings verified], [Tier 0 verified], [Measured], [Capacity]),",
        *rows,
        ")",
        "",
    ])


def report_typ(b: dict) -> str:
    r = Renderer(b)
    docs = sorted(b["documents"].values(), key=lambda d: d["name"])
    body = [r.chapter(d) for d in docs]
    return "\n".join([
        '#import "/templates/report.typ": report, callout, gap, source-entry, claim-entry',
        "",
        "#show: report.with(",
        f"  title: {string(TITLE)},",
        f"  subtitle: {string(SUBTITLE)},",
        f"  generated: {string(b['generated'])},",
        f"  provenance: {string('Independent research. Every fact is footnoted to a checked source. Generated ' + b['generated'])},",
        ")",
        "",
        "#outline(title: [Contents], depth: 1)",
        "",
        front_matter(b),
        *body,
        r.appendix(),
    ])


def country_typ(b: dict, iso: str) -> str:
    r = Renderer(b)
    d = b["documents"][iso]
    chapter = r.chapter(d)
    return "\n".join([
        '#import "/templates/report.typ": report, callout, gap, source-entry, claim-entry',
        "",
        "#show: report.with(",
        f"  title: {string(d['name'])},",
        f"  subtitle: {string('Critical data holdings and sovereign hosting, analysed on ' + d['name'] + chr(39) + 's own fundamentals')},",
        f"  generated: {string(b['generated'])},",
        f"  provenance: {string(d['name'] + '. Every fact is footnoted to a checked source. Generated ' + b['generated'])},",
        "  kicker: \"EU-27 · Country report\",",
        ")",
        "",
        "#outline(title: [Contents], depth: 2)",
        "",
        chapter,
        r.appendix(),
    ])


def compile_typ(source: str, name: str, out: Path) -> None:
    BUILD.mkdir(exist_ok=True)
    typ = BUILD / f"{name}.typ"
    typ.write_text(source, encoding="utf-8")
    out.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["typst", "compile", "--root", str(BOOK), str(typ), str(out)], check=True)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--countries", action="store_true", help="per-country PDFs instead of the report")
    ap.add_argument("--iso", action="append")
    ap.add_argument("-o", "--out", type=Path, help="deploy tree: writes eu27-report.pdf and report/<ISO>.pdf")
    args = ap.parse_args(argv)
    if not shutil.which("typst"):
        raise SystemExit("typst is not installed. Install with: brew install typst")
    b = json.loads(BUNDLE.read_text(encoding="utf-8"))

    if args.out:
        compile_typ(report_typ(b), "report", args.out / "eu27-report.pdf")
        for iso in sorted(b["documents"]):
            compile_typ(country_typ(b, iso), f"report-{iso}", args.out / "report" / f"{iso}.pdf")
        print(f"{args.out}: eu27-report.pdf and {len(b['documents'])} country PDFs")
        return 0
    if args.countries:
        isos = [i.upper() for i in args.iso] if args.iso else sorted(b["documents"])
        for iso in isos:
            compile_typ(country_typ(b, iso), f"report-{iso}", BUILD / "report" / f"{iso}.pdf")
        print(f"book/build/report: {len(isos)} country PDFs")
        return 0
    out = BUILD / "eu27-report.pdf"
    compile_typ(report_typ(b), "report", out)
    print(f"{out.relative_to(ROOT)}: {out.stat().st_size:,} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
