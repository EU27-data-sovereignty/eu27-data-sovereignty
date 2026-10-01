#!/usr/bin/env python3
"""
Citizen contributions and human review, under a two-person rule (DECISIONS #85).

    python3 model/contrib.py forms                 # regenerate the two GitHub issue forms from the model
    python3 model/contrib.py ingest [--from FILE]  # issues -> research/contrib/ (read-only `gh api`)
    python3 model/contrib.py status                # human-review status per fact; eligibility applied
    python3 model/contrib.py audit-sample --n 60 --seed 2026   # a random sample of unreviewed facts

Why this file exists
--------------------
Agents found every source so far, and no person had verified any finding. Citizens of each member state
close both gaps: they know where their state publishes things, they read its language, and they can
check a fact a machine only matched. So anyone may submit a source (`submit-source` form) or review a
printed fact (`review-fact` form), pseudonymously, through GitHub.

Nothing a contributor writes is trusted on its own. A submitted source goes through the same mechanical
checks as agent research (fetch, hash, quote, value in quote, tier; vetting.py). A fact counts as
**verified by a person** only when an *eligible* reviewer confirms it: someone on the roster
(model/contrib/reviewers.csv, added by a reviewed pull request), who is not the person who submitted
it, who declares they read the source's language, and who declares no conflict of interest. That is the
two-person rule: whoever found it, someone else checked it.

A rejection is never acted on silently: one eligible rejection makes the fact *disputed*; a second
withdraws it, unless two eligible reviewers have confirmed it.

Personal data: a GitHub handle is already public, and pseudonymous. It is stored because the two-person
rule needs it; it is shown in outputs only when the contributor opted into attribution.
"""
from __future__ import annotations

import argparse
import csv
import json
import random
import re
import subprocess
import sys
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "model"))

REPO = "pieteradejong/sovereign-data-centers"
CONTRIB = ROOT / "model" / "research" / "contrib"
SUBMISSIONS = CONTRIB / "submissions"
REVIEWS = CONTRIB / "reviews"
ROSTER = ROOT / "model" / "contrib" / "reviewers.csv"
ROSTER_FIELDS = ["handle", "languages", "countries", "added", "decision"]
FORMS = ROOT / ".github" / "ISSUE_TEMPLATE"

# The official languages of each member state (ISO 639-1), the fallback when a source records none.
LANGUAGES = {
    "AT": {"de"}, "BE": {"nl", "fr", "de"}, "BG": {"bg"}, "CY": {"el", "tr"}, "CZ": {"cs"}, "DE": {"de"},
    "DK": {"da"}, "EE": {"et"}, "EL": {"el"}, "ES": {"es"}, "FI": {"fi", "sv"}, "FR": {"fr"},
    "HR": {"hr"}, "HU": {"hu"}, "IE": {"en", "ga"}, "IT": {"it"}, "LT": {"lt"}, "LU": {"lb", "fr", "de"},
    "LV": {"lv"}, "MT": {"mt", "en"}, "NL": {"nl"}, "PL": {"pl"}, "PT": {"pt"}, "RO": {"ro"},
    "SE": {"sv"}, "SI": {"sl"}, "SK": {"sk"},
}
FIELDS = {  # form label -> claim kind
    "Name of the register or system": "register", "Who operates it": "operator",
    "How many records it holds": "count", "Its data size": "size", "Its legal basis": "legal_basis",
    "Where its infrastructure runs": "foreign_dependency", "Indicator value (yes / partial / no)": "indicator",
}
KINDS = {"A new fact (fills a gap)": "fills_gap", "A better source for a printed fact": "upgrade",
         "Newer information": "supersedes", "A correction (the printed value is wrong)": "contradicts"}
VERDICTS = {"Confirmed: the quote is on the page and establishes the value": "confirmed",
            "Rejected: the quote is missing or does not establish the value": "rejected",
            "Can't tell": "unsure"}
NO_CONFLICT = "None"


# --------------------------------------------------------------------------- #
# The model's vocabulary, for the forms
# --------------------------------------------------------------------------- #

