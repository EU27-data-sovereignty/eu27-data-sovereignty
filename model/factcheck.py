#!/usr/bin/env python3
"""
Every printed fact checked by a second model, the one that did not write it, before it ships (#87).

    python3 model/factcheck.py prepare [--all] [--size 30]   # facts due -> cache/factcheck/<run>/
    python3 model/factcheck.py stage <workflow-output> --run <id> --prepared <run>
    python3 model/factcheck.py record --run <id> --output <workflow-output> [--agents N --tokens N --duration T]
    python3 model/factcheck.py audit [--check]                # regenerate docs/fact-check-audit.md
    python3 model/factcheck.py status                         # what the gate would say
    python3 model/factcheck.py gate                           # exit 1 unless every printed fact passes

Why this file exists
--------------------
Before this, a fact was found by one model and reviewed blind by the same model, so the two readings
could share its blind spots (#83). Now every fact the build prints is put, as printed, to a checker that
is a *different* model from its author: Fable 5.1 when Opus 5.5 wrote it, Opus 5.5 when Fable 5.1 did,
and Fable 5.1 when the author was never recorded (every fact admitted before this decision).

A verdict holds for one fact *as printed*: `fact_sha256` hashes the claim, the question it answers, the
printed text and every citation behind it. Change any of that and the verdict lapses, so a push re-checks
only what changed while the gate still demands a current, agreeing verdict for every printed fact.

The checker's answer is not trusted about itself. The workflow asks for a model by name and the checker
reports the model it is; `stage` refuses a batch where the two differ, or where the checker is an
author. A fact the checker does not confirm is withheld as disputed by the content model (#89), with the
checker's reason; nothing here edits a register or a verdict to make the gate pass.

This is a check by a second machine, not by a person. Every output says so (evidence.DISCLAIMER).
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "model"))
sys.path.insert(0, str(ROOT / "model" / "research" / "vetting"))
import build_input  # noqa: E402
import document  # noqa: E402
import evidence  # noqa: E402

BUNDLE = ROOT / "web" / "public" / "data" / "eu27.json"
DIR = ROOT / "model" / "research" / "factcheck"
WORKFLOW = DIR / "workflow.js"
LEDGER = DIR / "ledger.csv"
STAGED = DIR / "staged"
MANIFESTS = DIR / "runs"
CACHE = ROOT / "cache" / "factcheck"
AUDIT = ROOT / "docs" / "fact-check-audit.md"
VETTING = ROOT / "model" / "research" / "vetting"
EUROSTAT_API = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data"

LFIELDS = ["claim", "fact_sha256", "author_model", "checker_model", "verdict", "reason", "checked_url", "run",
           "checked"]
# The two checkers, by the alias the workflow asks for and the id the model reports. Order matters:
# the first is the checker when no author is recorded.
CHECKERS = {"fable": "claude-fable-5-1", "opus": "claude-opus-5-5"}
ALIAS = {v: k for k, v in CHECKERS.items()}
UNRECORDED = "unrecorded"
VERDICTS = ("supported", "not_supported", "unclear")
RULE = [
    ("claude-opus-5-5", "claude-fable-5-1"),
    ("claude-fable-5-1", "claude-opus-5-5"),
    ("anything else: unrecorded, a person, or a program", "claude-fable-5-1"),
]


# --------------------------------------------------------------------------- #
# the rule
# --------------------------------------------------------------------------- #

def checker_for(authors: set[str]) -> str:
    """The checker for a fact: the first of the two checker models that wrote none of it, or ''
    when both did (then no checker is eligible and the fact cannot pass)."""
    return next((m for m in CHECKERS.values() if m not in authors), "")


def ineligible(checker: str, authors: set[str]) -> str:
    """'' if this checker's verdict can count for a fact with these authors, else the reason."""
    if checker not in CHECKERS.values():
        return f"checker {checker or '(none)'} is not one of {', '.join(CHECKERS.values())}"
    if checker in authors:
        return f"checker {checker} wrote this fact"
    return ""


def split_authors(field: str) -> set[str]:
    return {a for a in field.split(";") if a}


