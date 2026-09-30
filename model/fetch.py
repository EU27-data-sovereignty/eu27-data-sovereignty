#!/usr/bin/env python3
"""
The shared fetch layer: retrieve a source document once, keep it, and record what was kept.

Used by `fetch_eurostat.py` (the six Eurostat figures) and `fetch_sources.py` (the legal
corpus). Nothing here is specific to either.

Why this file exists
--------------------
`sources.py` records that a claim was checked against a URL. It cannot record that the URL
still says what it said: pages get rewritten, statutes get consolidated, and a bare link that
now reads differently looks exactly like a verified cell. So the bytes are kept.

Two rules follow from that, and they are the whole design:

* **The cache is rebuildable and untracked; the manifest is tracked.** `cache/` holds the
  documents and is gitignored -- national gazette PDFs are large and git history never shrinks
  (see the workspace rule on large binaries, and #52 for the same manifest pattern applied to
  the per-country artefacts). `fetch_manifest.csv` holds the sha256 of each one, so drift is
  detectable without carrying the bytes in the repository.
* **A failed fetch is a row, not a gap.** Seven of the 27 national gazettes refuse automated
  requests. Recording that as a row with its status makes it a measured fact; omitting it makes
  it indistinguishable from work not yet done. See `SOURCES.md`.

Fetching politely
-----------------
These are government servers, and a scraper that hammers 27 national gazettes earns an IP ban
and deserves one. Requests are serial, spaced by `DELAY`, carry a User-Agent that says who is
asking and why, and obey `robots.txt`. A 403 is never retried -- it is an answer.
"""
from __future__ import annotations

import csv
import hashlib
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request
import urllib.robotparser
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "cache"
MANIFEST = ROOT / "model" / "fetch_manifest.csv"

FIELDS = ["iso", "kind", "key", "url", "http_status", "content_type", "bytes", "sha256", "retrieved"]

# Says who is asking and points at the project, so an administrator who sees this in a log can
# find out what it is rather than guess. Identifying yourself is the cheapest courtesy there is.
UA = (
    "sovereign-data-centers/1.0 (research; +https://github.com/pieteradejong/sovereign-data-centers) "
    "python-urllib"
)
TIMEOUT = 30
DELAY = 1.5  # seconds between requests, to every host alike

# Enough to name the file usefully; the sha256 in the manifest is what actually identifies it.
EXTENSIONS = {
    "application/json": ".json",
    "application/pdf": ".pdf",
    "application/xml": ".xml",
    "text/html": ".html",
    "text/plain": ".txt",
    "text/xml": ".xml",
}

_robots: dict[str, urllib.robotparser.RobotFileParser | str | None] = {}
_last_request = 0.0


@dataclass(frozen=True)
class Result:
    """What came back. `status` is an HTTP code, or one of the STATUS_* strings below."""

    status: str
    content_type: str
    body: bytes

    @property
    def ok(self) -> bool:
        return self.status == "200"


STATUS_ROBOTS = "robots-denied"
STATUS_ROBOTS_UNREADABLE = "robots-unreadable"
STATUS_TIMEOUT = "timeout"
STATUS_ERROR = "error"


def _throttle() -> None:
    global _last_request
    wait = DELAY - (time.monotonic() - _last_request)
    if wait > 0:
        time.sleep(wait)
    _last_request = time.monotonic()


def robots_check(url: str) -> str:
    """One of "allow", STATUS_ROBOTS, STATUS_ROBOTS_UNREADABLE.

    Three outcomes, deliberately kept apart. `RobotFileParser.read()` collapses two of them:
    it swallows the HTTP error and treats a 403 on robots.txt as "disallow everything", which
    makes a host that blocked us look like a host that asked us not to come. Those are
    different facts and only the first is a rule we are obeying, so robots.txt is fetched here
    and its status kept.

    Of the seven refusals in this dataset exactly one -- Poland's `isap.sejm.gov.pl` -- is a
    published `Disallow: /`. The rest never served us their rules at all.
    """
    parts = urllib.parse.urlsplit(url)
    host = f"{parts.scheme}://{parts.netloc}"

    if host not in _robots:
        req = urllib.request.Request(f"{host}/robots.txt", headers={"User-Agent": UA})
        try:
            _throttle()
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                text = resp.read().decode("utf-8", errors="replace")
            rp = urllib.robotparser.RobotFileParser()
            rp.parse(text.splitlines())
            _robots[host] = rp
        except urllib.error.HTTPError as e:
            # 401/403: the host is refusing us, not publishing a rule. Say which.
            _robots[host] = "unreadable" if e.code in (401, 403) else None
        except Exception:
            # No robots.txt published, or unreachable. Not a prohibition.
            _robots[host] = None

    rp = _robots[host]
    if rp is None:
        return "allow"
    if rp == "unreadable":
        return STATUS_ROBOTS_UNREADABLE
    return "allow" if rp.can_fetch(UA, url) else STATUS_ROBOTS


