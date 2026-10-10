#!/usr/bin/env python3
"""
The contract of `NATIONAL-AI-STRATEGIES.md`, the authored note on a citizen-grade foundation model per state (#101).

The note is prose, so the gate cannot check its facts the way it checks the model's. What it can check, and
`tests/test_national_ai.py` does through this module:

- the header carries the authored-note wording and cites #101;
- section 5 holds exactly one entry per member state, alphabetical by English name, each with the fixed
  subsections and the eleven snapshot rows;
- every snapshot cell has a source (a URL with an access date) or is marked **[unverified]**;
- every URL in the note is in the committed link register `docs/national-ai-strategies-links.csv`, and a URL
  that did not answer (no 2xx or 3xx) sits on a line marked **[unverified]**;
- no ranking language outside the two sentences that say it ranks nothing (#10, #77);
- no currency figure outside the snapshot and sources of an entry, and reconstructed bands only in section 2 (#72);
- the route groups in section 6 list every state once, alphabetical inside a group;
- nothing in the model, the book, the web app or `/ask` reads the note.

    python3 model/national_ai_note.py check          # the summary the gate prints; exit 1 on any failure
    python3 model/national_ai_note.py links          # fetch every URL once and rewrite the link register (network)
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import re
import ssl
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NOTE = ROOT / "NATIONAL-AI-STRATEGIES.md"
LINKS = ROOT / "docs" / "national-ai-strategies-links.csv"
PARAMS = ROOT / "model" / "eu27_parameters.csv"
DECISION = "#101"

UNVERIFIED = "**[unverified]**"
RECONSTRUCTED = "**[reconstructed]**"

HEADER_WORDING = "Authored note"
HEADER_NOT_GENERATED = "Not generated"

STATES_HEADING = "## 5. The twenty-seven"
ACROSS_HEADING = "## 6. Across the EU-27"
ROUTES_HEADING = "## 2. The routes"
BLOCKS_HEADING = "## 3. The building blocks"
CAVEATS_HEADING = "## 7. Caveats"

STATE_SUBSECTIONS = (
    "#### Snapshot",
    "#### What good enough means here",
    "#### Recommended strategy",
    "#### What it does not need to do",
    "#### Main blocker, and what would change the recommendation",
    "#### Sources",
)
SNAPSHOT_FIELDS = (
    "Official and recognised languages",
    "Language shared with",
    "EuroHPC system on national soil",
    "EuroHPC AI Factory",
    "AI Gigafactory",
    "National or regional model efforts",
    "National AI strategy",
    "Public-sector LLM use",
    "Language resources",
    "Key institutions",
    "Power and grid",
)
# Subsections of an entry that must carry no figure in euro: the strategy is analysis, never a cost (#72).
NO_MONEY_SUBSECTIONS = STATE_SUBSECTIONS[1:5]
MONEY = re.compile(r"€\s?\d|\b\d[\d.,]*\s?(million|billion|bn|m)\b\s?(euro|EUR|€)|\bEUR\s?\d", re.I)

# Ranking language. The two sentences that say the note ranks nothing are allowed; nothing else is.
RANK = re.compile(r"\b(rank|ranked|ranking|ranks|ahead of|outperform\w*|leads the EU|the best in (the )?Europe|"
                  r"top (three|five|ten|\d+))\b", re.I)
RANK_ALLOWED = (
    "It ranks nothing.",
    "The groups below are a recommendation and not a ranking",
    "never ranked",
    "the project no longer ranks",
)

URL = re.compile(r"https?://[^\s<>()\[\]\"'`]+")
ACCESSED = re.compile(r"accessed (\d{4}-\d{2}-\d{2})")
H3 = re.compile(r"^### (.+?) \(([A-Z]{2})\)\s*$", re.M)

UA = "eu27-linkcheck/1 (+https://github.com/EU27-data-sovereignty/eu27-data-sovereignty)"


# --------------------------------------------------------------------------- #
# Parsing
# --------------------------------------------------------------------------- #

def states() -> dict[str, str]:
    """ISO-2 -> English name, from the parameters file, so the note and the model agree on the 27."""
    with PARAMS.open(newline="", encoding="utf-8") as fh:
        return {r["iso2"]: r["country"] for r in csv.DictReader(fh)}


def text() -> str:
    return NOTE.read_text(encoding="utf-8")


def section(body: str, start: str, end: str | None) -> str:
    i = body.index(start)
    j = body.index(end, i) if end else len(body)
    return body[i:j]


def urls(body: str) -> list[str]:
    return sorted({m.rstrip(").,;:'\"*") for m in URL.findall(body)})


def entries(body: str) -> list[dict]:
    """The per-state entries of section 5, in order of appearance."""
    part = section(body, STATES_HEADING, ACROSS_HEADING)
    heads = list(H3.finditer(part))
    out = []
    for n, h in enumerate(heads):
        end = heads[n + 1].start() if n + 1 < len(heads) else len(part)
        chunk = part[h.start():end]
        subs = {}
        for k, name in enumerate(STATE_SUBSECTIONS):
            if name not in chunk:
                continue
            i = chunk.index(name)
            nxt = [chunk.index(s, i + 1) for s in STATE_SUBSECTIONS[k + 1:] if s in chunk[i + 1:]]
            subs[name] = chunk[i:min(nxt) if nxt else len(chunk)]
        out.append({"name": h.group(1), "iso": h.group(2), "text": chunk, "subsections": subs})
    return out


def snapshot_rows(snapshot: str) -> list[list[str]]:
    rows = []
    for line in snapshot.splitlines():
        if line.startswith("|") and not line.startswith("|---") and not line.startswith("| Field"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 3:
                rows.append(cells)
    return rows


def route_groups(body: str) -> dict[str, list[str]]:
    """Section 6's route-group table: route label -> the ISO codes listed, in the order written."""
    part = section(body, ACROSS_HEADING, CAVEATS_HEADING)
    out: dict[str, list[str]] = {}
    for line in part.splitlines():
        if line.startswith("| R") and "|" in line[2:]:
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            out[cells[0]] = re.findall(r"\(([A-Z]{2})\)", cells[1])
    return out


