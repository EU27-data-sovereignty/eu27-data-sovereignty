#!/usr/bin/env python3
"""
The critical national data register: which Tier 0/Tier 1 records each member state holds, and
the official page that describes each one.

    python3 model/national_data.py            # coverage report; exits 1 if a row is invalid
    python3 model/national_data.py --strict   # also exits 1 if any (country, class) is missing

Why this file exists
--------------------
`TIER0-TIER1-SIZING.md` sizes the irreducible state record -- the identity spine and the
legal/fiscal state -- and names the record classes. But it does it for the Netherlands only,
carries no URLs, and its own open items ask for the tiering to be "a reusable section for
country write-ups". This is that, made machine-checkable.

Tiers 2 (health, imaging) and 3 (genomics, archives, video, geospatial) are deliberately out of
scope and have no rows here. From that document: "Tiers 2 and 3 are where the *bytes* are.
Tiers 0 and 1 are where the *sovereignty* is."

Every row carries the register, the body that operates it, the official page describing it, and
a quote from that page -- the same bargain `sources.csv` strikes for the parameter cells, for
the same reason: a URL shows that a page exists, not that it says what the row claims.

Three states, not two
---------------------
A reader must be able to tell "this state has no such register" from "nobody has looked yet":

    status: held       a row, with the register named and sourced
    status: not_held   a row, evidencing that no central register exists
    (no row)           not yet researched -- renders as "not yet recorded", never as absence

`status: not_held` requires `confidence: absence`, and the quote must come from an authoritative
enumeration -- the competent authority's own list of registers -- not from a page that merely
fails to mention one. **This guard is weaker than the one in `sources.py`**, which can check an
absence claim against the parameter cell in a different file (DECISIONS.md #58). Here the cell
*is* the row, so there is nothing independent to check against. Said plainly because the claim
is consequential: several member states genuinely keep fingerprints only on the document chip,
and "no central register" is a real finding that a careless row would fake.

Deliberately not a column
-------------------------
Where a register is *hosted* is a separate factual claim needing its own source. Recording it
here unsourced, next to sourced cells, is precisely what #25 exists to prevent. If it is wanted,
it gets its own column, its own URL and its own quote.

No individuals, ever
--------------------
Same rule as `institutions.py` and #26: bodies and instruments, never people. `quote` and
`register` are rejected if they contain anything email-shaped, because the app's own test
(`mobile/__tests__/parity.test.ts`) fails on an email anywhere in the shipped bundle -- and it
runs in neither `./test.sh` nor CI, so the failure would surface late and far from its cause.
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTER = ROOT / "model" / "national_data.csv"
PARAMETERS = ROOT / "model" / "eu27_parameters.csv"

FIELDS = [
    "iso", "tier", "record_class", "status", "register", "holder", "holder_url",
    "url", "publisher", "retrieved", "confidence", "quote",
]

# Tier 0 -- the identity spine. Without it the state cannot say who exists, and recovery from
# total loss would mean re-enrolling the population.
TIER0 = (
    "civil_registry",
    "facial_biometric",
    "fingerprint_biometric",
    "breeder_documents",
    "issuance_history",
    "digital_identity_credentials",
    "authentication_audit_log",
    "electoral_roll",
)

# Tier 1 -- the legal and fiscal state: what is owed, what is owned, what was adjudicated.
TIER1 = (
    "tax",
    "benefits_pensions",
    "land_property",
    "judicial_criminal",
    "education",
    "business_registry",
    "vehicle_licensing",
)

# Report and sort order. Tier 0 before tier 1 IS the argument -- TIER0-TIER1-SIZING.md orders by
# consequence of loss, not alphabetically, and sorting this list would destroy that.
RECORD_CLASSES = TIER0 + TIER1
TIER_OF = {c: 0 for c in TIER0} | {c: 1 for c in TIER1}

STATUS = ("held", "not_held")
CONFIDENCE = ("primary", "official", "secondary", "absence")

# Display labels, verbatim from the record-class tables in TIER0-TIER1-SIZING.md.
LABELS = {
    "civil_registry": "Civil registry core",
    "facial_biometric": "Facial biometric",
    "fingerprint_biometric": "Fingerprint biometric",
    "breeder_documents": "Breeder document scans",
    "issuance_history": "Document issuance history",
    "digital_identity_credentials": "Digital identity credentials",
    "authentication_audit_log": "Authentication audit log",
    "electoral_roll": "Electoral roll entry",
    "tax": "Tax",
    "benefits_pensions": "Benefits & pensions",
    "land_property": "Land & property registry",
    "judicial_criminal": "Judicial & criminal justice",
    "education": "Education",
    "business_registry": "Business registry",
    "vehicle_licensing": "Vehicle & licensing",
}

# Printed wherever the register is rendered. One string, in the bundle, so all four renderers
# hedge identically rather than growing four different disclaimers (DECISIONS.md #6).
NOTE = (
    "A blank row means this repository has not yet researched that register. It is not a "
    "statement that the country holds no such data. Tiers 2 (health records, imaging) and 3 "
    "(genomics, archives, video retention, geospatial) are out of scope: they hold most of the "
    "bytes, but Tiers 0 and 1 hold the sovereignty."
)

DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[a-z]{2,}", re.I)


def countries() -> list[str]:
    with PARAMETERS.open(newline="", encoding="utf-8") as fh:
        return [r["iso2"] for r in csv.DictReader(fh)]


def load(path: Path = REGISTER) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        if reader.fieldnames != FIELDS:
            raise SystemExit(f"{path.name}: header is {reader.fieldnames}, expected {FIELDS}")
        return list(reader)


def status_errors(where: str, r: dict[str, str]) -> list[str]:
    """The status/confidence pairing. An absence claim must be evidenced, not merely asserted."""
    errors: list[str] = []
    status, confidence = r["status"], r["confidence"]

    if status not in STATUS:
        errors.append(f"{where}: status must be one of {STATUS}")
        return errors
    if confidence not in CONFIDENCE:
        errors.append(f"{where}: confidence must be one of {CONFIDENCE}")
        return errors

    if status == "not_held" and confidence != "absence":
        errors.append(
            f"{where}: status 'not_held' claims no central register exists, which needs "
            f"confidence 'absence' and an authoritative enumeration in the quote"
        )
    if status == "held" and confidence == "absence":
        errors.append(f"{where}: confidence 'absence' contradicts status 'held'")
    if status == "held" and not r["register"].strip():
        errors.append(f"{where}: status 'held' but no register is named")
    return errors


def validate(rows: list[dict[str, str]]) -> list[str]:
    """Every reason a row is not usable evidence. Empty list means the register is sound."""
    errors: list[str] = []
    valid = set(countries())
    seen: set[tuple[str, str]] = set()

    for i, r in enumerate(rows, start=2):  # row 1 is the header
        where = f"row {i} ({r.get('iso', '?')}/{r.get('record_class', '?')})"

        if r["iso"] not in valid:
            errors.append(f"{where}: not an EU-27 ISO code")
        if r["record_class"] not in RECORD_CLASSES:
            errors.append(f"{where}: record_class must be one of {RECORD_CLASSES}")
        elif r["tier"] != str(TIER_OF[r["record_class"]]):
            errors.append(
                f"{where}: {r['record_class']} is tier {TIER_OF[r['record_class']]}, "
                f"not tier {r['tier']!r}"
            )

        errors += status_errors(where, r)

        if not r["holder"].strip():
            errors.append(f"{where}: holder is empty")
        for field in ("holder_url", "url"):
            if not r[field].startswith("https://"):
                errors.append(f"{where}: {field} is not an https URL")
        if not r["publisher"].strip():
            errors.append(f"{where}: publisher is empty")
        if not DATE.match(r["retrieved"]):
            errors.append(f"{where}: retrieved is not YYYY-MM-DD")
        if len(r["quote"].strip()) < 20:
            errors.append(f"{where}: quote is missing or too short to show the page says this")

        for field in ("register", "quote"):
            if EMAIL.search(r[field]):
                errors.append(
                    f"{where}: {field} contains an email address; this register names bodies "
                    f"and instruments, never people (DECISIONS.md #26)"
                )

        key = (r["iso"], r["record_class"])
        if key in seen:
            errors.append(f"{where}: duplicate of an earlier row")
        seen.add(key)

    order = [
        (r["iso"], RECORD_CLASSES.index(c) if (c := r["record_class"]) in RECORD_CLASSES else -1)
        for r in rows
    ]
    if order != sorted(order):
        errors.append("rows are not sorted by (iso, tier order); sort them so diffs stay readable")
    return errors


def coverage(rows: list[dict[str, str]]) -> dict[str, set[str]]:
    """Which countries have a row recorded, per record class."""
    out: dict[str, set[str]] = {c: set() for c in RECORD_CLASSES}
    for r in rows:
        if r["record_class"] in out:
            out[r["record_class"]].add(r["iso"])
    return out


def covered_cells(rows: list[dict[str, str]]) -> int:
    """Distinct (country, record class) pairs recorded, held or evidenced-absent alike."""
    return len({(r["iso"], r["record_class"]) for r in rows
                if r["record_class"] in RECORD_CLASSES})


def gaps(rows: list[dict[str, str]]) -> list[tuple[str, str]]:
    """Every (country, record class) nobody has researched yet, in report order."""
    cov = coverage(rows)
    return [(iso, c) for iso in countries() for c in RECORD_CLASSES if iso not in cov[c]]


def report(rows: list[dict[str, str]]) -> None:
    n = len(countries())
    cov = coverage(rows)

    print(f"{'record class':<30} {'countries':>12} {'rows':>6}")
    for tier, classes in ((0, TIER0), (1, TIER1)):
        print(f"-- tier {tier} " + "-" * 38)
        for c in classes:
            total = sum(1 for r in rows if r["record_class"] == c)
            print(f"{c:<30} {len(cov[c]):>6}/{n:<5} {total:>6}")
        filled = sum(len(cov[c]) for c in classes)
        print(f"{'  tier ' + str(tier) + ' subtotal':<30} {filled:>6}/{len(classes) * n:<5}")

    filled, target = covered_cells(rows), len(RECORD_CLASSES) * n
    print(f"\n{filled}/{target} (country, record class) pairs recorded "
          f"({100 * filled / target:.0f}%)")
    held = sum(1 for r in rows if r["status"] == "held")
    print(f"{len(rows)} rows, of which {held} name a register and "
          f"{len(rows) - held} evidence its absence.")

    missing = gaps(rows)
    if missing:
        by_country: dict[str, list[str]] = {}
        for iso, c in missing:
            by_country.setdefault(iso, []).append(c)
        print(f"\nnot yet researched in {len(by_country)} countries")


def for_country(rows: list[dict[str, str]], iso: str) -> list[dict]:
    """The register as a country brief renders it: all 15 classes, always, in tier order.

    A sparse table hides the gap. A full table with twelve blanks *is* the coverage report,
    visible to a reader who will never run the test suite -- which is why the vocabulary is
    closed and why this returns every class rather than only the recorded ones.
    """
    found = {r["record_class"]: r for r in rows if r["iso"] == iso}
    out = []
    for c in RECORD_CLASSES:
        r = found.get(c)
        out.append({
            "tier": TIER_OF[c],
            "record_class": c,
            "label": LABELS[c],
            "status": r["status"] if r else "unrecorded",
            "register": r["register"] if r else "",
            "holder": r["holder"] if r else "",
            "holder_url": r["holder_url"] if r else "",
            "url": r["url"] if r else "",
            "publisher": r["publisher"] if r else "",
            "retrieved": r["retrieved"] if r else "",
            "confidence": r["confidence"] if r else "",
            "quote": r["quote"] if r else "",
        })
    return out


def recorded(entries: list[dict]) -> int:
    """How many of the 15 classes this country has a row for."""
    return sum(1 for e in entries if e["status"] != "unrecorded")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Validate and report on the national data register.")
    ap.add_argument("--strict", action="store_true",
                    help="fail while any (country, record class) pair is unrecorded")
    args = ap.parse_args(argv)

    rows = load()
    errors = validate(rows)
    for e in errors:
        print(f"error: {e}", file=sys.stderr)
    report(rows)

    if errors:
        return 1
    if args.strict and gaps(rows):
        print("\nstrict: (country, record class) pairs remain unrecorded", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
