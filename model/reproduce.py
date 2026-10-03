#!/usr/bin/env python3
"""
Prove the published registers follow from the committed evidence (DECISIONS #84).

    python3 model/reproduce.py admit-check     # exit 1 if admission would change any register
    python3 model/reproduce.py clean-room [--evidence] [--keep]   # rebuild everything from a fresh clone

Why this file exists
--------------------
The registers a reader sees (sources/registry.csv, sources/citations.csv, national_data.csv,
sovereignty_indicators.csv, and the vetting disputes and outcomes) are written by admission, from staged
research, verification rows, rechecks and the tier table. Everything admission reads is committed. So
a stranger can re-run it; this check does exactly that and compares. The committed registers must be a
fixed point: admitting again changes nothing.

Admission always runs in one order: research.admit (the first research runs), then vetting.admit (which
may supersede or dispute what research admitted). `./run.sh admit` runs both; so does this check.

The files are snapshotted first and restored afterwards whatever happens, so the check never leaves the
tree changed.
"""
from __future__ import annotations

import contextlib
import difflib
import io
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "model"))

REGISTERS = [
    ROOT / "model" / "sources" / "registry.csv",
    ROOT / "model" / "sources" / "citations.csv",
    ROOT / "model" / "national_data.csv",
    ROOT / "model" / "sovereignty_indicators.csv",
    ROOT / "model" / "research" / "vetting" / "disputes.csv",
    ROOT / "model" / "research" / "vetting" / "outcomes.csv",
]


DERIVED = ("research.py", "vetting.py")          # the checked_by of every admitted citation


def reset_derived() -> None:
    """Strip everything a previous admission wrote, keeping only the base admission never produces:
    the Eurostat citations, the migrated citations of #67, the sources they cite and the rows they
    support. Admission then rebuilds the rest from the committed evidence alone, so its output cannot
    depend on how many times it has run (found 2026-09-30: without this, a gap vetting filled read as
    an existing fact on the next run, and 46 register rows changed)."""
    import csv  # noqa: PLC0415
    import national_data as nd  # noqa: PLC0415
    import provenance  # noqa: PLC0415
    import research  # noqa: PLC0415
    import vetting  # noqa: PLC0415
    base = [c for c in provenance.citations() if not c["checked_by"].startswith(DERIVED)]
    cited = {c["source_id"] for c in base}
    reg = {sid: r for sid, r in provenance.registry().items()
           if sid in cited or not r["notes"].startswith("sha256 ")}
    supported = {tuple(c["claim"].split(":")[1:3]) for c in base if c["claim"].startswith("record:")}
    rows = [r for r in nd.read_rows() if (r["iso"], r["record_class"]) in supported]
    provenance.write_registry(reg)
    provenance.write_citations(base)
    nd.write_rows(rows)
    with research.INDICATOR_VALUES.open("w", newline="", encoding="utf-8") as fh:
        csv.writer(fh, lineterminator="\n").writerow(["iso", "indicator", "value"])
    for path in (vetting.DISPUTES, vetting.OUTCOMES):
        path.unlink(missing_ok=True)


def admit_all() -> None:
    """From the base, research then vetting: a pure function of the committed evidence."""
    import research  # noqa: PLC0415
    import vetting  # noqa: PLC0415
    reset_derived()
    research.admit()
    if any(vetting.DIR.glob("[A-Z][A-Z].json")):
        vetting.admit()


def admit_check() -> int:
    before = {p: p.read_bytes() if p.exists() else None for p in REGISTERS}
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            admit_all()
        after = {p: p.read_bytes() if p.exists() else None for p in REGISTERS}
    finally:
        for p, data in before.items():
            if data is None:
                p.unlink(missing_ok=True)
            else:
                p.write_bytes(data)
    changed = [p for p in REGISTERS if before[p] != after[p]]
    for p in changed:
        old = (before[p] or b"").decode("utf-8").splitlines()
        new = (after[p] or b"").decode("utf-8").splitlines()
        diff = list(difflib.unified_diff(old, new, str(p.relative_to(ROOT)), "re-admitted", n=0, lineterm=""))
        print(f"{p.relative_to(ROOT)}: {sum(1 for d in diff if d[:1] in '+-') - 2} lines differ", file=sys.stderr)
        for line in diff[2:12]:
            print(f"    {line[:160]}", file=sys.stderr)
    print(f"{len(REGISTERS) - len(changed)} of {len(REGISTERS)} registers reproduce from the committed evidence")
    return 1 if changed else 0


