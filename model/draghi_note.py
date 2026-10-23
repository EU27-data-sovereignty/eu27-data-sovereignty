#!/usr/bin/env python3
"""
DRAGHI-REPORT.md: the authored note's contract, its quote register and its archived source (#118).

    python3 model/draghi_note.py check     # the contract, offline and without the PDFs; exit 1 on any problem
    python3 model/draghi_note.py fetch     # download both parts into assets/reports/draghi-2024/ and verify the manifest
    python3 model/draghi_note.py quotes    # regenerate docs/draghi-quotes.csv from the note's citations, each re-found in its PDF page
    python3 model/draghi_note.py links     # refetch every URL into docs/draghi-report-links.csv (network)

The note reads Mario Draghi's *The future of European competitiveness* (European Commission, September 2024)
against this project's per-state registers. The report is EU-level and names few member states, so most of a
state's entry is the author's analysis. The contract keeps the two kinds of statement apart and checkable:

- what Draghi says is a verbatim quotation followed by its PDF page, `"…" (A p. 36)` or `(B p. 84)`, and
  every quotation is a row of the committed quote register, found on that page of the hashed PDF by `quotes`;
- what the project knows about a state is a claim id the state's own document prints (`indicator:NL:C2`,
  `record:NL:tax:hosting`), resolved against the committed bundle, never a value restated without one;
- one entry per member state, alphabetical by English name, with the fixed subsections;
- no ranking language outside quotations, no currency figure in a state entry, and none elsewhere outside a
  quotation (#10, #72, #77);
- every URL in the committed link register, and nothing in the model, the book, the web app, the reader or
  `/ask` names the note.

The PDFs are gitignored (`assets/reports/**/*.pdf`); `assets/reports/MANIFEST.csv` carries their sha256, so the
gate checks the register offline and `fetch` plus `quotes` re-prove it from the published files.
"""
from __future__ import annotations

import csv
import datetime as dt
import hashlib
import json
import re
import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "model"))

from national_ai_note import RANK, load_links, urls, write_links  # noqa: E402

NOTE = ROOT / "DRAGHI-REPORT.md"
LINKS = ROOT / "docs" / "draghi-report-links.csv"
QUOTES = ROOT / "docs" / "draghi-quotes.csv"
MANIFEST = ROOT / "assets" / "reports" / "MANIFEST.csv"
BUNDLE = ROOT / "web" / "public" / "data" / "eu27.json"
DECISION = "#118"

# A citation's page is the page of the PDF file, which a reader and `pdftotext -f N` find the same way. Part B's
# printed folios match it; Part A's run two lower (the cover and the colophon carry none), so "A p. 36" is folio 34.
PARTS = {
    "A": {"file": "assets/reports/draghi-2024/part-a-competitiveness-strategy.pdf", "offset": 0},
    "B": {"file": "assets/reports/draghi-2024/part-b-in-depth-analysis.pdf", "offset": 0},
}

STATES = {
    "AT": "Austria", "BE": "Belgium", "BG": "Bulgaria", "HR": "Croatia", "CY": "Cyprus", "CZ": "Czechia",
    "DK": "Denmark", "EE": "Estonia", "FI": "Finland", "FR": "France", "DE": "Germany", "EL": "Greece",
    "HU": "Hungary", "IE": "Ireland", "IT": "Italy", "LV": "Latvia", "LT": "Lithuania", "LU": "Luxembourg",
    "MT": "Malta", "NL": "Netherlands", "PL": "Poland", "PT": "Portugal", "RO": "Romania", "SK": "Slovakia",
    "SI": "Slovenia", "ES": "Spain", "SE": "Sweden",
}

STATES_HEADING = "## 4. The twenty-seven"
CAVEATS_HEADING = "## 5. Caveats"
SECTIONS = ("## 1. The report", "## 2. What it says about hosting state data", "## 3. What it means for this project",
            STATES_HEADING, CAVEATS_HEADING)