def fetch(url: str, timeout: int = TIMEOUT) -> Result:
    """Retrieve one URL. Never raises: a failure is a Result with a non-200 status."""
    # Only a rule we could actually read stops us. When robots.txt was itself refused there
    # is no published rule to obey, so the request goes ahead and the document's own status is
    # recorded -- which is the more informative answer, and an honest one either way.
    if robots_check(url) == STATUS_ROBOTS:
        return Result(STATUS_ROBOTS, "", b"")

    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    try:
        _throttle()
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read()
            ctype = resp.headers.get_content_type()
            return Result(str(resp.status), ctype, body)
    except urllib.error.HTTPError as e:
        # A 403 is an answer, not a transient fault. Recorded, never retried.
        return Result(str(e.code), e.headers.get_content_type() if e.headers else "", b"")
    except TimeoutError:
        return Result(STATUS_TIMEOUT, "", b"")
    except Exception:
        return Result(STATUS_ERROR, "", b"")


BROWSERS = [
    "/Applications/Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/usr/bin/google-chrome",
    "/usr/bin/chromium",
]
RENDERED = "text/html; rendered"


def fetch_rendered(url: str, timeout: int = 60) -> Result:
    """The page as a browser shows it, for pages that build their text with JavaScript (#83).

    Only for a page that already answered 200 and whose quote was not in the served HTML: a refusal
    (403, robots) is an answer and is never routed around with a browser. The DOM of a rendered page
    can differ from one load to the next, so its hash identifies what we checked, not what a
    stranger will fetch; `content_type` says `rendered` so every reader can tell."""
    if robots_check(url) == STATUS_ROBOTS:
        return Result(STATUS_ROBOTS, "", b"")
    browser = next((b for b in BROWSERS if Path(b).exists()), None)
    if not browser:
        return Result(STATUS_ERROR, "", b"")
    try:
        _throttle()
        r = subprocess.run([browser, "--headless", "--disable-gpu", "--no-sandbox", f"--user-agent={UA}",
                            "--virtual-time-budget=10000", "--dump-dom", url],
                           capture_output=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return Result(STATUS_TIMEOUT, "", b"")
    return Result("200", RENDERED, r.stdout) if r.returncode == 0 and r.stdout.strip() else Result(STATUS_ERROR, "", b"")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def cache_path(iso: str, kind: str, key: str, url: str) -> Path:
    """Deterministic location for one document.

    The URL digest in the filename keeps two sources for the same cell from colliding, which
    they otherwise would: a compound cell needs one file per instrument it names.
    """
    stem = f"{key}-{sha256(url.encode())[:8]}"
    return CACHE / kind / iso / stem


def store(iso: str, kind: str, key: str, url: str, result: Result, retrieved: str) -> dict[str, str]:
    """Write the body to the cache if there is one, and return the manifest row either way."""
    path = cache_path(iso, kind, key, url).with_suffix(EXTENSIONS.get(result.content_type, ".bin"))
    if result.ok and result.body:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(result.body)
    return {
        "iso": iso,
        "kind": kind,
        "key": key,
        "url": url,
        "http_status": result.status,
        "content_type": result.content_type,
        "bytes": str(len(result.body)),
        "sha256": sha256(result.body) if result.body else "",
        "retrieved": retrieved,
    }


def load_manifest() -> list[dict[str, str]]:
    if not MANIFEST.exists():
        return []
    with MANIFEST.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        if reader.fieldnames != FIELDS:
            raise SystemExit(f"{MANIFEST.name}: header is {reader.fieldnames}, expected {FIELDS}")
        return list(reader)


def sort_key(row: dict[str, str]) -> tuple[str, str, str, str]:
    return (row["iso"], row["kind"], row["key"], row["url"])


def write_manifest(rows: list[dict[str, str]]) -> None:
    """Sorted, so a diff shows what was added rather than where it landed."""
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    with MANIFEST.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(sorted(rows, key=sort_key))


def merge(existing: list[dict[str, str]], fresh: list[dict[str, str]]) -> list[dict[str, str]]:
    """Fresh rows replace same-identity old ones; everything else is kept."""
    by_id = {sort_key(r): r for r in existing}
    for r in fresh:
        by_id[sort_key(r)] = r
    return list(by_id.values())


def verify() -> list[str]:
    """Every way the manifest and the cache disagree.

    A cached file that is *absent* is not an error: `cache/` is gitignored and rebuildable, and
    a fresh clone has none of it. A file that is present and has changed underneath us is.
    """
    errors: list[str] = []
    rows = load_manifest()

    for i, r in enumerate(rows, start=2):  # row 1 is the header
        where = f"row {i} ({r['iso']}/{r['kind']}/{r['key']})"
        if not r["url"].startswith(("http://", "https://")):
            errors.append(f"{where}: url is not an absolute http(s) URL")
        if r["http_status"] == "200" and not r["sha256"]:
            errors.append(f"{where}: fetched successfully but recorded no sha256")

        path = cache_path(r["iso"], r["kind"], r["key"], r["url"]).with_suffix(
            EXTENSIONS.get(r["content_type"], ".bin")
        )
        if path.exists() and r["sha256"] and sha256(path.read_bytes()) != r["sha256"]:
            errors.append(f"{where}: {path.relative_to(ROOT)} has changed since it was recorded")

    order = [sort_key(r) for r in rows]
    if order != sorted(order):
        errors.append("rows are not sorted; sort them so diffs stay readable")
    return errors
