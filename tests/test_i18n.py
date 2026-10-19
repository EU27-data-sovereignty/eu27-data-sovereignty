#!/usr/bin/env python3
"""
The admitted interface catalogue (#117): a language reaches the reader only from a draft that is complete in
both parts, reviewed by the other agent with every `fix` applied, and read by a native speaker.

    python3 -m unittest tests.test_i18n -v
"""
from __future__ import annotations

import io
import json
import re
import shutil
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "model"))

import i18n  # noqa: E402
import i18n_drafts  # noqa: E402


def _reader_part(langs: list[str], prefix: str = "") -> str:
    """A complete 'Reader strings' and 'Reader review' part, every cell `<lang>:<en>`, every verdict ok."""
    keys = i18n_drafts.reader_keys()
    esc = lambda v: v.replace("|", "\\|")  # noqa: E731
    rows = ["| key | en | " + " | ".join(langs) + " |", "|---|---|" + "---|" * len(langs)]
    rows += [f"| {k} | {esc(en)} | " + " | ".join(f"{prefix}{lg}:{esc(en)}" for lg in langs) + " |" for k, en in keys]
    review = ["| key | lang | verdict | note | suggestion |", "|---|---|---|---|---|"]
    review += [f"| {k} | {lg} | ok | | |" for k, _ in keys for lg in langs]
    return "\n## Reader strings\n\n" + "\n".join(rows) + "\n\n## Reader review\n\n" + "\n".join(review) + "\n"


def _apply_fixes(text: str) -> str:
    """Apply every `fix` suggestion to its cell and mark it `fixed`, as the reviewer's wording."""
    head, review = text.split("\n## Review\n", 1)
    review_part, rest = (review.split("\n## Reader strings\n", 1) + [""])[:2]
    fixes = []
    for line in review_part.splitlines():
        cells = [c.strip() for c in re.split(r"(?<!\\)\|", line)[1:-1]]
        if len(cells) >= 5 and cells[2] == "fix":
            fixes.append((cells[0], cells[1], cells[4]))
    langs = re.search(r"^\| key \| en \| (.+) \|$", head, re.M).group(1).split(" | ")
    out = []
    for line in head.splitlines():
        cells = [c.strip() for c in re.split(r"(?<!\\)\|", line)[1:-1]]
        for key, lang, wording in fixes:
            if cells and cells[0] == key:
                cells[2 + langs.index(lang)] = wording
                line = "| " + " | ".join(cells) + " |"
        out.append(line)
    review_part = re.sub(r"^(\| [^|]+ \| [a-z]{2} \| )fix( \|)", r"\1fixed\2", review_part, flags=re.M)
    return "\n".join(out) + "\n## Review\n" + review_part + ("\n## Reader strings\n" + rest if rest else "")


class Admission(unittest.TestCase):
    """A scratch copy of the drafts, so each test can change one state's file and watch admission."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        shutil.copytree(i18n_drafts.DRAFTS, self.tmp / "drafts")
        self._drafts = i18n_drafts.DRAFTS
        i18n_drafts.DRAFTS = self.tmp / "drafts"

    def tearDown(self):
        i18n_drafts.DRAFTS = self._drafts
        shutil.rmtree(self.tmp)

    def _write(self, iso: str, transform):
        p = self.tmp / "drafts" / f"{iso}.md"
        p.write_text(transform(p.read_text(encoding="utf-8")), encoding="utf-8")

    def _languages(self) -> dict:
        files, _ = i18n.build()
        return json.loads(files["mobile/assets/i18n/catalogue.json"])["languages"]

    def _ready(self, text: str, read: bool = True, fixes: bool = True, prefix: str = "") -> str:
        text = _apply_fixes(text) if fixes else text
        text = text.rstrip("\n") + "\n" + _reader_part(["de"], prefix)
        if read:
            text = text.replace("- Languages:", "- Read by (de): native speaker, 2026-10-19\n- Languages:", 1)
        return text

    def test_the_tree_admits_english_only(self):
        self.assertEqual(sorted(self._languages()), ["en"])

    def test_read_reviewed_and_fixed_is_admitted(self):
        self._write("AT", self._ready)
        langs = self._languages()
        self.assertIn("de", langs)
        de = langs["de"]
        self.assertEqual(de["strings"]["app.tab.countries"], "de:Countries")
        self.assertEqual(set(de["strings"]), set(langs["en"]["strings"]))
        self.assertEqual(de["provenance"][0]["read"], "native speaker, 2026-10-19")
        self.assertEqual(de["provenance"][0]["iso"], "AT")

    def test_unread_is_not_admitted(self):
        self._write("AT", lambda t: self._ready(t, read=False))
        self.assertNotIn("de", self._languages())

    def test_an_outstanding_fix_blocks_admission(self):
        self._write("AT", lambda t: self._ready(t, fixes=False))
        self.assertNotIn("de", self._languages())

    def test_a_fixed_cell_must_read_as_suggested(self):
        def tamper(t: str) -> str:
            t = self._ready(t)
            return re.sub(r"^(\| [^|]+ \| de \| fixed \| [^|]* \| )([^|]+)( \|)$", r"\1something else\3", t, count=1, flags=re.M)
        self._write("AT", tamper)
        self.assertNotIn("de", self._languages())

    def test_states_sharing_a_language_merge_with_overlays(self):
        self._write("AT", lambda t: self._ready(t, prefix="AT-"))
        self._write("DE", lambda t: self._ready(t, prefix=""))
        files, _ = i18n.build()
        de = json.loads(files["model/i18n/de.json"])
        self.assertEqual([p["iso"] for p in de["provenance"]], ["AT", "DE"])
        # A tie goes to the first state alphabetically; the other keeps its wording as an overlay.
        self.assertEqual(de["strings"]["app.tab.countries"], "AT-de:Countries")
        self.assertEqual(de["overlays"]["DE"]["app.tab.countries"], "de:Countries")
        self.assertNotIn("AT", de["overlays"])


class Catalogue(unittest.TestCase):
    def test_check_passes_on_the_tree(self):
        out = io.StringIO()
        with redirect_stdout(out):
            rc = i18n.check()
        self.assertEqual(rc, 0, out.getvalue())

    def test_every_label_and_gap_the_bundle_prints_has_a_key(self):
        bundle = json.loads(i18n.BUNDLE.read_text(encoding="utf-8"))
        en = set(i18n.english().values())
        for _key, text, _role in i18n.content_strings(bundle):
            self.assertIn(text, en)

    def test_keys_are_unique_across_both_tables(self):
        chrome, _ = i18n_drafts.spec()
        keys = [k for k, _ in chrome] + [k for k, _ in i18n_drafts.reader_keys()]
        self.assertEqual(len(keys), len(set(keys)))

    def test_only_label_and_gap_spans_are_keyed(self):
        # A categorical fact value is a fact (#82, #87), even where a label elsewhere has the same words ("EU
        # provider"): only the label is keyed, and the reader translates spans by role, never a fact span.
        bundle = json.loads(i18n.BUNDLE.read_text(encoding="utf-8"))
        rows = i18n.content_strings(bundle)
        self.assertTrue(rows)
        self.assertTrue(all(k.startswith(f"{role}.") and role in ("label", "gap") for k, _t, role in rows))

if __name__ == "__main__":
    unittest.main()
