#!/usr/bin/env python3
"""
TECHNICAL-UNIVERSITIES.md: the authored note's contract, and its link register.

    python3 model/technical_universities_note.py check    # the contract; exit 1 on any problem
    python3 model/technical_universities_note.py links    # refetch every URL into docs/technical-universities-links.csv

The note lists, per member state, the institutions on a named published list (CESAER, EuroTech) or the
state's technical university cited from a fetched page, or marked [unverified]. It is prose the model never
renders. What the gate can refuse: a state missing or out of order, a table with the wrong columns, a row
whose Basis is not one of the three allowed shapes, a URL that is not in the committed link register, a
ranking word, an institution out of alphabetical order, and any renderer that names the file.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "model"))

from national_ai_note import load_links, urls, write_links  # noqa: E402

NOTE = ROOT / "TECHNICAL-UNIVERSITIES.md"
LINKS = ROOT / "docs" / "technical-universities-links.csv"

STATES = {
    "AT": "Austria", "BE": "Belgium", "BG": "Bulgaria", "HR": "Croatia", "CY": "Cyprus", "CZ": "Czechia",
    "DK": "Denmark", "EE": "Estonia", "FI": "Finland", "FR": "France", "DE": "Germany", "EL": "Greece",
    "HU": "Hungary", "IE": "Ireland", "IT": "Italy", "LV": "Latvia", "LT": "Lithuania", "LU": "Luxembourg",
    "MT": "Malta", "NL": "Netherlands", "PL": "Poland", "PT": "Portugal", "RO": "Romania", "SK": "Slovakia",
    "SI": "Slovenia", "ES": "Spain", "SE": "Sweden",
}
COLUMNS = ["Institution", "City", "Website", "Basis"]
DATE = r"\d{4}-\d{2}-\d{2}"
BASIS = re.compile(rf"^(?:C[12], accessed {DATE}|C3: https?://\S+, accessed {DATE}|\[unverified\])$")
RANKING = re.compile(r"\b(top|best|number one|no\. ?1|#1|ranked|ranking|first-ranked|elite|prestigious)\b", re.I)
RENDERERS = ["model/document.py", "model/export_json.py", "model/generate_countries.py", "model/ask_corpus.py",
             "book", "web/src", "api"]


def _rows(block: str) -> list[list[str]]:
    out = []
    for line in block.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip().replace("\\|", "|") for c in re.split(r"(?<!\\)\|", line.strip())[1:-1]]
        if cells and set("".join(cells)) <= set("-: "):
            continue
        out.append(cells)
    return out


def check() -> int:
    problems: list[str] = []
    if not NOTE.exists():
        print("TECHNICAL-UNIVERSITIES.md: missing")
        return 1
    text = NOTE.read_text(encoding="utf-8")
    links = load_links(LINKS)

    # Criteria: three lines, each with a URL and an access date.
    crit = text.split("## Criteria", 1)[1].split("\n## ", 1)[0] if "## Criteria" in text else ""
    for c in ("C1", "C2"):
        if not re.search(rf"^- {c}: .*https?://\S+.*accessed {DATE}", crit, re.M):
            problems.append(f"criteria: {c} lacks a URL or an access date")
    if not re.search(r"^- C3: ", crit, re.M):
        problems.append("criteria: C3 missing")

    # States: every one, once, in alphabetical order of the English name, with the right heading.
    heads = re.findall(r"^## (.+?) \(([A-Z]{2})\)$", text, re.M)
    seen_iso = [iso for _, iso in heads]
    expected = sorted(STATES, key=lambda i: STATES[i])
    if seen_iso != expected:
        problems.append(f"state headings: got {seen_iso}, want {expected}")
    for name, iso in heads:
        if STATES.get(iso) != name:
            problems.append(f"{iso}: heading says {name!r}, want {STATES.get(iso)!r}")

    counts = {"C1": 0, "C2": 0, "C3": 0, "[unverified]": 0}
    n_rows = 0
    body = text.split("## Method", 1)[0]
    for i, (name, iso) in enumerate(heads):
        start = body.index(f"## {name} ({iso})")
        nxt = body.find("\n## ", start + 1)
        block = body[start: nxt if nxt != -1 else None]
        rows = _rows(block)
        if not rows or rows[0] != COLUMNS:
            problems.append(f"{iso}: table columns {rows[0] if rows else None} != {COLUMNS}")
            continue
        entries = rows[1:]
        if not entries:
            problems.append(f"{iso}: no institution")
        names = [r[0] for r in entries]
        if names != sorted(names, key=str.casefold):
            problems.append(f"{iso}: institutions are not in alphabetical order")
        for r in entries:
            n_rows += 1
            if len(r) != 4:
                problems.append(f"{iso}: row {r[0]!r} has {len(r)} cells")
                continue
            inst, city, site, basis = r
            if not re.match(r"^https://[^\s/]+(/\S*)?$", site) or site.endswith("/"):
                problems.append(f"{iso}: {inst}: website {site!r} is not an https URL without a trailing slash")
            if not BASIS.match(basis):
                problems.append(f"{iso}: {inst}: basis {basis!r} is not C1/C2 with a date, C3 with a URL and a date, or [unverified]")
            else:
                counts["[unverified]" if basis.startswith("[") else basis[:2]] += 1
            for u in [site] + re.findall(r"https?://\S+?(?=,|\s|$)", basis):
                if u not in links:
                    problems.append(f"{iso}: {inst}: {u} is not in {LINKS.name}; run `links`")
            if RANKING.search(inst) or RANKING.search(city):
                problems.append(f"{iso}: {inst}: ranking word")

    # No ranking language outside the one sentence that defines "leading".
    prose = re.sub(r'"Leading" means: on one of the lists below\. It is not a ranking', "", text)
    prose = re.sub(r"^\|.*$", "", prose, flags=re.M)
    for m in RANKING.finditer(prose):
        line = prose[: m.start()].count("\n") + 1
        problems.append(f"line {line}: ranking word {m.group(0)!r}")

    # Every URL in the note is in the register, and the register has nothing the note dropped.
    note_urls = set(urls(text))
    missing = sorted(u for u in note_urls if u not in links)
    if missing:
        problems.append(f"{len(missing)} URLs not in the link register (run `links`): {missing[:3]}")
    stale = sorted(u for u in links if u not in note_urls)
    if stale:
        problems.append(f"{len(stale)} register rows no longer in the note (run `links`): {stale[:3]}")

    # Method section: present, short.
    method = text.split("## Method", 1)[1] if "## Method" in text else ""
    bullets = [line for line in method.splitlines() if line.startswith("- ")]
    if not bullets or len(bullets) > 8:
        problems.append(f"method: {len(bullets)} bullets, want 1 to 8")

    # Rendered nowhere.
    for rel in RENDERERS:
        p = ROOT / rel
        files = [p] if p.is_file() else [f for f in p.rglob("*") if f.suffix in {".py", ".ts", ".tsx", ".typ"}]
        for f in files:
            try:
                if "TECHNICAL-UNIVERSITIES" in f.read_text(encoding="utf-8"):
                    problems.append(f"{f.relative_to(ROOT)} names the note; it is never rendered")
            except (UnicodeDecodeError, OSError):
                continue

    answered = sum(1 for r in links.values() if str(r.get("status", "")).startswith("2") or str(r.get("status", "")).startswith("3"))
    print(f"{len(heads)} states, {n_rows} rows (C1 {counts['C1']}, C2 {counts['C2']}, C3 {counts['C3']}, "
          f"[unverified] {counts['[unverified]']}), {len(note_urls)} URLs ({answered} answered at the last link check), "
          f"{len(problems)} problems")
    for p in problems:
        print("  " + p)
    return 1 if problems else 0


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "check"
    if cmd == "check":
        sys.exit(check())
    elif cmd == "links":
        write_links(NOTE, LINKS)
    else:
        print(__doc__)
        sys.exit(2)