def load_links() -> dict[str, dict[str, str]]:
    if not LINKS.exists():
        return {}
    with LINKS.open(newline="", encoding="utf-8") as fh:
        return {r["url"]: r for r in csv.DictReader(fh)}


# --------------------------------------------------------------------------- #
# The checks
# --------------------------------------------------------------------------- #

def problems(body: str | None = None) -> list[str]:
    body = body if body is not None else text()
    names = states()
    out: list[str] = []
    head = body.split("---", 1)[0]
    if HEADER_WORDING not in head or HEADER_NOT_GENERATED not in head or DECISION not in head:
        out.append("header: must say it is an authored note, not generated, and cite " + DECISION)
    for h in (ROUTES_HEADING, BLOCKS_HEADING, STATES_HEADING, ACROSS_HEADING, CAVEATS_HEADING):
        if h not in body:
            out.append(f"missing section: {h}")
    if out:
        return out

    ents = entries(body)
    seen = [e["iso"] for e in ents]
    if sorted(seen) != sorted(names):
        out.append(f"section 5 must hold exactly the 27 states once each; has {len(seen)}: "
                   f"missing {sorted(set(names) - set(seen))}, extra {sorted(set(seen) - set(names))}")
    expected = [iso for iso, _ in sorted(names.items(), key=lambda kv: kv[1])]
    if seen != expected:
        out.append("section 5 entries must be alphabetical by English name")
    links = load_links()
    for e in ents:
        tag = f"{e['iso']} ({e['name']})"
        if e["name"] != names.get(e["iso"]):
            out.append(f"{tag}: heading name must be the English name in eu27_parameters.csv")
        for s in STATE_SUBSECTIONS:
            if s not in e["subsections"]:
                out.append(f"{tag}: missing subsection {s}")
        snap = e["subsections"].get("#### Snapshot", "")
        rows = snapshot_rows(snap)
        labels = [r[0].strip("*") for r in rows]
        for f in SNAPSHOT_FIELDS:
            if not any(lbl.startswith(f) for lbl in labels):
                out.append(f"{tag}: snapshot lacks the row '{f}'")
        for r in rows:
            src = r[2]
            if not (URL.search(src) and ACCESSED.search(src)) and UNVERIFIED not in r[1] + src:
                out.append(f"{tag}: snapshot row '{r[0][:40]}' has neither a URL with an access date nor {UNVERIFIED}")
        for s in NO_MONEY_SUBSECTIONS:
            if MONEY.search(e["subsections"].get(s, "")):
                out.append(f"{tag}: a currency figure in {s}; strategies carry no cost (#72)")
        if RECONSTRUCTED in e["text"]:
            out.append(f"{tag}: {RECONSTRUCTED} belongs only in section 2's band table")
        srcs = e["subsections"].get("#### Sources", "")
        if len(urls(srcs)) < 3:
            out.append(f"{tag}: fewer than three sources")

    # Ranking language, anywhere, except the sentences that say it ranks nothing.
    scrubbed = body
    for allowed in RANK_ALLOWED:
        scrubbed = scrubbed.replace(allowed, "")
    for m in RANK.finditer(scrubbed):
        line = scrubbed[max(0, scrubbed.rfind("\n", 0, m.start())) + 1:scrubbed.find("\n", m.end())]
        if line.startswith("- [") or "FEASIBILITY-RANKING" in line or "ranking by published rule" in line:
            continue  # the contents list, and references to the superseded note or to #77 by name
        out.append(f"ranking language: '{m.group(0)}' in: {line.strip()[:100]}")

    # Reconstructed bands only in section 2 (the header may name the mark; entries are checked above).
    outside = body.replace(section(body, ROUTES_HEADING, BLOCKS_HEADING), "").split("---", 1)[1]
    if RECONSTRUCTED in outside:
        out.append(f"{RECONSTRUCTED} appears outside section 2's band table")
    # Every URL registered; non-200 ones marked unverified on their line.
    all_urls = urls(body)
    for u in all_urls:
        row = links.get(u)
        if row is None:
            out.append(f"link register: {u} is not in {LINKS.name}; run ./run.sh national-ai links")
            continue
        if not answered(row["status"]):
            lines = [ln for ln in body.splitlines() if u in ln]
            if not all(UNVERIFIED in ln for ln in lines):
                out.append(f"link register: {u} answered {row['status']} but its line is not marked {UNVERIFIED}")
    for u in links:
        if u not in all_urls:
            out.append(f"link register: {u} is registered but no longer cited; run ./run.sh national-ai links")

    # Route groups: every state once, alphabetical within a group.
    groups = route_groups(body)
    listed = [iso for g in groups.values() for iso in g]
    if sorted(listed) != sorted(names):
        out.append(f"section 6 route groups must list every state once; listed {len(listed)}")
    for g, isos in groups.items():
        if isos != sorted(isos, key=lambda i: names.get(i, i)):
            out.append(f"section 6 group '{g}' is not alphabetical by English name; order carries no meaning")

    # Never rendered.
    skip = {"node_modules", ".venv", "dist", "build", "__pycache__", "research"}
    for d in ("model", "book", "api", "web/src", "mobile"):
        for p in (ROOT / d).rglob("*"):
            if skip & set(p.relative_to(ROOT).parts):
                continue
            if p.is_file() and p.suffix in (".py", ".ts", ".tsx", ".typ") and p.name != Path(__file__).name:
                if NOTE.name in p.read_text(encoding="utf-8", errors="ignore"):
                    out.append(f"{p.relative_to(ROOT)} reads the note; it is never rendered (#101)")
    return out


