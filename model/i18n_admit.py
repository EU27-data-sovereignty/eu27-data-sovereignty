#!/usr/bin/env python3
"""
Admission: the language tables the app reads, written from STRINGS.md and the drafts that have earned it.

    python3 model/i18n_admit.py           # write model/i18n/ and the Content-Language headers in vercel.json
    python3 model/i18n_admit.py --check   # exit 1 if either differs from what the sources give

English always comes from docs/i18n/STRINGS.md, the source every draft translates. A draft language is admitted
when its file passes model/i18n_drafts.py's contract, every key and every cell reviewed by the agent on the other
model, and the review holds no `fix` for that language (#112). Admission is all or nothing per language, so an
admitted table has every key and no page mixes a translated string with an English stand-in for a missing one.

Whether a person who reads the language has checked it is recorded, not required (#112, amending #111): the
owner chose to collect those readings on the live site while it has no traffic. `read` is true once the file
carries `- Read by (<lang>): <role>, <date>`, and a page served in an unread language says, in that language and
in English, that its labels are a machine translation nobody who reads it has checked.

The drafts stay where they are, as the trail; this script only copies cells out of them.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import i18n_drafts as drafts

OUT = drafts.ROOT / "model" / "i18n"
VERCEL = drafts.ROOT / "vercel.json"


def _read_by(text: str) -> set[str]:
    return set(re.findall(r"^- Read by \(([a-z]{2})\):\s*\S.*$", text, re.MULTILINE))


def _open_fixes(text: str) -> set[str]:
    """Languages with a `fix` verdict still standing in the file's review table."""
    rows = drafts._table_after(text, "Review")[1:]
    return {r[1] for r in rows if len(r) > 2 and r[2] == "fix"}


def english_official() -> set[str]:
    """States where English is itself an official language (IE, MT): STRINGS.md marks it as the source there."""
    text = drafts.STRINGS.read_text(encoding="utf-8")
    rows = drafts._rows(text.split("## Official languages")[1].split("## The standards")[0].splitlines())[1:]
    return {r[0] for r in rows if "en is the source" in r[2]}


def site_languages(languages: dict[str, list[dict]]) -> list[dict]:
    """The languages a reader can choose for the whole site (#113), from STRINGS.md's "Site-wide languages": each
    reads its home state's table, and is offered once that table is admitted."""
    text = drafts.STRINGS.read_text(encoding="utf-8")
    if "## Site-wide languages" not in text:
        return []
    rows = drafts._rows(text.split("## Site-wide languages")[1].splitlines())[1:]
    by_tag = {e["tag"]: e for entries in languages.values() for e in entries}
    out = []
    for lang, home in ((r[0], r[1]) for r in rows):
        e = by_tag.get(home, {})
        out.append({"lang": lang, "tag": home, "admitted": bool(e.get("admitted")), "read": bool(e.get("read"))})
    return out


def admitted() -> tuple[dict[str, dict[str, str]], dict[str, list[dict]]]:
    """(tag -> table, ISO -> [{lang, tag, admitted, read}]) from the source table and the drafts."""
    keys, states = drafts.spec()
    tags = drafts.tags()
    en = dict(keys)
    out_tables: dict[str, dict[str, str]] = {"en": en}
    languages: dict[str, list[dict]] = {}

    english = english_official()
    for iso, (_name, langs) in states.items():
        path = drafts.DRAFTS / f"{iso}.md"
        text = path.read_text(encoding="utf-8") if path.exists() else ""
        problems, _info = drafts.check_one(iso, keys, langs)
        read, fixes = _read_by(text), _open_fixes(text)
        grid = drafts._table_after(text, "Strings")
        head = grid[0] if grid else []
        # Where English is official it comes first, so the state's address opens in it (`/ie`, `/mt`).
        entries = [{"lang": "en", "tag": f"en-{iso}", "admitted": True, "read": True}] if iso in english else []
        for lang in langs:
            tag = tags[iso][lang]
            ok = not problems and lang not in fixes and lang in head
            if ok:
                col = head.index(lang)
                table = {r[0]: r[col] for r in grid[1:] if len(r) > col}
                ok = set(table) == set(en) and all(table.values())
                if ok:
                    out_tables[tag] = {k: table[k] for k in en}
            entries.append({"lang": lang, "tag": tag, "admitted": ok, "read": lang in read})
        languages[iso] = entries
    return out_tables, languages


def content_language(languages: dict[str, list[dict]]) -> list[dict]:
    """Vercel header blocks: each state page served in an admitted language names it (`/ie` is en-IE)."""
    blocks = []
    for iso, entries in sorted(languages.items()):
        served = [e for e in entries if e["admitted"]]
        for i, e in enumerate(served):
            path = f"/{iso.lower()}" if i == 0 else f"/{iso.lower()}/{e['lang']}"
            blocks.append({"source": path, "headers": [{"key": "Content-Language", "value": e["tag"]}]})
    return blocks


def vercel_text(languages: dict[str, list[dict]]) -> str:
    config = json.loads(VERCEL.read_text(encoding="utf-8"))
    kept = [b for b in config.get("headers", [])
            if not any(h["key"] == "Content-Language" for h in b.get("headers", []))]
    config["headers"] = kept + content_language(languages)
    return json.dumps(config, ensure_ascii=False, indent=2) + "\n"


def tables() -> dict[str, str]:
    """Published path under model/i18n/ -> file text, everything admission writes there."""
    out_tables, languages = admitted()
    files: dict[str, object] = {f"strings/{name}.json": out_tables[name] for name in sorted(out_tables)}
    files["languages.json"] = languages
    files["site.json"] = site_languages(languages)
    return {path: json.dumps(data, ensure_ascii=False, indent=2) + "\n" for path, data in files.items()}


def main(argv: list[str]) -> int:
    want = tables()
    have = {str(p.relative_to(OUT)): p.read_text(encoding="utf-8") for p in OUT.rglob("*.json")} if OUT.exists() else {}
    vercel = vercel_text(admitted()[1])
    if "--check" in argv:
        stale = [f"model/i18n/{p}" for p in sorted(set(want) | set(have)) if want.get(p) != have.get(p)]
        if vercel != VERCEL.read_text(encoding="utf-8"):
            stale.append("vercel.json (Content-Language headers)")
        for p in stale:
            print(f"{p}: differs from STRINGS.md and the drafts; run python3 model/i18n_admit.py")
        return 1 if stale else 0
    for p in set(have) - set(want):
        (OUT / p).unlink()
    for p, text in want.items():
        (OUT / p).parent.mkdir(parents=True, exist_ok=True)
        (OUT / p).write_text(text, encoding="utf-8")
    VERCEL.write_text(vercel, encoding="utf-8")
    n = sum(1 for p in want if p.startswith("strings/") and p != "strings/en.json")
    print(f"wrote model/i18n/ (English and {n} admitted language table(s)) and vercel.json's Content-Language headers")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