# --------------------------------------------------------------------------- #
# the facts, as printed
# --------------------------------------------------------------------------- #

def load_bundle() -> dict:
    return json.loads(BUNDLE.read_text(encoding="utf-8"))


def eurostat_url(locator: str) -> str:
    """The API request for exactly one printed Eurostat value, from its locator
    ("nrg_pc_205; currency=EUR; ...; geo=AT; time=2025-S2")."""
    parts = [p.strip() for p in locator.split(";")]
    query = "&".join(["format=JSON", *parts[1:]])
    return f"{EUROSTAT_API}/{parts[0]}?{query}"


def citation_record(source_id: str, src: dict, locator: str, quote: str, value_as_found: str,
                    dataset: bool) -> dict:
    """One citation as the checker sees it and as the fact hash covers it."""
    original, gloss = evidence.split_quote(quote)
    return {"source_id": source_id, "url": src["url"], "archived_url": src.get("archived_url", ""),
            "api_url": eurostat_url(locator) if dataset else "", "fetched": src.get("notes", ""),
            "locator": locator, "quote": original, "quote_english": gloss, "value_as_found": value_as_found}


_TABLES: tuple[dict, dict] | None = None


def describe(claim: str) -> str:
    global _TABLES
    if _TABLES is None:
        _TABLES = build_input.tables()
    return build_input.describe(claim, *_TABLES)


def fact_record(claim: str, printed: str, categorical: bool, citations: list[dict]) -> dict:
    """A printed fact as the checker sees it and as `fact_sha256` hashes it. The bundle (`facts`) and the
    content model (`document.Sources`, which withholds a fact the check disagreed with, #89) both build
    it here, so the two can never hash the same fact differently."""
    return {"claim": claim, "what": describe(claim), "printed": printed, "categorical": categorical,
            "citations": citations}


def facts(bundle: dict) -> list[dict]:
    """Every printed fact, with everything a checker needs and nothing it should not see: the question,
    the printed text, and each citation's URL, locator and quote. Grades and checklists are left out;
    they describe the process, not the fact."""
    out = []
    for iso, doc in sorted(bundle["documents"].items()):
        for span in document.walk_spans(doc):
            if span.get("role") != "fact":
                continue
            for claim in span["c"]:
                cites = [citation_record(c["source_id"], bundle["sources"][c["source_id"]], c["locator"],
                                         c["quote"], c["value_as_found"],
                                         bool(c["checks"].get("dataset_value_reproduced")))
                         for c in bundle["claims"].get(claim, [])]
                out.append({**fact_record(claim, span["t"], span.get("k") == "categorical", cites),
                            "iso": iso})
    return out


def withholding(row: dict | None, sha: str) -> str:
    """Why a fact is withheld after the fact check, or ''. Only a verdict on this exact fact counts: once
    the fact or its source changes, the old verdict withholds nothing and the fact is checked again."""
    if not row or row["verdict"] == "supported" or row["fact_sha256"] != sha:
        return ""
    what = "could not confirm" if row["verdict"] == "unclear" else "did not confirm"
    return (f"the fact check ({row['checker_model']}, run {row['run']}) {what} this: "
            f"{_clean(row['reason'], 240)} It is withheld until the fact or its source is corrected and "
            "checked again")


def fact_sha256(fact: dict) -> str:
    body = {k: fact[k] for k in ("claim", "what", "printed", "categorical", "citations")}
    return hashlib.sha256(json.dumps(body, ensure_ascii=False, sort_keys=True).encode()).hexdigest()


def authors(bundle: dict) -> dict[str, set[str]]:
    """Who wrote each printed fact, as far as the files record it. A vetting finding records its
    researcher's model from #87 on; a citizen's finding records the person; a Eurostat value was read
    by a program. Everything else was admitted before authors were recorded."""
    by_url: dict[tuple[str, str], set[str]] = {}
    for p in sorted(VETTING.glob("[A-Z][A-Z].json")):
        doc = json.loads(p.read_text(encoding="utf-8"))
        model = doc.get("researcher_model", "")
        for f in doc.get("findings", []):
            if model:
                by_url.setdefault((f["claim"], f["url"]), set()).add(model)
    import contrib  # noqa: PLC0415
    for s in contrib.load(contrib.SUBMISSIONS):
        by_url.setdefault((s["claim"], s["url"]), set()).add(f"person:{s.get('submitter', '')}")
    out = {}
    for claim, cites in bundle["claims"].items():
        who: set[str] = set()
        for c in cites:
            if c["checks"].get("dataset_value_reproduced"):
                who.add("program:fetch_eurostat.py")
            who |= by_url.get((claim, bundle["sources"][c["source_id"]]["url"]), set())
        out[claim] = who or {UNRECORDED}
    return out


