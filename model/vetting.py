#!/usr/bin/env python3
"""
Vet printed facts against top-tier sources, and admit what survives (DECISIONS.md #83).

    python3 model/vetting.py prepare [--iso DE ...]          # input for the workflow -> cache/vetting/<run>/
    python3 model/vetting.py stage <workflow-output>         # workflow output -> research/vetting/<ISO>.json
    python3 model/vetting.py hosts [--apply stub.csv]        # hosts to tier before admission
    python3 model/vetting.py verify [--iso DE ...]           # fetch, hash, find the quote (slow, polite)
    python3 model/vetting.py admit                           # apply agreed, verified findings
    python3 model/vetting.py report                          # outcomes per state

Why this file exists
--------------------
Every printed fact rested on the one source a single agent found in one pass. A vetting run
(`research/vetting/workflow.js`) sends one researcher per state to look for a better source (a
T1/T2 source saying the same thing), newer information, contradictions and filled gaps, and one
blind reviewer who sees only the URL, the quote and the question -- never the proposed value.

Nothing the run returns is trusted. A finding is admitted only when
1. its source is T1 or T2 (`evidence.tier`),
2. the page was fetched, hashed, and contains the quote (`research.match`, as for run 1),
3. the blind reviewer found the quote and independently reached the same value (`agree`), and
4. the printed value passes the value-in-quote rule against it (#82), checked at render time.

The researcher's own label for a finding (upgrade, supersedes, contradicts) is not trusted either.
What decides is whether its value differs from the printed one. If it does, the published rule
(`resolve`) settles it: a higher tier wins, and the same authority with a later date wins.
Otherwise the fact is **disputed** and shown with both sources. Nothing is replaced by judgement.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "model"))
import evidence  # noqa: E402
import fetch  # noqa: E402
import research  # noqa: E402

DIR = ROOT / "model" / "research" / "vetting"
WORKFLOW = DIR / "workflow.js"
VERIFICATION = DIR / "verification.csv"
DISPUTES = DIR / "disputes.csv"
OUTCOMES = DIR / "outcomes.csv"
VFIELDS = ["iso", "claim", "relation", "url", "http_status", "content_type", "sha256", "match",
           "archived_url", "checked"]
DFIELDS = ["claim", "printed", "printed_source_id", "other_source_id", "other_value", "rule", "checked"]
OFIELDS = ["iso", "claim", "status", "relation", "result"]
CATEGORICAL = {"foreign_dependency"}
FIELD_OF_KIND = {"register": "register", "operator": "holder", "count": "record_count",
                 "size": "data_size", "foreign_dependency": "foreign_dependency",
                 "legal_basis": "legal_basis", "hosting": "hosting"}
DOC_TYPE = {"legislation": "statute", "official_page": "webpage", "annual_report": "annual_report",
            "audit_report": "report", "statistics": "report", "procurement": "webpage", "eu_document": "report"}


def categorical(claim: str) -> bool:
    return claim.startswith("indicator:") or claim.split(":")[-1] in CATEGORICAL


# --------------------------------------------------------------------------- #
# stage
# --------------------------------------------------------------------------- #

def prompt_sha256() -> str:
    return hashlib.sha256(WORKFLOW.read_bytes()).hexdigest() if WORKFLOW.exists() else ""


RUNS = ROOT / "cache" / "vetting"


def prepare(isos: list[str] | None, date: str) -> int:
    """Write the workflow's input: one file per state, and the args to pass. The run id is the date
    and the input's hash, so the same input on the same day is the same run."""
    import subprocess  # noqa: PLC0415
    raw = subprocess.run([sys.executable, str(DIR / "build_input.py")], capture_output=True, check=True).stdout
    states = [s for s in json.loads(raw) if not isos or s["iso"] in isos]
    body = json.dumps(states, ensure_ascii=False, sort_keys=True).encode()
    run = f"{date}-{hashlib.sha256(body).hexdigest()[:8]}"
    folder = RUNS / run / "in"
    folder.mkdir(parents=True, exist_ok=True)
    args = []
    for s in states:
        path = folder / f"{s['iso']}.json"
        path.write_text(json.dumps({"facts": s["facts"], "gaps": s["gaps"]}, ensure_ascii=False, indent=1),
                        encoding="utf-8")
        args.append({"iso": s["iso"], "name": s["name"], "path": str(path),
                     "n_facts": len(s["facts"]), "n_gaps": len(s["gaps"])})
    (RUNS / run / "args.json").write_text(json.dumps(args, indent=1), encoding="utf-8")
    (RUNS / run / "input.sha256").write_text(hashlib.sha256(body).hexdigest() + "\n")
    print(f"run {run}: {len(args)} states, {sum(a['n_facts'] for a in args)} facts, "
          f"{sum(a['n_gaps'] for a in args)} gaps\nargs: {RUNS / run / 'args.json'}")
    return 0