def subjects() -> list[tuple[str, str]]:
    """(label, id) for every holding class and indicator, in the model's order."""
    with (ROOT / "model" / "holding_classes.csv").open(newline="", encoding="utf-8") as fh:
        classes = [(f"Holding: {r['label']}", r["class_id"]) for r in csv.DictReader(fh)]
    with (ROOT / "model" / "indicators.csv").open(newline="", encoding="utf-8") as fh:
        inds = [(f"Indicator {r['id']}: {r['label']}", f"indicator:{r['id']}") for r in csv.DictReader(fh)]
    return classes + inds


def _dropdown(id_: str, label: str, options: list[str], description: str = "") -> dict:
    return {"type": "dropdown", "id": id_, "attributes": {"label": label, "description": description,
                                                           "options": options},
            "validations": {"required": True}}


def _field(type_: str, id_: str, label: str, description: str, required: bool = True) -> dict:
    return {"type": type_, "id": id_, "attributes": {"label": label, "description": description},
            "validations": {"required": required}}


def forms() -> dict[str, dict]:
    """The two issue forms, generated from the model so their choices cannot drift from it."""
    countries = list(LANGUAGES)
    attest = {"type": "checkboxes", "id": "terms", "attributes": {"label": "Terms", "options": [
        {"label": "The document is public: anyone can open the URL without logging in.", "required": True},
        {"label": "It is not confidential, classified or leaked material.", "required": True},
        {"label": "My submission contains no one's personal data.", "required": True},
        {"label": "I license my contribution under CC BY 4.0 and sign it off under the Developer "
                  "Certificate of Origin (https://developercertificate.org).", "required": True},
        {"label": "Credit me by my GitHub handle in the outputs (optional).", "required": False}]}}
    submit = {
        "name": "Submit a source", "description": "A public document that establishes a fact about a member state",
        "title": "[source] ", "labels": ["submission"],
        "body": [
            {"type": "markdown", "attributes": {"value": (
                "Thank you. Every submission is checked by machine (the page is fetched and the quote "
                "must be on it) and then by a different person who reads the language. See "
                "CONTRIBUTING.md. Quote in the document's own language; a translation is optional.")}},
            _dropdown("country", "Country", countries),
            _dropdown("subject", "What it is about", [label for label, _ in subjects()]),
            _dropdown("field", "Which fact", list(FIELDS)),
            _dropdown("kind", "What this is", list(KINDS)),
            _field("input", "url", "URL", "The exact page or PDF, https only."),
            _field("textarea", "quote", "Quote", "8 to 60 words, copied verbatim from the page, in its own language."),
            _field("textarea", "quote_english", "English translation", "Optional.", required=False),
            _field("input", "value", "Value", "What the quote establishes. Every number in it must be in the quote."),
            _field("input", "published", "Published", "YYYY, YYYY-MM or YYYY-MM-DD, if the page says.", required=False),
            attest,
        ],
    }
    review = {
        "name": "Check a fact", "description": "Confirm or reject a printed fact against its source",
        "title": "[review] ", "labels": ["review"],
        "body": [
            {"type": "markdown", "attributes": {"value": (
                "Open the fact's source, find the quote, and say whether it establishes the printed "
                "value. Reviewers must be on the reviewer roster (docs/reviewing.md); anyone may still "
                "report a problem here.")}},
            _field("input", "claim", "Claim id or submission",
                   "Filled in by the 'Check this fact' link (e.g. record:NL:tax:register), or a submission's issue number (e.g. #123)."),
            _dropdown("verdict", "Verdict", list(VERDICTS)),
            _field("textarea", "reason", "Reason", "One or two sentences."),
            _field("input", "languages", "Languages you read", "ISO codes, e.g. nl, en, de."),
            _field("input", "conflict", "Conflict of interest",
                   f"Do you work for the operator, a vendor, or the body concerned? Write {NO_CONFLICT} if not."),
            {"type": "checkboxes", "id": "terms", "attributes": {"label": "Terms", "options": [
                {"label": "I license this review under CC BY 4.0 and sign it off under the DCO.", "required": True}]}},
        ],
    }
    return {"submit-source.yml": submit, "review-fact.yml": review}


