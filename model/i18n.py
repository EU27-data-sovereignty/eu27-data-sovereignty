#!/usr/bin/env python3
"""
The admitted interface catalogue (#117): which languages the reader may show, and in what words.

    python3 model/i18n.py strings   # rewrite the generated labels-and-gaps table in docs/i18n/STRINGS-reader.md
    python3 model/i18n.py admit     # write model/i18n/ and mobile/assets/i18n/catalogue.json from the drafts
    python3 model/i18n.py check     # all three are what the commands above would write; exit 1 otherwise
    python3 model/i18n.py why       # per state column: admitted, or the first reason it is not

A language is admitted from a state's draft column only when the draft passes `model/i18n_drafts.py`'s
checks, both of its parts (the chrome of STRINGS.md and the reader's STRINGS-reader.md) are drafted, no review
verdict is an outstanding `fix`, and the draft carries `- Read by (<lang>): <role>, <date>`: one native speaker
has read that column. Machine drafting and a machine review are never enough on their own.

The states that share a language (de: DE, AT, BE, LU) are merged: the most common wording per key is the
language's, ties going to the first state alphabetically, and a state whose admitted wording differs keeps it
as an overlay. Every language file names, per state column it was built from, who drafted, reviewed and read
it and the sha256 of the draft file, so a third party can trace any word on the reader's screen to its draft.

English is the source, not a translation: `en.json` is STRINGS.md plus STRINGS-reader.md and is always present.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import i18n_drafts as drafts  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
BUNDLE = ROOT / "web" / "public" / "data" / "eu27.json"
OUT = ROOT / "model" / "i18n"
CATALOGUE = ROOT / "mobile" / "assets" / "i18n" / "catalogue.json"
START, END = "<!-- generated:start -->\n", "<!-- generated:end -->"

# Each language's name in itself, for the reader's picker. Luxembourgish is a national, not an EU, language.
AUTONYMS = {
    "bg": "Български", "cs": "Čeština", "da": "Dansk", "de": "Deutsch", "el": "Ελληνικά", "en": "English",
    "es": "Español", "et": "Eesti", "fi": "Suomi", "fr": "Français", "ga": "Gaeilge", "hr": "Hrvatski",
    "hu": "Magyar", "it": "Italiano", "lb": "Lëtzebuergesch", "lt": "Lietuvių", "lv": "Latviešu", "mt": "Malti",
    "nl": "Nederlands", "pl": "Polski", "pt": "Português", "ro": "Română", "sk": "Slovenčina", "sl": "Slovenščina",
    "sv": "Svenska",
}
READ_BY = re.compile(r"^- Read by \(([a-z]{2})\):\s*(.+)$", re.M)


# --- the generated table ---------------------------------------------------------------------------------------

def _slug(text: str) -> str:
    ascii_ = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "_", ascii_.lower()).strip("_")[:48] or "x"


def content_strings(bundle: dict) -> list[tuple[str, str, str]]:
    """Every distinct label and gap text the bundle prints, keyed, sorted by key: (key, en, role)."""
    found: dict[str, str] = {}

    def walk(x):
        if isinstance(x, dict):
            if x.get("role") in ("label", "gap") and isinstance(x.get("t"), str):
                text = x["t"].strip()
                if re.search(r"[A-Za-z]", text):
                    found.setdefault(text, x["role"])
            for v in x.values():
                walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)

    walk(bundle.get("documents", {}))
    walk(bundle.get("infrastructure", {}))
    taken: set[str] = set()
    rows = []
    for text, role in sorted(found.items(), key=lambda kv: (kv[1], _slug(kv[0]), kv[0])):
        key = f"{role}.{_slug(text)}"
        n = 2
        while key in taken:
            key = f"{role}.{_slug(text)}_{n}"
            n += 1
        taken.add(key)
        rows.append((key, text, role))
    return sorted(rows)


def strings_table(bundle: dict) -> str:
    lines = ["| key | en | where it prints |", "|---|---|---|"]
    where = {"label": "a table label in the content model", "gap": "a gap marker in the content model"}
    for key, text, role in content_strings(bundle):
        lines.append(f"| {key} | {text.replace('|', chr(92) + '|')} | {where[role]} |")
    return "\n".join(lines) + "\n"


def _with_table(text: str, table: str) -> str:
    a, b = text.index(START) + len(START), text.index(END)
    return text[:a] + table + text[b:]


# --- admission ------------------------------------------------------------------------------------------------

def english() -> dict[str, str]:
    keys, _ = drafts.spec()
    return dict(keys) | dict(drafts.reader_keys())


def _cells(text: str, heading: str, langs: list[str]) -> dict[str, dict[str, str]]:
    """lang -> {key: cell} from one strings table of a draft."""
    out: dict[str, dict[str, str]] = {lang: {} for lang in langs}
    for r in drafts._table_after(text, heading)[1:]:
        for lang, cell in zip(langs, r[2:]):
            out[lang][r[0]] = cell
    return out


def admitted_columns() -> tuple[dict[str, list[dict]], list[str]]:
    """lang -> the admitted state columns, and one line per column saying why it was or was not admitted."""
    keys, states = drafts.spec()
    reader = drafts.reader_keys()
    columns: dict[str, list[dict]] = {}
    report = []
    for iso, (_name, langs) in states.items():
        problems, info = drafts.check_one(iso, keys, langs)
        path = drafts.DRAFTS / f"{iso}.md"
        text = path.read_text(encoding="utf-8") if path.exists() else ""
        read = dict(READ_BY.findall(text))
        chrome, own = _cells(text, "Strings", langs), _cells(text, "Reader strings", langs)
        for lang in langs:
            open_fix = [k for (k, lg), v in info["verdicts"].items() if lg == lang and v == "fix"]
            why = ("draft fails its check" if problems
                   else "reader part not drafted" if reader and info["reader"] != "drafted"
                   else f"{len(open_fix)} fix verdict(s) not applied" if open_fix
                   else "not read by a native speaker" if lang not in read
                   else "")
            report.append(f"{iso} {lang}: {'admitted' if not why else why}")
            if why:
                continue
            columns.setdefault(lang, []).append({
                "iso": iso,
                "tag": drafts.tags().get(iso, {}).get(lang, ""),
                "strings": chrome[lang] | own[lang],
                "drafted": info["drafted"],
                "reviewed": info["reviewed"],
                "read": read[lang].strip(),
                "draft_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            })
    return columns, report


def merge(lang: str, cols: list[dict], keys: list[str]) -> dict:
    """One language from its admitted state columns: the common wording, and each state's differences."""
    cols = sorted(cols, key=lambda c: c["iso"])
    base = {}
    for key in keys:
        values = [c["strings"][key] for c in cols if key in c["strings"]]
        if values:
            counts = Counter(values)
            top = max(counts.values())
            base[key] = next(v for v in values if counts[v] == top)
    overlays = {c["iso"]: d for c in cols if (d := {k: v for k, v in c["strings"].items() if base.get(k) != v})}
    return {
        "lang": lang,
        "name": AUTONYMS.get(lang, lang),
        "strings": base,
        "overlays": overlays,
        "provenance": [{k: c[k] for k in ("iso", "tag", "drafted", "reviewed", "read", "draft_sha256")}
                       for c in cols],
    }


