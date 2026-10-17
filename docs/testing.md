# Testing: what is tested, where it runs, and what it proves

Every suite in the project: where it runs, and what failing it would mean. The rule throughout is that a new
check is shown to **fail first**, on a deliberately broken input, before it is trusted to pass (#92).

## Where the checks run

The whole pipeline, its timings and the proposed speed-ups are in [`process.md`](process.md). Every CI/CD workflow, job and check, by event, is in [`ci-cd.md`](ci-cd.md).

| When | What runs | Where it is defined |
|---|---|---|
| Before every commit you make | `./test.sh` (all stages below); the security gate on commit | `test.sh` |
| On every pull request | the gate without PDFs, `npm audit --audit-level=high` (root and `web/`), and `factcheck.py gate` reported as a warning, not a failure (#98) | `.github/workflows/ci.yml`, calling `gate.yml` |
| On every push and pull request | gitleaks over the full history, then the security gate | `.github/workflows/security.yml`, calling dotfiles' `security-reusable.yml` |
| On every push to `main` (a production deploy) | the gate with PDFs and `factcheck.py gate`, then the deploy of the gate's own build and `model/smoke.py` | `.github/workflows/deploy.yml`, calling `gate.yml` |
| Every Monday, 06:17 UTC | `model/smoke.py` against the live site, `fetch_eurostat.py --check` for new vintages, and `research.py recheck --check`: every cited source re-fetched; fails on one newly gone or missing a quote (#98) | `.github/workflows/monitor.yml` |
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
| 5 | Authored notes and agent drafts keep their contracts | `model/notes.py check`, the register: the national-AI note (#103), the sovereign-appliance note (#104), the language drafts ([`docs/i18n/README.md`](i18n/README.md)), the technical-universities note; one line each. A new note registers there, never as a stage; `tests/test_notes.py` fails on an unregistered checker |
| 6 | `/ask` type-check | `api/` compiles against the real Anthropic SDK |
| 7 | Generated files current | the briefs, CSVs, bundle, `/ask` corpus and reports equal a fresh regeneration |
| 8 | Admission reproduces | the registers rebuild from the committed evidence |
| 9 | Fact-check ledger and audit file reproduce | `factcheck.py replay` and `audit --check` ([`docs/fact-check.md`](fact-check.md)) |
| 10 | PDFs compile and are inspected | 28 PDFs build; `book/check_pdfs.py` checks each one: disclaimer, both appendices, country named, fonts embedded, size budget, and the 4 previews (needs poppler; CI installs it) |
| 11–14 | Web: types, lint, formatting, Vitest | `tsc`, ESLint, Prettier, and the component and `/ask` unit tests |
| 15 | Production build | `vite build` succeeds |
| 16 | Size budget | gzipped: data bundle ≤ 1,100 KB (900 KB until 2026-10-06), all JavaScript ≤ 400 KB |
| 17 | The mobile reader | `mobile/test.sh --ci`, the reader's own suite ([`../mobile/README.md`](../mobile/README.md), #113): node, deps, no tracked env, shell, tooling, exact pins, identity, env keys, scripts, format, lint, types; the 28 parts regenerated and checked against the manifest and the committed bundle (`model/edition.py check`); the generated tokens current; Jest with coverage floors, incl. parity with `web/` byte for byte; expo-doctor; the web export; npm audit against `mobile/audit-allowlist.json`. With `MOBILE_TEST_FLAGS=--integration` (the deploy's gate only): the edition channel round-trip against local Supabase |
| 18 | Browser tests | Playwright in Chrome, Firefox, desktop Safari (WebKit), iPhone SE and iPhone 17 Pro: every route renders real data, at 375 px, in print; axe in light and dark mode (Chrome); visual regression against macOS baselines (Chrome on macOS only) |

| 19 | The live `/ask` | `model/ask_smoke.py --require`: one question to https://eu27.cloud/api/ask, through a real Anthropic API call, must answer with citations. A rejected or missing key fails it |

`--no-e2e` skips stage 18, `--no-pdf` skips stage 10, `--no-mobile` skips stage 17 (no `mobile/node_modules`) and
`--no-live` skips stage 19. Stage 19 tests the live site,
not the checkout, and costs one request within the `eu27` workspace spend limit. Use `--no-live` offline or while the
key is being replaced.

**In CI the stages run as parallel jobs** (`.github/workflows/gate.yml`, #97). `./test.sh --only GROUP` runs one
group:
- `model`: stages 1–5 and 7–9;
- `web`: stages 6 and 11–16;
- `pdf`: stage 10;
- `mobile`: stage 17; its `--integration` round-trip runs only when the caller passes `mobile_integration: true`
  (deploy.yml does, ci.yml does not: `supabase start` would be the critical path on every branch push);
- `e2e`: stage 18, with `--project NAME` for one Playwright project. Four of the five projects need Playwright's own
  Firefox and WebKit, which `./init.sh` installs (`cd web && npx playwright install firefox webkit` by hand); the stage
  refuses to start without them rather than failing every test at launch;
- `live`: stage 19. CI runs it in the deploy job, after the deploy and against it, not in the gate. A broken key
  must not block the redeploy that fixes it.

The six groups partition the stages, and `tests/test_workflows.py` fails if a stage is outside every group or
a group is not run. Locally, `./test.sh` with no flag still runs everything in order.

## The Python suite, by subject

- **Content and evidence:** `test_evidence`, `test_methodology`, `test_provenance`, `test_sources`,
  `test_research`, `test_vetting`, `test_national_data`, `test_national_ai`, `test_sovereign_appliance`, `test_i18n_drafts`, `test_notes`, `test_permissions`, `test_sovereignty`, `test_model`, `test_book`,
  `test_ask_corpus`, `test_emoji`, `test_institutions`, `test_gaps`.
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
- **The mobile reader's edition (#110, #111, #112):** `test_export_split` (the 28 parts merge back to the single
  bundle byte for byte, every part renders alone, the two tracked manifests are the committed bundle's) and
  `test_edition` (the publisher and verifier against a fake Storage server: immutable per edition, idempotent,
  the pointer last, altered bytes refused by name, the service key never in a URL, on stdout or in a summary).
- **The mobile reader's release (#114, #116):** `test_release` (the EAS release ledger `mobile/releases.csv` is
  generated, held in shape by `check`, and every row retraceable to a build, a commit and an edition manifest) and
  `test_privacy` (the `/privacy` page the stores link to names every processor the plans name and makes the same
  claims the reader's own tests hold it to).

## The live-site smoke test

`python3 model/smoke.py [--site URL] [--bundle web/public/data/eu27.json]` checks, from outside:
- every reader route answers with HTML;
- the report, all 27 country PDFs and the 4 previews answer with their type;
- every security header `vercel.json` sets is served as set;
- indexing is off;
- `www` redirects to the apex;
- the TLS certificate is valid for 14 more days or longer;
- with `--bundle`, the served data is the committed data;
- with `--edition-url` and `--manifest`, the mobile reader's edition channel serves the committed manifest and
  every part under it, read anonymously (#111); an empty URL is reported as not configured.

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

- **The mobile reader's four Dependabot alerts** (`node-forge`, `braces`, `decode-uri-component`, `uuid`) are
  Expo-toolchain transitives the rebuild (#109) carries too, allowlisted with reasons in
  `mobile/audit-allowlist.json`; they close when the owner dismisses them in the Security tab with those reasons.
