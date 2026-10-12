#!/usr/bin/env python3
"""
The contract of `SOVEREIGN-APPLIANCE.md`, the authored note on state-owned data boxes in existing facilities (#104).

The note is prose, so the gate cannot check its facts the way it checks the model's. What it can check, and
`tests/test_sovereign_appliance.py` does through this module:

- the header carries the authored-note wording, cites #59 (the bounded exception) and #104, and says it ranks nothing;
- the sections the contract names are present;
- no ranking language outside the sentence that says it ranks nothing (#10, #77);
- no currency figure anywhere (#72, #73), stricter than #103's note, which allows bands in one section;
- no member state is named outside `## Precedents` and `## Sources`, and there every paragraph or list item that
  names one carries a URL with an access date or is marked **[unverified]**;
- every URL in the note is in the committed link register `docs/sovereign-appliance-links.csv`, and a URL that did
  not answer (no 2xx or 3xx) sits on a line marked **[unverified]**;
- nothing in the model, the book, the web app or `/ask` reads the note.

The generic parts (the ranking and money patterns, the URL probe, the link register) are `national_ai_note`'s (#103).

    python3 model/sovereign_appliance_note.py check   # the summary the gate prints; exit 1 on any failure
    python3 model/sovereign_appliance_note.py links   # fetch every URL once and rewrite the link register (network)
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import national_ai_note as nai  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
NOTE = ROOT / "SOVEREIGN-APPLIANCE.md"
LINKS = ROOT / "docs" / "sovereign-appliance-links.csv"
DECISION = "#104"
EXCEPTION = "#59"
RANKS_NOTHING = "It ranks nothing."

UNVERIFIED = nai.UNVERIFIED
REQUIRED = ("## Contents", "## Precedents", "## Caveats", "## Status and next steps")
NAMING_ALLOWED = ("## Precedents", "## Sources")
RENDERERS = ("model", "book", "api", "web/src", "mobile")
RENDERER_SKIP = {"node_modules", ".venv", "dist", "build", "__pycache__", "research"}


def text() -> str:
    return NOTE.read_text(encoding="utf-8")


def load_links() -> dict[str, dict[str, str]]:
    return nai.load_links(LINKS)


def sections(body: str) -> dict[str, str]:
    """H2 heading -> its text up to the next H2. The header before the first H2 is under ''."""
    out: dict[str, str] = {}
    key = ""
    for line in body.splitlines(keepends=True):
        if line.startswith("## "):
            key = line.rstrip()
        out[key] = out.get(key, "") + line
    return out


def units(part: str) -> list[str]:
    """The paragraphs, list items and table rows of a section: the unit a citation must sit in."""
    out: list[str] = []
    cur: list[str] = []
    for line in part.splitlines():
        fresh = not line.strip() or line.startswith(("- ", "|", "#"))
        if fresh and cur:
            out.append("\n".join(cur))
            cur = []
        if line.strip() and not line.startswith("#"):
            cur.append(line)
    if cur:
        out.append("\n".join(cur))
    return out


def state_pattern(names: dict[str, str]) -> re.Pattern[str]:
    """A member state's English name, or a word starting with it (Estonian, Luxembourgish)."""
    alts = sorted((re.escape(n) for n in names.values()), key=len, reverse=True)
    return re.compile(r"\b(?:" + "|".join(alts) + r")\w*")


def renderers(root: Path = ROOT) -> list[str]:
    """Source files under the rendering paths that name the note. Only this checker may."""
    hits = []
    for d in RENDERERS:
        base = root / d
        if not base.exists():
            continue
        for p in base.rglob("*"):
            if RENDERER_SKIP & set(p.relative_to(root).parts):
                continue
            if p.is_file() and p.suffix in (".py", ".ts", ".tsx", ".typ") and p.name != Path(__file__).name:
                if NOTE.name in p.read_text(encoding="utf-8", errors="ignore"):
                    hits.append(str(p.relative_to(root)))
    return hits