def _dump(obj) -> str:
    return json.dumps(obj, ensure_ascii=False, indent=1, sort_keys=True) + "\n"


def build() -> tuple[dict[str, str], list[str]]:
    """Every file admission writes, path relative to ROOT -> content, plus the per-column report."""
    en = english()
    sources = [drafts.STRINGS, drafts.READER_STRINGS]
    files = {
        "model/i18n/en.json": _dump({
            "lang": "en", "name": AUTONYMS["en"], "strings": en, "overlays": {},
            "provenance": [{"source": str(p.relative_to(ROOT)), "sha256": hashlib.sha256(p.read_bytes()).hexdigest()}
                           for p in sources],
        }),
    }
    columns, report = admitted_columns()
    languages = {"en": json.loads(files["model/i18n/en.json"])}
    for lang in sorted(columns):
        languages[lang] = merge(lang, columns[lang], list(en))
        files[f"model/i18n/{lang}.json"] = _dump(languages[lang])
    _, states = drafts.spec()
    index = {
        "languages": sorted(languages),
        "states": {iso: langs for iso, (_n, langs) in states.items()},
        "files": {name.split("/")[-1]: hashlib.sha256(body.encode()).hexdigest()
                  for name, body in sorted(files.items())},
    }
    files["model/i18n/index.json"] = _dump(index)
    files[str(CATALOGUE.relative_to(ROOT))] = _dump({"languages": languages, "states": index["states"]})
    return files, report


def admit() -> int:
    files, report = build()
    OUT.mkdir(exist_ok=True)
    for stale in OUT.glob("*.json"):
        if str(stale.relative_to(ROOT)) not in files:
            stale.unlink()
    CATALOGUE.parent.mkdir(parents=True, exist_ok=True)
    for rel, body in files.items():
        (ROOT / rel).write_text(body, encoding="utf-8")
    langs = json.loads(files["model/i18n/index.json"])["languages"]
    print(f"admitted {len(langs)} language(s): {', '.join(langs)}; wrote {len(files)} files")
    return 0


def check() -> int:
    problems = []
    bundle = json.loads(BUNDLE.read_text(encoding="utf-8"))
    text = drafts.READER_STRINGS.read_text(encoding="utf-8")
    if _with_table(text, strings_table(bundle)) != text:
        problems.append("docs/i18n/STRINGS-reader.md: the labels-and-gaps table is stale (python3 model/i18n.py strings)")
    keys = [k for k, _ in drafts.reader_keys()]
    if len(keys) != len(set(keys)):
        problems.append("docs/i18n/STRINGS-reader.md: a key appears twice")
    files, report = build()
    for rel, body in files.items():
        p = ROOT / rel
        if not p.exists() or p.read_text(encoding="utf-8") != body:
            problems.append(f"{rel}: not what admission writes (python3 model/i18n.py admit)")
    for stray in sorted(OUT.glob("*.json")) if OUT.exists() else []:
        if str(stray.relative_to(ROOT)) not in files:
            problems.append(f"{stray.relative_to(ROOT)}: not admitted from any draft")
    langs = json.loads(files["model/i18n/index.json"])["languages"]
    print(f"{len(langs)} language(s) admitted ({', '.join(langs)}), {len(english())} keys, "
          f"{sum(1 for r in report if r.endswith('admitted'))} of {len(report)} state columns admitted, "
          f"{len(problems)} problems")
    for p in problems:
        print("  " + p)
    return 1 if problems else 0


def strings() -> int:
    bundle = json.loads(BUNDLE.read_text(encoding="utf-8"))
    text = drafts.READER_STRINGS.read_text(encoding="utf-8")
    drafts.READER_STRINGS.write_text(_with_table(text, strings_table(bundle)), encoding="utf-8")
    print(f"wrote {len(content_strings(bundle))} labels and gaps into {drafts.READER_STRINGS.relative_to(ROOT)}")
    return 0


def why() -> int:
    for line in admitted_columns()[1]:
        print(line)
    return 0


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "check"
    commands = {"strings": strings, "admit": admit, "check": check, "why": why}
    if cmd not in commands:
        print(__doc__)
        sys.exit(2)
    sys.exit(commands[cmd]())