def _yaml(obj, indent: int = 0) -> str:
    """Minimal YAML for the forms (stdlib only): dicts, lists, strings, booleans."""
    pad = "  " * indent
    if isinstance(obj, dict):
        out = []
        for k, v in obj.items():
            if isinstance(v, (dict, list)) and v:
                out.append(f"{pad}{k}:\n{_yaml(v, indent + 1)}")
            else:
                out.append(f"{pad}{k}: {_scalar(v)}")
        return "\n".join(out)
    out = []
    for v in obj:
        if isinstance(v, dict):
            inner = _yaml(v, indent + 1).lstrip()
            out.append(f"{pad}- {inner}")
        else:
            out.append(f"{pad}- {_scalar(v)}")
    return "\n".join(out)


def _scalar(v) -> str:
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, list):
        return "[]"
    return json.dumps(str(v), ensure_ascii=False)


def write_forms() -> int:
    for name, form in forms().items():
        (FORMS / name).write_text("# Generated by model/contrib.py forms -- do not edit by hand.\n"
                                  + _yaml(form) + "\n", encoding="utf-8")
        print(f"wrote .github/ISSUE_TEMPLATE/{name}")
    return 0


# --------------------------------------------------------------------------- #
# Ingest: issue -> staging
# --------------------------------------------------------------------------- #

def parse_form(body: str) -> dict[str, str]:
    """An issue form's body ('### Label\\n\\nvalue') as {label: value}. '_No response_' is empty."""
    out: dict[str, str] = {}
    for block in re.split(r"^### ", body or "", flags=re.M)[1:]:
        label, _, value = block.partition("\n")
        value = value.strip()
        out[label.strip()] = "" if value == "_No response_" else value
    return out


def checked(value: str, prefix: str) -> bool:
    return any(line.lower().startswith("- [x] " + prefix.lower()) for line in value.splitlines())


def submission(issue: dict) -> dict | None:
    """A staged finding from a submit-source issue, or None if the form is incomplete."""
    f = parse_form(issue.get("body", ""))
    subject = dict(subjects()).get(f.get("What it is about", ""), "")
    field = FIELDS.get(f.get("Which fact", ""), "")
    iso = f.get("Country", "")
    if not (subject and field and iso in LANGUAGES and f.get("URL") and f.get("Quote") and f.get("Value")):
        return None
    if subject.startswith("indicator:"):
        claim = f"indicator:{iso}:{subject.split(':')[1]}"
    else:
        claim = f"record:{iso}:{subject}:{field}"
    terms = f.get("Terms", "")
    if not all(checked(terms, p) for p in ("The document is public", "It is not confidential",
                                           "My submission contains no", "I license my contribution")):
        return None
    return {"issue": issue["number"], "iso": iso, "claim": claim,
            "relation": KINDS.get(f.get("What this is", ""), "fills_gap"),
            "url": f["URL"].strip(), "quote": f["Quote"].strip(), "quote_english": f.get("English translation", "").strip(),
            "value": f["Value"].strip(), "published": f.get("Published", "").strip(),
            "title": issue.get("title", "").removeprefix("[source]").strip(), "publisher": "",
            "doc_type": "official_page", "submitter": issue["user"]["login"],
            "attribution": checked(terms, "Credit me"), "created": issue["created_at"][:10]}


def review(issue: dict) -> dict | None:
    f = parse_form(issue.get("body", ""))
    claim = f.get("Claim id or submission", "").strip()
    verdict = VERDICTS.get(f.get("Verdict", ""))
    if not claim or not verdict or not checked(f.get("Terms", ""), "I license this review"):
        return None
    langs = {x.strip().lower() for x in re.split(r"[,;\s]+", f.get("Languages you read", "")) if x.strip()}
    return {"issue": issue["number"], "claim": claim, "verdict": verdict, "reason": f.get("Reason", ""),
            "languages": sorted(langs), "conflict": f.get("Conflict of interest", "").strip(),
            "reviewer": issue["user"]["login"], "date": issue["created_at"][:10]}