SUBSECTIONS = (
    "#### Where Draghi names it",
    "#### Proposals that land on its holdings",
    "#### What the project prints today",
    "#### Open questions",
)
NONE_NAMED = re.compile(r"^none: searched both parts \d{4}-\d{2}-\d{2}\b", re.M)

HEADER_WORDING = "Authored note"
HEADER_NOT_GENERATED = "Not generated"
RANK_ALLOWED = ("It ranks nothing.",)

# A quotation and its page: “…” (A p. 36). Straight or curly double quotes; the page is the PDF page (see PARTS).
CITED = re.compile(r"[“\"]([^”\"]{8,})[”\"]\s*\((A|B) p\. (\d{1,3})\)")
PAGE_REF = re.compile(r"\((A|B) p\. (\d{1,3})\)")
QUOTED = re.compile(r"“[^”]*”|\"[^\"\n]*\"")
CLAIM = re.compile(r"`((?:indicator|record|param):([A-Z]{2}):[A-Za-z0-9_:]+)`")
# A claim and the words it prints: `record:AT:civil_registry:operator` reads “Federal Minister of the Interior”.
READS = re.compile(r"`((?:indicator|record|param):[A-Z]{2}:[A-Za-z0-9_:]+)`\s+reads\s+“([^”]+)”")
MONEY = re.compile(r"€\s?\d|\b\d[\d.,]*\s?(million|billion|trillion|bn)\b|\b(EUR|USD)\s?\d", re.I)

RENDERERS = ["model/document.py", "model/export_json.py", "model/generate_countries.py", "model/ask_corpus.py",
             "book", "web/src", "api", "mobile/src"]


def text() -> str:
    return NOTE.read_text(encoding="utf-8")


def norm(s: str) -> str:
    """The form quotes are compared in: one space for any run of whitespace, typographic quotes kept."""
    return re.sub(r"\s+", " ", s).strip()


def load_quotes(path: Path = QUOTES) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def load_manifest(path: Path = MANIFEST) -> dict[str, dict[str, str]]:
    if not path.exists():
        return {}
    with path.open(newline="", encoding="utf-8") as fh:
        return {r["path"]: r for r in csv.DictReader(fh)}


def load_claims(path: Path = BUNDLE) -> dict[str, list[str]]:
    """Every claim the committed bundle prints as a fact, with the text it prints. A withheld (disputed) or gap span
    is not a fact, so a state entry can cite only what a reader of that state's document actually sees."""
    if not path.exists():
        return {}
    out: dict[str, set[str]] = {}

    def walk(x):
        if isinstance(x, dict):
            if x.get("role") == "fact":
                for c in x.get("c") or []:
                    out.setdefault(c, set()).add(x["t"])
            for v in x.values():
                walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)
    walk(json.loads(path.read_text(encoding="utf-8")).get("documents", {}))
    return {k: sorted(v) for k, v in out.items()}


def section(body: str, start: str, end: str | None) -> str:
    if start not in body:
        return ""
    i = body.index(start)
    j = body.find(end, i + 1) if end else -1
    return body[i: j if j != -1 else None]


def entries(body: str) -> list[dict]:
    part = section(body, STATES_HEADING, CAVEATS_HEADING)
    heads = list(re.finditer(r"^### (.+?) \(([A-Z]{2})\)$", part, re.M))
    out = []
    for n, h in enumerate(heads):
        chunk = part[h.start(): heads[n + 1].start() if n + 1 < len(heads) else len(part)]
        subs = {}
        for k, name in enumerate(SUBSECTIONS):
            if name in chunk:
                i = chunk.index(name)
                later = [chunk.index(s) for s in SUBSECTIONS[k + 1:] if s in chunk]
                subs[name] = chunk[i: min(later) if later else len(chunk)]
        out.append({"name": h.group(1), "iso": h.group(2), "text": chunk, "subsections": subs})
    return out


