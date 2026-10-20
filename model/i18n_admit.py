#!/usr/bin/env python3
"""
Admission: the language tables the app reads, written from STRINGS.md and the drafts that have earned it (#111).

    python3 model/i18n_admit.py           # write model/i18n/
    python3 model/i18n_admit.py --check   # exit 1 if model/i18n/ differs from what the sources give

English always comes from docs/i18n/STRINGS.md, the source every draft translates. A draft language is admitted
only when a person who reads it has said so on the file, `- Read by (<lang>): <role>, <date>`, and the review
has no `fix` left for that language: a fix is applied by the drafter and re-reviewed to `ok` first (stage 1 of
docs/plans/localisation-plan.md). Admission is all or nothing per language, so an admitted table has every key
and no page ever mixes a translated string with an English stand-in for a missing one.

The drafts stay where they are, as the trail; this script only copies cells out of them. On 2026-10-20 no file
carries a reading, so the only table written is English, and every country page is served in English.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import i18n_drafts as drafts

OUT = drafts.ROOT / "model" / "i18n"


def _read_by(text: str) -> set[str]:
    return set(re.findall(r"^- Read by \(([a-z]{2})\):\s*\S.*$", text, re.MULTILINE))


def _open_fixes(text: str) -> set[str]:
    """Languages with a `fix` verdict still standing in the file's review table."""
    rows = drafts._table_after(text, "Review")[1:]
    return {r[1] for r in rows if len(r) > 2 and r[2] == "fix"}


def tables() -> dict[str, str]:
    """Published path under model/i18n/ -> file text, everything admission writes."""
    keys, states = drafts.spec()
    tags = drafts.tags()
    en = {k: v for k, v in keys}
    out_tables: dict[str, dict[str, str]] = {"en": en}
    languages: dict[str, list[dict]] = {}

    for iso, (_name, langs) in states.items():
        path = drafts.DRAFTS / f"{iso}.md"
        text = path.read_text(encoding="utf-8") if path.exists() else ""
        read, fixes = _read_by(text), _open_fixes(text)
        grid = drafts._table_after(text, "Strings")
        head = grid[0] if grid else []
        entries = []
        for lang in langs:
            tag = tags[iso][lang]
            admitted = lang in read and lang not in fixes and lang in head
            if admitted:
                col = head.index(lang)
                table = {r[0]: r[col] for r in grid[1:] if len(r) > col}
                if set(table) != set(en) or not all(table.values()):
                    admitted = False
                else:
                    out_tables[tag] = {k: table[k] for k in en}
            entries.append({"lang": lang, "tag": tag, "admitted": admitted})
        languages[iso] = entries

    files: dict[str, object] = {f"strings/{name}.json": out_tables[name] for name in sorted(out_tables)}
    files["languages.json"] = languages
    return {path: json.dumps(data, ensure_ascii=False, indent=2) + "\n" for path, data in files.items()}


def main(argv: list[str]) -> int:
    want = tables()
    have = {str(p.relative_to(OUT)): p.read_text(encoding="utf-8") for p in OUT.rglob("*.json")} if OUT.exists() else {}
    if "--check" in argv:
        stale = sorted(p for p in set(want) | set(have) if want.get(p) != have.get(p))
        for p in stale:
            print(f"model/i18n/{p}: differs from STRINGS.md and the drafts; run python3 model/i18n_admit.py")
        return 1 if stale else 0
    for p in set(have) - set(want):
        (OUT / p).unlink()
    for p, text in want.items():
        (OUT / p).parent.mkdir(parents=True, exist_ok=True)
        (OUT / p).write_text(text, encoding="utf-8")
    admitted = sorted(p for p in want if p.startswith("strings/") and p != "strings/en.json")
    print(f"wrote model/i18n/: English and {len(admitted)} admitted language table(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
