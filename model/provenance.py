#!/usr/bin/env python3
"""
The source register: every original document once, every claim pointing at one.

    python3 model/provenance.py                  # validate; coverage per namespace; exits 1 on an error
    python3 model/provenance.py --sync-eurostat  # regenerate the Eurostat citations from eurostat_pull.csv

Why this file exists
--------------------
Until 2026-09-24 provenance lived in five ledgers with five schemas -- sources.csv, source_urls.csv,
fetch_manifest.csv, eurostat_pull.csv, national_data.csv -- sharing no identifier, so one document
cited from two places was two unrelated strings, and nothing could answer "what is this figure's
source?" for anything but a legal cell. DECISIONS.md #67.

Two files replace the idea of a ledger per claim type:

    sources/registry.csv   one row per original document or dataset, keyed by source_id
    sources/citations.csv  one row per (claim, source): the claim it supports, where in the
                           document (locator), and the evidence -- a quote, or for a dataset the
                           value found at that locator

Claim ids name exactly what is asserted, in namespaces:

    param:<ISO>:<column>                     a cell of eu27_parameters.csv
    assumption:<name>                        a row of assumptions.csv / scaling_rules.csv / params.csv
    workload:<ISO>:<workload>:<field>        a workload input
    inventory:<ISO>:<metric>                 a government IT inventory figure (it_inventory.csv)
    record:<ISO|*>:<record_class>:<kind>     a critical holding (national_data.csv): its existence
                                             (register), operator, legal basis, hosting, foreign
                                             dependency, record count or data size (#73)
    indicator:<ISO>:<id>                     a data-sovereignty indicator (indicators.csv), #77
    doc:<path>#<anchor>                      a claim in an authored note

The bargain is the one sources.csv struck (#54): a URL shows that a document exists, not that it
says what the claim does. So a citation carries a quote of at least 20 characters -- or, where the
source is a dataset and there are no words to quote, the locator and the value found there, which
this file compares with the cell it supports. A dataset value that does not reproduce the cell is not
a citation of it, and does not count as coverage.

`confidence: assumption` is for a working assumption declared as one, with its rationale in the
quote field. It is never counted as sourced -- it is counted as *declared*, which is the honest
state of a planning parameter nobody has measured.
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIR = ROOT / "model" / "sources"
REGISTRY = DIR / "registry.csv"
CITATIONS = DIR / "citations.csv"
PARAMETERS = ROOT / "model" / "eurostat_pull.csv"   # used by --sync-eurostat
PARAMS_CSV = ROOT / "model" / "eu27_parameters.csv"
ASSUMPTIONS = ROOT / "model" / "assumptions.csv"

REGISTRY_FIELDS = ["source_id", "title", "publisher", "url", "doc_type", "published", "language",
                   "license", "archived_url", "notes"]
CITATION_FIELDS = ["claim", "source_id", "locator", "quote", "value_as_found", "unit", "confidence",
                   "retrieved", "checked_by"]

DOC_TYPES = ("statute", "regulation", "dataset", "report", "annual_report", "standard", "webpage",
             "register", "unused")
CONFIDENCE = ("primary", "official", "secondary", "absence", "assumption")
NAMESPACES = ("param", "assumption", "workload", "inventory", "record", "indicator", "doc")
RECORD_KINDS = ("register", "operator", "legal_basis", "hosting", "foreign_dependency", "count", "size")

SOURCE_ID = re.compile(r"^[a-z0-9-]+:[a-z0-9_.-]+(@[A-Za-z0-9_.-]+)?$")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
TOLERANCE_PCT = 0.5   # the same tolerance tests/test_fetch.py holds the Eurostat pull to


def _read(path: Path, fields: list[str]) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        if reader.fieldnames != fields:
            raise SystemExit(f"{path.name}: header is {reader.fieldnames}, expected {fields}")
        return list(reader)


def registry() -> dict[str, dict[str, str]]:
    return {r["source_id"]: r for r in _read(REGISTRY, REGISTRY_FIELDS)}


def citations() -> list[dict[str, str]]:
    return _read(CITATIONS, CITATION_FIELDS)


def _write(path: Path, fields: list[str], rows: list[dict[str, str]], key) -> None:
    """Sorted and in the file's own dialect, so a diff shows what changed rather than where."""
    ending = "\r\n" if path.exists() and b"\r\n" in path.read_bytes()[:4096] else "\n"
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, lineterminator=ending)
        w.writeheader()
        w.writerows(sorted(rows, key=key))


def write_registry(reg: dict[str, dict[str, str]]) -> None:
    _write(REGISTRY, REGISTRY_FIELDS, list(reg.values()), key=lambda r: r["source_id"])


def write_citations(cites: list[dict[str, str]]) -> None:
    _write(CITATIONS, CITATION_FIELDS, cites, key=lambda c: (c["claim"], c["source_id"], c["locator"]))


def record_classes() -> tuple[str, ...]:
    """The closed Tier 0/1 vocabulary, owned by national_data.py."""
    from national_data import RECORD_CLASSES  # noqa: PLC0415 -- national_data imports this module too
    return RECORD_CLASSES


