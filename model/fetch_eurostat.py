#!/usr/bin/env python3
"""
Re-pull the six Eurostat figures for all 27 member states (ROADMAP step 4).

    python3 model/fetch_eurostat.py            # fetch, cache, write the pull, print the diff
    python3 model/fetch_eurostat.py --offline  # re-read the cache; diff without touching the network

Why this file exists
--------------------
`eu27_parameters.csv` describes its six Eurostat columns as sourced, but carries no dataset
code and no retrieval date, so "sourced" cannot be checked by anyone -- including by us. This
pulls each figure from the public dissemination API, keeps the raw JSON-stat response in the
cache, and writes `eurostat_pull.csv` with the dataset code, the period actually used and the
API's own `updated` vintage beside every value. A figure that carries those is verifiable by a
stranger in a way a paraphrased legal requirement is not.

**It reports a diff; it never rewrites the parameters.** A script that silently edits the
inputs is a script that can silently edit them wrongly, and every parameter change re-renders
27 briefs and stales 54 tracked artefacts (#52). Corrections are read first, then applied by
hand in one batch.

Picking the period
------------------
Not simply the latest. National accounts are reported at different times, so the most recent
period is routinely partial -- `nama_10_a64_e` had 10 of 27 states for 2025 and all 27 for
2024. Taking "latest" would silently mix vintages across countries. Instead each figure uses
the most recent period for which **all 27 report**, and that period is recorded per row.

The filters were calibrated against the existing column rather than assumed, which is what
`DECISIONS.md` #14 asks for. Two would have been wrong by guess:

* `renewables_pct` is the renewable share **of electricity** (`REN_ELC`), not of gross final
  energy (`REN`). Guessing `REN` disagrees with every one of the 27 by 36% on average.
* `elec_price_eur_mwh` excludes VAT and other recoverable taxes (`X_VAT`), not all taxes
  (`X_TAX`).
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import sys
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fetch as fetchlib  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
PARAMETERS = ROOT / "model" / "eu27_parameters.csv"
PULL = ROOT / "model" / "eurostat_pull.csv"

API = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data"
FIELDS = ["iso", "column", "value", "current", "dataset", "period", "updated", "retrieved"]

# How many recent periods to ask for while looking for one the whole EU-27 reports.
PERIODS = 6

# column -> (dataset, fixed dimension filters, multiplier onto the column's unit, decimals)
SERIES: dict[str, tuple[str, dict[str, str], float, int]] = {
    "population_m": ("tps00001", {"indic_de": "JAN"}, 1e-6, 3),
    "gdp_eur_bn": ("nama_10_gdp", {"na_item": "B1GQ", "unit": "CP_MEUR"}, 1e-3, 1),
    "gov_employment_k": (
        "nama_10_a64_e",
        {"nace_r2": "O", "unit": "THS_PER", "na_item": "EMP_DC"},
        1.0,
        1,
    ),
    "elec_price_eur_mwh": (
        "nrg_pc_205",
        {"nrg_cons": "MWH2000-19999", "unit": "KWH", "currency": "EUR", "tax": "X_VAT"},
        1000.0,
        1,
    ),
    "renewables_pct": ("nrg_ind_ren", {"nrg_bal": "REN_ELC", "unit": "PC"}, 1.0, 1),
    "land_km2": ("reg_area3", {"landuse": "L0008", "unit": "KM2"}, 1.0, 0),
}


def countries() -> list[str]:
    with PARAMETERS.open(newline="", encoding="utf-8") as fh:
        return [r["iso2"] for r in csv.DictReader(fh)]


def parameters() -> dict[str, dict[str, str]]:
    with PARAMETERS.open(newline="", encoding="utf-8") as fh:
        return {r["iso2"]: r for r in csv.DictReader(fh)}


def url_for(dataset: str, filters: dict[str, str], isos: list[str]) -> str:
    """Ask only for the 27 states, so the cached response is evidence for exactly our rows."""
    q = [("format", "JSON"), ("lastTimePeriod", str(PERIODS))]
    q += sorted(filters.items())
    q += [("geo", iso) for iso in isos]
    return f"{API}/{dataset}?{urllib.parse.urlencode(q)}"


def series(doc: dict, isos: list[str]) -> tuple[dict[str, dict[str, float]], list[str]]:
    """JSON-stat -> {geo: {period: value}}, plus periods oldest-first.

    Values are held in a sparse flat array indexed across every dimension, so the offset for
    one (geo, period) is the sum of each dimension's position times the product of the sizes
    that follow it.
    """
    dims, sizes = doc["id"], doc["size"]
    strides = {}
    for pos, name in enumerate(dims):
        stride = 1
        for s in sizes[pos + 1 :]:
            stride *= s
        strides[name] = stride

    geo_idx = doc["dimension"]["geo"]["category"]["index"]
    time_idx = doc["dimension"]["time"]["category"]["index"]
    values = doc["value"]

    # Every other dimension was filtered to a single value, so it contributes offset 0.
    out: dict[str, dict[str, float]] = {}
    for iso in isos:
        if iso not in geo_idx:
            continue
        for period, t in time_idx.items():
            flat = geo_idx[iso] * strides["geo"] + t * strides["time"]
            v = values.get(str(flat))
            if v is not None:
                out.setdefault(iso, {})[period] = float(v)

    periods = sorted(time_idx, key=lambda p: time_idx[p])
    return out, periods


def complete_period(data: dict[str, dict[str, float]], periods: list[str], isos: list[str]) -> str | None:
    """The most recent period every one of the 27 reports. None if there is no such period."""
    for period in reversed(periods):
        if all(period in data.get(iso, {}) for iso in isos):
            return period
    return None


def pull(offline: bool = False) -> tuple[list[dict[str, str]], list[str]]:
    isos = countries()
    current = parameters()
    today = dt.date.today().isoformat()
    rows: list[dict[str, str]] = []
    manifest: list[dict[str, str]] = []
    notes: list[str] = []

    for column, (dataset, filters, scale, decimals) in SERIES.items():
        url = url_for(dataset, filters, isos)
        path = fetchlib.cache_path("EU", "eurostat", column, url).with_suffix(".json")

        if offline:
            if not path.exists():
                notes.append(f"{column}: not in the cache; run without --offline first")
                continue
            body = path.read_bytes()
        else:
            result = fetchlib.fetch(url)
            manifest.append(fetchlib.store("EU", "eurostat", column, url, result, today))
            if not result.ok:
                notes.append(f"{column}: {dataset} returned {result.status}")
                continue
            body = result.body

        doc = json.loads(body)
        data, periods = series(doc, isos)
        period = complete_period(data, periods, isos)
        if period is None:
            best = max((sum(p in data.get(i, {}) for i in isos) for p in periods), default=0)
            notes.append(
                f"{column}: no period in the last {PERIODS} has all 27 reporting "
                f"(best was {best}/27); skipped"
            )
            continue

        for iso in isos:
            value = round(data[iso][period] * scale, decimals)
            rows.append(
                {
                    "iso": iso,
                    "column": column,
                    "value": f"{value:.{decimals}f}",
                    "current": current[iso][column],
                    "dataset": dataset,
                    "period": period,
                    "updated": doc.get("updated", ""),
                    "retrieved": today,
                }
            )

    if manifest:
        fetchlib.write_manifest(fetchlib.merge(fetchlib.load_manifest(), manifest))
    return rows, notes


def write_pull(rows: list[dict[str, str]]) -> None:
    with PULL.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(sorted(rows, key=lambda r: (r["iso"], r["column"])))


def report(rows: list[dict[str, str]], notes: list[str]) -> None:
    """What the API now says against what the CSV holds. Reported, never applied."""
    for n in notes:
        print(f"note: {n}", file=sys.stderr)

    by_column: dict[str, list[dict[str, str]]] = {}
    for r in rows:
        by_column.setdefault(r["column"], []).append(r)

    print(f"{'column':<20} {'dataset':<15} {'period':<8} {'differs':>8}  {'max drift':>10}")
    total = 0
    for column, rs in by_column.items():
        drifts = []
        for r in rs:
            try:
                cur, new = float(r["current"]), float(r["value"])
            except ValueError:
                continue
            if cur:
                drifts.append((abs(new - cur) / abs(cur), r["iso"]))
        differs = [d for d in drifts if d[0] > 0.005]
        total += len(differs)
        worst = max(drifts, default=(0.0, "-"))
        print(
            f"{column:<20} {rs[0]['dataset']:<15} {rs[0]['period']:<8} "
            f"{len(differs):>4}/{len(rs):<3}  {worst[0] * 100:>7.1f}% {worst[1]}"
        )
    print(f"\n{total} of {len(rows)} values differ from eu27_parameters.csv by more than 0.5%")
    print(f"wrote {PULL.relative_to(ROOT)} -- review before changing any parameter")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Re-pull the Eurostat figures and diff them.")
    ap.add_argument("--offline", action="store_true", help="use the cache; do not hit the network")
    args = ap.parse_args(argv)

    rows, notes = pull(offline=args.offline)
    if not rows:
        for n in notes:
            print(f"note: {n}", file=sys.stderr)
        print("error: nothing pulled", file=sys.stderr)
        return 1
    write_pull(rows)
    report(rows, notes)
    return 0


if __name__ == "__main__":
    sys.exit(main())
