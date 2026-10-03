# Testing: what is tested, where it runs, and what it proves

Every suite in the project: where it runs, and what failing it would mean. The rule throughout is that a new
check is shown to **fail first**, on a deliberately broken input, before it is trusted to pass (#92).

## Where the checks run

| When | What runs | Where it is defined |
|---|---|---|
| Before every commit you make | `./test.sh` (all stages below); the security gate on commit | `test.sh` |
| On every pull request | `./test.sh --no-pdf`, `npm audit --audit-level=high` (root and `web/`), gitleaks, Python tests | `.github/workflows/ci.yml` |
| On every push to `main` (a production deploy) | `./test.sh` with PDFs, the dependency audit, `factcheck.py gate`, then the deploy and `model/smoke.py` | `.github/workflows/deploy.yml` |
| Every Monday, 06:17 UTC | `model/smoke.py` against the live site, and `fetch_eurostat.py --check` for new vintages | `.github/workflows/monitor.yml` |
| Every day, 07:41 UTC | `model/ask_smoke.py`: one fixed question to the live `/ask`, which must answer with a citation | `.github/workflows/monitor.yml` |
| Before a release, by hand | the fact-check stability sample (`factcheck.py prepare --sample 50`) and mutation testing (below) | `docs/fact-check.md`, this file |
| Before trusting a checkout or a release | `./run.sh reproduce`: a fresh clone of HEAD, every output regenerated, then `./test.sh --no-e2e` | `model/reproduce.py` |

## The stages of `./test.sh`

| # | Stage | What it proves |
|---|---|---|
| 1 | Python unit tests (`tests/`) | The model, evidence rules, fact check, provenance, workflows and docs hold. See below |
| 2 | Verification ledger | `model/sources.py`: the source ledger is valid |
| 3 | National data register | `model/national_data.py`: the register is valid |
| 4 | Every fact sourced | `document.py --check`: every printed value resolves to a checked citation |
| 5 | `/ask` type-check | `api/` compiles against the real Anthropic SDK |
| 6 | Generated files current | the briefs, CSVs, bundle, `/ask` corpus and reports equal a fresh regeneration |
| 7 | Admission reproduces | the registers rebuild from the committed evidence |
| 8 | Fact-check ledger and audit file reproduce | `factcheck.py replay` and `audit --check` ([`docs/fact-check.md`](fact-check.md)) |
| 9 | PDFs compile and are inspected | 28 PDFs build; `book/check_pdfs.py` checks each one: disclaimer, both appendices, country named, fonts embedded, size budget, and the 4 previews (needs poppler; CI installs it) |
| 10–13 | Web: types, lint, formatting, Vitest | `tsc`, ESLint, Prettier, and the component and `/ask` unit tests |
| 14 | Production build | `vite build` succeeds |
| 15 | Size budget | gzipped: data bundle ≤ 900 KB, all JavaScript ≤ 400 KB |
| 16 | Browser tests | Playwright in Chrome, Firefox, desktop Safari (WebKit), iPhone SE and iPhone 17 Pro: every route renders real data, at 375 px, in print; axe in light and dark mode (Chrome); visual regression against macOS baselines (Chrome on macOS only) |

`--no-e2e` skips stage 16 and `--no-pdf` skips stage 9.

## The Python suite, by subject

- **Content and evidence:** `test_evidence`, `test_methodology`, `test_provenance`, `test_sources`,
  `test_research`, `test_vetting`, `test_national_data`, `test_sovereignty`, `test_model`, `test_book`,
  `test_ask_corpus`, `test_emoji`, `test_institutions`.
- **The fact check:** `test_factcheck`. It covers the rule, the hash, stage refusals, the gate, withholding,
  the appendix in every asset, the runbook's commands and the ledger replay.
- **Generated inputs:** `test_properties`. Seeded random cases, 500 per property:
  - a figure is found in any EU number format, and a changed digit never is;
  - a number found only in the translation does not count;
  - the fact hash changes with any covered field, and only then;
  - no author set gets a checker that wrote it;
  - every state sits inside its own range.

  Each was shown failing against a deliberately broken rule.
- **Hypothesis:** `test_hypothesis` searches and shrinks the same rules. It needs `requirements-dev.txt` (exact pins
  with hashes; CI installs it) and skips with a message without it.
- **The network layer:** `test_fetch_network`, against a real HTTP server on localhost:
  - robots `Disallow` is obeyed, and a refused robots.txt is not a rule;
  - a 403 is recorded once, never retried;
  - redirects are followed;
  - a dead host is an error result, not an exception;
  - archive snapshots must match the exact host.

  It uses no internet.
- **The live site:** `test_smoke` keeps `model/smoke.py` covering every e2e route and every member state. It
  also shows the smoke test fails against a server that serves the wrong things.
- **Delivery:** `test_workflows`, `test_vercel_config`, `test_ignore_rules`, `test_artifacts`, `test_tokens`,
  `test_repeatability`, `test_docs`, `test_contrib`, `test_fetch`.

## The live-site smoke test

`python3 model/smoke.py [--site URL] [--bundle web/public/data/eu27.json]` checks, from outside:
- every reader route answers with HTML;
- the report, all 27 country PDFs and the 4 previews answer with their type;
- every security header `vercel.json` sets is served as set;
- indexing is off;
- `www` redirects to the apex;
- the TLS certificate is valid for 14 more days or longer;
- with `--bundle`, the served data is the committed data.

It runs after every deploy and every week.

## Phones

The browser tests run on emulated iPhone SE and iPhone 17 Pro, in WebKit, Safari's engine: every route
renders, nothing scrolls sideways, and the disclaimer stays visible. Three fixes came from an iPhone audit on
2026-10-02:
- **The disclaimer banner** took a quarter of a phone screen. Its first sentence now stays visible on every
  page, and the rest is one tap away.
- **The `/ask` question field** was 14 px. Safari zooms into anything under 16 px, so it is now 16 px.
- **Navigation links** were 20 px tall. They are now 28 px, over WCAG 2.2's 24 px minimum.

## Visual regression

`web/e2e/visual.spec.ts` compares 10 screenshots against committed baselines: 4 pages in light and dark mode
at 1280 px, and 2 at 375 px. Fonts render differently per operating system, so the baselines are macOS
Chrome ones, and the test is skipped elsewhere, including in CI. After a deliberate design change, update
them with `npx playwright test e2e/visual.spec.ts --project=chrome --update-snapshots`, and commit the
images with the change.

## Fact-check stability

`python3 model/factcheck.py prepare --sample 50 --seed <n>` draws confirmed facts and puts them to the
*other* checker model. Then:
1. Run the workflow.
2. `stage --sample 1`.
3. `factcheck.py stability --run <id> --prepared <run>`.

The result measures how often a second checker disagrees with the first. It goes in
`model/research/factcheck/stability/` and the audit file, and never changes a verdict. Run it before each
release, or quarterly.

## Mutation testing

This is an audit, not a CI step. Run `mutmut` (3.8.0, in a throwaway venv and a throwaway clone) on
`model/evidence.py` against `test_evidence`, `test_properties` and `test_hypothesis`. It makes small changes
to the code and checks that some test fails for each one. A surviving mutant is an assertion the suite is
missing. Results and follow-ups are recorded in `CHANGELOG.md`.

Result on 2026-10-02: 83 of 98 killed. After tests were added for the gaps it showed, 91 of 98 (93%). The 7
survivors:
- the `__main__` print block;
- two likely-equivalent changes: the thousands-group count, and the blank-query flag in `_url_key`;
- three narrow paths without a test yet: the tier of an unparseable archive URL, the Eurostat hash filter in
  `dataset_hashes`, and the human-verified grade in `assess`.

Run the audit again with `python3 tests/tools/mutation_audit.py model/evidence.py tests.test_evidence
tests.test_properties tests.test_hypothesis`, from a throwaway clone.

## Still waiting on the owner

- **The live `/ask` check** runs daily, but reports "not configured" until `ANTHROPIC_API_KEY` is set in
  Vercel. Then set the repository variable `ASK_LIVE` to `true` so that a failure fails the run.
- **The mobile reader** (`mobile/`, schema 1) carries 4 Dependabot alerts that only a port or a removal clears.