def indicator_ids() -> tuple[str, ...]:
    with (ROOT / "model" / "indicators.csv").open(newline="", encoding="utf-8") as fh:
        return tuple(r["id"] for r in csv.DictReader(fh))


def parameters() -> dict[str, dict[str, str]]:
    with PARAMS_CSV.open(newline="", encoding="utf-8") as fh:
        return {r["iso2"]: r for r in csv.DictReader(fh)}


def reproduces(found: str, cell: str) -> bool:
    """Does a dataset value support a numeric cell, within TOLERANCE_PCT?"""
    try:
        a, b = float(found), float(cell)
    except ValueError:
        return False
    return abs(a - b) <= abs(b) * TOLERANCE_PCT / 100 if b else a == 0


def validate(reg: dict[str, dict[str, str]], cites: list[dict[str, str]]) -> list[str]:
    """Every reason the register is not sound. Empty list means it is."""
    errors: list[str] = []
    for sid, r in reg.items():
        where = f"registry {sid}"
        if not SOURCE_ID.match(sid):
            errors.append(f"{where}: source_id must be <publisher>:<doc>[@vintage], lower-case")
        if r["doc_type"] not in DOC_TYPES:
            errors.append(f"{where}: doc_type must be one of {DOC_TYPES}")
        if not r["url"].startswith("https://") and r["doc_type"] != "standard":
            errors.append(f"{where}: url must be https (a paywalled standard may have none)")
        for field in ("title", "publisher"):
            if not r[field].strip():
                errors.append(f"{where}: {field} is empty")

    cited = {c["source_id"] for c in cites}
    for sid, r in reg.items():
        if sid not in cited and r["doc_type"] != "unused":
            errors.append(f"registry {sid}: cited by nothing; cite it or mark doc_type unused")

    params = parameters()
    seen: set[tuple[str, str, str]] = set()
    for i, c in enumerate(cites, start=2):
        where = f"citation row {i} ({c['claim']})"
        ns = c["claim"].split(":", 1)[0]
        if ns not in NAMESPACES:
            errors.append(f"{where}: claim namespace must be one of {NAMESPACES}")
        src = reg.get(c["source_id"])
        if src is None:
            errors.append(f"{where}: source_id {c['source_id']} is not in the registry")
        if c["confidence"] not in CONFIDENCE:
            errors.append(f"{where}: confidence must be one of {CONFIDENCE}")
        if not DATE.match(c["retrieved"]):
            errors.append(f"{where}: retrieved is not YYYY-MM-DD")
        if not c["locator"].strip():
            errors.append(f"{where}: locator is empty; say where in the document")
        if src and src["doc_type"] == "dataset":
            if not c["value_as_found"].strip():
                errors.append(f"{where}: a dataset citation needs value_as_found")
        elif len(c["quote"].strip()) < 20:
            errors.append(f"{where}: quote is missing or too short to show the document says this")
        if ns == "param":
            parts = c["claim"].split(":")
            if len(parts) != 3 or parts[1] not in params or parts[2] not in params[parts[1]]:
                errors.append(f"{where}: param claim must be param:<ISO>:<column of eu27_parameters.csv>")
        if ns == "record":
            parts = c["claim"].split(":")
            if (len(parts) != 4 or (parts[1] not in params and parts[1] != "*")
                    or parts[2] not in record_classes() or parts[3] not in RECORD_KINDS):
                errors.append(f"{where}: record claim must be record:<ISO|*>:<record_class of "
                              f"national_data.py>:<{'|'.join(RECORD_KINDS)}>")
        if ns == "indicator":
            parts = c["claim"].split(":")
            if len(parts) != 3 or parts[1] not in params or parts[2] not in indicator_ids():
                errors.append(f"{where}: indicator claim must be indicator:<ISO>:<id of indicators.csv>")
        key = (c["claim"], c["source_id"], c["locator"])
        if key in seen:
            errors.append(f"{where}: duplicate of an earlier row")
        seen.add(key)

    order = [(c["claim"], c["source_id"]) for c in cites]
    if order != sorted(order):
        errors.append("citations are not sorted by (claim, source_id); sort them so diffs stay readable")
    order = list(reg)
    if order != sorted(order):
        errors.append("registry is not sorted by source_id")
    return errors


def supported(c: dict[str, str], reg: dict[str, dict[str, str]], params: dict) -> bool:
    """Does this citation actually support its claim? Assumptions are declared, never supported."""
    if c["confidence"] == "assumption":
        return False
    src = reg.get(c["source_id"])
    if src and src["doc_type"] == "dataset" and c["claim"].startswith("param:"):
        _, iso, col = c["claim"].split(":")
        return reproduces(c["value_as_found"], params.get(iso, {}).get(col, ""))
    return True