def clean_room(evidence: bool = False, keep: bool = False) -> int:
    """Rebuild everything from a fresh clone of HEAD and compare it with what is committed (#84).

    Only committed files exist in the clone, so this proves the published outputs follow from the
    repository alone: not from this machine's cache, its uncommitted edits or its history."""
    import os  # noqa: PLC0415
    import shutil  # noqa: PLC0415
    import subprocess  # noqa: PLC0415
    import tempfile  # noqa: PLC0415

    tmp = Path(tempfile.mkdtemp(prefix="eu27-reproduce-"))
    clone = tmp / "repo"
    env = {**os.environ, "SOURCE_DATE_EPOCH": (ROOT / ".build-epoch").read_text().strip()}
    failures: list[str] = []

    def run(label: str, *cmd: str, cwd: Path = clone) -> subprocess.CompletedProcess:
        print(f"  {label}", flush=True)
        r = subprocess.run(cmd, cwd=cwd, env=env, capture_output=True, text=True)
        if r.returncode:
            failures.append(f"{label}: exit {r.returncode}\n{(r.stderr or r.stdout)[-800:]}")
        return r

    try:
        print(f"clean room: {tmp}")
        run("clone HEAD", "git", "clone", "--quiet", str(ROOT), str(clone), cwd=tmp)
        head = subprocess.run(["git", "rev-parse", "--short=12", "HEAD"], cwd=clone, capture_output=True,
                              text=True).stdout.strip()
        print(f"  commit {head}")
        for script in ("generate_countries.py", "export_json.py", "ask_corpus.py", "evidence_report.py"):
            run(f"regenerate ({script})", sys.executable, f"model/{script}")
        drift = subprocess.run(["git", "status", "--porcelain"], cwd=clone, capture_output=True, text=True).stdout
        if drift.strip():
            failures.append("generated files differ from the committed ones:\n" + drift[:1500])
        # Then the whole gate, as CI runs it, in the clone (#92): unit tests (with the fact-check ledger
        # replay), admission, the PDFs and their inspection, types, lint, Vitest, the build and the size
        # budget. Only the browser tests are left out (--no-e2e): they need Chrome, not the repository.
        run("install dependencies (npm ci)", "npm", "ci", "--silent")
        run("install web dependencies (npm ci)", "npm", "ci", "--silent", cwd=clone / "web")
        run("the full gate (./test.sh --no-e2e)", "./test.sh", "--no-e2e")
        if evidence:
            # The third-party audit, scripted: no cache, every source fetched again from the web.
            run("recheck every cited source from the live web (slow)", sys.executable,
                "model/research.py", "recheck")
            got = subprocess.run(["git", "diff", "--stat", "--", "model/research/recheck.csv"], cwd=clone,
                                 capture_output=True, text=True).stdout.strip()
            print(f"  evidence drift since the committed recheck: {got or 'none'}")
    finally:
        if not keep:
            shutil.rmtree(tmp, ignore_errors=True)
    for f in failures:
        print(f"FAILED {f}", file=sys.stderr)
    print("reproduced from scratch" if not failures else f"{len(failures)} step(s) did not reproduce")
    return 1 if failures else 0


if __name__ == "__main__":
    args = sys.argv[1:]
    if args == ["admit-check"]:
        sys.exit(admit_check())
    if args == ["admit"]:
        admit_all()
        sys.exit(0)
    if args[:1] == ["clean-room"]:
        sys.exit(clean_room(evidence="--evidence" in args, keep="--keep" in args))
    raise SystemExit(__doc__)
