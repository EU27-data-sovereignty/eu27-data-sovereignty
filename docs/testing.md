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
| 16 | Browser tests | Playwright with axe: every route renders real data, in light and dark mode, at 375 px, and in print |

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

## Not yet in place (each needs the owner's OK)

- **Live `/ask` check:** needs `ANTHROPIC_API_KEY` in Vercel, and costs about one request a day.
- **Mutation testing** (a dev dependency), and **`hypothesis`** in place of the seeded generators.
- **Fact-check stability sampling:** a quarterly re-check of about 50 confirmed facts by the other model.
- **Visual-regression baselines:** screenshots committed to git.
- **Firefox and WebKit:** browser downloads in CI.
- **Weekly link check of every cited source:** `research.py recheck` takes hours, so it stays a manual
  `./run.sh recheck`.
- **Removing the red `security` workflow:** that means pushing the dotfiles repository.