def claims_by_namespace() -> dict[str, set[str]]:
    """Every claim this repository publishes, per namespace -- the denominator for coverage."""
    params = parameters()
    out: dict[str, set[str]] = {ns: set() for ns in NAMESPACES}
    skip = {"iso2", "country", "data_status"}   # identifiers and the status note, not claims
    for iso, row in params.items():
        out["param"] |= {f"param:{iso}:{col}" for col in row if col not in skip}
    with ASSUMPTIONS.open(newline="", encoding="utf-8") as fh:
        out["assumption"] |= {f"assumption:{r['Assumption']}" for r in csv.DictReader(fh)}
    # One register claim per (country, record class); counts and sizes join with Part C.
    out["record"] |= {f"record:{iso}:{c}:register" for iso in params for c in record_classes()}
    out["indicator"] |= {f"indicator:{iso}:{i}" for iso in params for i in indicator_ids()}
    return out


def coverage(reg, cites) -> dict[str, tuple[int, int, int]]:
    """Per namespace: (supported, declared as assumption, total claims)."""
    params = parameters()
    claims = claims_by_namespace()
    ok: dict[str, set[str]] = {ns: set() for ns in NAMESPACES}
    declared: dict[str, set[str]] = {ns: set() for ns in NAMESPACES}
    for c in cites:
        ns = c["claim"].split(":", 1)[0]
        if ns not in ok:
            continue
        if supported(c, reg, params):
            ok[ns].add(c["claim"])
        elif c["confidence"] == "assumption":
            declared[ns].add(c["claim"])
    return {ns: (len(ok[ns]), len(declared[ns] - ok[ns]), len(claims[ns] | ok[ns] | declared[ns]))
            for ns in NAMESPACES}


def label(source_id: str, reg: dict[str, dict[str, str]] | None = None) -> str:
    """The short citation a rendering prints: 'Eurostat tps00001, 2025'."""
    r = (reg or registry())[source_id]
    doc = source_id.split(":", 1)[1].split("@")[0]
    if re.fullmatch(r"[0-9a-f]{10}", doc):
        # A researched source (research.py) is keyed by a URL hash, which means nothing to a
        # reader; name it by its title instead, shortened at a word boundary.
        title = r["title"] if len(r["title"]) <= 60 else r["title"][:57].rsplit(" ", 1)[0] + "…"
        doc = f"— {title}"
    return f"{r['publisher']} {doc}, {r['published']}" if r["published"] else f"{r['publisher']} {doc}"


def sources_for(claim: str, cites=None) -> list[str]:
    return [c["source_id"] for c in (cites if cites is not None else citations()) if c["claim"] == claim]


def sync_eurostat() -> int:
    """Rewrite every dataset citation of a Eurostat column from the pinned pull (fetch_eurostat.py)."""
    sys.path.insert(0, str(ROOT / "model"))
    from fetch_eurostat import SERIES  # noqa: PLC0415 -- only this command needs it

    reg = registry()
    with PARAMETERS.open(newline="", encoding="utf-8") as fh:
        pull = list(csv.DictReader(fh))
    ids = {col: f"eurostat:{ds.lower()}@{period}" for col, (ds, _f, _s, _d, period) in SERIES.items()}
    missing = [sid for sid in ids.values() if sid not in reg]
    if missing:
        raise SystemExit(f"add these to the registry first: {missing}")

    keep = [c for c in citations() if not (c["claim"].startswith("param:")
                                           and c["claim"].split(":")[2] in SERIES)]
    for p in pull:
        ds, filters, _scale, _dec, period = SERIES[p["column"]]
        dims = "; ".join(f"{k}={v}" for k, v in sorted(filters.items()))
        locator = f"{ds}; {dims}; geo={p['iso']}; time={period}"   # Eurostat also codes Greece EL
        keep.append({
            "claim": f"param:{p['iso']}:{p['column']}", "source_id": ids[p["column"]],
            "locator": locator, "quote": "", "value_as_found": p["value"], "unit": "",
            "confidence": "primary", "retrieved": p["retrieved"], "checked_by": "fetch_eurostat.py",
        })
    keep.sort(key=lambda c: (c["claim"], c["source_id"]))
    with CITATIONS.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=CITATION_FIELDS)
        w.writeheader()
        w.writerows(keep)
    print(f"{len(pull)} Eurostat citations written; {len(keep)} citations in total")
    return 0


def report(reg, cites) -> None:
    print(f"{len(reg)} sources, {len(cites)} citations\n")
    print(f"{'namespace':<12} {'supported':>10} {'declared':>9} {'claims':>8}")
    for ns, (ok, declared, total) in coverage(reg, cites).items():
        if total:
            print(f"{ns:<12} {ok:>10} {declared:>9} {total:>8}   {100 * ok / total:5.1f}% sourced")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Validate and report on the source register.")
    ap.add_argument("--sync-eurostat", action="store_true",
                    help="regenerate Eurostat dataset citations from model/eurostat_pull.csv")
    args = ap.parse_args(argv)
    if args.sync_eurostat:
        return sync_eurostat()

    reg, cites = registry(), citations()
    errors = validate(reg, cites)
    for e in errors:
        print(f"error: {e}", file=sys.stderr)
    report(reg, cites)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