def summary(body: str | None = None) -> dict[str, int]:
    body = body if body is not None else text()
    ents = entries(body)
    links = load_links()
    return {
        "states": len(ents),
        "urls": len(urls(body)),
        "urls_answered": sum(1 for u in urls(body) if answered(links.get(u, {}).get("status", "0"))),
        "unverified_marks": body.count(UNVERIFIED),
        "words": len(body.split()),
    }


# --------------------------------------------------------------------------- #
# The link register
# --------------------------------------------------------------------------- #

def answered(status: str) -> bool:
    """A page that answered 2xx or 3xx is reachable: EUR-Lex answers 202 to a first request and some hosts
    answer a 308 the stdlib opener does not follow. Only 4xx, 5xx and a transport error count as not answered."""
    return status[:1] in ("2", "3")


def ascii_url(u: str) -> str:
    """Percent-encode the non-ASCII characters of an IRI so the stdlib opener accepts it."""
    from urllib.parse import quote  # noqa: PLC0415
    return quote(u, safe=":/?#[]@!$&'()*+,;=%")


def probe(u: str) -> tuple[str, str, str]:
    """One request per URL, the project's user agent first; a 403 is retried once with a plain user agent,
    because some official sites refuse any agent that names itself. The status recorded is the last answer."""
    ctx = ssl.create_default_context()
    target = ascii_url(u)
    agents = [UA, "curl/8.7.1"]
    status, err = "0", "unreachable"
    for agent in agents:
        for attempt in range(2):
            try:
                req = urllib.request.Request(target, headers={"User-Agent": agent, "Accept": "*/*"})
                with urllib.request.urlopen(req, timeout=25, context=ctx) as r:
                    return u, str(r.status), ""
            except urllib.error.HTTPError as e:
                status, err = str(e.code), ""
                if e.code in (429, 503) and attempt == 0:
                    time.sleep(3)
                    continue
                break
            except Exception as e:  # noqa: BLE001
                status, err = "0", type(e).__name__
                if attempt == 0:
                    time.sleep(2)
                    continue
                break
        if status != "403":
            break
    if status == "0":
        # A transport error in the stdlib opener (the system Python's TLS stack rejects some hosts' handshakes)
        # is tried once more through curl. The answer is recorded like any other.
        import subprocess  # noqa: PLC0415
        try:
            out = subprocess.run(["curl", "-sS", "-o", "/dev/null", "-L", "--max-time", "25", "-A", UA,
                                  "-w", "%{http_code}", target], capture_output=True, text=True, timeout=40)
            code = out.stdout.strip()[-3:]
            if code.isdigit() and code != "000":
                return u, code, "curl"
        except Exception:  # noqa: BLE001
            pass
    return u, status, err


