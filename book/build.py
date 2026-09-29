#!/usr/bin/env python3
"""
Typeset the print book's authored parts.

    python3 book/build.py                  # the book -> build/book.pdf
    python3 book/build.py --part 1         # one part, for fast proofing
    python3 book/build.py --typ-only       # emit .typ, skip the typst call

Parts I, II and V are authored prose in manuscript/. The generated Parts III (the twenty-seven)
and IV (reference tables) printed the Dutch-scaled capacity figures that #72 and #73 withdrew,
so they are gone until they can be rendered from the content model (model/document.py) the
report and the country PDFs already use -- see book/report.py. Nothing here states a fact
about a country.

Standard library only.
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

BOOK = Path(__file__).resolve().parent
ROOT = BOOK.parent
MANUSCRIPT = BOOK / "manuscript"
BUILD = BOOK / "build"

TITLE = "Sovereign Data Centers for European States"
SUBTITLE = "Critical government data, analysed state by state"

AUTHORED = {
    1: "part-1-argument.typ",
    2: "part-2-method.typ",
    5: "part-5-conclusion.typ",
}


def assemble(parts: list[int], generated: str) -> str:
    out = [
        '#import "/templates/style.typ": book, datatable, standfirst',
        "",
        "#show: book.with(",
        f'  title: "{TITLE}",',
        f'  subtitle: "{SUBTITLE}",',
        f'  generated: "{generated}",',
        f'  provenance: "Authored draft. Country facts are in the EU-27 report, with sources. Generated {generated}",',
        ")",
        "",
        "#outline(title: [Contents], depth: 2, indent: 1em)",
        "",
    ]
    for n in parts:
        src = MANUSCRIPT / AUTHORED[n]
        if not src.exists():
            raise SystemExit(f"missing manuscript file: {src.relative_to(ROOT)}")
        out += [src.read_text(encoding="utf-8"), ""]
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--typ-only", action="store_true", help="emit .typ without compiling")
    p.add_argument("--part", type=int, action="append", choices=sorted(AUTHORED),
                   help="compile only these parts (repeatable)")
    p.add_argument("-o", "--out", type=Path, help="output path (default build/book.pdf)")
    args = p.parse_args(argv)

    sys.path.insert(0, str(ROOT / "model"))
    from generate_countries import gen_date  # noqa: PLC0415

    parts = sorted(set(args.part)) if args.part else sorted(AUTHORED)
    BUILD.mkdir(exist_ok=True)
    typ = BUILD / "book.typ"
    typ.write_text(assemble(parts, gen_date()), encoding="utf-8")
    print(f"{typ.relative_to(ROOT)}: parts {', '.join(map(str, parts))}")
    if args.typ_only:
        return 0
    if not shutil.which("typst"):
        raise SystemExit("typst is not installed. Install with: brew install typst")
    out = args.out.resolve() if args.out else (BUILD / "book.pdf")
    subprocess.run(["typst", "compile", "--root", str(BOOK), str(typ), str(out)], check=True)
    print(f"{out.relative_to(ROOT) if out.is_relative_to(ROOT) else out}: {out.stat().st_size:,} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