def problems(body: str | None = None, root: Path = ROOT) -> list[str]:
    body = body if body is not None else text()
    names = nai.states()
    out: list[str] = []
    head = body.split("---", 1)[0]
    for needed in (nai.HEADER_WORDING, nai.HEADER_NOT_GENERATED, EXCEPTION, DECISION, RANKS_NOTHING):
        if needed not in head:
            out.append(f"header: must contain '{needed}'")
    for h in REQUIRED:
        if h not in body:
            out.append(f"missing section: {h}")
    if out:
        return out

    # Ranking language, anywhere, except the sentence that says it ranks nothing.
    scrubbed = body
    for allowed in nai.RANK_ALLOWED:
        scrubbed = scrubbed.replace(allowed, "")
    for m in nai.RANK.finditer(scrubbed):
        line = scrubbed[max(0, scrubbed.rfind("\n", 0, m.start())) + 1:scrubbed.find("\n", m.end())]
        if line.startswith("- [") or "FEASIBILITY-RANKING" in line:
            continue
        out.append(f"ranking language: '{m.group(0)}' in: {line.strip()[:100]}")

    # No currency figure anywhere: the note carries no cost (#72, #73).
    for m in nai.MONEY.finditer(body):
        line = body[max(0, body.rfind("\n", 0, m.start())) + 1:body.find("\n", m.end())]
        out.append(f"currency figure: '{m.group(0)}' in: {line.strip()[:100]}")

    # Member states named only where allowed, and there only with a source in the same unit.
    pat = state_pattern(names)
    for heading, part in sections(body).items():
        if heading in NAMING_ALLOWED:
            for u in units(part):
                if pat.search(u) and not ((nai.URL.search(u) and nai.ACCESSED.search(u)) or UNVERIFIED in u):
                    out.append(f"{heading}: names a state without a URL and access date or {UNVERIFIED}: "
                               f"{u.strip()[:90]}")
        else:
            for m in pat.finditer(part):
                line = part[max(0, part.rfind("\n", 0, m.start())) + 1:part.find("\n", m.end())]
                if line.startswith("- ["):
                    continue  # the contents list
                out.append(f"{heading or 'header'}: names a member state ('{m.group(0)}'); only "
                           f"{' and '.join(NAMING_ALLOWED)} may: {line.strip()[:90]}")

    # Every URL registered; non-answering ones marked unverified on their line.
    links = load_links()
    all_urls = nai.urls(body)
    for u in all_urls:
        row = links.get(u)
        if row is None:
            out.append(f"link register: {u} is not in {LINKS.name}; run ./run.sh appliance links")
            continue
        if not nai.answered(row["status"]):
            lines = [ln for ln in body.splitlines() if u in ln]
            if not all(UNVERIFIED in ln for ln in lines):
                out.append(f"link register: {u} answered {row['status']} but its line is not marked {UNVERIFIED}")
    for u in links:
        if u not in all_urls:
            out.append(f"link register: {u} is registered but no longer cited; run ./run.sh appliance links")

    for hit in renderers(root):
        out.append(f"{hit} reads the note; it is never rendered ({DECISION})")
    return out


def summary(body: str | None = None) -> dict[str, int]:
    body = body if body is not None else text()
    links = load_links()
    all_urls = nai.urls(body)
    return {
        "sections": sum(1 for ln in body.splitlines() if ln.startswith("## ")),
        "urls": len(all_urls),
        "urls_answered": sum(1 for u in all_urls if nai.answered(links.get(u, {}).get("status", "0"))),
        "unverified_marks": body.count(UNVERIFIED),
        "words": len(body.split()),
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["check", "links"])
    args = ap.parse_args(argv)
    if args.command == "links":
        return nai.write_links(NOTE, LINKS)
    errs = problems()
    s = summary()
    for e in errs:
        print(f"  ❌ {e}", file=sys.stderr)
    print(f"{NOTE.name}: {s['sections']} sections, {s['urls']} URLs ({s['urls_answered']} answered at the last "
          f"link check), {s['unverified_marks']} unverified marks, {s['words']:,} words, {len(errs)} problems")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
