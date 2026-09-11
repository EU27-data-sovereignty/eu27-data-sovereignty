#!/usr/bin/env python3
"""
Fetch the legal corpus: the instruments behind the sourceable cells, for all 27 states.

    python3 model/fetch_sources.py             # fetch everything in source_urls.csv
    python3 model/fetch_sources.py --iso NL    # one country
    python3 model/fetch_sources.py --report    # what the manifest already says; no network

Why this file exists
--------------------
`sources.csv` records that a claim was checked against a URL. Keeping the document means the
quote can still be checked later, when the page has been reorganised or the statute
consolidated -- and a quote that no longer appears in its source becomes a finding instead of
an invisible rot. `SOURCES.md` explains the whole arrangement; `source_urls.csv` is the input
this reads.

Each row of `source_urls.csv` carries a `policy`:

* **auto** -- fetched normally.
* **manual** -- the host refuses automated requests (a bot challenge, or a connection that
  never completes). The document is fetched by hand into `cache/legal/<ISO>/` and `--adopt`
  hashes it into the manifest, so its provenance is recorded identically and only the
  transport differs.
* **forbidden** -- the host's `robots.txt` publishes `Disallow: /`. Never fetched. Poland's
  `isap.sejm.gov.pl` is the one such case here, and it is worth being exact about why it is
  marked rather than detected: it serves `robots.txt` only to browser user-agents, so an
  automated client is told nothing and would sail straight past a rule that plainly exists.
  Being *able* to fetch something is not permission to.

Refusals are recorded as rows with their status rather than worked around. Pretending
otherwise would mean either a fake user-agent, which lies to an administrator about who is
asking, or a silent gap, which is indistinguishable from work not yet done.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fetch as fetchlib  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
URLS = ROOT / "model" / "source_urls.csv"
KIND = "legal"


def targets(iso: str | None = None) -> list[dict[str, str]]:
    with URLS.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    return [r for r in rows if iso is None or r["iso"] == iso]


def run(iso: str | None = None) -> list[dict[str, str]]:
    today = dt.date.today().isoformat()
    fresh: list[dict[str, str]] = []

    for t in targets(iso):
        policy = t.get("policy", "auto")
        if policy == "forbidden":
            # The host publishes Disallow: / for all agents. Not fetched, ever -- and recorded
            # as such, because a source we are not allowed to retrieve is a fact about the
            # source, not a gap in the work. Some of these sites serve robots.txt only to
            # browser user-agents, so being *able* to fetch is not permission to.
            fresh.append(
                fetchlib.store(
                    t["iso"], KIND, t["column"], t["url"],
                    fetchlib.Result(fetchlib.STATUS_ROBOTS, "", b""), today,
                )
            )
            print(f"no {t['iso']} {t['column']:<26} {'robots-denied':<14} {'':>8}  (not attempted)")
            continue

        result = fetchlib.fetch(t["url"])
        row = fetchlib.store(t["iso"], KIND, t["column"], t["url"], result, today)
        fresh.append(row)
        mark = "ok " if result.ok else "-- "
        print(f"{mark}{t['iso']} {t['column']:<26} {result.status:<14} {len(result.body):>8} B")

    fetchlib.write_manifest(fetchlib.merge(fetchlib.load_manifest(), fresh))
    return fresh


def adopt(iso: str | None = None) -> list[dict[str, str]]:
    """Record files already sitting in the cache, however they got there.

    The manual route for a blocked gazette. Provenance is identical -- a URL, a publisher, a
    date and a hash; only the transport differs, and the manifest says so via `http_status`.
    """
    today = dt.date.today().isoformat()
    fresh: list[dict[str, str]] = []

    for t in targets(iso):
        stem = fetchlib.cache_path(t["iso"], KIND, t["column"], t["url"])
        found = [p for p in stem.parent.glob(f"{stem.name}.*")] if stem.parent.exists() else []
        if not found:
            continue
        path = found[0]
        body = path.read_bytes()
        fresh.append(
            {
                "iso": t["iso"],
                "kind": KIND,
                "key": t["column"],
                "url": t["url"],
                "http_status": "manual",
                "content_type": fetchlib.EXTENSIONS.get(path.suffix, path.suffix.lstrip(".")),
                "bytes": str(len(body)),
                "sha256": fetchlib.sha256(body),
                "retrieved": today,
            }
        )
        print(f"adopted {t['iso']} {t['column']:<26} {path.name}")

    if fresh:
        fetchlib.write_manifest(fetchlib.merge(fetchlib.load_manifest(), fresh))
    return fresh


def report() -> None:
    rows = [r for r in fetchlib.load_manifest() if r["kind"] == KIND]
    if not rows:
        print("nothing fetched yet; run ./run.sh fetch legal")
        return

    ok = [r for r in rows if r["http_status"] == "200"]
    manual = [r for r in rows if r["http_status"] == "manual"]
    blocked = [r for r in rows if r["http_status"] not in ("200", "manual")]

    print(f"{len(ok)} fetched, {len(manual)} adopted by hand, {len(blocked)} refused\n")
    if blocked:
        print(f"{'iso':<5}{'column':<28}{'status':<16}url")
        for r in sorted(blocked, key=fetchlib.sort_key):
            print(f"{r['iso']:<5}{r['key']:<28}{r['http_status']:<16}{r['url'][:60]}")
        print("\nThese need the manual route: see SOURCES.md.")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Fetch the legal corpus into the cache.")
    ap.add_argument("--iso", help="restrict to one member state")
    ap.add_argument("--adopt", action="store_true", help="hash files already in the cache")
    ap.add_argument("--report", action="store_true", help="summarise the manifest; no network")
    args = ap.parse_args(argv)

    if args.report:
        report()
        return 0
    if args.adopt:
        adopt(args.iso)
        return 0

    run(args.iso)
    print()
    report()
    return 0


if __name__ == "__main__":
    sys.exit(main())