def stage_round(path: Path, run_id: str, date: str) -> int:
    """Stage a later round (#93) under rounds/<run>/, split by the state in each claim id, so the first
    run's staging files are never overwritten. Each finding keeps its own models."""
    results = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(results, dict):
        results = results["result"]
    sha = prompt_sha256()
    per: dict[str, dict] = {}
    for r in results:
        if not r or not r.get("research"):
            continue
        verdicts = {v["id"]: v for v in (r.get("review") or {}).get("verdicts", [])}
        models = {"researcher_model": r["research"].get("researcher_model", ""),
                  "reviewer_model": (r.get("review") or {}).get("reviewer_model", "")}
        for i, f in enumerate(r["research"]["findings"]):
            iso = f["claim"].split(":")[1]
            doc = per.setdefault(iso, {"iso": iso, "run": run_id, "date": date, "workflow_sha256": sha,
                                       "blind": True, "findings": [], "outcomes": []})
            f = {**f, "url": research.clean_url(f["url"]), "review": verdicts.get(i), **models}
            if categorical(f["claim"]):
                # A closed vocabulary (#79): "Yes: the agency runs ..." is "yes". The wording as written is
                # kept beside it; a value that does not start with a term of the vocabulary stays as it was
                # and cannot pass the reviewer's agreement.
                m = re.match(r"\s*(yes|partial|partly|no|national|eu_provider|non_eu_provider|mixed)\b",
                             f["value"], re.I)
                if m:
                    f = {**f, "value_as_written": f["value"],
                         "value": {"partly": "partial"}.get(m.group(1).lower(), m.group(1).lower())}
            doc["findings"].append(f)
        for o in r["research"]["outcomes"]:
            iso = o["claim"].split(":")[1]
            per.setdefault(iso, {"iso": iso, "run": run_id, "date": date, "workflow_sha256": sha, "blind": True,
                                 "findings": [], "outcomes": []})["outcomes"].append(o)
    folder = ROUNDS / run_id
    folder.mkdir(parents=True, exist_ok=True)
    for iso, doc in sorted(per.items()):
        (folder / f"{iso}.json").write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"staged round {run_id}: {sum(len(d['findings']) for d in per.values())} findings in {len(per)} states")
    return 0


def prepare_withheld(date: str, size: int = 12) -> int:
    """The input for a round on the facts the fact check withheld (#93): each with what it answers, how it
    printed, its source and the checker's reason, in batches across states."""
    import factcheck  # noqa: PLC0415
    ledger = factcheck.load_ledger()
    rows = {c: r for c, r in ledger.items() if r["verdict"] != "supported"}
    facts = []
    for f in factcheck.unwithheld_facts():
        r = rows.get(f["claim"])
        if r and factcheck.fact_sha256(f) == r["fact_sha256"]:
            facts.append({"claim": f["claim"], "what": f["what"], "printed": f["printed"],
                          "source_url": f["citations"][0]["url"] if f["citations"] else "",
                          "checker_reason": r["reason"]})
    facts.sort(key=lambda f: f["claim"])
    body = json.dumps(facts, ensure_ascii=False, sort_keys=True).encode()
    run = f"{date}-withheld-{hashlib.sha256(body).hexdigest()[:8]}"
    folder = RUNS / run / "in"
    folder.mkdir(parents=True, exist_ok=True)
    args = []
    for n in range(0, len(facts), size):
        name = f"W{n // size + 1:02d}"
        path = folder / f"{name}.json"
        path.write_text(json.dumps({"facts": facts[n:n + size], "gaps": []}, ensure_ascii=False, indent=1),
                        encoding="utf-8")
        args.append({"iso": name, "name": "several EU member states", "path": str(path),
                     "n_facts": len(facts[n:n + size]), "n_gaps": 0})
    (RUNS / run / "args.json").write_text(json.dumps(args, indent=1), encoding="utf-8")
    (RUNS / run / "input.sha256").write_text(hashlib.sha256(body).hexdigest() + "\n")
    print(f"run {run}: {len(facts)} withheld facts in {len(args)} batches\nargs: {RUNS / run / 'args.json'}")
    return 0


