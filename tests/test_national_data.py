"""The critical national data register, and the ratchet that keeps its coverage honest.

Mirrors tests/test_sources.py, including the part that is easy to leave out: the floor is
asserted from BOTH sides. One test fails if coverage drops (a row was deleted), the other
fails if coverage rises without the floor moving with it. Together they assert equality, so
progress cannot be silently undone and the constant cannot silently go stale.
"""
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "model"))

import national_data as nd  # noqa: E402
import provenance  # noqa: E402

# Raise as holdings are admitted. 1053 = 39 holding classes x 27 member states (#73).
NATIONAL_DATA_FLOOR = 419


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

    # The original fifteen Tier 0/1 record classes, which the widened taxonomy (#73) must keep
    # with their ids and tiers unchanged: citations and the NL rows already refer to them.
    ORIGINAL = {
        "civil_registry": 0, "facial_biometric": 0, "fingerprint_biometric": 0,
        "breeder_documents": 0, "issuance_history": 0, "digital_identity_credentials": 0,
        "authentication_audit_log": 0, "electoral_roll": 0, "tax": 1, "benefits_pensions": 1,
        "land_property": 1, "judicial_criminal": 1, "education": 1, "business_registry": 1,
        "vehicle_licensing": 1,
    }

    def test_the_taxonomy_is_read_from_holding_classes_csv(self):
        self.assertEqual(len(nd.RECORD_CLASSES), 39)
        self.assertEqual(len(set(nd.RECORD_CLASSES)), 39)
        self.assertEqual(set(nd.TIER_OF.values()), {0, 1, 2, 3})

    def test_the_original_fifteen_keep_their_ids_and_tiers(self):
        for c, tier in self.ORIGINAL.items():
            with self.subTest(record_class=c):
                self.assertEqual(nd.TIER_OF.get(c), tier)

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
        self.assertEqual(list(nd.RECORD_CLASSES),
                         sorted(nd.RECORD_CLASSES, key=lambda c: nd.TIER_OF[c]),
                         "tier order is the report order")


class ValidationRules(unittest.TestCase):
    """Each rule is checked against a row that breaks exactly it."""

    BASE = {
        "iso": "NL", "tier": "0", "record_class": "civil_registry", "status": "held",
        "register": "Basisregistratie Personen (BRP)", "holder": "RvIG",
        "holder_url": "https://www.rvig.nl/", "url": "https://www.rvig.nl/brp",
        "publisher": "RvIG", "retrieved": "2026-09-21", "confidence": "official",
        "quote": "De overheid registreert persoonsgegevens in de BRP.",
        **{f: "" for f in nd.EXTRA_FIELDS},
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


class ProvenanceLivesInTheSourceRegister(unittest.TestCase):
    """The page and quote moved to model/sources/ (#67); national_data.csv keeps only the facts."""

    ROW = {"iso": "NL", "record_class": "civil_registry"}
    CITE = {"claim": "record:NL:civil_registry:register"}

    def test_the_old_inline_columns_are_gone_from_the_file_but_joined_on_load(self):
        self.assertTrue(set(nd.PROVENANCE).isdisjoint(nd.FIELDS))
        for r in nd.load():
            self.assertTrue(set(nd.PROVENANCE) <= set(r))

    def test_the_old_header_is_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            old = Path(d) / "national_data.csv"
            old.write_text(",".join(nd.FIELDS + nd.PROVENANCE) + "\n", encoding="utf-8")
            with self.assertRaises(SystemExit):
                nd.load(old)

    def test_every_row_has_exactly_one_register_citation(self):
        self.assertEqual(nd.citation_errors(nd.load(), provenance.citations()), [])

    def test_a_row_without_a_citation_is_rejected(self):
        errors = nd.citation_errors([self.ROW], [])
        self.assertTrue(any("needs exactly one" in e for e in errors))

    def test_a_filled_extra_field_needs_its_own_citation(self):
        """#73/#75: legal basis, hosting, counts and sizes are claims, each with its own source."""
        row = {**self.ROW, "hosting": "Government data centre"}
        errors = nd.citation_errors([row], [self.CITE])
        self.assertTrue(any(":hosting is not cited" in e for e in errors), errors)

    def test_a_citation_without_a_row_is_rejected(self):
        errors = nd.citation_errors([], [self.CITE])
        self.assertTrue(any("has no such row" in e for e in errors))

    def test_count_and_size_citations_need_no_row(self):
        """Part C cites record counts and sizes; only :register claims mirror a row here."""
        self.assertEqual(nd.citation_errors([], [{"claim": "record:NL:civil_registry:count"}]), [])


if __name__ == "__main__":
    unittest.main()
