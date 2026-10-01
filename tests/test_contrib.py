#!/usr/bin/env python3
"""
Citizen contributions and the two-person rule (model/contrib.py, DECISIONS #85).

    python3 -m unittest discover -s tests -v

The rule is mechanical, so it is tested as one: who may review, what a review does, and that the forms
offer exactly the model's vocabulary. Staging is redirected to a temporary directory; nothing here
reads or writes GitHub.
"""
from __future__ import annotations

import csv
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "model"))

import contrib  # noqa: E402


def issue(number, login, body, labels, created="2026-10-01T10:00:00Z", title="t"):
    return {"number": number, "user": {"login": login}, "body": body, "labels": [{"name": l} for l in labels],
            "created_at": created, "title": title}


def form(**fields) -> str:
    return "\n\n".join(f"### {k}\n\n{v}" for k, v in fields.items())


TERMS_SUBMIT = "\n".join([
    "- [X] The document is public: anyone can open the URL without logging in.",
    "- [X] It is not confidential, classified or leaked material.",
    "- [X] My submission contains no one's personal data.",
    "- [X] I license my contribution under CC BY 4.0 and sign it off under the Developer Certificate of Origin (https://developercertificate.org).",
    "- [ ] Credit me by my GitHub handle in the outputs (optional).",
])
TERMS_REVIEW = "- [X] I license this review under CC BY 4.0 and sign it off under the DCO."


def submit_body(**over) -> str:
    f = {"Country": "NL", "What it is about": "Holding: Tax", "Which fact": "Name of the register or system",
         "What this is": "A new fact (fills a gap)", "URL": "https://www.belastingdienst.nl/x",
         "Language of the document": "nl",
         "Quote": "De Belastingdienst beheert het centrale register van alle belastingplichtigen in Nederland",
         "English translation": "_No response_", "Value": "centrale register", "Published": "2026",
         "Terms": TERMS_SUBMIT}
    f.update(over)
    return form(**f)


def review_body(claim, verdict="Confirmed: the quote is on the page and establishes the value",
                languages="nl, en", conflict="None") -> str:
    return form(**{"Claim id or submission": claim, "Verdict": verdict, "Reason": "Found it on the page.",
                   "Languages you read": languages, "Conflict of interest": conflict, "Terms": TERMS_REVIEW})


class Forms(unittest.TestCase):
    def test_the_forms_offer_exactly_the_models_vocabulary(self):
        f = contrib.forms()["submit-source.yml"]
        drop = {b["id"]: b["attributes"]["options"] for b in f["body"] if b["type"] == "dropdown"}
        self.assertEqual(drop["country"], list(contrib.LANGUAGES))
        self.assertEqual(drop["subject"], [label for label, _ in contrib.subjects()])
        with (ROOT / "model" / "holding_classes.csv").open(encoding="utf-8") as fh:
            n_classes = sum(1 for _ in csv.DictReader(fh))
        self.assertEqual(sum(1 for s in drop["subject"] if s.startswith("Holding:")), n_classes)

    def test_the_committed_forms_are_the_generated_ones(self):
        for name, f in contrib.forms().items():
            committed = (contrib.FORMS / name).read_text(encoding="utf-8")
            self.assertIn(contrib._yaml(f), committed, f"{name} is stale: run python3 model/contrib.py forms")


class Parsing(unittest.TestCase):
    def test_a_complete_submission_becomes_a_staged_finding(self):
        s = contrib.submission(issue(7, "alice", submit_body(), ["submission"]))
        self.assertEqual(s["claim"], "record:NL:tax:register")
        self.assertEqual((s["relation"], s["submitter"], s["attribution"]), ("fills_gap", "alice", False))
        self.assertEqual(s["quote_english"], "")

    def test_an_indicator_submission_names_the_indicator_claim(self):
        s = contrib.submission(issue(8, "alice", submit_body(**{
            "What it is about": "Indicator L1: Jurisdiction requirement", "Which fact": "Indicator value (yes / partial / no)",
            "Value": "yes"}), ["submission"]))
        self.assertEqual(s["claim"], "indicator:NL:L1")

    def test_a_submission_without_every_required_attestation_is_refused(self):
        body = submit_body(Terms=TERMS_SUBMIT.replace("- [X] It is not confidential", "- [ ] It is not confidential"))
        self.assertIsNone(contrib.submission(issue(9, "alice", body, ["submission"])))