def stage(path: Path, run_id: str, date: str) -> int:
    """Split the workflow's return value into one staging file per state. Staging is never rendered.
    Accepts the task's output file as written (a wrapper with "result") or the bare result list."""
    results = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(results, dict):
        results = results["result"]
    sha = prompt_sha256()
    n = 0
    for r in results:
        if not r or not r.get("research"):
            continue
        verdicts = {v["id"]: v for v in (r.get("review") or {}).get("verdicts", [])}
        findings = []
        for i, f in enumerate(r["research"]["findings"]):
            findings.append({**f, "url": research.clean_url(f["url"]), "review": verdicts.get(i)})
        doc = {"iso": r["iso"], "run": run_id, "date": date, "workflow_sha256": sha,
               "researcher_model": r["research"].get("researcher_model", ""),
               "reviewer_model": (r.get("review") or {}).get("reviewer_model", ""), "blind": True,
               "findings": findings, "outcomes": r["research"]["outcomes"]}
        (DIR / f"{r['iso']}.json").write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n",
                                              encoding="utf-8")
        n += 1
    print(f"staged {n} states")
    return 0


ROUNDS = DIR / "rounds"


def staged(isos: list[str] | None = None) -> dict[str, dict]:
    """Every staged finding, per state: the vetting runs' and the citizens' (contrib.py, #85). A citizen
    finding carries `source: citizen` and its issue number; its review is a person's, not a model's.
    Later rounds (`rounds/<run>/<ISO>.json`, #93) are added after the first run's, in run order; each of
    their findings carries its own researcher and reviewer model."""
    out = {p.stem: json.loads(p.read_text(encoding="utf-8")) for p in sorted(DIR.glob("[A-Z][A-Z].json"))
           if not isos or p.stem in isos}
    for folder in sorted(p for p in ROUNDS.glob("*") if p.is_dir()):
        for p in sorted(folder.glob("[A-Z][A-Z].json")):
            if isos and p.stem not in isos:
                continue
            r = json.loads(p.read_text(encoding="utf-8"))
            doc = out.setdefault(p.stem, {"iso": p.stem, "findings": [], "outcomes": [], "reviewer_model": ""})
            doc["findings"] += r["findings"]
            doc["outcomes"] += r["outcomes"]
    import contrib  # noqa: PLC0415
    for s in contrib.load(contrib.SUBMISSIONS):
        if isos and s["iso"] not in isos:
            continue
        doc = out.setdefault(s["iso"], {"iso": s["iso"], "findings": [], "outcomes": [], "reviewer_model": ""})
        doc["findings"].append({**s, "url": research.clean_url(s["url"]), "question": s["claim"],
                                "source": "citizen", "note": f"submitted in issue #{s['issue']}"})
    return out


# --------------------------------------------------------------------------- #
# verify
# --------------------------------------------------------------------------- #

def load_verification() -> dict[tuple, dict[str, str]]:
    if not VERIFICATION.exists():
        return {}
    with VERIFICATION.open(newline="", encoding="utf-8") as fh:
        return {(r["iso"], r["claim"], r["relation"], r["url"]): r for r in csv.DictReader(fh)}


