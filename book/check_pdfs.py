#!/usr/bin/env python3
"""
Check the compiled PDFs a reader downloads, not only the typst source that makes them (#92).

    python3 book/check_pdfs.py <dir written by book/report.py -o>

For the EU-27 report and every country PDF: it opens with the disclaimer; it carries the methodology and
the fact-check appendices (#88); a country PDF names its country; every font is embedded, so it reads the
same everywhere; and it stays within a size budget. The four report previews exist. Needs poppler's
pdftotext and pdffonts; test.sh runs this only where they are installed, and CI installs them.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "book"))
import report  # noqa: E402

DISCLAIMER = "no person has reviewed the findings"
APPENDICES = ("Appendix: methodology", "Appendix: fact check")
BUDGET_MB = {"report": 20, "country": 3}       # today ~12 MB and at most ~1.1 MB


def text(pdf: Path) -> str:
    return re.sub(r"\s+", " ", subprocess.run(["pdftotext", str(pdf), "-"], capture_output=True, check=True,
                                              text=True).stdout)


def unembedded(pdf: Path) -> list[str]:
    rows = subprocess.run(["pdffonts", str(pdf)], capture_output=True, check=True, text=True).stdout.splitlines()[2:]
    return [r.split()[0] for r in rows if r.split()[-5] != "yes"]


def check(out: Path) -> list[str]:
    bundle = json.loads(report.BUNDLE.read_text(encoding="utf-8"))
    pdfs = {"EU-27 report": (out / "eu27-report.pdf", "report", "")}
    pdfs |= {iso: (out / "report" / f"{iso}.pdf", "country", d["name"]) for iso, d in bundle["documents"].items()}
    problems = []
    for name, (pdf, kind, country) in sorted(pdfs.items()):
        if not pdf.exists():
            problems.append(f"{name}: {pdf.name} missing")
            continue
        body = text(pdf)
        if DISCLAIMER not in body:
            problems.append(f"{name}: no disclaimer")
        problems += [f"{name}: no '{a}'" for a in APPENDICES if a not in body]
        if country and country not in body:
            problems.append(f"{name}: does not name {country}")
        problems += [f"{name}: font {f} not embedded" for f in unembedded(pdf)]
        mb = pdf.stat().st_size / 1e6
        if mb > BUDGET_MB[kind]:
            problems.append(f"{name}: {mb:.1f} MB over the {BUDGET_MB[kind]} MB budget")
    for p in report.PREVIEWS:
        png = out / "previews" / f"report-{p}.png"
        if not png.exists() or png.stat().st_size < 10_000:
            problems.append(f"preview {p}: missing or empty")
    return problems


if __name__ == "__main__":
    problems = check(Path(sys.argv[1]))
    for p in problems:
        print(f"PDF: {p}")
    print(f"{len(problems)} problems in 28 PDFs and {len(report.PREVIEWS)} previews")
    sys.exit(1 if problems else 0)