def write_links() -> int:
    """Fetch every URL in the note once and rewrite the register. Polite: six at a time, one request each."""
    today = dt.date.today().isoformat()
    todo = urls(text())
    with ThreadPoolExecutor(max_workers=6) as ex:
        results = sorted(ex.map(probe, todo))
    LINKS.parent.mkdir(exist_ok=True)
    with LINKS.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, lineterminator="\n")
        w.writerow(["url", "status", "error", "checked"])
        for u, status, err in results:
            w.writerow([u, status, err, today])
    bad = [r for r in results if not answered(r[1])]
    for u, status, err in bad:
        print(f"{status:>3} {err:<20} {u}")
    print(f"{len(results)} URLs, {len(results) - len(bad)} answered, {len(bad)} did not -> {LINKS.relative_to(ROOT)}")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["check", "links"])
    args = ap.parse_args(argv)
    if args.command == "links":
        return write_links()
    errs = problems()
    s = summary()
    for e in errs:
        print(f"  ❌ {e}", file=sys.stderr)
    print(f"NATIONAL-AI-STRATEGIES.md: {s['states']} states, {s['urls']} URLs ({s['urls_answered']} answered "
          f"at the last link check), {s['unverified_marks']} unverified marks, {s['words']:,} words, {len(errs)} problems")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
