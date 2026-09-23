"""The critical national data register, and the ratchet that keeps its coverage honest.

Mirrors tests/test_sources.py, including the part that is easy to leave out: the floor is
asserted from BOTH sides. One test fails if coverage drops (a row was deleted), the other
fails if coverage rises without the floor moving with it. Together they assert equality, so
progress cannot be silently undone and the constant cannot silently go stale.
"""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "model"))

import national_data as nd  # noqa: E402

# Raise as registers are recorded. 405 = 15 record classes x 27 member states.
NATIONAL_DATA_FLOOR = 3


class Register(unittest.TestCase):
    def setUp(self):
        self.rows = nd.load()  # raises if the header is not exactly FIELDS

    def test_every_row_is_usable_evidence(self):
        self.assertEqual(nd.validate(self.rows), [])

    def test_coverage_never_regresses(self):
        covered = nd.covered_cells(self.rows)
        self.assertGreaterEqual(
            covered,
            NATIONAL_DATA_FLOOR,
            f"coverage fell to {covered} from a floor of {NATIONAL_DATA_FLOOR}: a row was "
            "removed. Registers are only ever added, or replaced by a better source.",
        )

    def test_the_floor_is_kept_current(self):
        covered = nd.covered_cells(self.rows)
        self.assertLessEqual(
            covered - NATIONAL_DATA_FLOOR,
            0,
            f"{covered} pairs are recorded but NATIONAL_DATA_FLOOR is still "
            f"{NATIONAL_DATA_FLOOR}. Raise it in this file so the progress cannot be undone.",
        )


class Vocabulary(unittest.TestCase):
    """The closed vocabularies are what make a blank row mean 'not researched'."""

    def test_the_two_tiers_partition_the_record_classes(self):
        self.assertEqual(len(nd.TIER0), 8)
        self.assertEqual(len(nd.TIER1), 7)
        self.assertEqual(set(nd.TIER0) & set(nd.TIER1), set())
        self.assertEqual(len(nd.RECORD_CLASSES), 15)

    def test_record_class_order_is_by_consequence_of_loss_not_alphabet(self):
        """TIER0-TIER1-SIZING.md orders by consequence of loss; sorting would destroy it."""
        self.assertNotEqual(list(nd.RECORD_CLASSES), sorted(nd.RECORD_CLASSES))
        self.assertEqual(nd.RECORD_CLASSES[0], "civil_registry")

    def test_every_record_class_knows_its_tier(self):
        self.assertEqual(set(nd.TIER_OF), set(nd.RECORD_CLASSES))
        for c in nd.TIER0:
            self.assertEqual(nd.TIER_OF[c], 0)
        for c in nd.TIER1:
            self.assertEqual(nd.TIER_OF[c], 1)


class ValidationRules(unittest.TestCase):
    """Each rule is checked against a row that breaks exactly it."""

    BASE = {
        "iso": "NL", "tier": "0", "record_class": "civil_registry", "status": "held",
        "register": "Basisregistratie Personen (BRP)", "holder": "RvIG",
        "holder_url": "https://www.rvig.nl/", "url": "https://www.rvig.nl/brp",
        "publisher": "RvIG", "retrieved": "2026-09-21", "confidence": "official",
        "quote": "De overheid registreert persoonsgegevens in de BRP.",
    }

    def errors(self, **overrides):
        return nd.validate([{**self.BASE, **overrides}])

    def test_the_base_row_is_valid(self):
        self.assertEqual(self.errors(), [])

    def test_a_class_declared_in_the_wrong_tier_is_rejected(self):
        self.assertTrue(any("tier" in e for e in self.errors(tier="1")))

    def test_not_held_requires_evidenced_absence(self):
        """Claiming no register exists is a real finding and needs a real enumeration."""
        self.assertTrue(any("absence" in e for e in self.errors(status="not_held")))
        self.assertEqual(
            self.errors(status="not_held", confidence="absence", register=""), []
        )

    def test_held_cannot_claim_absence(self):
        self.assertTrue(any("contradicts" in e for e in self.errors(confidence="absence")))

    def test_a_short_quote_is_not_evidence(self):
        self.assertTrue(any("quote" in e for e in self.errors(quote="yes")))

    def test_a_non_https_url_is_rejected(self):
        self.assertTrue(any("url" in e for e in self.errors(url="http://www.rvig.nl/brp")))

    def test_an_email_address_is_rejected(self):
        """The bundle's own test fails on an email anywhere in it, in a suite CI never runs."""
        bad = self.errors(quote="Write to voorlichting@rvig.nl for the register description.")
        self.assertTrue(any("email" in e for e in bad))

    def test_an_unknown_country_is_rejected(self):
        self.assertTrue(any("ISO" in e for e in self.errors(iso="UK")))

    def test_duplicate_country_and_class_is_rejected(self):
        rows = [dict(self.BASE), dict(self.BASE)]
        self.assertTrue(any("duplicate" in e for e in nd.validate(rows)))

    def test_rows_out_of_order_are_rejected(self):
        rows = [
            {**self.BASE, "record_class": "tax", "tier": "1"},
            {**self.BASE, "record_class": "civil_registry", "tier": "0"},
        ]
        self.assertTrue(any("sorted" in e for e in nd.validate(rows)))


class TheDutchBriefStaysInSync(unittest.TestCase):
    """countries/NL/GOAL.md is hand-written, which makes it a second source of truth.

    The generator is forbidden to touch NL (#5), and tests/test_model.py only asserts that it
    stays away -- nothing asserts the prose still matches the register. NL is the country the
    whole model derives from and the first one a Dutch reader checks, so the drift that matters
    most is the one nothing was watching. This is the cheapest sufficient guard: a containment
    check, not a parser.
    """

    NL_GOAL = ROOT / "countries" / "NL" / "GOAL.md"

    def setUp(self):
        self.rows = [r for r in nd.load() if r["iso"] == "NL"]
        self.text = self.NL_GOAL.read_text(encoding="utf-8")

    def test_the_brief_has_the_section_at_all(self):
        self.assertIn("Critical national data in scope", self.text)

    def test_every_recorded_dutch_register_is_named_in_the_brief(self):
        for r in self.rows:
            with self.subTest(record_class=r["record_class"]):
                self.assertIn(r["register"], self.text)

    def test_every_recorded_dutch_source_is_linked_from_the_brief(self):
        for r in self.rows:
            with self.subTest(record_class=r["record_class"]):
                self.assertIn(r["url"], self.text)

    def test_the_stated_count_matches_the_register(self):
        entries = nd.for_country(nd.load(), "NL")
        self.assertIn(
            f"**{nd.recorded(entries)} of {len(entries)} record classes recorded.**", self.text
        )


if __name__ == "__main__":
    unittest.main()