def verify(isos: list[str] | None) -> int:
    today = dt.date.today().isoformat()
    rows = load_verification()
    texts: dict[str, tuple] = {}
    archives: dict[str, str] = {}
    fresh = []

    def save() -> None:
        with VERIFICATION.open("w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=VFIELDS, lineterminator="\n")
            w.writeheader()
            w.writerows(sorted(rows.values(), key=lambda r: (r["iso"], r["claim"], r["relation"], r["url"])))

    for iso, doc in staged(isos).items():
        for f in doc["findings"]:
            key = (iso, f["claim"], f["relation"], f["url"])
            if key in rows and rows[key]["match"] in ("exact", "loose"):
                continue
            if not agree(f) or _tier_of(f["url"]) > 2:
                continue                  # cannot be admitted whatever the page says; not fetched
            if not f["url"].startswith("https://"):
                rows[key] = dict(zip(VFIELDS, [iso, f["claim"], f["relation"], f["url"], "not-https", "", "",
                                               "rejected", "", today]))
                continue
            if f["url"] not in texts:
                result = fetch.fetch(f["url"])
                text = research.extract(result.body, result.content_type) if result.ok else ""
                texts[f["url"]] = (result, text)
                if result.ok:
                    fresh.append(fetch.store(iso, "vetting", f["claim"].replace(":", "_"), f["url"], result, today))
            result, text = texts[f["url"]]
            m = research.match(f["quote"], text) if result.ok else "fetch_failed"
            if m == "not_found" and result.content_type.startswith("text/html"):
                # Built with JavaScript: the browser, only for a page that answered 200 (#83).
                if (f["url"], "rendered") not in texts:
                    rr = fetch.fetch_rendered(f["url"])
                    texts[(f["url"], "rendered")] = (rr, research.extract(rr.body, "text/html") if rr.ok else "")
                rr, rtext = texts[(f["url"], "rendered")]
                if rr.ok and research.match(f["quote"], rtext) in ("exact", "loose"):
                    result, m = rr, research.match(f["quote"], rtext)
            if m in ("exact", "loose") and f["url"] not in archives:
                archives[f["url"]] = research.archived(f["url"])
            rows[key] = {"iso": iso, "claim": f["claim"], "relation": f["relation"], "url": f["url"],
                         "http_status": str(result.status), "content_type": result.content_type,
                         "sha256": fetch.sha256(result.body) if result.body else "", "match": m,
                         "archived_url": archives.get(f["url"], ""), "checked": today}
        save()
        print(f"{iso}: verified", file=sys.stderr, flush=True)
    fetch.write_manifest(fetch.merge(fetch.load_manifest(), fresh))
    save()
    return report()


# --------------------------------------------------------------------------- #
# agree, resolve
# --------------------------------------------------------------------------- #

_WORD = re.compile(r"[^\W\d_]{4,}", re.U)


def agree(finding: dict) -> bool:
    """Did the blind reviewer find the quote and reach the same value on its own?

    Categorical: the same term. Free text: every figure in the value is among the reviewer's, and
    the two share a distinctive word (4+ letters), so a reviewer who read a different register off
    the same quote does not count as agreeing."""
    if finding.get("source") == "citizen":
        # Two-person rule (#85): a different, eligible person confirmed this submission.
        import contrib  # noqa: PLC0415
        return contrib.status().get(f"#{finding['issue']}", {}).get("state") == "verified"
    v = finding.get("review") or {}
    got, want = (v.get("established") or "").strip(), finding["value"].strip()
    if not v.get("quote_found") or not got:
        return False
    if categorical(finding["claim"]):
        return got.lower() == want.lower()
    theirs = set().union(*(r for _, r in evidence.numbers(got))) if evidence.numbers(got) else set()
    if any(not readings & theirs for _, readings in evidence.numbers(want) if readings):
        return False
    return bool({w.casefold() for w in _WORD.findall(want)} & {w.casefold() for w in _WORD.findall(got)})


def same_value(printed: str, finding: dict) -> bool:
    """Does the finding say what the report prints? Categorical: the same term. Otherwise the
    printed value passes the value-in-quote rule against the finding's quote."""
    if categorical(finding["claim"]):
        return printed.strip().lower() == finding["value"].strip().lower()
    # Figures alone cannot decide it: a name has no figures, and every name would then "agree" with
    # every other. The two values must also share a distinctive word, as in agree().
    shared = ({w.casefold() for w in _WORD.findall(printed)}
              & {w.casefold() for w in _WORD.findall(finding["value"])})
    return bool(shared) and evidence.value_in_quote(printed, finding["quote"], finding.get("title", ""))["ok"]


def resolve(old: dict, new: dict, new_published: str) -> str:
    """Which of two disagreeing sources the report follows, by the published rule (#83):
    'higher_tier' or 'later_same_authority' for the new one, else '' (disputed)."""
    if evidence.tier(new)[0] < evidence.tier(old)[0]:
        return "higher_tier"
    if (evidence.host(new["url"]) == evidence.host(old["url"]) and new_published and old.get("published")
            and new_published > old["published"]):
        return "later_same_authority"
    return ""


# --------------------------------------------------------------------------- #
# admit
# --------------------------------------------------------------------------- #

def admit() -> int:
    import national_data as nd  # noqa: PLC0415
    import provenance  # noqa: PLC0415

    ok = {k: r for k, r in load_verification().items() if r["match"] in ("exact", "loose")}
    reg = provenance.registry()
    cites = {(c["claim"], c["source_id"], c["locator"]): c for c in provenance.citations()}
    rows = {(r["iso"], r["record_class"]): r for r in nd.read_rows()}
    with research.INDICATOR_VALUES.open(newline="", encoding="utf-8") as fh:
        indicators = {(r["iso"], r["indicator"]): r["value"] for r in csv.DictReader(fh)}
    disputes = {r["claim"]: r for r in _read(DISPUTES, DFIELDS)}
    # No clock: every date admission writes is the date the evidence was checked, so re-running
    # admit on another day reproduces the registers byte for byte (./run.sh admit --check).
    outcomes = []
    tally: dict[str, int] = {}

    def printed_value(claim: str) -> str:
        p = claim.split(":")
        if p[0] == "indicator":
            return indicators.get((p[1], p[2]), "")
        row = rows.get((p[1], p[2]))
        if row and row["status"] == "not_held" and p[3] == "register":
            # An admitted absence is a printed finding, not a gap: a source that says the register
            # exists contradicts it, and goes through resolve() like any disagreement.
            return "No central register"
        return row.get(FIELD_OF_KIND.get(p[3], ""), "") if row and row["status"] == "held" else ""

    def set_value(claim: str, value: str, url: str) -> None:
        p = claim.split(":")
        if p[0] == "indicator":
            indicators[(p[1], p[2])] = value.strip().lower()
            return
        row = rows.setdefault((p[1], p[2]), {f: "" for f in nd.FIELDS})
        row.update({"iso": p[1], "record_class": p[2], "tier": str(nd.TIER_OF[p[2]])})
        if p[3] == "register":
            row.update({"status": "held", "register": value.strip(), "holder_url": row.get("holder_url") or url})
        else:
            row[FIELD_OF_KIND[p[3]]] = value.strip().lower() if p[3] in CATEGORICAL else value.strip()

    def cite(claim: str, f: dict, v: dict, model: str) -> str:
        sid = research.register_source(reg, {**f, "doc_type": f.get("doc_type", "")}, v)
        if f.get("language") and not reg[sid].get("language"):
            reg[sid]["language"] = f["language"]
        reg[sid]["doc_type"] = DOC_TYPE.get(f.get("doc_type", ""), "webpage")
        if f.get("published") and not reg[sid]["published"]:
            reg[sid]["published"] = f["published"]
        quote = f["quote"].strip() + (f" [English: {f['quote_english'].strip()}]" if f.get("quote_english", "").strip() else "")
        locator = "PDF text" if "pdf" in v["content_type"] else "page text"
        value = f["value"].strip().lower() if categorical(claim) else f["value"].strip()
        cites[(claim, sid, locator)] = {
            "claim": claim, "source_id": sid, "locator": locator, "quote": quote, "value_as_found": value,
            "unit": "", "confidence": "absence" if value == "no" else "official", "retrieved": v["checked"],
            "checked_by": (f"vetting.py: quote {v['match']} in fetched document; submitted by a citizen in issue "
                           f"#{f['issue']}; confirmed by a person (two-person rule)" if f.get("source") == "citizen" else
                           f"vetting.py: quote {v['match']} in fetched document; blind review agreed ({model})"),
        }
        return sid

    # Facts the cross-model fact check ever withheld (#89). A `corrects` finding may replace only these
    # (#93). Read from the staged verdicts, which never change, so admission still reproduces.
    import factcheck  # noqa: PLC0415
    withheld_ever = {v["claim"] for v in factcheck.history() if v["verdict"] != "supported"}

    for iso, doc in staged().items():
        for f in doc["findings"]:
            model = f.get("reviewer_model") or doc.get("reviewer_model") or "model not recorded"
            claim, rel = f["claim"], f["relation"]
            v = ok.get((iso, claim, rel, f["url"]))
            # In the order that explains a rejection: a finding the reviewer rejected, or on a weak
            # source, was never fetched, so "not verified" would misstate why it is out.
            result = ("below_T2" if _tier_of(f["url"]) > 2 else
                      "review_disagreed" if not agree(f) else
                      "not_verified" if not v else "")
            p = claim.split(":")
            if not result and p[0] == "record" and p[3] != "register" and printed_value(f"record:{p[1]}:{p[2]}:register") == "" \
                    and not any(g["claim"] == f"record:{p[1]}:{p[2]}:register" and ok.get((iso, g["claim"], g["relation"], g["url"])) and agree(g)
                                for g in doc["findings"]):
                result = "holding_not_established"   # as in run 1: no operator for a register nobody verified
            if not result:
                printed = printed_value(claim)
                new_src = {"url": f["url"], "doc_type": DOC_TYPE.get(f.get("doc_type", ""), "webpage")}
                if not printed:
                    set_value(claim, f["value"], f["url"])
                    cite(claim, f, v, model)
                    result = "filled_gap"
                elif research.source_id(f["url"]) in {c["source_id"] for c in cites.values() if c["claim"] == claim}:
                    # The same document again is not a second source: recorded, never counted as
                    # corroboration, and it never overwrites the earlier citation's record.
                    result = "same_source"
                elif same_value(printed, f):
                    cite(claim, f, v, model)
                    result = "corroborated"
                elif rel == "corrects" and claim in withheld_ever:
                    # #93: the printed value already failed the cross-model check; a verified, blindly agreed
                    # T1/T2 finding replaces it. The new value is itself fact-checked before it can ship.
                    sid = cite(claim, f, v, model)
                    for c in cites.values():
                        if c["claim"] == claim and c["source_id"] != sid and "superseded" not in c["checked_by"]:
                            c["checked_by"] += f"; superseded {v['checked']} by {sid} (corrects a value the fact check did not confirm)"
                    set_value(claim, f["value"], f["url"])
                    disputes.pop(claim, None)
                    result = "corrected_withheld"
                else:
                    old = _best_source(claim, cites, reg)
                    rule = resolve(old, new_src, f.get("published", "")) if old else "higher_tier"
                    sid = cite(claim, f, v, model)
                    if rule:
                        for c in cites.values():
                            if c["claim"] == claim and c["source_id"] != sid and "superseded" not in c["checked_by"]:
                                c["checked_by"] += f"; superseded {v['checked']} by {sid} ({rule})"
                        set_value(claim, f["value"], f["url"])
                        disputes.pop(claim, None)
                        result = f"superseded_{rule}"
                    else:
                        disputes[claim] = {"claim": claim, "printed": printed, "printed_source_id": old["source_id"],
                                           "other_source_id": sid, "other_value": f["value"].strip(), "rule": "no rule settles it",
                                           "checked": v["checked"]}
                        result = "disputed"
            tally[result] = tally.get(result, 0) + 1
            outcomes.append({"iso": iso, "claim": claim, "status": "found", "relation": rel, "result": result})
        for o in doc["outcomes"]:
            if o["status"] != "found":
                outcomes.append({"iso": iso, "claim": o["claim"], "status": o["status"], "relation": "", "result": ""})

    provenance.write_registry(reg)
    provenance.write_citations(list(cites.values()))
    nd.write_rows(list(rows.values()))
    with research.INDICATOR_VALUES.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["iso", "indicator", "value"], lineterminator="\n")
        w.writeheader()
        w.writerows({"iso": i, "indicator": k, "value": val} for (i, k), val in sorted(indicators.items()))
    _write(DISPUTES, DFIELDS, sorted(disputes.values(), key=lambda r: r["claim"]))
    _write(OUTCOMES, OFIELDS, sorted(outcomes, key=lambda r: (r["iso"], r["claim"], r["result"])))
    print(" ".join(f"{k}={n}" for k, n in sorted(tally.items())))
    return 0


