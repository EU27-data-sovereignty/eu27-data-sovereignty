#!/usr/bin/env python3
"""
The release ledger of the mobile reader (DECISIONS.md #114): generated from EAS, never written by hand.

    python3 model/release.py record --build <eas-build-id> [--dir mobile] [--ledger mobile/releases.csv]
    python3 model/release.py check  [--dir mobile] [--ledger mobile/releases.csv]

Why this file exists
--------------------
EAS keeps the build number (`appVersionSource: remote`, `autoIncrement`), so nothing in the tree says which
build went to the store from which commit. `record` asks EAS for one build (`eas build:view --json`, the
CLI pinned in mobile/eas.json, read-only) and appends what a third party needs to retrace it: the app
version and build number, the build and fingerprint ids, the git commit, the runtime version and channel,
and the edition inside that binary (the sha256 of `mobile/assets/data/manifest.json` at that commit, which
`tests/test_export_split.py` pins to the committed bundle). `check` holds the ledger's shape on every run of
`mobile/test.sh` (`release`): the columns, one row per build id, the version in `app.json` not behind the
last recorded one, and every commit present in this repository.

No credential is handled here: `eas` reads EXPO_TOKEN or the login session itself.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COLUMNS = ["recorded_at", "platform", "app_version", "build_number", "build_id", "fingerprint", "runtime_version",
           "channel", "git_commit", "edition_manifest_sha256", "status"]
NIL_PROJECT = "00000000-0000-0000-0000-000000000000"

Result = tuple[str, bool, str]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def version_tuple(v: str) -> tuple[int, ...]:
    return tuple(int(p) for p in v.split("."))


def read_ledger(ledger: Path) -> list[dict[str, str]]:
    if not ledger.exists():
        return []
    with ledger.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        if reader.fieldnames != COLUMNS:
            raise ValueError(f"{ledger}: columns are {reader.fieldnames}, expected {COLUMNS}")
        return list(reader)


def commit_exists(commit: str) -> bool:
    return subprocess.run(["git", "-C", str(ROOT), "cat-file", "-e", f"{commit}^{{commit}}"],
                          capture_output=True).returncode == 0


# --------------------------------------------------------------------------- #
# check: the ledger's shape, on every test run
# --------------------------------------------------------------------------- #

def check(app_dir: Path, ledger: Path) -> list[Result]:
    results: list[Result] = []
    app = json.loads((app_dir / "app.json").read_text(encoding="utf-8"))["expo"]
    try:
        rows = read_ledger(ledger)
    except ValueError as e:
        return [("ledger columns", False, str(e))]
    results.append(("ledger columns", True, f"{len(rows)} row(s)"))
    ids = [r["build_id"] for r in rows]
    results.append(("one row per build", len(ids) == len(set(ids)), ""))
    for r in rows:
        results.append((f"commit {r['git_commit'][:7]} exists", commit_exists(r["git_commit"]), r["build_id"]))
        results.append((f"build {r['build_id'][:8]} names an edition",
                        len(r["edition_manifest_sha256"]) == 64, ""))
    if rows:
        last = max(version_tuple(r["app_version"]) for r in rows)
        current = version_tuple(app["version"])
        results.append(("app.json version is not behind the ledger", current >= last,
                        f"app.json {app['version']}, ledger {'.'.join(map(str, last))}"))
    project = app.get("extra", {}).get("eas", {}).get("projectId", "")
    if project == NIL_PROJECT:
        print("warning: app.json still carries the placeholder EAS project id; run `eas init --force` (TODO.md)")
    return results


# --------------------------------------------------------------------------- #
# record: one build, from EAS
# --------------------------------------------------------------------------- #

def eas_cli(app_dir: Path) -> str:
    """The one pinned CLI: eas.json's cli.version, run through npx as the deploy does (#114)."""
    version = json.loads((app_dir / "eas.json").read_text(encoding="utf-8"))["cli"]["version"]
    return f"eas-cli@{version}"


def eas_build(app_dir: Path, build_id: str) -> dict:
    out = subprocess.run(["npx", "--yes", eas_cli(app_dir), "build:view", build_id, "--json", "--non-interactive"],
                         cwd=app_dir, capture_output=True, text=True, check=True).stdout
    # eas prints notices before the JSON; the document is the last `{`-opened block.
    return json.loads(out[out.index("{"):])


def row_from(build: dict, manifest_sha: str, recorded_at: str) -> dict[str, str]:
    metrics = build.get("metrics") or {}
    return {
        "recorded_at": recorded_at,
        "platform": str(build.get("platform", "")).lower(),
        "app_version": build.get("appVersion", "") or "",
        "build_number": build.get("appBuildVersion", "") or "",
        "build_id": build["id"],
        "fingerprint": (build.get("fingerprint") or {}).get("hash", "") or metrics.get("fingerprintHash", "") or "",
        "runtime_version": build.get("runtimeVersion", "") or "",
        "channel": build.get("channel", "") or (build.get("updateChannel") or {}).get("name", "") or "",
        "git_commit": build.get("gitCommitHash", "") or "",
        "edition_manifest_sha256": manifest_sha,
        "status": str(build.get("status", "")).lower(),
    }


def record(app_dir: Path, ledger: Path, build_id: str) -> int:
    build = eas_build(app_dir, build_id)
    commit = build.get("gitCommitHash") or ""
    if not commit or not commit_exists(commit):
        print(f"build {build_id} names commit {commit!r}, which is not in this repository", file=sys.stderr)
        return 1
    manifest = subprocess.run(["git", "-C", str(ROOT), "show", f"{commit}:mobile/assets/data/manifest.json"],
                              capture_output=True, check=True).stdout
    row = row_from(build, hashlib.sha256(manifest).hexdigest(),
                   dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat())
    rows = read_ledger(ledger)
    if any(r["build_id"] == row["build_id"] for r in rows):
        print(f"build {build_id} is already in {ledger}")
        return 0
    rows.append(row)
    with ledger.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=COLUMNS, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print(f"recorded {row['platform']} {row['app_version']} ({row['build_number']}) build {build_id[:8]} "
          f"at commit {commit[:7]}, edition manifest {row['edition_manifest_sha256'][:16]}")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("record", help="append one EAS build to the ledger")
    r.add_argument("--build", required=True, help="the EAS build id")
    c = sub.add_parser("check", help="the ledger's shape")
    for p in (r, c):
        p.add_argument("--dir", type=Path, default=ROOT / "mobile")
        p.add_argument("--ledger", type=Path, default=ROOT / "mobile" / "releases.csv")
    a = ap.parse_args(argv)
    if a.cmd == "record":
        return record(a.dir, a.ledger, a.build)
    results = check(a.dir, a.ledger)
    failed = [x for x in results if not x[1]]
    for name, ok, detail in results:
        print(f"{'ok  ' if ok else 'FAIL'} {name}{f'  ({detail})' if detail else ''}")
    print(f"{len(results) - len(failed)} of {len(results)} checks passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
