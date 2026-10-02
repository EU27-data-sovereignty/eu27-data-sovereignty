#!/usr/bin/env python3
"""
Every printed fact checked by the model that did not write it, before it ships (#87).

    python3 -m unittest discover -s tests -v

The rule picks the checker; the hash ties a verdict to the fact as printed; `stage` refuses a checker that
is not the model asked for or that wrote the fact; the gate fails on anything missing, stale, disagreeing
or ineligible; and every asset carries the appendix that explains it.
"""
from __future__ import annotations

import copy
import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "model"))
sys.path.insert(0, str(ROOT / "book"))

import document  # noqa: E402
import factcheck  # noqa: E402

BUNDLE = json.loads(factcheck.BUNDLE.read_text(encoding="utf-8"))
FABLE, OPUS = factcheck.CHECKERS["fable"], factcheck.CHECKERS["opus"]


class Rule(unittest.TestCase):
    def test_the_checker_is_the_model_that_did_not_write_it(self):
        self.assertEqual(factcheck.checker_for({OPUS}), FABLE)
        self.assertEqual(factcheck.checker_for({FABLE}), OPUS)

    def test_an_unrecorded_person_or_program_author_goes_to_fable(self):
        for who in ({"unrecorded"}, {"person:someone"}, {"program:fetch_eurostat.py"}):
            self.assertEqual(factcheck.checker_for(who), FABLE)

    def test_no_checker_when_both_models_wrote_it(self):
        self.assertEqual(factcheck.checker_for({OPUS, FABLE}), "")

    def test_ineligible_names_the_reason(self):
        self.assertEqual(factcheck.ineligible(FABLE, {OPUS}), "")
        self.assertIn("wrote this fact", factcheck.ineligible(OPUS, {OPUS}))
        self.assertIn("not one of", factcheck.ineligible("claude-sonnet-5-5", {"unrecorded"}))


class FactHash(unittest.TestCase):
    def setUp(self):
        self.fact = next(f for f in factcheck.facts(BUNDLE) if f["citations"] and f["citations"][0]["quote"])

    def test_stable(self):
        self.assertEqual(factcheck.fact_sha256(self.fact), factcheck.fact_sha256(copy.deepcopy(self.fact)))

    def test_changes_with_the_printed_text_quote_or_fetched_document(self):
        before = factcheck.fact_sha256(self.fact)
        for path in (("printed",), ("citations", 0, "quote"), ("citations", 0, "fetched"),
                     ("citations", 0, "url"), ("what",)):
            f = copy.deepcopy(self.fact)
            target = f
            for k in path[:-1]:
                target = target[k]
            target[path[-1]] = str(target[path[-1]]) + " (changed)"
            self.assertNotEqual(factcheck.fact_sha256(f), before, path)

    def test_every_printed_fact_is_listed_once(self):
        claims = [f["claim"] for f in factcheck.facts(BUNDLE)]
        self.assertEqual(len(claims), len(set(claims)))
        self.assertEqual(sorted(claims), sorted(BUNDLE["claims"]))