def _tier_of(url: str) -> int:
    try:
        return evidence.tier({"url": url, "doc_type": "webpage"})[0]
    except KeyError:
        return 9                          # a host nobody has classified is not top tier


def _best_source(claim: str, cites: dict, reg: dict) -> dict | None:
    mine = [c for c in cites.values() if c["claim"] == claim and "superseded" not in c["checked_by"]]
    srcs = [{**reg[c["source_id"]], "source_id": c["source_id"]} for c in mine if c["source_id"] in reg]
    return min(srcs, key=lambda s: _tier_of(s["url"])) if srcs else None


def _read(path: Path, fields: list[str]) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def _write(path: Path, fields: list[str], rows: list[dict]) -> None:
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def load_disputes() -> dict[str, dict[str, str]]:
    return {r["claim"]: r for r in _read(DISPUTES, DFIELDS)}


# --------------------------------------------------------------------------- #
# report
# --------------------------------------------------------------------------- #

def hosts(apply: Path | None) -> int:
    """Hosts the staged findings cite that authorities.csv does not classify. Without --apply, write a
    stub with a suggested tier for each (a person confirms); with --apply, merge a confirmed stub."""
    if apply:
        rows = {r["host"]: r for r in _read(evidence.AUTHORITIES, ["host", "tier", "kind"])}
        new = [r for r in _read(apply, ["host", "tier", "kind", "example"]) if r["host"] not in rows]
        for r in new:
            rows[r["host"]] = {"host": r["host"], "tier": r["tier"], "kind": r["kind"]}
        _write(evidence.AUTHORITIES, ["host", "tier", "kind"], sorted(rows.values(), key=lambda r: r["host"]))
        print(f"{len(new)} hosts classified from {apply}")
        return 0
    seen: dict[str, str] = {}
    for d in staged().values():
        for f in d["findings"]:
            h = evidence.host(f["url"])
            if h not in evidence.authorities():
                seen.setdefault(h, f"{f.get('publisher', '')} | {f['url']}")
    stub = RUNS / "hosts-stub.csv"
    stub.parent.mkdir(parents=True, exist_ok=True)
    rows = [{"host": h, "tier": "2", "kind": "public_body", "example": ex} for h, ex in sorted(seen.items())]
    _write(stub, ["host", "tier", "kind", "example"], rows)
    print(f"{len(rows)} unclassified hosts; stub with suggested tier 2 written to {stub}\n"
          "Confirm each against docs/vetting.md (T1 official portal or statistics office; T3 company; "
          "T4 mirror, press), keep the stub with the run, then: vetting.py hosts --apply <stub>")
    return 0


