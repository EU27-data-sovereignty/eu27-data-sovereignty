#!/usr/bin/env python3
"""
The language tables and the app hold each other to one list of strings (#111).

    python3 -m unittest tests.test_i18n -v

model/i18n/ is what admission writes and nothing else; every key the app or the model looks up is in the
table; every key in the table is looked up somewhere, or is named below with the reason it is not yet; and a
keyed heading in the bundle says exactly what the table's English says, so the two cannot drift apart.
"""
from __future__ import annotations

import io
import json
import re
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "model"))

import i18n_admit  # noqa: E402

EN = json.loads((ROOT / "model" / "i18n" / "strings" / "en.json").read_text(encoding="utf-8"))
LANGUAGES = json.loads((ROOT / "model" / "i18n" / "languages.json").read_text(encoding="utf-8"))
BUNDLE = json.loads((ROOT / "web" / "public" / "data" / "eu27.json").read_text(encoding="utf-8"))

# Keys in the table that nothing looks up yet, each with the reason. A key leaves this list when it is wired.
NOT_YET = {
    "fact.disputed": "no state page prints it: the disputed count is on /countries, which is English (#112)",
}


def _web_keys() -> set[str]:
    keys: set[str] = set()
    for f in (ROOT / "web" / "src").rglob("*.ts*"):
        if "__tests__" in f.parts:
            continue
        text = f.read_text(encoding="utf-8")
        keys |= set(re.findall(r"\bt\('([a-z_]+\.[a-z_]+)'[,)]", text))
        keys |= set(re.findall(r"label: '([a-z_]+\.[a-z_]+)'", text))
    return keys


def _bundle_keyed() -> list[tuple[str, str]]:
    """(key, text) for every keyed section title and label in the bundle's documents."""
    out: list[tuple[str, str]] = []

    def walk(node: object) -> None:
        if isinstance(node, dict):
            if "key" in node and ("title" in node or node.get("role") == "label"):
                out.append((node["key"], node.get("title", node.get("t", ""))))
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    walk(BUNDLE)
    return out


class Tables(unittest.TestCase):
    def test_a_language_is_admitted_only_with_a_clean_cross_review(self):
        keys, states = i18n_admit.drafts.spec()
        for iso, entries in LANGUAGES.items():
            if any(e["admitted"] for e in entries):
                problems, _ = i18n_admit.drafts.check_one(iso, keys, states[iso][1])
                self.assertEqual(problems, [], f"{iso} is admitted with an unclean draft")

    def test_vercel_names_the_language_of_every_translated_state_page(self):
        config = json.loads((ROOT / "vercel.json").read_text(encoding="utf-8"))
        named = {b["source"]: h["value"] for b in config["headers"] for h in b["headers"]
                 if h["key"] == "Content-Language"}
        self.assertEqual(named, {b["source"]: b["headers"][0]["value"]
                                 for b in i18n_admit.content_language(LANGUAGES)})

    def test_model_i18n_is_what_admission_writes(self):
        out = io.StringIO()
        with redirect_stdout(out):
            rc = i18n_admit.main(["--check"])
        self.assertEqual(rc, 0, out.getvalue())

    def test_an_admitted_language_has_a_whole_table(self):
        for iso, langs in LANGUAGES.items():
            for lang in langs:
                if lang["lang"] == "en":
                    continue  # English where it is official (IE, MT) reads the source table
                path = ROOT / "model" / "i18n" / "strings" / f"{lang['tag']}.json"
                self.assertEqual(lang["admitted"], path.exists(), f"{iso} {lang['tag']}")
                if path.exists():
                    table = json.loads(path.read_text(encoding="utf-8"))
                    self.assertEqual(list(table), list(EN), f"{lang['tag']}: keys differ from English")


class Wiring(unittest.TestCase):
    def test_every_key_looked_up_is_in_the_table(self):
        used = _web_keys() | {k for k, _ in _bundle_keyed()}
        self.assertEqual(sorted(used - set(EN)), [])

    def test_every_key_in_the_table_is_looked_up_or_named_with_its_reason(self):
        used = _web_keys() | {k for k, _ in _bundle_keyed()}
        self.assertEqual(sorted(set(EN) - used - set(NOT_YET)), [])
        self.assertEqual(sorted(set(NOT_YET) & used), [], "wired now: take it off NOT_YET")

    def test_a_keyed_heading_in_the_bundle_says_what_the_table_says(self):
        keyed = _bundle_keyed()
        self.assertTrue(keyed, "the bundle carries no keyed headings")
        wrong = sorted({(k, t) for k, t in keyed if EN.get(k) != t})
        self.assertEqual(wrong, [])


if __name__ == "__main__":
    unittest.main()
