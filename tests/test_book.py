"""The book is typeset by typst and CI has no typst, so its output is otherwise ungated.

These tests do not compile anything. They import the builder and assert on the *typst source*
it emits, which needs only the JSON bundle -- so they run everywhere `unittest discover` does,
including CI.

What they protect is the one rule that cannot be recovered after the fact: the interior is
monochrome (DECISIONS.md #28) and must typeset identically off a Mac. A country flag emoji
would satisfy neither -- typst can only reach those glyphs by falling back to Apple Color
Emoji, so the same source would render colour flags here and empty boxes on a Linux machine,
silently.
"""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "book"))

import build as book  # noqa: E402

BUNDLE = ROOT / "web" / "public" / "data" / "eu27.json"

# U+1F1E6..U+1F1FF REGIONAL INDICATOR SYMBOL LETTER A..Z -- flag emoji are pairs of these.
REGIONAL_INDICATORS = range(0x1F1E6, 0x1F200)


def flag_chars(text: str) -> list[str]:
    return [c for c in text if ord(c) in REGIONAL_INDICATORS]


class NoFlagsInTheBook(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not BUNDLE.exists():
            raise unittest.SkipTest("run ./run.sh data first")
        cls.bundle = json.loads(BUNDLE.read_text(encoding="utf-8"))

    def test_the_assembled_book_contains_no_flag_emoji(self):
        typ = book.assemble(self.bundle, [1, 2, 3, 4, 5])
        self.assertEqual(flag_chars(typ), [], "a flag emoji reached the mono book interior")

    def test_no_standalone_brief_contains_a_flag_emoji(self):
        for iso, c in sorted(self.bundle["countries"].items()):
            with self.subTest(iso=iso):
                self.assertEqual(flag_chars(book.country_entry(c, standalone=True)), [])


class OutlineScansByIsoCode(unittest.TestCase):
    """The chapter head is the outline entry -- typst has no short-title."""

    @classmethod
    def setUpClass(cls):
        if not BUNDLE.exists():
            raise unittest.SkipTest("run ./run.sh data first")
        cls.bundle = json.loads(BUNDLE.read_text(encoding="utf-8"))

    def test_every_country_chapter_head_carries_its_iso(self):
        for iso, c in sorted(self.bundle["countries"].items()):
            with self.subTest(iso=iso):
                head = book.country_entry(c, standalone=False).splitlines()[0]
                self.assertTrue(head.startswith(f"== {iso} "), head)
                self.assertIn(c["name"], head)

    def test_a_standalone_brief_has_no_chapter_head(self):
        """Its title block already carries the name; the heading would duplicate it."""
        de = self.bundle["countries"]["DE"]
        self.assertFalse(book.country_entry(de, standalone=True).startswith("== DE"))


if __name__ == "__main__":
    unittest.main()