MANIFESTS = DIR / "runs"


def tool_versions() -> dict[str, str]:
    """The versions that produced this run's mechanical steps, as reported by the tools themselves."""
    import platform  # noqa: PLC0415
    import subprocess  # noqa: PLC0415
    out = {"python": platform.python_version(), "os": f"{platform.system()} {platform.release()} {platform.machine()}"}
    for name, cmd in (("typst", ["typst", "--version"]), ("node", ["node", "--version"]),
                      ("chrome", [next((b for b in fetch.BROWSERS if Path(b).exists()), "chrome"), "--version"])):
        try:
            out[name] = subprocess.run(cmd, capture_output=True, text=True, timeout=30).stdout.strip()
        except (OSError, subprocess.SubprocessError):
            out[name] = "not available"
    return out


def manifest(run_id: str, output: Path, prepared: str, tokens: str, duration: str) -> int:
    """Record one agent run: what went in, what asked, who answered, what came out (#84). Small and
    committed; the raw output is kept gzipped under cache/vetting/<prepared>/ with its hash here."""
    import gzip  # noqa: PLC0415
    import subprocess  # noqa: PLC0415
    raw = output.read_bytes()
    folder = RUNS / (prepared or run_id)
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "output.json.gz").write_bytes(gzip.compress(raw, mtime=0))
    doc = json.loads(raw)
    states = staged()
    rows = _read(OUTCOMES, OFIELDS)
    totals: dict[str, int] = {}
    for r in rows:
        k = r["result"] or r["status"]
        totals[k] = totals.get(k, 0) + 1
    commit = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    record = {
        "run": run_id,
        "prepared": prepared,
        "input_sha256": (folder / "input.sha256").read_text().strip() if (folder / "input.sha256").exists() else "",
        "output_sha256": hashlib.sha256(raw).hexdigest(),
        "workflow_sha256": prompt_sha256(),
        "built_from_commit": commit,
        "states": len(states),
        "reviewer_model": sorted({d.get("reviewer_model", "") for d in states.values()} - {""}),
        "agents": doc.get("agentCount") if isinstance(doc, dict) else None,
        "tokens": tokens, "duration": duration,
        "tools": tool_versions(),
        "findings": sum(len(d["findings"]) for d in states.values()),
        "outcomes": dict(sorted(totals.items())),
    }
    MANIFESTS.mkdir(exist_ok=True)
    (MANIFESTS / f"{run_id}.json").write_text(json.dumps(record, indent=1, ensure_ascii=False) + "\n",
                                              encoding="utf-8")
    print(f"wrote {(MANIFESTS / f'{run_id}.json').relative_to(ROOT)}")
    return 0


