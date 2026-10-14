#!/usr/bin/env python3
"""
INTERNET-ENTRY-POINTS.md: the authored note's contract, its derived counts, and its link register.

    python3 model/internet_entry_points_note.py check    # the contract; exit 1 on any problem
    python3 model/internet_entry_points_note.py counts   # rewrite every state's Counts line from its own table
    python3 model/internet_entry_points_note.py links    # refetch every URL into docs/internet-entry-points-links.csv
    python3 model/internet_entry_points_note.py retry    # re-probe, one at a time, the basis pages that answered 429 or not at all

The note lists, per member state, where the internet enters it: E1, a subsea cable landing point as the
Submarine Cable Map labels it, cited from the map's own JSON page for that point; E2, an internet exchange point
cited from its PeeringDB page; E3, a statute or regulator page that names such a facility. A state with no row
of a kind has one row that says so. Under each table one Counts line states how many rows of each kind the table
holds and the three defined terms (no-landing, single-landing, single-exchange); the checker recomputes that
line from the rows and refuses one that differs, so no count in the note is typed by hand. It is prose the
model never renders. What the gate can refuse: a state missing or out of order, a table with the wrong columns,
a row whose Basis is not one of the allowed shapes or cites the map's HTML pages instead of its JSON, a row out
of order, a 'none' row beside a real row, an E1 row filed under a state its label does not name, an E3 row citing
a page the source register does not hold, a Counts line that disagrees with its table, a URL that is not in the
committed link register, a ranking or size word in the prose or a Place cell, a number in a place, and any
renderer that names the file. A Name cell is the cited page's own words and is not scanned.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "model"))

from national_ai_note import load_links as _load_links, urls, write_links  # noqa: E402

NOTE = ROOT / "INTERNET-ENTRY-POINTS.md"
LINKS = ROOT / "docs" / "internet-entry-points-links.csv"

STATES = {
    "AT": "Austria", "BE": "Belgium", "BG": "Bulgaria", "HR": "Croatia", "CY": "Cyprus", "CZ": "Czechia",
    "DK": "Denmark", "EE": "Estonia", "FI": "Finland", "FR": "France", "DE": "Germany", "EL": "Greece",
    "HU": "Hungary", "IE": "Ireland", "IT": "Italy", "LV": "Latvia", "LT": "Lithuania", "LU": "Luxembourg",
    "MT": "Malta", "NL": "Netherlands", "PL": "Poland", "PT": "Portugal", "RO": "Romania", "SK": "Slovakia",
    "SI": "Slovenia", "ES": "Spain", "SE": "Sweden",
}
COLUMNS = ["Kind", "Name", "Place", "Cables or website", "Basis"]
KINDS = ("E1", "E2", "E3")
DATE = r"\d{4}-\d{2}-\d{2}"
# The E1 and E2 hosts and paths are pinned: the map's HTML pages are an empty application shell, so a row that
# cited one could never be checked against its served bytes; the JSON page for the same point can.
E1_URL = r"https://www\.submarinecablemap\.com/api/v3/landing-point/[a-z0-9-]+\.json"
E2_URL = r"https://www\.peeringdb\.com/ix/\d+"
BASIS = re.compile(rf"^(?:E1: {E1_URL}, accessed {DATE}|E2: {E2_URL}, accessed {DATE}|E3: https?://\S+, accessed {DATE}"
                   rf"|\[unverified\]|none: searched {DATE})$")
NONE_ROWS = {"E1": ["E1", "(none on the map)", "—", "—"], "E2": ["E2", "(none in PeeringDB)", "—", "—"]}
PLANNED = re.compile(r"\(planned(?:, RFS \d{4})?\)")   # the map gives some planned cables no year
WEBSITE = re.compile(r"^https?://[^\s/]+(/\S*)?$")
# The universities' list plus size words: a landing station or an exchange is listed because it is on the cited
# page, never because the note finds it large, central or important.
RANKING = re.compile(r"\b(top|best|leading|foremost|premier|world-class|excellent|number one|no\. ?1|#1|ranked|ranking|"
                     r"first-ranked|elite|prestigious|largest|biggest|major|key|hubs?|gateways?|strategic|important|"
                     r"primary|central|principal|backbones?)\b", re.I)   # not "main": Frankfurt am Main is a Place
QUOTED = re.compile(r'"[^"\n]*"')    # a quoted phrase is someone else's words; the scan reads the rest of the line
REGISTRY = ROOT / "model" / "sources" / "registry.csv"
TERMS = re.compile(r"\b(no-landing|single-landing|single-exchange)\b")
RENDERERS = ["model/document.py", "model/export_json.py", "model/generate_countries.py", "model/ask_corpus.py",
             "book", "web/src", "api"]


def load_links(path: Path = LINKS) -> dict[str, dict[str, str]]:
    return _load_links(path)


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


def _is_none(row: list[str]) -> bool:
    return len(row) == 5 and row[4].startswith("none:")


def _cables(cell: str) -> list[str]:
    # Cables are comma-separated; the comma inside "(planned, RFS <year>)" is not a separator.
    return [c.strip() for c in re.split(r",(?![^()]*\))", cell) if c.strip()] if cell != "—" else []


def tally(entries: list[list[str]]) -> dict[str, int]:
    """The counts a state's rows give, the only arithmetic in the note. An E1 row is in service when at least
    one of its cables is not marked planned, planned-only when every cable is, unverified when its Basis is
    [unverified] or it has no cable cell to read (its page did not answer)."""
    t = {"E1": 0, "E1_service": 0, "E1_planned": 0, "E1_unverified": 0, "E2": 0, "E3": 0}
    for r in entries:
        if len(r) != 5 or _is_none(r) or r[0] not in KINDS:
            continue
        t[r[0]] += 1
        if r[0] == "E1":
            cables = _cables(r[3])
            if not cables or r[4].startswith("["):
                t["E1_unverified"] += 1
            elif all(PLANNED.search(c) for c in cables):
                t["E1_planned"] += 1
            else:
                t["E1_service"] += 1
    return t


def counts_line(entries: list[list[str]]) -> str:
    t = tally(entries)
    yn = lambda b: "yes" if b else "no"  # noqa: E731
    return (f"Counts: E1 {t['E1']} (in service {t['E1_service']}, planned-only {t['E1_planned']}, "
            f"unverified {t['E1_unverified']}), E2 {t['E2']}, E3 {t['E3']}; "
            f"no-landing {yn(t['E1_service'] == 0)}; single-landing {yn(t['E1_service'] == 1)}; "
            f"single-exchange {yn(t['E2'] <= 1)}.")


def blocks(text: str) -> list[tuple[str, str, str]]:
    """(name, iso, block text) for every state heading, in the order written."""
    body = text.split("\n## Method", 1)[0]
    heads = re.findall(r"^## (.+?) \(([A-Z]{2})\)$", body, re.M)
    out = []
    for name, iso in heads:
        start = body.index(f"\n## {name} ({iso})\n") + 1
        nxt = body.find("\n## ", start + 1)
        out.append((name, iso, body[start: nxt if nxt != -1 else None]))
    return out


def registry_urls(root: Path = ROOT) -> set[str]:
    """The URLs the project's source register holds: the only pages an E3 row may cite."""
    import csv  # noqa: PLC0415
    path = root / "model" / "sources" / "registry.csv"
    if not path.exists():
        return set()
    with path.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    return {r["url"] for r in rows} | {r["archived_url"] for r in rows if r.get("archived_url")}


