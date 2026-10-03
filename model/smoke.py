#!/usr/bin/env python3
"""
Smoke-test the live site: what a reader gets, checked from outside, after every deploy and every week.

    python3 model/smoke.py [--site https://eu27.cloud] [--bundle web/public/data/eu27.json] [--summary FILE]

Why this file exists
--------------------
The gate tests the build; only a request to the live domain shows what was actually served. The deploy
workflow ran a few curl lines; the weekly monitor needs the same checks, so they live here once, in stdlib
Python, and both call it. Read-only: it only sends GET and HEAD requests.

Checked: every route a reader can open answers 200 with HTML; the EU-27 report, all 27 country PDFs and the
4 report previews answer with their type; every security header `vercel.json` sets on `/(.*)` is served as
set; indexing is still off (robots and `X-Robots-Tag`); `www` redirects to the apex; the TLS certificate is
valid for at least `--min-days` more days; and, with `--bundle`, the served data bundle is the committed one.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import socket
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "book"))

# Every route a reader can open; tests/test_smoke.py keeps it a superset of the e2e ROUTES.
ROUTES = ["/", "/countries", "/country/DE", "/country/NL", "/holdings", "/holdings/civil_registry", "/sources",
          "/sovereignty", "/ask", "/methodology", "/fact-check", "/fact-check/DE"]
ISOS = ["AT", "BE", "BG", "CY", "CZ", "DE", "DK", "EE", "EL", "ES", "FI", "FR", "HR", "HU", "IE", "IT", "LT",
        "LU", "LV", "MT", "NL", "PL", "PT", "RO", "SE", "SI", "SK"]
AGENT = "eu27-smoke/1 (+https://github.com/pieteradejong/sovereign-data-centers)"


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):  # noqa: ANN002, ANN003
        return None


def request(url: str, method: str = "GET", follow: bool = True) -> tuple[int, dict[str, str], bytes]:
    opener = urllib.request.build_opener() if follow else urllib.request.build_opener(NoRedirect)
    req = urllib.request.Request(url, method=method, headers={"User-Agent": AGENT})
    try:
        with opener.open(req, timeout=30) as r:
            return r.status, {k.lower(): v for k, v in r.headers.items()}, r.read() if method == "GET" else b""
    except urllib.error.HTTPError as e:
        return e.code, {k.lower(): v for k, v in e.headers.items()}, b""
    except (urllib.error.URLError, OSError):     # unresolvable, refused, TLS failure: a failed check, not a crash
        return 0, {}, b""


def expected_headers() -> dict[str, str]:
    """The headers vercel.json sets on every path, lower-cased names."""
    conf = json.loads((ROOT / "vercel.json").read_text(encoding="utf-8"))
    rule = next(h for h in conf["headers"] if h["source"] == "/(.*)")
    return {h["key"].lower(): h["value"] for h in rule["headers"]}


def cert_days_left(host: str) -> float:
    ctx = ssl.create_default_context()
    with socket.create_connection((host, 443), timeout=30) as sock, ctx.wrap_socket(sock, server_hostname=host) as s:
        not_after = s.getpeercert()["notAfter"]
    end = dt.datetime.strptime(not_after, "%b %d %H:%M:%S %Y %Z").replace(tzinfo=dt.timezone.utc)
    return (end - dt.datetime.now(dt.timezone.utc)).total_seconds() / 86400


def run(site: str, bundle: Path | None, min_days: int) -> list[tuple[str, bool, str]]:
    import report  # noqa: PLC0415 -- the preview names are the build's own
    results: list[tuple[str, bool, str]] = []

    def check(name: str, ok: bool, detail: str = "") -> None:
        results.append((name, ok, detail))

    for path in ROUTES:
        code, h, _ = request(site + path)
        check(f"GET {path}", code == 200 and h.get("content-type", "").startswith("text/html"),
              f"{code} {h.get('content-type', '')}")
    for path, kind in ([("/eu27-report.pdf", "application/pdf")]
                       + [(f"/report/{iso}.pdf", "application/pdf") for iso in ISOS]
                       + [(f"/previews/report-{p}.png", "image/png") for p in report.PREVIEWS]):
        code, h, _ = request(site + path, method="HEAD")
        check(f"HEAD {path}", code == 200 and h.get("content-type", "").startswith(kind),
              f"{code} {h.get('content-type', '')}")

    code, headers, _ = request(site + "/", method="HEAD")
    for name, value in expected_headers().items():
        check(f"header {name}", headers.get(name) == value, headers.get(name, "(missing)"))
    code, _, body = request(site + "/robots.txt")
    check("robots.txt disallows indexing", "Disallow: /" in body.decode("utf-8", "replace").splitlines())

    host = urllib.parse.urlparse(site).hostname or ""
    if not host.startswith("www."):
        code, h, _ = request(f"https://www.{host}/", method="HEAD", follow=False)
        check("www redirects to the apex", code in (301, 308) and h.get("location", "").rstrip("/") == site.rstrip("/"),
              f"{code} {h.get('location', '')}")
    try:
        days = cert_days_left(host)
        check(f"TLS certificate valid for {min_days}+ days", days >= min_days, f"{days:.0f} days left")
    except (OSError, ssl.SSLError) as e:
        check(f"TLS certificate valid for {min_days}+ days", False, str(e))

    if bundle:
        want = hashlib.sha256(bundle.read_bytes()).hexdigest()
        got = ""
        for _ in range(6):                       # the edge may serve the previous deploy for a few seconds
            got = hashlib.sha256(request(site + "/data/eu27.json")[2]).hexdigest()
            if got == want:
                break
            time.sleep(10)
        check("served data bundle is the committed one", got == want, f"served {got[:16]}, committed {want[:16]}")
    return results


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--site", default="https://eu27.cloud")
    ap.add_argument("--bundle", type=Path, help="also require the served bundle to equal this file")
    ap.add_argument("--min-days", type=int, default=14, help="minimum days the TLS certificate must still be valid")
    ap.add_argument("--summary", type=Path, help="append a markdown table (e.g. $GITHUB_STEP_SUMMARY)")
    a = ap.parse_args(argv)
    results = run(a.site.rstrip("/"), a.bundle, a.min_days)
    failed = [r for r in results if not r[1]]
    for name, ok, detail in results:
        print(f"{'ok  ' if ok else 'FAIL'} {name}{f'  ({detail})' if detail and not ok else ''}")
    print(f"{len(results) - len(failed)} of {len(results)} smoke checks passed on {a.site}")
    if a.summary:
        with a.summary.open("a", encoding="utf-8") as fh:
            fh.write(f"### Smoke test: {len(results) - len(failed)} of {len(results)} passed\n\n")
            fh.write("| Check | Result |\n|---|---|\n")
            for name, ok, detail in results:
                fh.write(f"| {name} | {'ok' if ok else 'FAIL ' + detail} |\n")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