def report() -> int:
    rows = _read(OUTCOMES, OFIELDS)
    if not rows:
        v = list(load_verification().values())
        print(f"{len(v)} findings verified so far: "
              + " ".join(f"{m}={sum(1 for r in v if r['match'] == m)}" for m in sorted({r['match'] for r in v})))
        return 0
    kinds = sorted({r["result"] or r["status"] for r in rows})
    print(f"{'iso':<4}" + "".join(f"{k[:14]:>15}" for k in kinds))
    for iso in sorted({r["iso"] for r in rows}):
        print(f"{iso:<4}" + "".join(f"{sum(1 for r in rows if r['iso'] == iso and (r['result'] or r['status']) == k):>15}"
                                    for k in kinds))
    print(f"{'all':<4}" + "".join(f"{sum(1 for r in rows if (r['result'] or r['status']) == k):>15}" for k in kinds))
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["prepare", "stage", "hosts", "verify", "admit", "report", "manifest"])
    ap.add_argument("--output", type=Path, help="manifest: the workflow's task output file")
    ap.add_argument("--prepared", default="", help="manifest: the run id printed by prepare")
    ap.add_argument("--tokens", default="", help="manifest: subagent tokens, from the workflow's usage")
    ap.add_argument("--duration", default="", help="manifest: wall-clock duration, from the workflow's usage")
    ap.add_argument("--apply", type=Path, help="hosts: merge a confirmed stub into authorities.csv")
    ap.add_argument("result", nargs="?", type=Path, help="stage: the workflow's JSON result")
    ap.add_argument("--run", default="", help="stage: the workflow run id")
    ap.add_argument("--withheld", action="store_true", help="prepare: a round on the facts the fact check withheld (#93)")
    ap.add_argument("--round", action="store_true", help="stage: a later round, under rounds/<run>/ (#93)")
    ap.add_argument("--date", default=dt.date.today().isoformat())
    ap.add_argument("--iso", action="append")
    args = ap.parse_args(argv)
    if args.command == "manifest":
        return manifest(args.run, args.output, args.prepared, args.tokens, args.duration)
    if args.command == "prepare":
        if args.withheld:
            return prepare_withheld(args.date)
        return prepare([i.upper() for i in args.iso] if args.iso else None, args.date)
    if args.command == "hosts":
        return hosts(args.apply)
    if args.command == "stage":
        return (stage_round if args.round else stage)(args.result, args.run, args.date)
    if args.command == "verify":
        return verify([i.upper() for i in args.iso] if args.iso else None)
    if args.command == "admit":
        return admit()
    return report()


if __name__ == "__main__":
    sys.exit(main())