class TwoPersonRule(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.saved = (contrib.SUBMISSIONS, contrib.REVIEWS, contrib.ROSTER)
        contrib.SUBMISSIONS, contrib.REVIEWS = self.tmp / "s", self.tmp / "r"
        contrib.ROSTER = self.tmp / "reviewers.csv"
        contrib.ROSTER.write_text("handle,languages,countries,added,decision\n"
                                  "bob,nl;en,NL,2026-10-01,#85\ncarol,nl,NL,2026-10-01,#85\n"
                                  "dave,de,DE,2026-10-01,#85\nalice,nl,NL,2026-10-01,#85\n", encoding="utf-8")
        contrib.ingest_issues([issue(7, "alice", submit_body(), ["submission"])])

    def tearDown(self):
        contrib.SUBMISSIONS, contrib.REVIEWS, contrib.ROSTER = self.saved

    def review(self, number, login, claim="#7", **kw):
        contrib.ingest_issues([issue(number, login, review_body(claim, **kw), ["review"])])

    def state(self, claim="#7"):
        return contrib.status(reg={}).get(claim, {})

    def test_one_eligible_confirmation_verifies(self):
        self.review(10, "bob")
        self.assertEqual(self.state()["state"], "verified")

    def test_the_submitter_cannot_review_their_own_submission(self):
        self.review(10, "alice")
        self.assertEqual(self.state()["state"], "unreviewed")
        self.assertEqual(self.state()["ignored"][0]["why"], "the reviewer submitted this fact")

    def test_someone_not_on_the_roster_does_not_count(self):
        self.review(10, "mallory")
        self.assertEqual(self.state()["ignored"][0]["why"], "not on the reviewer roster")

    def test_the_declared_document_language_decides_who_may_review(self):
        contrib.ingest_issues([issue(20, "alice", submit_body(**{"Language of the document": "de"}), ["submission"])])
        self.review(21, "dave", claim="#20", languages="de")
        self.assertEqual(self.state("#20")["state"], "verified")

    def test_a_reviewer_who_does_not_read_the_language_does_not_count(self):
        self.review(10, "dave", languages="de")
        self.assertEqual(self.state()["ignored"][0]["why"], "does not read the source's language")

    def test_a_declared_conflict_does_not_count(self):
        self.review(10, "bob", conflict="I work for the Belastingdienst")
        self.assertEqual(self.state()["ignored"][0]["why"], "declared a conflict of interest")

    def test_one_rejection_disputes_two_withdraw(self):
        rejected = "Rejected: the quote is missing or does not establish the value"
        self.review(10, "bob", verdict=rejected)
        self.assertEqual(self.state()["state"], "disputed")
        self.review(11, "carol", verdict=rejected)
        self.assertEqual(self.state()["state"], "withdrawn")

    def test_two_confirmations_outvote_one_rejection(self):
        self.review(10, "bob", verdict="Rejected: the quote is missing or does not establish the value")
        self.review(11, "carol")
        self.assertEqual(self.state()["state"], "disputed")
        contrib.ROSTER.write_text(contrib.ROSTER.read_text() + "erin,nl,NL,2026-10-01,#85\n", encoding="utf-8")
        self.review(12, "erin")
        self.assertEqual(self.state()["state"], "verified")

    def test_a_reviewer_counts_once_however_often_they_review(self):
        rejected = "Rejected: the quote is missing or does not establish the value"
        self.review(10, "bob", verdict=rejected)
        self.review(11, "bob", verdict=rejected)
        self.assertEqual(self.state()["state"], "disputed")


class Disclaimer(unittest.TestCase):
    def test_no_human_verification_reads_exactly_as_before(self):
        import evidence  # noqa: PLC0415
        self.assertEqual(evidence.disclaimer(0, 1390), evidence.DISCLAIMER)

    def test_a_measured_share_is_stated_once_there_is_one(self):
        import evidence  # noqa: PLC0415
        self.assertIn("12 of 1390 facts also verified by a person", evidence.disclaimer(12, 1390))


if __name__ == "__main__":
    unittest.main()