# --------------------------------------------------------------------------- #
# the ledger
# --------------------------------------------------------------------------- #

def _read(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def _write(path: Path, fields: list[str], rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def load_ledger() -> dict[str, dict[str, str]]:
    return {r["claim"]: r for r in _read(LEDGER)}


def assess(bundle: dict, ledger: dict[str, dict[str, str]]) -> list[tuple[dict, str, str]]:
    """(fact, its current sha, '' if it passes or the reason it does not) for every printed fact."""
    who = authors(bundle)
    out = []
    for f in facts(bundle):
        sha, row = fact_sha256(f), ledger.get(f["claim"])
        if row is None:
            why = "never checked"
        elif row["fact_sha256"] != sha:
            why = "changed since it was checked"
        elif row["verdict"] != "supported":
            why = f"checker found it {row['verdict'].replace('_', ' ')}: {row['reason']}"
        else:
            why = ineligible(row["checker_model"], who[f["claim"]])
        out.append((f, sha, why))
    return out


# --------------------------------------------------------------------------- #
# prepare / stage / record
# --------------------------------------------------------------------------- #

def prompt_sha256() -> str:
    return hashlib.sha256(WORKFLOW.read_bytes()).hexdigest() if WORKFLOW.exists() else ""


def prepare(everything: bool, size: int, date: str) -> int:
    """Write the workflow's input: the facts due, in batches of one state and one checker model, sorted
    by source so a checker fetches each page once. The run id is the date and the input's hash. The
    workflow's hash is recorded here, when the run is prepared, not when its manifest is written."""
    bundle = load_bundle()
    who = authors(bundle)
    due = [(f, sha) for f, sha, why in assess(bundle, load_ledger()) if why or everything]
    groups: dict[tuple[str, str], list[dict]] = {}
    unassignable = []
    for f, sha in due:
        checker = checker_for(who[f["claim"]])
        if not checker:
            unassignable.append(f["claim"])
            continue
        groups.setdefault((f["iso"], checker), []).append(
            {**f, "fact_sha256": sha, "author_model": ";".join(sorted(who[f["claim"]]))})
    batches = []
    for (iso, checker), items in sorted(groups.items()):
        items.sort(key=lambda x: (x["citations"][0]["url"] if x["citations"] else "", x["claim"]))
        for n in range(0, len(items), size):
            batches.append({"iso": iso, "checker_model": checker, "facts": items[n:n + size]})
    body = json.dumps(batches, ensure_ascii=False, sort_keys=True).encode()
    run = f"{date}-{hashlib.sha256(body).hexdigest()[:8]}"
    folder = CACHE / run / "in"
    folder.mkdir(parents=True, exist_ok=True)
    args = []
    for n, b in enumerate(batches, start=1):
        name = f"{b['iso']}-{n:03d}"
        path = folder / f"{name}.json"
        path.write_text(json.dumps(b, ensure_ascii=False, indent=1), encoding="utf-8")
        args.append({"batch": name, "iso": b["iso"], "name": bundle["documents"][b["iso"]]["name"],
                     "model": ALIAS[b["checker_model"]], "checker_model": b["checker_model"],
                     "path": str(path), "n_facts": len(b["facts"])})
    (CACHE / run / "args.json").write_text(json.dumps(args, indent=1), encoding="utf-8")
    (CACHE / run / "input.sha256").write_text(hashlib.sha256(body).hexdigest() + "\n")
    (CACHE / run / "workflow.sha256").write_text(prompt_sha256() + "\n")
    per_model = {m: sum(a["n_facts"] for a in args if a["checker_model"] == m) for m in CHECKERS.values()}
    print(f"run {run}: {sum(per_model.values())} facts due of {len(facts(bundle))} printed, "
          f"{len(args)} batches (one agent each); "
          + ", ".join(f"{m}: {n}" for m, n in per_model.items()))
    if unassignable:
        print(f"{len(unassignable)} facts have no eligible checker (both models wrote them): "
              + ", ".join(unassignable))
    print(f"args: {CACHE / run / 'args.json'}")
    return 0


def _clean(text: str, limit: int = 400) -> str:
    return re.sub(r"\s+", " ", str(text or "")).strip()[:limit]


def stage(path: Path, run_id: str, prepared: str) -> int:
    """Check the workflow's answers against what was asked, and keep them. A batch is refused, whole,
    when its checker reports a different model than the one asked for, when the checker is an author of
    any fact in it, or when it answers for facts it was not given."""
    results = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(results, dict):
        results = results["result"]
    folder = CACHE / prepared / "in"
    out = STAGED / run_id
    kept, refused = 0, []
    for r in results:
        if not r or not r.get("review"):
            refused.append(f"{(r or {}).get('batch', '?')}: no answer")
            continue
        batch = json.loads((folder / f"{r['batch']}.json").read_text(encoding="utf-8"))
        asked, reported = batch["checker_model"], _clean(r["review"].get("checker_model", ""), 80)
        given = {f["claim"]: f for f in batch["facts"]}
        verdicts = r["review"].get("verdicts", [])
        problems = []
        if reported != asked:
            problems.append(f"asked for {asked}, checker reported {reported or '(nothing)'}")
        problems += [f"{c}: {why}" for c, f in given.items()
                     if (why := ineligible(asked, split_authors(f["author_model"])))]
        problems += [f"{v.get('claim')}: not in this batch" for v in verdicts if v.get("claim") not in given]
        problems += [f"{v.get('claim')}: verdict {v.get('verdict')!r}" for v in verdicts
                     if v.get("verdict") not in VERDICTS]
        if problems:
            refused.append(f"{r['batch']}: " + "; ".join(problems))
            continue
        answered = {v["claim"]: v for v in verdicts}
        rows = [{"claim": c, "fact_sha256": f["fact_sha256"], "author_model": f["author_model"],
                 "checker_model": asked,
                 "verdict": answered[c]["verdict"] if c in answered else "unclear",
                 "reason": _clean(answered[c]["reason"]) if c in answered else "the checker gave no verdict",
                 "quote_found": answered.get(c, {}).get("quote_found", False),
                 "checked_url": _clean(answered.get(c, {}).get("checked_url", ""), 500)}
                for c, f in given.items()]
        out.mkdir(parents=True, exist_ok=True)
        (out / f"{r['batch']}.json").write_text(json.dumps(
            {"run": run_id, "prepared": prepared, "batch": r["batch"], "iso": batch["iso"],
             "checker_model": asked, "reported_model": reported, "verdicts": rows},
            ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        kept += 1
    print(f"staged {kept} batches")
    for line in refused:
        print(f"refused {line}")
    return 1 if refused else 0


def record(run_id: str, output: Path | None, tokens: str, duration: str, agents: str) -> int:
    """Apply a staged run to the ledger, write its manifest, and regenerate the audit file. The raw
    workflow output is kept gzipped under cache/factcheck/<prepared>/, its sha256 in the manifest."""
    staged = sorted((STAGED / run_id).glob("*.json"))
    if not staged:
        print(f"nothing staged for run {run_id}")
        return 1
    docs = [json.loads(p.read_text(encoding="utf-8")) for p in staged]
    prepared = docs[0]["prepared"]
    date = run_id[:10] if re.match(r"\d{4}-\d{2}-\d{2}", run_id) else prepared[:10]
    ledger = load_ledger()
    for d in docs:
        for v in d["verdicts"]:
            ledger[v["claim"]] = {"claim": v["claim"], "fact_sha256": v["fact_sha256"],
                                  "author_model": v["author_model"], "checker_model": v["checker_model"],
                                  "verdict": v["verdict"], "reason": v["reason"],
                                  "checked_url": v["checked_url"], "run": run_id, "checked": date}
    _write(LEDGER, LFIELDS, [ledger[c] for c in sorted(ledger)])

    verdicts = [v for d in docs for v in d["verdicts"]]
    folder = CACHE / prepared
    raw = output.read_bytes() if output else b""
    if output:
        import gzip  # noqa: PLC0415
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "output.json.gz").write_bytes(gzip.compress(raw, mtime=0))
    commit = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    manifest = {
        "run": run_id, "prepared": prepared, "date": date,
        "input_sha256": _first_line(folder / "input.sha256"),
        "workflow_sha256": _first_line(folder / "workflow.sha256"),
        "output_sha256": hashlib.sha256(raw).hexdigest() if output else "",
        "built_from_commit": commit,
        "bundle_sha256": hashlib.sha256(BUNDLE.read_bytes()).hexdigest(),
        "batches": len(docs), "agents": agents, "tokens": tokens, "duration": duration,
        "facts_checked": len(verdicts),
        "checker_model": {m: sum(1 for v in verdicts if v["checker_model"] == m)
                          for m in sorted({v["checker_model"] for v in verdicts})},
        "verdicts": {k: sum(1 for v in verdicts if v["verdict"] == k) for k in VERDICTS},
    }
    MANIFESTS.mkdir(parents=True, exist_ok=True)
    (MANIFESTS / f"{run_id}.json").write_text(json.dumps(manifest, indent=1) + "\n", encoding="utf-8")
    print(f"ledger: {len(verdicts)} verdicts from run {run_id}; manifest "
          f"{_rel(MANIFESTS / f'{run_id}.json')}")
    return audit(check=False)


def _rel(path: Path) -> str:
    return str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path)


def _first_line(path: Path) -> str:
    return path.read_text().strip() if path.exists() else ""


def manifests() -> list[dict]:
    """Every recorded run, newest first."""
    runs = [json.loads(p.read_text(encoding="utf-8")) for p in MANIFESTS.glob("*.json")]
    return sorted(runs, key=lambda m: (m["date"], m["run"]), reverse=True)


def history() -> list[dict]:
    """Every verdict ever staged, oldest run first: the disagreements a later run superseded stay on
    the record."""
    out = []
    for m in reversed(manifests()):
        for p in sorted((STAGED / m["run"]).glob("*.json")):
            out += [{**v, "run": m["run"], "date": m["date"]}
                    for v in json.loads(p.read_text(encoding="utf-8"))["verdicts"]]
    return out


# --------------------------------------------------------------------------- #
# the audit file and the gate
# --------------------------------------------------------------------------- #

def summary(bundle: dict) -> dict:
    """The counts every output states, from one place."""
    ledger = load_ledger()
    rows = assess(bundle, ledger)
    passing = [f for f, _, why in rows if not why]
    current = [ledger[f["claim"]] for f, sha, _ in rows
               if f["claim"] in ledger and ledger[f["claim"]]["fact_sha256"] == sha]
    printed = {f["claim"] for f, _, _ in rows}
    return {
        "printed": len(rows), "passing": len(passing),
        # Facts the check did not confirm and the content model therefore withholds (#89).
        "withheld": [r for c, r in sorted(ledger.items()) if c not in printed and r["verdict"] != "supported"],
        "failing": [(f, why) for f, _, why in rows if why],
        "by_checker": {m: sum(1 for r in current if r["checker_model"] == m) for m in CHECKERS.values()},
        "by_verdict": {k: sum(1 for r in current if r["verdict"] == k) for k in VERDICTS},
        "by_author": _count(";".join(sorted(a)) for a in authors(bundle).values()),
    }


def _count(items) -> dict[str, int]:
    out: dict[str, int] = {}
    for i in items:
        out[i] = out.get(i, 0) + 1
    return dict(sorted(out.items()))


def _md_cell(text: str) -> str:
    return str(text).replace("|", "\\|").replace("\n", " ")


def audit_text(bundle: dict) -> str:
    s = summary(bundle)
    ledger = load_ledger()
    lines = [
        "# Fact-check audit",
        "",
        "> Generated by `model/factcheck.py audit` from `model/research/factcheck/` (the ledger, the staged "
        "verdicts and the run manifests) and the published data bundle. Do not edit by hand; "
        "`factcheck.py gate` fails when this file differs from what it would generate (DECISIONS.md #87).",
        ">",
        f"> **{evidence.DISCLAIMER}** This check is made by a second model, not by a person.",
        "",
        "## Status",
        "",
        f"**{s['passing']} of {s['printed']} printed facts** have a current verdict of *supported* from a "
        "checker model that did not write them. A deploy to production requires all of them. "
        f"**{len(s['withheld'])}** more are withheld because the check did not confirm them.",
        "",
        "| Checker model | Current verdicts |",
        "|---|---:|",
        *[f"| {m} | {n} |" for m, n in s["by_checker"].items()],
        "",
        "| Verdict | Facts |",
        "|---|---:|",
        *[f"| {k.replace('_', ' ')} | {n} |" for k, n in s["by_verdict"].items()],
        "",
        "| Author of the fact, as recorded | Facts |",
        "|---|---:|",
        *[f"| {_md_cell(a)} | {n} |" for a, n in s["by_author"].items()],
        "",
        "## The rule",
        "",
        "| Fact written by | Checked by |",
        "|---|---|",
        *[f"| {a} | {c} |" for a, c in RULE],
        "",
        "A verdict holds for the fact exactly as printed: a SHA-256 of the claim, the question it answers, "
        "the printed text and every citation behind it (URL, fetched-document hash, locator, quote). Any "
        "change to these voids the verdict until the fact is checked again.",
        "",
        "## Not passing",
        "",
    ]
    if s["failing"]:
        lines += ["| Claim | Printed | Why |", "|---|---|---|",
                  *[f"| `{f['claim']}` | {_md_cell(f['printed'])} | {_md_cell(why)} |" for f, why in s["failing"]]]
    else:
        lines += ["None. Every printed fact passes."]
    lines += ["", "## Withheld after the fact check", "",
              "Facts the checker did not confirm as printed. Each is shown as disputed, with this reason, instead "
              "of being printed, until the fact or its source is corrected and checked again (DECISIONS.md #89).",
              ""]
    if s["withheld"]:
        lines += ["| Claim | Checker | Verdict | Run | Reason |", "|---|---|---|---|---|",
                  *[f"| `{r['claim']}` | {r['checker_model']} | {r['verdict'].replace('_', ' ')} | {r['run']} | "
                    f"{_md_cell(r['reason'])} |" for r in s["withheld"]]]
    else:
        lines += ["None."]
    past = [v for v in history() if v["verdict"] != "supported"]
    lines += ["", "## Every disagreement on record", "",
              "Each verdict other than *supported*, from every run, including those a later check superseded "
              "after the fact or its source changed.", ""]
    if past:
        lines += ["| Run | Claim | Checker | Verdict | Reason | Now |", "|---|---|---|---|---|---|"]
        for v in past:
            row = ledger.get(v["claim"], {})
            now = ("superseded: " + row["verdict"].replace("_", " ") + f" in {row['run']}"
                   if row and row["run"] != v["run"] else "current")
            lines.append(f"| {v['run']} | `{v['claim']}` | {v['checker_model']} | "
                         f"{v['verdict'].replace('_', ' ')} | {_md_cell(v['reason'])} | {now} |")
    else:
        lines += ["None."]
    lines += ["", "## Runs", ""]
    runs = manifests()
    if runs:
        lines += ["| Run | Date | Facts checked | By model | Verdicts | Commit | Bundle SHA-256 | Workflow SHA-256 |",
                  "|---|---|---:|---|---|---|---|---|"]
        for m in runs:
            lines.append(
                f"| {m['run']} | {m['date']} | {m['facts_checked']} | "
                + "; ".join(f"{k}: {n}" for k, n in m["checker_model"].items()) + " | "
                + "; ".join(f"{k.replace('_', ' ')}: {n}" for k, n in m["verdicts"].items() if n) + " | "
                + f"{m['built_from_commit'][:12]} | {m['bundle_sha256'][:16]} | {m['workflow_sha256'][:16]} |")
    else:
        lines += ["No run recorded yet."]
    lines += ["", "## How a check runs", "", *[f"{n}. {t}" for n, t in enumerate(STEPS, start=1)], ""]
    return "\n".join(lines)


# The process, in words, for the audit file and every asset's appendix (factcheck_appendix.py).
STEPS = [
    "`factcheck.py prepare` lists every printed fact whose verdict is missing, stale or not passing, "
    "hashes each as printed, names its author from the recorded files, and assigns the checker by the rule.",
    "The checked-in workflow (`model/research/factcheck/workflow.js`) asks for that checker model by name, "
    "one agent per batch of one state's facts. The checker fetches each cited page (or the Eurostat API "
    "response), looks for the quote, and decides whether it supports the statement exactly as printed: "
    "value, unit, date, country and scope. It answers supported, not supported or unclear, with a reason.",
    "`factcheck.py stage` refuses any batch whose checker reports a different model than the one asked for, "
    "or is an author of a fact in it.",
    "`factcheck.py record` writes the verdicts to the ledger, the run's manifest (input, workflow and bundle "
    "hashes, commit, counts) and this audit file.",
    "A fact the checker does not confirm is withheld: it is shown as disputed, with the checker's reason, "
    "instead of printed, until the fact or its source is corrected and checked again. The verdict stays "
    "on the record.",
    "Before every production deploy, `factcheck.py gate` requires a current *supported* verdict from an "
    "eligible checker for every printed fact, and this file to be current.",
]


def audit(check: bool) -> int:
    text = audit_text(load_bundle())
    if check:
        current = AUDIT.read_text(encoding="utf-8") if AUDIT.exists() else ""
        if current != text:
            print(f"{_rel(AUDIT)} is stale: run `./run.sh factcheck audit`")
            return 1
        return 0
    AUDIT.parent.mkdir(parents=True, exist_ok=True)
    AUDIT.write_text(text, encoding="utf-8")
    print(f"wrote {_rel(AUDIT)}")
    return 0


def gate(strict: bool) -> int:
    bundle = load_bundle()
    s = summary(bundle)
    stale = audit(check=True) != 0
    print(f"{s['passing']} of {s['printed']} printed facts checked, supported, checker ≠ author")
    for f, why in s["failing"][:50]:
        print(f"  {f['claim']}: {why}")
    if len(s["failing"]) > 50:
        print(f"  ... and {len(s['failing']) - 50} more (docs/fact-check-audit.md lists all)")
    ok = not s["failing"] and not stale
    if strict and not ok:
        print("fact-check gate: FAILED. Run /factcheck, resolve every disagreement, commit, push again.")
        return 1
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["prepare", "stage", "record", "audit", "status", "gate"])
    ap.add_argument("result", nargs="?", type=Path, help="stage: the workflow's output")
    ap.add_argument("--all", action="store_true", help="prepare: re-check every printed fact")
    ap.add_argument("--size", type=int, default=30, help="prepare: facts per batch (one agent each)")
    ap.add_argument("--run", default="", help="stage, record: the workflow run id")
    ap.add_argument("--prepared", default="", help="stage: the run id printed by prepare")
    ap.add_argument("--output", type=Path, help="record: the workflow's task output file")
    ap.add_argument("--tokens", default="", help="record: subagent tokens, from the workflow's usage")
    ap.add_argument("--duration", default="", help="record: wall-clock duration, from the workflow's usage")
    ap.add_argument("--agents", default="", help="record: agents the workflow ran")
    ap.add_argument("--check", action="store_true", help="audit: fail if the file is stale, write nothing")
    ap.add_argument("--date", default=dt.date.today().isoformat())
    a = ap.parse_args(argv)
    if a.command == "prepare":
        return prepare(a.all, a.size, a.date)
    if a.command == "stage":
        return stage(a.result, a.run, a.prepared)
    if a.command == "record":
        return record(a.run, a.output, a.tokens, a.duration, a.agents)
    if a.command == "audit":
        return audit(a.check)
    return gate(strict=a.command == "gate")


if __name__ == "__main__":
    sys.exit(main())