def renderers(root: Path = ROOT) -> list[str]:
    hits = []
    for rel in RENDERERS:
        p = root / rel
        files = [p] if p.is_file() else [f for f in p.rglob("*") if f.suffix in {".py", ".ts", ".tsx", ".typ"}]
        for f in files:
            try:
                if "INTERNET-ENTRY-POINTS" in f.read_text(encoding="utf-8"):
                    hits.append(str(f.relative_to(root)))
            except (UnicodeDecodeError, OSError):
                continue
    return sorted(hits)


def problems(text: str, root: Path = ROOT) -> tuple[list[str], dict[str, int]]:
    """Every problem the contract names, and the counts the summary line prints."""
    probs: list[str] = []
    links = load_links()
    registry = registry_urls(root)
    counts = {k: 0 for k in ("rows", "E1", "E1_service", "E2", "E3", "[unverified]", "none")}

    head = "\n".join(text.splitlines()[:12])
    for token in ("authored note", "Not generated", "It ranks nothing"):
        if token not in head:
            probs.append(f"header: {token!r} missing from the first lines")

    # Definitions: E1 and E2 each name their enumeration page and the date it was read; E3 and the satellite
    # line say what is in and out.
    defs = text.split("## Definitions", 1)[1].split("\n## ", 1)[0] if "## Definitions" in text else ""
    items = [" ".join(i.split()) for i in re.split(r"\n(?=- )", defs) if i.strip().startswith("- ")]   # wrapped bullets, one each
    for c in ("E1", "E2"):
        if not any(re.match(rf"- {c}: .*https?://\S+.*accessed {DATE}", i) for i in items):
            probs.append(f"definitions: {c} lacks a URL or an access date")
    if not any(i.startswith("- E3: ") for i in items):
        probs.append("definitions: E3 missing")
    if not any(i.startswith("- Satellite") for i in items):
        probs.append("definitions: the satellite line is missing")

    # States: every one, once, in alphabetical order of the English name, with the right heading.
    found = blocks(text)
    seen_iso = [iso for _, iso, _ in found]
    expected = sorted(STATES, key=lambda i: STATES[i])
    if seen_iso != expected:
        probs.append(f"state headings: got {seen_iso}, want {expected}")
    for name, iso, _ in found:
        if STATES.get(iso) != name:
            probs.append(f"{iso}: heading says {name!r}, want {STATES.get(iso)!r}")

    for name, iso, block in found:
        rows = _rows(block)
        if not rows or rows[0] != COLUMNS:
            probs.append(f"{iso}: table columns {rows[0] if rows else None} != {COLUMNS}")
            continue
        entries = rows[1:]
        if not entries:
            probs.append(f"{iso}: no rows")
        keys = [(r[0], r[1].casefold()) for r in entries if len(r) >= 2]
        if keys != sorted(keys):
            probs.append(f"{iso}: rows are not in order of Kind then Name")
        real = {k: [r for r in entries if len(r) == 5 and r[0] == k and not _is_none(r)] for k in KINDS}
        nones = {k: [r for r in entries if len(r) == 5 and r[0] == k and _is_none(r)] for k in KINDS}
        for k in ("E1", "E2"):
            if nones[k] and real[k]:
                probs.append(f"{iso}: {k}: a 'none' row beside a real row")
            if len(nones[k]) > 1:
                probs.append(f"{iso}: {k}: more than one 'none' row")
            if not nones[k] and not real[k]:
                probs.append(f"{iso}: {k}: no row and no 'none' row")
        if nones["E3"]:
            probs.append(f"{iso}: E3 never has a 'none' row")
        for r in entries:
            counts["rows"] += 1
            if len(r) != 5:
                probs.append(f"{iso}: row {r[:2]!r} has {len(r)} cells")
                continue
            kind, nm, place, cell, basis = r
            if kind not in KINDS:
                probs.append(f"{iso}: {nm}: kind {kind!r} is not E1, E2 or E3")
                continue
            if _is_none(r):
                if r[:4] != NONE_ROWS.get(kind):
                    probs.append(f"{iso}: {kind}: a 'none' row must read {NONE_ROWS.get(kind)}")
                elif BASIS.match(basis):
                    counts["none"] += 1
                else:
                    probs.append(f"{iso}: {kind}: basis {basis!r} is not 'none: searched <date>'")
                continue
            if not BASIS.match(basis):
                probs.append(f"{iso}: {nm}: basis {basis!r} is not {kind} with its page and a date, or [unverified]")
            elif basis.startswith("["):
                counts["[unverified]"] += 1
            elif basis[:2] != kind:
                probs.append(f"{iso}: {nm}: an {kind} row with an {basis[:2]} basis")
            else:
                counts[kind] += 1
            if kind == "E1":
                # The map's label decides the state (Definitions), so the name ends with the state's English name.
                if not nm.endswith(", " + STATES.get(iso, "")):
                    probs.append(f"{iso}: {nm}: the map's label does not end with the state's name")
                cables = _cables(cell)
                if not cables and not basis.startswith("["):
                    probs.append(f"{iso}: {nm}: an E1 row names its cables unless it is [unverified]")
                if cables and not basis.startswith("[") and not all(PLANNED.search(c) for c in cables):
                    counts["E1_service"] += 1
            elif kind == "E2":
                if cell != "—" and (not WEBSITE.match(cell) or cell.endswith("/")):
                    probs.append(f"{iso}: {nm}: website {cell!r} is not an http(s) URL without a trailing slash, or —")
            else:
                if cell != "—":
                    probs.append(f"{iso}: {nm}: an E3 row's fourth cell is —")
                # An E3 page is one the project's source register already holds (Definitions).
                for u in re.findall(r"https?://\S+?(?=,|\s|$)", basis):
                    if u not in registry:
                        probs.append(f"{iso}: {nm}: {u} is not in model/sources/registry.csv; E3 cites only registered pages")
            for u in ([cell] if kind == "E2" and cell != "—" else []) + re.findall(r"https?://\S+?(?=,|\s|$)", basis):
                if u not in links:
                    probs.append(f"{iso}: {nm}: {u} is not in {LINKS.name}; run `links`")
            # A Name is the cited page's own words (PeeringDB has a "TOP-IX" and a "FICIX 1 (Espoo) IPv6 MTU 9000"),
            # so the word and figure rules fall on the Place cell and the prose, which are the note's own.
            if RANKING.search(place):
                probs.append(f"{iso}: {nm}: ranking or size word in the place")
            if re.search(r"\d{2,}", place):
                probs.append(f"{iso}: {nm}: a number in the place; rows carry no figures")
        # The Counts line: present once, and exactly what the rows give.
        want = counts_line(entries)
        got = re.findall(r"^Counts: .*$", block, re.M)
        if len(got) != 1:
            probs.append(f"{iso}: {len(got)} Counts lines, want one; run `counts`")
        elif got[0] != want:
            probs.append(f"{iso}: counts line is {got[0]!r}, want {want!r}; run `counts`")

    # No ranking or size language in the prose, and the three defined terms only where they are defined and in
    # the Counts lines; table rows are checked cell by cell above. A quoted phrase is someone else's words (the
    # owner's request, a page's wording) and is stripped before the scan; the satellite line of the Definitions is
    # the one place the note names what it leaves out.
    in_defs = False
    for n, line in enumerate(text.splitlines(), 1):
        if line.startswith("## "):
            in_defs = line.strip() == "## Definitions"
        if line.startswith("|") or line.startswith("Counts: ") or line.startswith("- Satellite"):
            continue
        for m in RANKING.finditer(QUOTED.sub('""', line)):
            probs.append(f"line {n}: ranking or size word {m.group(0)!r}")
        if not in_defs:
            for m in TERMS.finditer(line):
                probs.append(f"line {n}: {m.group(0)!r} outside Definitions and the Counts lines")

    # Every URL in the note is in the register, and the register has nothing the note dropped.
    note_urls = set(urls(text))
    missing = sorted(u for u in note_urls if u not in links)
    if missing:
        probs.append(f"{len(missing)} URLs not in the link register (run `links`): {missing[:3]}")
    stale = sorted(u for u in links if u not in note_urls)
    if stale:
        probs.append(f"{len(stale)} register rows no longer in the note (run `links`): {stale[:3]}")

    method = text.split("## Method", 1)[1] if "## Method" in text else ""
    bullets = [line for line in method.splitlines() if line.startswith("- ")]
    if not bullets or len(bullets) > 8:
        probs.append(f"method: {len(bullets)} bullets, want 1 to 8")

    for rel in renderers(root):
        probs.append(f"{rel} names the note; it is never rendered")

    counts["urls"] = len(note_urls)
    counts["answered"] = sum(1 for r in links.values() if str(r.get("status", ""))[:1] in ("2", "3"))
    counts["states"] = len(found)
    return probs, counts


