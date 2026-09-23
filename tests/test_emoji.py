"""The flag table, asserted against literal glyphs rather than the same arithmetic twice.

`model/emoji.py` computes its glyphs from codepoints so that file can stay ASCII. A test that
recomputed them the same way would pass on any consistent bug -- an off-by-one in the offset,
say, would produce a self-consistent set of wrong flags. So the expected values are written
out here as real characters, once, and read by eye.

`web/src/utils/format.ts` carries the same derivation for the web and mobile readers and is
checked against the same 27 pairs in `web/src/__tests__/format.test.ts`. Two implementations,
one table, asserted twice.
"""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "model"))

import capacity_model as cm  # noqa: E402
import emoji  # noqa: E402

# Every member state, in the order model/eu27_parameters.csv lists them.
EXPECTED = {
    "AT": "🇦🇹",  # Austria
    "BE": "🇧🇪",  # Belgium
    "BG": "🇧🇬",  # Bulgaria
    "HR": "🇭🇷",  # Croatia
    "CY": "🇨🇾",  # Cyprus
    "CZ": "🇨🇿",  # Czechia
    "DK": "🇩🇰",  # Denmark
    "EE": "🇪🇪",  # Estonia
    "FI": "🇫🇮",  # Finland
    "FR": "🇫🇷",  # France
    "DE": "🇩🇪",  # Germany
    "EL": "🇬🇷",  # Greece -- Eurostat's EL, the Greek flag
    "HU": "🇭🇺",  # Hungary
    "IE": "🇮🇪",  # Ireland
    "IT": "🇮🇹",  # Italy
    "LV": "🇱🇻",  # Latvia
    "LT": "🇱🇹",  # Lithuania
    "LU": "🇱🇺",  # Luxembourg
    "MT": "🇲🇹",  # Malta
    "NL": "🇳🇱",  # Netherlands
    "PL": "🇵🇱",  # Poland
    "PT": "🇵🇹",  # Portugal
    "RO": "🇷🇴",  # Romania
    "SK": "🇸🇰",  # Slovakia
    "SI": "🇸🇮",  # Slovenia
    "ES": "🇪🇸",  # Spain
    "SE": "🇸🇪",  # Sweden
}


class Flags(unittest.TestCase):
    def test_every_member_state_maps_to_its_own_flag(self):
        for iso, expected in EXPECTED.items():
            with self.subTest(iso=iso):
                self.assertEqual(emoji.flag(iso), expected)

    def test_the_table_covers_exactly_the_dataset(self):
        """A state added to eu27_parameters.csv must be added here too."""
        params = cm.read_csv(ROOT / "model" / "eu27_parameters.csv")
        self.assertEqual({r["iso2"] for r in params}, set(EXPECTED))

    def test_greece_is_the_only_override(self):
        """EL is Eurostat's code for Greece; the flag sequence needs ISO alpha-2 GR."""
        self.assertEqual(emoji.OVERRIDES, {"EL": "GR"})
        self.assertEqual(emoji.flag("EL"), emoji.flag("GR"))

    def test_every_flag_is_two_regional_indicators(self):
        for iso in EXPECTED:
            with self.subTest(iso=iso):
                chars = list(emoji.flag(iso))
                self.assertEqual(len(chars), 2)
                for ch in chars:
                    self.assertTrue(0x1F1E6 <= ord(ch) <= 0x1F1FF, f"{ch!r} is not an indicator")

    def test_a_bad_code_raises_rather_than_rendering_boxes(self):
        for bad in ("", "N", "NLD", "N1", "nl ", "ÑL"):
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):
                    emoji.flag(bad)

    def test_lowercase_is_accepted(self):
        self.assertEqual(emoji.flag("nl"), emoji.flag("NL"))


if __name__ == "__main__":
    unittest.main()