class Sandbox(unittest.TestCase):
    """Runs factcheck against a temporary ledger, staging area and audit file."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.patches = [mock.patch.object(factcheck, name, self.tmp / rel) for name, rel in
                        (("LEDGER", "ledger.csv"), ("STAGED", "staged"), ("MANIFESTS", "runs"),
                         ("CACHE", "cache"), ("AUDIT", "audit.md"))]
        for p in self.patches:
            p.start()
        self.facts = factcheck.facts(BUNDLE)
        self.who = factcheck.authors(BUNDLE)

    def tearDown(self):
        for p in self.patches:
            p.stop()

    def full_ledger(self, **override) -> dict:
        rows = {}
        for f in self.facts:
            rows[f["claim"]] = {"claim": f["claim"], "fact_sha256": factcheck.fact_sha256(f),
                                "author_model": ";".join(sorted(self.who[f["claim"]])),
                                "checker_model": factcheck.checker_for(self.who[f["claim"]]),
                                "verdict": "supported", "reason": "fixture", "checked_url": "", "run": "r1",
                                "checked": "2026-10-01"}
        return {c: {**r, **override.get(c, {})} for c, r in rows.items()}

    def write(self, ledger: dict) -> None:
        factcheck._write(factcheck.LEDGER, factcheck.LFIELDS, [ledger[c] for c in sorted(ledger)])

    def gate(self) -> tuple[int, str]:
        out = io.StringIO()
        with redirect_stdout(out):
            code = factcheck.gate(strict=True)
        return code, out.getvalue()


class Gate(Sandbox):
    def passing(self, ledger: dict) -> None:
        self.write(ledger)
        with redirect_stdout(io.StringIO()):
            factcheck.audit(check=False)

    def test_passes_when_every_fact_is_current_supported_and_eligible(self):
        self.passing(self.full_ledger())
        code, out = self.gate()
        self.assertEqual(code, 0, out)
        self.assertIn(f"{len(self.facts)} of {len(self.facts)} printed facts", out)

    def test_a_withheld_fact_does_not_block_the_gate(self):
        ledger = self.full_ledger()
        withheld = {"claim": "record:XX:none:register", "fact_sha256": "1" * 64, "author_model": "unrecorded",
                    "checker_model": FABLE, "verdict": "not_supported", "reason": "fixture", "checked_url": "",
                    "run": "r1", "checked": "2026-10-01"}
        self.passing({**ledger, withheld["claim"]: withheld})
        code, out = self.gate()
        self.assertEqual(code, 0, out)
        self.assertIn("record:XX:none:register", factcheck.AUDIT.read_text(encoding="utf-8"))

    def test_fails_on_a_fact_never_checked(self):
        ledger = self.full_ledger()
        claim = self.facts[0]["claim"]
        del ledger[claim]
        self.passing(ledger)
        code, out = self.gate()
        self.assertEqual(code, 1)
        self.assertIn(f"{claim}: never checked", out)

    def test_fails_when_the_fact_changed_after_its_check(self):
        claim = self.facts[0]["claim"]
        self.passing(self.full_ledger(**{claim: {"fact_sha256": "0" * 64}}))
        code, out = self.gate()
        self.assertEqual(code, 1)
        self.assertIn(f"{claim}: changed since it was checked", out)

    def test_fails_on_a_disagreement(self):
        claim = self.facts[0]["claim"]
        self.passing(self.full_ledger(**{claim: {"verdict": "not_supported", "reason": "says 2019, not 2021"}}))
        code, out = self.gate()
        self.assertEqual(code, 1)
        self.assertIn("not supported: says 2019, not 2021", out)

    def test_fails_when_the_checker_wrote_the_fact(self):
        claim = self.facts[0]["claim"]
        self.passing(self.full_ledger(**{claim: {"checker_model": OPUS}}))
        with mock.patch.object(factcheck, "authors", lambda b: {**self.who, claim: {OPUS}}):
            code, out = self.gate()
        self.assertEqual(code, 1)
        self.assertIn(f"checker {OPUS} wrote this fact", out)

    def test_fails_on_a_checker_outside_the_two(self):
        claim = self.facts[0]["claim"]
        self.passing(self.full_ledger(**{claim: {"checker_model": "claude-sonnet-5-5"}}))
        code, out = self.gate()
        self.assertEqual(code, 1)
        self.assertIn("is not one of", out)

    def test_fails_when_the_audit_file_is_stale(self):
        self.passing(self.full_ledger())
        factcheck.AUDIT.write_text("edited by hand\n", encoding="utf-8")
        code, out = self.gate()
        self.assertEqual(code, 1)
        self.assertIn("is stale", out)


class Stage(Sandbox):
    def batch(self, checker: str = FABLE, author: str = "unrecorded") -> tuple[str, list[dict]]:
        facts = [{**f, "fact_sha256": factcheck.fact_sha256(f), "author_model": author} for f in self.facts[:3]]
        folder = factcheck.CACHE / "prep" / "in"
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "XX-001.json").write_text(json.dumps({"iso": facts[0]["iso"], "checker_model": checker,
                                                         "facts": facts}), encoding="utf-8")
        return "XX-001", facts

    def run_stage(self, results: list) -> tuple[int, str]:
        path = self.tmp / "out.json"
        path.write_text(json.dumps(results), encoding="utf-8")
        out = io.StringIO()
        with redirect_stdout(out):
            code = factcheck.stage(path, "run1", "prep")
        return code, out.getvalue()

    def answer(self, facts: list[dict], model: str) -> dict:
        return {"checker_model": model, "verdicts": [
            {"claim": f["claim"], "verdict": "supported", "quote_found": True, "checked_url": "https://x",
             "reason": "ok"} for f in facts]}

    def test_keeps_a_batch_from_the_model_asked_for(self):
        name, facts = self.batch()
        code, out = self.run_stage([{"batch": name, "review": self.answer(facts, FABLE)}])
        self.assertEqual(code, 0, out)
        staged = json.loads((factcheck.STAGED / "run1" / f"{name}.json").read_text())
        self.assertEqual({v["checker_model"] for v in staged["verdicts"]}, {FABLE})

    def test_refuses_a_checker_reporting_another_model(self):
        name, facts = self.batch()
        code, out = self.run_stage([{"batch": name, "review": self.answer(facts, OPUS)}])
        self.assertEqual(code, 1)
        self.assertIn(f"asked for {FABLE}, checker reported {OPUS}", out)
        self.assertFalse((factcheck.STAGED / "run1" / f"{name}.json").exists())

    def test_refuses_a_checker_that_wrote_the_facts(self):
        name, facts = self.batch(checker=OPUS, author=OPUS)
        code, out = self.run_stage([{"batch": name, "review": self.answer(facts, OPUS)}])
        self.assertEqual(code, 1)
        self.assertIn("wrote this fact", out)

    def test_refuses_a_verdict_for_a_fact_not_given(self):
        name, facts = self.batch()
        review = self.answer(facts, FABLE)
        review["verdicts"].append({**review["verdicts"][0], "claim": "record:XX:none:register"})
        code, out = self.run_stage([{"batch": name, "review": review}])
        self.assertEqual(code, 1)
        self.assertIn("not in this batch", out)

    def test_an_email_address_in_a_checkers_text_is_removed(self):
        name, facts = self.batch()
        review = self.answer(facts, FABLE)
        review["verdicts"][0]["reason"] = "Names the contact someone@example.org and the register."
        self.run_stage([{"batch": name, "review": review}])
        staged = json.loads((factcheck.STAGED / "run1" / f"{name}.json").read_text())
        self.assertEqual(staged["verdicts"][0]["reason"],
                         "Names the contact [email address removed] and the register.")

    def test_a_missing_verdict_is_recorded_as_unclear_not_supported(self):
        name, facts = self.batch()
        review = self.answer(facts, FABLE)
        review["verdicts"] = review["verdicts"][:1]
        self.run_stage([{"batch": name, "review": review}])
        staged = json.loads((factcheck.STAGED / "run1" / f"{name}.json").read_text())
        self.assertEqual([v["verdict"] for v in staged["verdicts"]], ["supported", "unclear", "unclear"])


class Withhold(unittest.TestCase):
    """A fact the check did not confirm, exactly as printed, is withheld as disputed (#89)."""

    @classmethod
    def setUpClass(cls):
        cls.src = document.Sources()
        cls.facts = factcheck.facts(BUNDLE)

    def sha_via_sources(self, f: dict) -> str:
        found = self.src.evidence(f["claim"], f["printed"], f["categorical"])
        cites = [factcheck.citation_record(c["source_id"], self.src.reg[c["source_id"]], c["locator"],
                                           c["quote"], c["value_as_found"],
                                           bool(a["checks"].get("dataset_value_reproduced")))
                 for c, a in found]
        return factcheck.fact_sha256(factcheck.fact_record(f["claim"], f["printed"], f["categorical"], cites))

    def test_the_content_model_and_the_bundle_hash_every_fact_the_same(self):
        for f in self.facts:
            self.assertEqual(self.sha_via_sources(f), factcheck.fact_sha256(f), f["claim"])

    def row(self, f: dict, **kw) -> dict:
        return {"claim": f["claim"], "fact_sha256": factcheck.fact_sha256(f), "author_model": "unrecorded",
                "checker_model": FABLE, "verdict": "not_supported", "reason": "says 2019, not 2021.",
                "checked_url": "", "run": "r9", "checked": "2026-10-02", **kw}

    def span(self, f: dict, row: dict) -> dict:
        with mock.patch.object(self.src, "checked", {f["claim"]: row}):
            return self.src.fact(f["claim"], f["printed"], categorical=f["categorical"])

    def test_a_disagreement_on_this_exact_fact_withholds_it(self):
        f = self.facts[0]                      # its ledger row is replaced by the fixture
        span = self.span(f, self.row(f))
        self.assertEqual(span["role"], "disputed")
        self.assertIn("did not confirm this: says 2019, not 2021.", span["t"])
        self.assertIn("run r9", span["t"])

    def test_unclear_also_withholds(self):
        f = self.facts[0]                      # its ledger row is replaced by the fixture
        span = self.span(f, self.row(f, verdict="unclear"))
        self.assertEqual(span["role"], "disputed")
        self.assertIn("could not confirm", span["t"])

    def test_a_verdict_on_an_older_version_withholds_nothing(self):
        f = self.facts[0]                      # its ledger row is replaced by the fixture
        self.assertEqual(self.span(f, self.row(f, fact_sha256="0" * 64))["role"], "fact")

    def test_a_supported_verdict_prints_the_fact(self):
        f = self.facts[0]
        self.assertEqual(self.span(f, self.row(f, verdict="supported"))["role"], "fact")

    def test_the_bundle_withholds_every_current_disagreement(self):
        printed = {f["claim"] for f in self.facts}
        for claim, r in factcheck.load_ledger().items():
            if r["verdict"] != "supported":
                self.assertNotIn(claim, printed, claim)


class Commands(unittest.TestCase):
    SKILL = (ROOT / ".claude" / "skills" / "factcheck" / "SKILL.md").read_text(encoding="utf-8")

    def test_every_factcheck_subcommand_the_skill_names_exists(self):
        import re  # noqa: PLC0415
        named = set(re.findall(r"\./run\.sh factcheck ([a-z]+)", self.SKILL))
        source = (ROOT / "model" / "factcheck.py").read_text(encoding="utf-8")
        choices = set(re.findall(r'"([a-z]+)"', re.search(r"choices=\[([^\]]+)\]", source).group(1)))
        self.assertTrue(named)
        self.assertEqual(sorted(named - choices), [])

    def test_the_skill_runs_the_checked_in_workflow_and_never_pushes(self):
        self.assertIn("scriptPath: model/research/factcheck/workflow.js", self.SKILL)
        self.assertTrue(factcheck.WORKFLOW.exists())
        self.assertIn("Never push without the", self.SKILL)

    def test_the_workflow_sets_the_model_on_every_checker(self):
        js = factcheck.WORKFLOW.read_text(encoding="utf-8")
        self.assertIn("model: b.model", js)
        self.assertEqual(js.count("agent("), 1)


class Appendix(unittest.TestCase):
    """Every asset carries the fact-check appendix (#87)."""

    def test_each_country_appendix_lists_exactly_its_printed_facts(self):
        for iso, doc in BUNDLE["documents"].items():
            facts = next(x for x in BUNDLE["factcheck"]["countries"][iso]["sections"] if x["id"] == "f-facts")
            table = facts["blocks"][-1]
            self.assertEqual(sorted(r[0]["t"] for r in table["rows"]), sorted(document.claims_used(doc)), iso)

    def test_the_appendix_prints_no_fact_and_says_it_is_not_a_person(self):
        docs = [BUNDLE["factcheck"]["eu"], *BUNDLE["factcheck"]["countries"].values()]
        for d in docs:
            self.assertFalse([s for s in document.walk_spans(d) if s["role"] == "fact"])
        import evidence  # noqa: PLC0415
        text = " ".join(s["t"] for s in document.walk_spans(BUNDLE["factcheck"]["eu"]))
        self.assertIn(evidence.DISCLAIMER, text)
        self.assertIn("not by a person", text)

    def test_the_pdfs_carry_it(self):
        import report  # noqa: PLC0415
        self.assertIn("= Appendix: fact check", report.report_typ(BUNDLE))
        self.assertIn("= Appendix: fact check", report.country_typ(BUNDLE, "DE"))

    def test_every_brief_carries_it(self):
        for iso in BUNDLE["documents"]:
            brief = (ROOT / "countries" / iso / "GOAL.md").read_text(encoding="utf-8")
            self.assertIn("## Appendix: fact check", brief, iso)

    def test_the_web_poster_and_ask_carry_it(self):
        web = ROOT / "web" / "src"
        self.assertIn('path="fact-check/:iso"', (web / "App.tsx").read_text(encoding="utf-8"))
        self.assertIn('href="/fact-check"', (web / "components" / "ProvenanceBanner.tsx").read_text(encoding="utf-8"))
        self.assertIn("/fact-check/${code}", (web / "pages" / "Country.tsx").read_text(encoding="utf-8"))
        self.assertIn("bundle.factcheck.lines[code]", (web / "pages" / "Poster.tsx").read_text(encoding="utf-8"))
        self.assertEqual(sorted(BUNDLE["factcheck"]["lines"]), sorted(BUNDLE["documents"]))
        corpus = (ROOT / "api" / "_corpus.json").read_text(encoding="utf-8")
        self.assertIn("Fact check: how each printed fact was checked by a second model", corpus)


if __name__ == "__main__":
    unittest.main()