def check() -> int:
    if not NOTE.exists():
        print("INTERNET-ENTRY-POINTS.md: missing")
        return 1
    probs, c = problems(NOTE.read_text(encoding="utf-8"))
    print(f"{c['states']} states, {c['rows']} rows (E1 {c['E1']}, in service {c['E1_service']}, E2 {c['E2']}, E3 {c['E3']}, "
          f"[unverified] {c['[unverified]']}, none {c['none']}), {c['urls']} URLs ({c['answered']} answered at the last link check), "
          f"{len(probs)} problems")
    for p in probs:
        print("  " + p)
    return 1 if probs else 0


def with_counts(text: str) -> str:
    """The note with every state's Counts line rewritten from its table: the one write this module does to
    the note, so that no count in it is typed by hand."""
    out = text
    for name, iso, block in blocks(text):
        rows = _rows(block)
        if not rows or rows[0] != COLUMNS:
            continue
        want = counts_line(rows[1:])
        lines = [line for line in block.rstrip("\n").splitlines() if not line.startswith("Counts: ")]
        last = max(i for i, line in enumerate(lines) if line.startswith("|"))
        if last + 1 < len(lines) and lines[last + 1] == "":
            lines[last + 2:last + 2] = [want]
        else:
            lines[last + 1:last + 1] = ["", want]
        new = "\n".join(lines) + "\n"
        out = out.replace(block, new, 1)
    return out


