#!/usr/bin/env python3
"""
The language drafts under docs/i18n/drafts/: their contract, and the summary table.

    python3 model/i18n_drafts.py check      # every draft complete, reviewed by a different agent; exit 1 otherwise
    python3 model/i18n_drafts.py summary    # rewrite the table in docs/i18n/README.md from the drafts

A draft is agent output (docs/plans/localisation-plan.md). Nothing renders it: not the bundle, not the
web app, not the PDFs, not /ask. This script only says whether each file keeps the shape that a later
admission could read, and whether a second, different agent has gone over every cell.
"""
from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STRINGS = ROOT / "docs" / "i18n" / "STRINGS.md"
DRAFTS = ROOT / "docs" / "i18n" / "drafts"
README = ROOT / "docs" / "i18n" / "README.md"

VERDICTS = {"ok", "fix"}
BCP47 = re.compile(r"^[a-z]{2,3}-[A-Z]{2}$")   # language subtag (ISO 639-1) + region (ISO 3166-1)


def _rows(table_lines: list[str]) -> list[list[str]]:
    out = []
    for line in table_lines:
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in re.split(r"(?<!\\)\|", line.strip())[1:-1]]
        if cells and set("".join(cells)) <= set("-: "):
            continue
        out.append([c.replace("\\|", "|") for c in cells])
    return out


def _table_after(text: str, heading: str) -> list[list[str]]:
    m = re.search(rf"^## {re.escape(heading)}\s*$", text, re.M)
    if not m:
        return []
    body = text[m.end():]
    nxt = re.search(r"^## ", body, re.M)
    if nxt:
        body = body[: nxt.start()]
    return _rows(body.splitlines())


def spec() -> tuple[list[tuple[str, str]], dict[str, tuple[str, list[str]]]]:
    text = STRINGS.read_text(encoding="utf-8")
    keys = [(r[0], r[1]) for r in _rows(text.split("## Official languages")[0].splitlines())[1:]]
    states = {}
    for r in _rows(text.split("## Official languages")[1].split("## The standards")[0].splitlines())[1:]:
        iso, name, langs = r[0], r[1], r[2]
        codes = [c for c in (c.strip().split(" ")[0] for c in langs.split(",")) if re.fullmatch(r"[a-z]{2}", c)]
        states[iso] = (name, codes)
    return keys, states


def tags() -> dict[str, dict[str, str]]:
    """ISO -> {language subtag: BCP 47 tag}, from STRINGS.md's fourth column."""
    text = STRINGS.read_text(encoding="utf-8")
    out = {}
    for r in _rows(text.split("## Official languages")[1].split("## The standards")[0].splitlines())[1:]:
        out[r[0]] = {t.split("-")[0]: t for t in (x.strip() for x in r[3].split(",")) if t}
    return out


def _field(text: str, label: str) -> str:
    m = re.search(rf"^- {re.escape(label)}:\s*(.+)$", text, re.M)
    return m.group(1).strip() if m else ""