def fetch_issues(label: str) -> list[dict]:
    """Every issue with this label, open or closed. Read-only."""
    r = subprocess.run(["gh", "api", "--paginate", f"repos/{REPO}/issues?labels={label}&state=all&per_page=100"],
                       capture_output=True, text=True, check=True)
    return [i for page in re.findall(r"\[.*?\](?=\[|$)", r.stdout, re.S) for i in json.loads(page)] \
        if r.stdout.strip().startswith("[") else []


def ingest(source: Path | None = None) -> int:
    issues = json.loads(source.read_text(encoding="utf-8")) if source else \
        fetch_issues("submission") + fetch_issues("review")
    return ingest_issues(issues)


def ingest_issues(issues: list[dict]) -> int:
    n_sub = n_rev = 0
    for issue in issues:
        if "pull_request" in issue:
            continue
        labels = {lab["name"] if isinstance(lab, dict) else lab for lab in issue.get("labels", [])}
        if "submission" in labels and (s := submission(issue)):
            SUBMISSIONS.mkdir(parents=True, exist_ok=True)
            (SUBMISSIONS / f"{s['issue']}.json").write_text(json.dumps(s, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
            n_sub += 1
        if "review" in labels and (r := review(issue)):
            REVIEWS.mkdir(parents=True, exist_ok=True)
            (REVIEWS / f"{r['issue']}.json").write_text(json.dumps(r, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
            n_rev += 1
    print(f"staged {n_sub} submissions and {n_rev} reviews")
    return 0


def load(folder: Path) -> list[dict]:
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted(folder.glob("*.json"))] if folder.exists() else []


# --------------------------------------------------------------------------- #
# The two-person rule
# --------------------------------------------------------------------------- #

def roster() -> dict[str, dict]:
    if not ROSTER.exists():
        return {}
    with ROSTER.open(newline="", encoding="utf-8") as fh:
        return {r["handle"].lower(): r for r in csv.DictReader(fh)}


def eligible(r: dict, submitter: str, languages: set[str], reviewers: dict[str, dict]) -> str:
    """'' if this review counts, else why not. The rule is mechanical and published (#85)."""
    who = r["reviewer"].lower()
    if who not in reviewers:
        return "not on the reviewer roster"
    if submitter and who == submitter.lower():
        return "the reviewer submitted this fact"
    if r["conflict"].strip().lower() not in (NO_CONFLICT.lower(), "no", "none.", "n/a", "geen", "keine", "aucun"):
        return "declared a conflict of interest"
    rostered = {x.strip().lower() for x in reviewers[who]["languages"].split(";") if x.strip()}
    if not (languages & set(r["languages"]) & rostered):
        return "does not read the source's language"
    return ""


def status(reg: dict | None = None) -> dict[str, dict]:
    """claim -> {state, confirmed: [...], rejected: [...], ignored: [...]}.

    state: verified (≥1 eligible confirmation, no eligible rejection, or ≥2 confirmations outvoting one),
           disputed (one eligible rejection not outvoted), withdrawn (≥2 eligible rejections, fewer than
           2 confirmations), or unreviewed."""
    import provenance  # noqa: PLC0415
    reg = reg if reg is not None else provenance.registry()
    by_claim: dict[str, list[dict]] = {}
    for c in provenance.citations():
        by_claim.setdefault(c["claim"], []).append(c)
    subs = {f"#{s['issue']}": s for s in load(SUBMISSIONS)}
    submitters = {s["claim"]: s["submitter"] for s in subs.values()}
    reviewers = roster()
    out: dict[str, dict] = {}
    for r in load(REVIEWS):
        claim = r["claim"]
        if claim in subs:                     # a review of a submission, by its issue number
            submitters = {**submitters, claim: subs[claim]["submitter"]}
            by_claim.setdefault(claim, [])
            iso_of = subs[claim]["iso"]
            langs = LANGUAGES.get(iso_of, set())
            why = eligible(r, subs[claim]["submitter"], langs, reviewers)
            st = out.setdefault(claim, {"confirmed": [], "rejected": [], "ignored": []})
            if why:
                st["ignored"].append({**r, "why": why})
            elif r["verdict"] in ("confirmed", "rejected"):
                st[r["verdict"]].append(r)
            continue
        iso = claim.split(":")[1] if claim.count(":") >= 2 else ""
        langs = {reg[c["source_id"]]["language"].lower()[:2] for c in by_claim.get(claim, [])
                 if c["source_id"] in reg and reg[c["source_id"]].get("language")} or LANGUAGES.get(iso, set())
        why = eligible(r, submitters.get(claim, ""), langs, reviewers)
        st = out.setdefault(claim, {"confirmed": [], "rejected": [], "ignored": []})
        if why:
            st["ignored"].append({**r, "why": why})
        elif r["verdict"] in ("confirmed", "rejected"):
            st[r["verdict"]].append(r)
    for st in out.values():
        c = len({r["reviewer"].lower() for r in st["confirmed"]})
        x = len({r["reviewer"].lower() for r in st["rejected"]})
        st["state"] = ("withdrawn" if x >= 2 and c < 2 else
                       "disputed" if x >= 1 and c < 2 else
                       "verified" if c >= 1 else "unreviewed")
    return out


# URL templates for renderers: {claim} and {iso} are replaced, URL-encoded, by the page or PDF that
# links them, so no renderer hard-codes the repository or the form's field names.
REVIEW_TEMPLATE = f"https://github.com/{REPO}/issues/new?template=review-fact.yml&title=%5Breview%5D%20{{claim}}&claim={{claim}}"
SUBMIT_TEMPLATE = f"https://github.com/{REPO}/issues/new?template=submit-source.yml&title=%5Bsource%5D%20&country={{iso}}"


def review_url(claim: str) -> str:
    q = urllib.parse.urlencode({"template": "review-fact.yml", "title": f"[review] {claim}", "claim": claim})
    return f"https://github.com/{REPO}/issues/new?{q}"


def submit_url(iso: str = "") -> str:
    q = urllib.parse.urlencode({"template": "submit-source.yml", "title": "[source] ", **({"country": iso} if iso else {})})
    return f"https://github.com/{REPO}/issues/new?{q}"


# --------------------------------------------------------------------------- #
# The audit sample
# --------------------------------------------------------------------------- #

def audit_sample(n: int, seed: int) -> int:
    """A seeded random sample of printed facts nobody has reviewed, stratified by state: the human
    sampling audit #25/#67 require. Prints the review links; posts nothing."""
    bundle = json.loads((ROOT / "web" / "public" / "data" / "eu27.json").read_text(encoding="utf-8"))
    reviewed = set(status())
    by_state: dict[str, list[str]] = {}
    for claim in sorted(bundle["claims"]):
        if claim not in reviewed:
            by_state.setdefault(claim.split(":")[1], []).append(claim)
    rng = random.Random(seed)
    states = sorted(by_state)
    picks: list[str] = []
    while len(picks) < n and any(by_state.values()):
        for iso in states:
            if by_state[iso] and len(picks) < n:
                picks.append(by_state[iso].pop(rng.randrange(len(by_state[iso]))))
    print(f"# Audit sample: {len(picks)} facts, seed {seed}\n")
    for claim in picks:
        print(f"- [ ] `{claim}` — {review_url(claim)}")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["forms", "ingest", "status", "audit-sample"])
    ap.add_argument("--from", dest="source", type=Path, help="ingest: issues JSON instead of the GitHub API")
    ap.add_argument("--n", type=int, default=60)
    ap.add_argument("--seed", type=int, default=2026)
    args = ap.parse_args(argv)
    if args.command == "forms":
        return write_forms()
    if args.command == "ingest":
        return ingest(args.source)
    if args.command == "audit-sample":
        return audit_sample(args.n, args.seed)
    st = status()
    counts: dict[str, int] = {}
    for s in st.values():
        counts[s["state"]] = counts.get(s["state"], 0) + 1
    print(f"{len(st)} facts with reviews: " + " ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