def links(full: bool = True) -> int:
    """The shared parallel pass, then a sequential, paused retry of every basis page that answered 429 or not at
    all: PeeringDB rate-limits six concurrent anonymous requests, and a rate limit is not a dead page. Websites
    (the E2 fourth cell) are PeeringDB's field, not a basis, and are left as they answered. `retry` runs only the
    second part on the committed register."""
    import csv  # noqa: PLC0415
    import time  # noqa: PLC0415
    from national_ai_note import answered, probe  # noqa: PLC0415
    if full:
        write_links(NOTE, LINKS)
    with LINKS.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    basis = re.compile(rf"^(?:{E1_URL}|{E2_URL})$")
    for attempt in range(2):
        todo = [r for r in rows if basis.match(r["url"]) and (r["status"] == "429" or r["status"] == "0")]
        if not todo:
            break
        print(f"retrying {len(todo)} basis pages one at a time (pass {attempt + 1})")
        for r in todo:
            time.sleep(3)
            _, r["status"], r["error"] = probe(r["url"])
    with LINKS.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["url", "status", "error", "checked"], lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    bad = [r for r in rows if not answered(r["status"])]
    print(f"{len(rows)} URLs, {len(rows) - len(bad)} answered, {len(bad)} did not after the retry -> {LINKS.relative_to(ROOT)}")
    return 0


def counts() -> int:
    text = NOTE.read_text(encoding="utf-8")
    new = with_counts(text)
    changed = sum(1 for a, b in zip(text.splitlines(), new.splitlines()) if a != b) + abs(len(new.splitlines()) - len(text.splitlines()))
    NOTE.write_text(new, encoding="utf-8")
    print(f"{len(blocks(new))} states' Counts lines written, {changed} lines changed")
    return 0


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "check"
    if cmd == "check":
        sys.exit(check())
    elif cmd == "counts":
        sys.exit(counts())
    elif cmd == "links":
        sys.exit(links())
    elif cmd == "retry":
        sys.exit(links(full=False))
    else:
        print(__doc__)
        sys.exit(2)