def check_one(iso: str, keys: list[tuple[str, str]], langs: list[str]) -> tuple[list[str], dict]:
    problems: list[str] = []
    path = DRAFTS / f"{iso}.md"
    info = {"iso": iso, "langs": langs, "drafted": "", "reviewed": "", "ok": 0, "fix": 0, "cells": 0}
    if not path.exists():
        return [f"{iso}: no draft file"], info
    text = path.read_text(encoding="utf-8")
    if unicodedata.normalize("NFC", text) != text:
        problems.append(f"{iso}: file is not Unicode NFC")
    want_tags = tags().get(iso, {})
    declared = dict(re.findall(r"\b([a-z]{2}) [^;()]+\(([a-z]{2,3}-[A-Z]{2})\)", _field(text, "Languages")))
    for lang in langs:
        tag = declared.get(lang)
        if not tag or not BCP47.match(tag):
            problems.append(f"{iso}: {lang} has no BCP 47 tag on the Languages line")
        elif tag != want_tags.get(lang):
            problems.append(f"{iso}: {lang} tagged {tag}, STRINGS.md says {want_tags.get(lang)}")
    info["drafted"] = _field(text, "Drafted by")
    info["reviewed"] = _field(text, "Reviewed by")
    if not info["drafted"]:
        problems.append(f"{iso}: no 'Drafted by' line")

    rows = _table_after(text, "Strings")
    if not rows:
        return problems + [f"{iso}: no Strings table"], info
    header, body = rows[0], rows[1:]
    want = ["key", "en", *langs]
    if header != want:
        problems.append(f"{iso}: columns {header} != {want}")
    got_keys = [r[0] for r in body]
    if got_keys != [k for k, _ in keys]:
        missing = [k for k, _ in keys if k not in got_keys]
        extra = [k for k in got_keys if k not in {k for k, _ in keys}]
        problems.append(f"{iso}: keys differ (missing {missing}, extra {extra}, order {'ok' if sorted(got_keys)==sorted(k for k,_ in keys) else 'differs'})")
    src = dict(keys)
    for r in body:
        if len(r) != len(want):
            problems.append(f"{iso}: row {r[0]} has {len(r)} cells, want {len(want)}")
            continue
        key, en, *cells = r
        if key in src and en != src[key]:
            problems.append(f"{iso}: {key} en column differs from STRINGS.md")
        for lang, cell in zip(langs, cells):
            info["cells"] += 1
            if not cell:
                problems.append(f"{iso}: {key} {lang} is empty")
            elif cell != cell.strip():
                problems.append(f"{iso}: {key} {lang} has leading or trailing whitespace")
            elif "\u2026" in src.get(key, "") and "\u2026" not in cell:
                problems.append(f"{iso}: {key} {lang} drops the ellipsis (U+2026)")
            elif "EU-27" in src.get(key, "") and "EU-27" not in cell:
                problems.append(f"{iso}: {key} {lang} drops 'EU-27'")
            elif key == "notice.disclaimer" and not 0.6 <= len(cell) / len(src[key]) <= 2.2:
                problems.append(f"{iso}: disclaimer {lang} length {len(cell)} vs source {len(src[key])}: not a full translation?")

    review = _table_after(text, "Review")
    if not review:
        problems.append(f"{iso}: not reviewed")
        return problems, info
    if not info["reviewed"]:
        problems.append(f"{iso}: no 'Reviewed by' line")
    d_agent = info["drafted"].split(",")[0].strip()
    r_agent = info["reviewed"].split(",")[0].strip()
    if d_agent and r_agent and d_agent == r_agent:
        problems.append(f"{iso}: reviewed by its own drafter ({r_agent})")
    seen = {}
    for r in review[1:]:
        if len(r) < 3:
            problems.append(f"{iso}: review row too short: {r}")
            continue
        key, lang, verdict = r[0], r[1], r[2].lower()
        if verdict not in VERDICTS:
            problems.append(f"{iso}: review {key} {lang}: verdict '{r[2]}' not ok/fix")
            continue
        seen[(key, lang)] = verdict
        info[verdict] += 1
    for key, _ in keys:
        for lang in langs:
            if (key, lang) not in seen:
                problems.append(f"{iso}: {key} {lang} has no review verdict")
    return problems, info


def check(verbose: bool = True) -> int:
    keys, states = spec()
    all_problems, infos = [], []
    for iso, (name, langs) in states.items():
        p, info = check_one(iso, keys, langs)
        info["name"] = name
        infos.append(info)
        all_problems += p
    reviewed = sum(1 for i in infos if i["reviewed"])
    print(f"{len(states)} states, {len(keys)} keys, {sum(i['cells'] for i in infos)} cells, "
          f"{reviewed} reviewed, {sum(i['ok'] for i in infos)} ok, {sum(i['fix'] for i in infos)} fix, "
          f"{len(all_problems)} problems")
    if verbose:
        for p in all_problems:
            print("  " + p)
    return 1 if all_problems else 0


def summary() -> None:
    keys, states = spec()
    lines = ["| ISO | State | Languages | Drafted by | Reviewed by | ok | fix |", "|---|---|---|---|---|---|---|"]
    for iso, (name, langs) in states.items():
        _, i = check_one(iso, keys, langs)
        lines.append(f"| {iso} | {name} | {', '.join(langs)} | {i['drafted'] or '—'} | {i['reviewed'] or '—'} | {i['ok']} | {i['fix']} |")
    table = "\n".join(lines) + "\n"
    text = README.read_text(encoding="utf-8")
    start, end = "<!-- summary:start -->\n", "<!-- summary:end -->"
    a, b = text.index(start) + len(start), text.index(end)
    README.write_text(text[:a] + table + text[b:], encoding="utf-8")
    print(f"wrote {README.relative_to(ROOT)}")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "check"
    if cmd == "check":
        sys.exit(check())
    elif cmd == "summary":
        summary()
    else:
        print(__doc__)
        sys.exit(2)