def problems(body: str | None = None, quotes: list[dict] | None = None, claims: dict[str, list[str]] | None = None,
             links: dict | None = None) -> list[str]:
    body = body if body is not None else text()
    quotes = quotes if quotes is not None else load_quotes()
    claims = claims if claims is not None else load_claims()
    links = links if links is not None else load_links(LINKS)
    out: list[str] = []

    head = body.split("---", 1)[0]
    if HEADER_WORDING not in head or HEADER_NOT_GENERATED not in head or DECISION not in head:
        out.append(f"header: must say it is an authored note, not generated, and cite {DECISION}")
    for h in SECTIONS:
        if h not in body:
            out.append(f"missing section: {h}")
    if out:
        return out

    # Quotations: every one is a register row on that page, found in the hashed PDF.
    register = {(r["part"], r["page"], norm(r["quote"])): r for r in quotes}
    pages = {(r["part"], r["page"]) for r in quotes}
    cited_keys = set()
    for m in CITED.finditer(body):
        key = (m.group(2), m.group(3), norm(m.group(1)))
        cited_keys.add(key)
        row = register.get(key)
        if row is None:
            out.append(f"quotation not in {QUOTES.name}: ({key[0]} p. {key[1]}) {key[2][:60]}")
        elif row.get("found") != "yes":
            out.append(f"quotation not found on its page at the last `quotes` run: ({key[0]} p. {key[1]}) {key[2][:60]}")
    # A long quotation is either Draghi's, with its page, or a claim's printed text; a short one is a term.
    anchored = {m.start(1) for m in CITED.finditer(body)} | {m.start(2) for m in READS.finditer(body)}
    for m in re.finditer(r"“([^”]{40,})”", body):
        if m.start(1) not in anchored:
            out.append(f"quotation with neither a page nor a claim id: “{m.group(1)[:60]}…”")
    for m in PAGE_REF.finditer(body):
        if (m.group(1), m.group(2)) not in pages:
            out.append(f"page reference ({m.group(1)} p. {m.group(2)}) has no quotation in the register")
    unused = [k for k in register if k not in cited_keys]
    if unused:
        out.append(f"{len(unused)} register rows are quoted nowhere in the note: {[f'{k[0]} p. {k[1]}' for k in unused[:3]]}")

    # States: all 27, once, alphabetical by English name, each with the fixed subsections.
    ents = entries(body)
    want = sorted(STATES, key=lambda i: STATES[i])
    got = [e["iso"] for e in ents]
    if got != want:
        out.append(f"section 4 must hold the 27 states in English-name order: got {got}")
    for e in ents:
        tag = e["iso"]
        if STATES.get(tag) != e["name"]:
            out.append(f"{tag}: heading says {e['name']!r}, want {STATES.get(tag)!r}")
        for s in SUBSECTIONS:
            if s not in e["subsections"]:
                out.append(f"{tag}: missing subsection {s!r}")
        named = e["subsections"].get(SUBSECTIONS[0], "")
        if not CITED.search(named) and not NONE_NAMED.search(named):
            out.append(f"{tag}: 'Where Draghi names it' holds neither a cited quotation nor 'none: searched both parts <date>'")
        if not CLAIM.search(e["subsections"].get(SUBSECTIONS[2], "")):
            out.append(f"{tag}: 'What the project prints today' cites no claim id")
        for claim, iso in CLAIM.findall(e["text"]):
            if iso != tag:
                out.append(f"{tag}: cites {claim}, another state's claim")
            elif claim not in claims:
                out.append(f"{tag}: cites {claim}, which the committed bundle does not print as a fact")
        for claim, said in READS.findall(e["text"]):
            if claim in claims and not any(norm(said) in norm(t) for t in claims[claim]):
                out.append(f"{tag}: {claim} reads {said[:50]!r} here, but the bundle prints {claims[claim][0][:50]!r}")
        for m in MONEY.finditer(e["text"]):
            out.append(f"{tag}: currency figure {m.group(0)!r}; a state entry carries none (#72)")

    # Outside the entries, a currency figure only inside a quotation.
    rest = body.replace(section(body, STATES_HEADING, CAVEATS_HEADING), "")
    for line in rest.splitlines():
        for m in MONEY.finditer(QUOTED.sub("", line)):
            out.append(f"currency figure outside a quotation: {m.group(0)!r} in: {line.strip()[:80]}")

    # Ranking language, outside quotations and the one sentence that says it ranks nothing.
    scrubbed = QUOTED.sub("", body)
    for allowed in RANK_ALLOWED:
        scrubbed = scrubbed.replace(allowed, "")
    for line in scrubbed.splitlines():
        if line.startswith("- ["):
            continue
        for m in RANK.finditer(line):
            out.append(f"ranking language: {m.group(0)!r} in: {line.strip()[:80]}")

    # URLs: every one registered, and a URL that did not answer sits on a line marked [unverified].
    note_urls = set(urls(body))
    missing = sorted(note_urls - set(links))
    if missing:
        out.append(f"{len(missing)} URLs not in {LINKS.name} (run `links`): {missing[:3]}")
    stale = sorted(set(links) - note_urls)
    if stale:
        out.append(f"{len(stale)} register rows no longer in the note (run `links`): {stale[:3]}")
    for u, r in links.items():
        if u in note_urls and not str(r.get("status", "")).startswith(("2", "3")):
            line = next((ln for ln in body.splitlines() if u in ln), "")
            if "**[unverified]**" not in line:
                out.append(f"{u} answered {r.get('status')} at the last link check and its line is not marked **[unverified]**")

    # The archived source: both parts in the manifest, and the register's hashes are the manifest's.
    manifest = load_manifest()
    for part, spec in PARTS.items():
        row = manifest.get(spec["file"])
        if row is None:
            out.append(f"{MANIFEST.name}: no row for {spec['file']}")
            continue
        for q in quotes:
            if q["part"] == part and q.get("pdf_sha256") != row["sha256"]:
                out.append(f"{QUOTES.name}: a part {part} row was checked against another file than the manifest's")
                break

    # Rendered nowhere.
    for rel in RENDERERS:
        p = ROOT / rel
        files = [p] if p.is_file() else [f for f in p.rglob("*") if f.suffix in {".py", ".ts", ".tsx", ".typ"}] if p.exists() else []
        for f in files:
            try:
                if "DRAGHI-REPORT" in f.read_text(encoding="utf-8"):
                    out.append(f"{f.relative_to(ROOT)} names the note; it is never rendered")
            except (UnicodeDecodeError, OSError):
                continue
    return out


