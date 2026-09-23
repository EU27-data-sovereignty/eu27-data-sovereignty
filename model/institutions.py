#!/usr/bin/env python3
"""
The institutional map: one row per (country, function) contact point, with its published route.

    python3 model/institutions.py            # coverage report; exits 1 if a row is invalid
    python3 model/institutions.py --strict   # also exits 1 if any (country, function) is missing

Why this file exists
--------------------
`OUTREACH.md` names the bodies to approach in each member state, but it is prose: its ministry,
committee and press rows are marked "check before send" precisely because nothing in the repo
holds them to a source. This is the machine-checkable half. Every row carries the body, the
channel it publishes for inbound contact, and a quote from the page that publishes it -- the same
bargain `sources.csv` strikes for the parameter cells, for the same reason: a URL shows that a
page exists, not that it says what the row claims.

Institutions only
-----------------
No row here names a person. `DECISIONS.md` #26 and #49 keep individuals out of the public repo
entirely -- a public official's work contact is still personal data under GDPR, and a public
repository is a scrape target. Named officeholders live in the private contacts repo, which
cross-references this file for the institution they sit in.

The same rule constrains `route_url`: it must be an institution's *published* channel -- a press
office, a committee secretariat, a general inbox, a web form. An address shaped like an
individual's mailbox (`first.last@`) is rejected even when a page publishes it, because the whole
point of routing through the institution is that the route survives the officeholder.
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INSTITUTIONS = ROOT / "model" / "institutions.csv"
PARAMETERS = ROOT / "model" / "eu27_parameters.csv"

FIELDS = [
    "iso", "function", "body", "body_url", "route_type", "route_url",
    "publisher", "retrieved", "confidence", "quote",
]

# The concerns a national sovereign-cloud programme has to talk to. Keys are stable; the bodies
# holding each function are not, which is why the body is sourced and the function is not.
FUNCTIONS = (
    "policy",           # digital-government policy owner: ministry, government CIO
    "operator",         # government cloud / datacenter operator
    "certification",    # cloud security certification authority
    "procurement",      # central purchasing body
    "scrutiny",         # parliamentary committee, court of audit, statutory IT reviewer
    "press",            # institutional press desk
    "energy",           # energy ministry, energy regulator, transmission system operator
    "cyber",            # national CERT/CSIRT or NCSC
    "dataprotection",   # data protection authority
    "telecom",          # telecoms regulator, national research network, digital-infra lead
    "planning",         # spatial planning and permitting authority
    "finance",          # finance ministry, budget holder
)

# How the body takes inbound contact. Anything person-specific is deliberately absent.
ROUTE_TYPES = ("press", "secretariat", "general", "webform", "postal")

# `absence` is meaningless here: a country always has someone holding the function, even if the
# body is the ministry rather than a dedicated agency. An unfindable route is an unsourced row.
CONFIDENCE = ("primary", "official", "secondary")

DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

# Local parts that read as an individual's mailbox rather than an institutional one.
PERSONAL_LOCAL = re.compile(r"^[a-z]{2,}[._-][a-z]{2,}$", re.I)

# Institutional local parts that happen to contain a separator, so PERSONAL_LOCAL cannot see them.
GENERIC_LOCAL = re.compile(
    r"^(info|contact|press|pers|presse|prensa|stampa|media|office|secretariat|secretariaat|"
    r"sekretariat|secretaria|segreteria|kontakt|comms|communication|communications|voorlichting|"
    r"mail|post|posta|postmaster|enquiries|helpdesk|support|service|servicedesk|cert|csirt|"
    r"soc|abuse|dpo|gdpr|privacy|foi|woo|procurement|tenders|general|admin|reception)\b",
    re.I,
)


def countries() -> list[str]:
    with PARAMETERS.open(newline="", encoding="utf-8") as fh:
        return [r["iso2"] for r in csv.DictReader(fh)]


def load(path: Path = INSTITUTIONS) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        if reader.fieldnames != FIELDS:
            raise SystemExit(f"{path.name}: header is {reader.fieldnames}, expected {FIELDS}")
        return list(reader)


def route_errors(where: str, route_type: str, route_url: str) -> list[str]:
    """Every reason a route is not an institutional channel this project may use."""
    errors: list[str] = []
    if route_type not in ROUTE_TYPES:
        errors.append(f"{where}: route_type must be one of {ROUTE_TYPES}")

    if route_url.startswith("mailto:"):
        address = route_url[len("mailto:"):]
        local, _, domain = address.partition("@")
        if not domain:
            errors.append(f"{where}: route_url is a mailto: without a domain")
        elif not GENERIC_LOCAL.match(local) and PERSONAL_LOCAL.match(local):
            errors.append(
                f"{where}: route_url looks like an individual's mailbox; route through the "
                f"institution's published channel instead (CONVENTIONS rule 2)"
            )
    elif route_url.startswith("https://"):
        if route_type == "postal":
            errors.append(f"{where}: a postal route needs the address, not a URL")
    elif route_type == "postal":
        if len(route_url.strip()) < 10:
            errors.append(f"{where}: postal route is too short to be an address")
    else:
        errors.append(f"{where}: route_url must be an https:// URL or a mailto: address")
    return errors


def validate(rows: list[dict[str, str]]) -> list[str]:
    """Every reason a row is not usable as a contact point. Empty list means the map is sound."""
    errors: list[str] = []
    valid = set(countries()) | {"EU"}  # Tier 0 in OUTREACH.md is the Union itself
    seen: set[tuple[str, str, str]] = set()

    for i, r in enumerate(rows, start=2):  # row 1 is the header
        where = f"row {i} ({r.get('iso', '?')}/{r.get('function', '?')})"

        if r["iso"] not in valid:
            errors.append(f"{where}: not an EU-27 ISO code or EU")
        if r["function"] not in FUNCTIONS:
            errors.append(f"{where}: function must be one of {FUNCTIONS}")
        if not r["body"].strip():
            errors.append(f"{where}: body is empty")
        if not r["body_url"].startswith("https://"):
            errors.append(f"{where}: body_url is not an https URL")
        errors += route_errors(where, r["route_type"], r["route_url"])
        if not r["publisher"].strip():
            errors.append(f"{where}: publisher is empty")
        if not DATE.match(r["retrieved"]):
            errors.append(f"{where}: retrieved is not YYYY-MM-DD")
        if r["confidence"] not in CONFIDENCE:
            errors.append(f"{where}: confidence must be one of {CONFIDENCE}")
        if len(r["quote"].strip()) < 20:
            errors.append(f"{where}: quote is missing or too short to show the page says this")

        key = (r["iso"], r["function"], r["body"])
        if key in seen:
            errors.append(f"{where}: duplicate of an earlier row")
        seen.add(key)

    order = [(r["iso"], FUNCTIONS.index(f) if (f := r["function"]) in FUNCTIONS else -1)
             for r in rows]
    if order != sorted(order):
        errors.append("rows are not sorted by (iso, function order); sort them so diffs stay readable")
    return errors


def coverage(rows: list[dict[str, str]]) -> dict[str, set[str]]:
    """Which countries have at least one body recorded, per function."""
    out: dict[str, set[str]] = {f: set() for f in FUNCTIONS}
    for r in rows:
        if r["function"] in out and r["iso"] != "EU":
            out[r["function"]].add(r["iso"])
    return out


def gaps(rows: list[dict[str, str]]) -> list[tuple[str, str]]:
    """Every (country, function) with nobody to contact, in report order."""
    cov = coverage(rows)
    return [(iso, f) for iso in countries() for f in FUNCTIONS if iso not in cov[f]]


def report(rows: list[dict[str, str]]) -> None:
    n = len(countries())
    cov = coverage(rows)

    print(f"{'function':<16} {'countries':>12} {'rows':>6}")
    for f in FUNCTIONS:
        total = sum(1 for r in rows if r["function"] == f)
        print(f"{f:<16} {len(cov[f]):>6}/{n:<5} {total:>6}")

    filled, target = sum(len(v) for v in cov.values()), len(FUNCTIONS) * n
    eu = sum(1 for r in rows if r["iso"] == "EU")
    print(f"\n{filled}/{target} (country, function) pairs filled ({100 * filled / target:.0f}%)")
    print(f"{len(rows)} rows, of which {eu} are EU-level (tier 0).")

    missing = gaps(rows)
    if missing:
        by_country: dict[str, list[str]] = {}
        for iso, f in missing:
            by_country.setdefault(iso, []).append(f)
        print(f"\ngaps in {len(by_country)} countries:")
        for iso, fs in by_country.items():
            print(f"  {iso}: {', '.join(fs)}")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Validate and report on the institutional map.")
    ap.add_argument("--strict", action="store_true",
                    help="fail while any (country, function) pair has no body")
    args = ap.parse_args(argv)

    rows = load()
    errors = validate(rows)
    for e in errors:
        print(f"error: {e}", file=sys.stderr)
    report(rows)

    if errors:
        return 1
    if args.strict and gaps(rows):
        print("\nstrict: (country, function) pairs remain unfilled", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
