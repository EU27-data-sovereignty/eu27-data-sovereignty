#!/usr/bin/env python3
"""
The verification ledger: one row per sourced claim in `eu27_parameters.csv`.

    python3 model/sources.py            # coverage report; exits 1 if a row is invalid
    python3 model/sources.py --strict   # also exits 1 if any required cell is unsourced

Why this file exists
--------------------
The capacity figures in this repository are openly scaled placeholders and say so.
The legal and regulatory columns are different: they are assertions about what 27 real
jurisdictions require, researched from public policy documents by one person and not
checked against primary sources. `DECISIONS.md` #25 gates publication on fixing that,
and `ROADMAP.md` makes it the gate for indexing, a custom domain and the book.

`sources.csv` is where that verification is recorded. **The quote is the point.** A URL
alone shows that a page exists, not that it says what the cell claims, and a cell whose
source has silently been rewritten is worse than an uncited one because it looks checked.

The tiered rule (ROADMAP step 2)
--------------------------------
* TIER1 columns assert a legal obligation -- what a state *requires*. Only the
  instrument itself will do: `confidence` must be `primary`.
* TIER2 columns describe what a state runs, buys or depends on. An official government
  page is enough: `primary` or `official`.
* JUDGEMENT columns are the author's ordinal ratings, derived from the columns above.
  They are not sourceable and are disclosed as judgements rather than cited; a row for
  one of them is an error, not a contribution.

Absence is a claim too
----------------------
22 of the 81 tier-1 cells assert that something does **not** exist -- 21 of the 27
`certification_scheme` cells say "No national scheme". No instrument enacts the absence of a
scheme, so under a rule admitting only `primary` those cells could never be sourced, tier 1
was capped at 59/81 = 72.8%, and `--strict` could never pass. That is an unsatisfiable
specification, not a research backlog.

`confidence: absence` closes it. Evidence of absence is not an instrument but an **authoritative
enumeration** -- the competent authority's own register of schemes, or a supervisory body's
published list -- showing the category is empty. A claim about a complete list is evidenced by
the complete list.

It is deliberately hard to abuse: a row may only be `absence` if the cell it cites actually
asserts an absence (`NEGATIVE` below). It cannot be used to dodge finding an instrument that
exists, which is the one way this value could make the ledger dishonest rather than complete.
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / "model" / "sources.csv"
PARAMETERS = ROOT / "model" / "eu27_parameters.csv"

FIELDS = ["country", "column", "url", "publisher", "retrieved", "confidence", "quote"]

# Asserts a legal obligation: the instrument itself, nothing weaker.
TIER1 = ("legal_instrument", "data_classification", "certification_scheme")

# Describes what the state runs, buys or depends on: an official page suffices.
TIER2 = ("sovereign_cloud_initiative", "procurement_vehicle", "digital_id", "hyperscaler_gov_exposure")

# Author judgements derived from the above. Disclosed, not cited. See DECISIONS.md #10.
JUDGEMENT = ("gov_cloud_maturity", "certification_strength", "hyperscaler_dependency")

REQUIRED = TIER1 + TIER2
CONFIDENCE = ("primary", "official", "secondary", "absence")

# Tier 1 asserts a legal obligation, so it takes the instrument -- or, where the claim is that
# no such instrument exists, an authoritative enumeration showing so.
TIER1_CONFIDENCE = ("primary", "absence")

# A cell asserting that something does not exist. Only these may be cited as `absence`.
NEGATIVE = re.compile(r"\bno\s+(national|separate|single|in-country|sovereign|dedicated)\b"
                      r"|\brather than a single\b", re.I)

DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def countries() -> list[str]:
    with PARAMETERS.open(newline="", encoding="utf-8") as fh:
        return [r["iso2"] for r in csv.DictReader(fh)]


def cells() -> dict[str, dict[str, str]]:
    """Every parameter row by ISO, so a source row can be checked against the cell it cites."""
    with PARAMETERS.open(newline="", encoding="utf-8") as fh:
        return {r["iso2"]: r for r in csv.DictReader(fh)}


def asserts_absence(country: str, column: str) -> bool:
    row = cells().get(country)
    return bool(row and NEGATIVE.search(row.get(column, "")))


def load() -> list[dict[str, str]]:
    with SOURCES.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        if reader.fieldnames != FIELDS:
            raise SystemExit(f"{SOURCES.name}: header is {reader.fieldnames}, expected {FIELDS}")
        return list(reader)


def validate(rows: list[dict[str, str]]) -> list[str]:
    """Every reason a row is not usable evidence. Empty list means the ledger is sound."""
    errors: list[str] = []
    valid = set(countries())
    seen: set[tuple[str, str, str]] = set()

    for i, r in enumerate(rows, start=2):  # row 1 is the header
        where = f"row {i} ({r.get('country', '?')}/{r.get('column', '?')})"
        col = r["column"]

        if r["country"] not in valid:
            errors.append(f"{where}: not an EU-27 ISO code")
        if col in JUDGEMENT:
            errors.append(f"{where}: {col} is an author judgement and is disclosed, not cited")
        elif col not in REQUIRED:
            errors.append(f"{where}: {col} is not a sourceable column")
        if not r["url"].startswith(("http://", "https://")):
            errors.append(f"{where}: url is not an absolute http(s) URL")
        if not r["publisher"].strip():
            errors.append(f"{where}: publisher is empty")
        if not DATE.match(r["retrieved"]):
            errors.append(f"{where}: retrieved is not YYYY-MM-DD")
        if r["confidence"] not in CONFIDENCE:
            errors.append(f"{where}: confidence must be one of {CONFIDENCE}")
        elif col in TIER1 and r["confidence"] not in TIER1_CONFIDENCE:
            errors.append(
                f"{where}: {col} asserts a legal obligation and needs a primary source, "
                f"or `absence` where the cell says no such instrument exists"
            )
        if r["confidence"] == "absence" and col in REQUIRED and r["country"] in valid:
            if not asserts_absence(r["country"], col):
                errors.append(
                    f"{where}: cited as `absence` but the cell does not assert one; "
                    f"`absence` evidences a missing scheme, it does not excuse a missing source"
                )
        if len(r["quote"].strip()) < 20:
            errors.append(f"{where}: quote is missing or too short to show the page says this")

        key = (r["country"], col, r["url"])
        if key in seen:
            errors.append(f"{where}: duplicate of an earlier row")
        seen.add(key)

    order = [(r["country"], r["column"]) for r in rows]
    if order != sorted(order):
        errors.append("rows are not sorted by (country, column); sort them so diffs stay readable")
    return errors


def coverage(rows: list[dict[str, str]]) -> dict[str, set[str]]:
    """Which countries have at least one source row, per required column."""
    out: dict[str, set[str]] = {c: set() for c in REQUIRED}
    for r in rows:
        if r["column"] in out:
            out[r["column"]].add(r["country"])
    return out


def covered_cells(rows: list[dict[str, str]]) -> int:
    return sum(len(v) for v in coverage(rows).values())


def negative_cells() -> dict[str, int]:
    """Per column, how many of the 27 cells assert an absence rather than an instrument."""
    data = cells()
    return {c: sum(1 for iso in data if NEGATIVE.search(data[iso].get(c, ""))) for c in REQUIRED}


def report(rows: list[dict[str, str]]) -> None:
    n = len(countries())
    cov = coverage(rows)
    neg = negative_cells()
    by_absence: dict[str, int] = {c: 0 for c in REQUIRED}
    for r in rows:
        if r["confidence"] == "absence" and r["column"] in by_absence:
            by_absence[r["column"]] += 1

    print(f"{'column':<28} {'tier':<5} {'sourced':>9} {'of which absence':>17} {'negative cells':>15}")
    for col in REQUIRED:
        tier = "1" if col in TIER1 else "2"
        print(
            f"{col:<28} {tier:<5} {len(cov[col]):>4}/{n:<4} "
            f"{by_absence[col]:>17} {neg[col]:>15}"
        )
    total, target = covered_cells(rows), len(REQUIRED) * n
    print(f"\n{total}/{target} cells sourced ({100 * total / target:.0f}%)")
    print(
        f"{sum(neg.values())} of {target} cells assert an absence and need an authoritative "
        f"enumeration rather than an instrument."
    )


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Validate and report on the verification ledger.")
    ap.add_argument("--strict", action="store_true", help="fail while any required cell is unsourced")
    args = ap.parse_args(argv)

    rows = load()
    errors = validate(rows)
    for e in errors:
        print(f"error: {e}", file=sys.stderr)
    report(rows)

    if errors:
        return 1
    if args.strict and covered_cells(rows) < len(REQUIRED) * len(countries()):
        print("\nstrict: required cells remain unsourced", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