def check() -> int:
    body = text() if NOTE.exists() else ""
    if not body:
        print("DRAGHI-REPORT.md: missing, 1 problems")
        return 1
    found = problems(body)
    quotes = load_quotes()
    status, more = reprove(quotes)
    found += more
    ents = entries(body)
    named = sum(1 for e in ents if CITED.search(e["subsections"].get(SUBSECTIONS[0], "")))
    n_claims = len({c for e in ents for c, _ in CLAIM.findall(e["text"])})
    print(f"{len(ents)} states ({named} named by the report), {len(quotes)} quotations ({status}), "
          f"{n_claims} claim ids, {len(urls(body))} URLs, {len(found)} problems")
    for p in found:
        print("  " + p)
    return 1 if found else 0


def reprove(rows: list[dict]) -> tuple[str, list[str]]:
    """Where the PDFs are on disk (a local clone after `fetch`), re-find every quotation on its page, read-only.
    Where they are not (CI), say so in the headline: the register's own `found` column is all that was checked."""
    missing = [s["file"] for s in PARTS.values() if not (ROOT / s["file"]).exists()]
    if missing or shutil.which("pdftotext") is None:
        why = "no PDF here; run `fetch`" if missing else "no pdftotext here"
        return f"re-proving SKIPPED ({why}), {sum(1 for q in rows if q.get('found') == 'yes')} found at the last `quotes` run", []
    manifest = load_manifest()
    out = []
    for part, spec in PARTS.items():
        if sha256(ROOT / spec["file"]) != manifest.get(spec["file"], {}).get("sha256"):
            out.append(f"{spec['file']} on disk does not match {MANIFEST.name}")
    if out:
        return "re-proving refused: a PDF differs from the manifest", out
    cache: dict[tuple[str, int], str] = {}
    for r in rows:
        key = (r["part"], int(r["page"]))
        if key not in cache:
            cache[key] = norm(page_text(*key))
        if norm(r["quote"]) not in cache[key]:
            out.append(f"quotation not on its page in the hashed PDF: ({key[0]} p. {key[1]}) {r['quote'][:60]}")
    return f"{len(rows) - len(out)} re-found in the hashed PDFs", out


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def fetch() -> int:
    """Download any part that is missing, then verify every part against the manifest."""
    bad = 0
    for path, row in load_manifest().items():
        dest = ROOT / path
        if not dest.exists():
            dest.parent.mkdir(parents=True, exist_ok=True)
            req = urllib.request.Request(row["url"], headers={"User-Agent": "eu27-data-sovereignty (research)"})
            with urllib.request.urlopen(req, timeout=120) as r, dest.open("wb") as fh:
                shutil.copyfileobj(r, fh)
        got = sha256(dest)
        ok = got == row["sha256"] and dest.stat().st_size == int(row["bytes"])
        bad += not ok
        print(f"{'ok  ' if ok else 'DIFF'} {path} {got[:16]}… {dest.stat().st_size} bytes")
    return 1 if bad else 0


def page_text(part: str, printed: int) -> str:
    spec = PARTS[part]
    pdf = str(ROOT / spec["file"])
    n = printed + spec["offset"]
    r = subprocess.run(["pdftotext", "-f", str(n), "-l", str(n), pdf, "-"], capture_output=True, text=True, check=True)
    return r.stdout


def quotes() -> int:
    """Re-prove every register row against the hashed PDF: the manifest hash first, then the quote on its page."""
    if shutil.which("pdftotext") is None:
        print("pdftotext is not installed (brew install poppler)")
        return 2
    manifest = load_manifest()
    hashes = {}
    for part, spec in PARTS.items():
        f = ROOT / spec["file"]
        if not f.exists():
            print(f"{spec['file']} is missing; run `fetch`")
            return 2
        hashes[part] = sha256(f)
        if hashes[part] != manifest.get(spec["file"], {}).get("sha256"):
            print(f"{spec['file']} does not match {MANIFEST.name}")
            return 1
    # The register is generated: one row per quotation the note cites, nothing kept by hand.
    rows = list({(m.group(2), m.group(3), norm(m.group(1))): {"part": m.group(2), "page": m.group(3), "quote": norm(m.group(1))}
                 for m in CITED.finditer(text())}.values())
    today = dt.date.today().isoformat()
    cache: dict[tuple[str, int], str] = {}
    for r in rows:
        key = (r["part"], int(r["page"]))
        if key not in cache:
            cache[key] = norm(page_text(*key))
        r["found"] = "yes" if norm(r["quote"]) in cache[key] else "no"
        r["pdf_sha256"] = hashes[r["part"]]
        r["checked"] = today
    rows.sort(key=lambda r: (r["part"], int(r["page"]), r["quote"]))
    with QUOTES.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["part", "page", "quote", "found", "pdf_sha256", "checked"], lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    missing = [r for r in rows if r["found"] != "yes"]
    for r in missing:
        print(f"not found: ({r['part']} p. {r['page']}) {r['quote'][:70]}")
    print(f"{len(rows)} quotations, {len(rows) - len(missing)} found on their page -> {QUOTES.relative_to(ROOT)}")
    return 1 if missing else 0


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "check"
    if cmd == "check":
        sys.exit(check())
    elif cmd == "fetch":
        sys.exit(fetch())
    elif cmd == "quotes":
        sys.exit(quotes())
    elif cmd == "links":
        sys.exit(write_links(NOTE, LINKS))
    else:
        print(__doc__)
        sys.exit(2)
