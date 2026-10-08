# Changelog

What changed and when. Reasoning for the choices behind these changes lives in
[`DECISIONS.md`](DECISIONS.md); this file records the work itself.

---

## 2026-10-08

### Changed: the project is renamed `eu27-data-sovereignty`, and its issue links point at the current repo (#100)

- **Names.** The GitHub repo is `EU27-data-sovereignty/eu27-data-sovereignty` and the Vercel project is
  `eu27-data-sovereignty` (fallback `https://eu27-data-sovereignty.vercel.app`). `eu27.cloud` is unchanged.
- **Links.** The "review this fact", "submit a source" and "report a correction" links, the user agent of the
  source fetcher and of the smoke test, `CONTRIBUTING.md` and `LICENSE-DATA` now name the new repo. Before, they
  named `pieteradejong/sovereign-data-centers` and worked only through GitHub's redirects.

### Changed: the web app takes the EU27.CLOUD brand (#99)

- **Header and footer.** The EU27.CLOUD badge and wordmark in the header, the full lockup in the footer, light and
  dark variants; a sun/moon theme toggle; a favicon set.
- **Page bands.** The EU silhouette artwork on night navy, with a gold rule; method pages tinted method teal (#88).
- **Palette and type.** Dark theme rebased on night navy `#0A0F1D` with gold links; EU blue and gold as highlight
  and accent; Montserrat headings, self-hosted; 10 px corners. All from `design/tokens.json`.
- **Front-page subtitle**, on the web and the report cover: "A research-backed framework for every EU member
  state: which critical government data should remain within national borders—and which sovereign data centres
  should host it."
- **Page layouts.** The front page puts a tile map of the 27 beside its title, with progress meters, entry cards
  and a question box. Countries become cards; Critical holdings group by tier with domain filters; the ranking
  becomes a ladder; Hosting groups its rows as cards by state with a dependency filter; Sources gains tier and
  grade distributions with search and filters; Ask sits beside its examples; method pages get a contents list.

## 2026-10-07

### Changed: CI checks once, reports the fact check on pull requests, and rechecks every cited source weekly (#98)

- **Pull requests.** `ci.yml` runs only the gate, on pull requests. Its duplicate Python job, whose staleness check
  covered 2 of 5 generators, and its duplicate gitleaks job are removed; `deploy.yml` and `security.yml` cover both.
- **The fact check, before the merge.** A pull request's gate now runs `factcheck.py gate` and warns, without
  failing, when the deploy's fact check would fail.
- **Cited sources, weekly.** The Monday monitor runs `research.py recheck --check`: every source behind a printed
  fact is re-fetched, and the run fails if one is newly gone or lost a quote. It commits nothing; the owner re-runs
  `./run.sh recheck` locally. The run's CSV and fetch manifest are kept for 90 days.
- **Documented.** `docs/ci-cd.md`: every workflow, job and check by event, the data integrity checks, the
  supply-chain rules, these changes and their known limits.

## 2026-10-06

### Changed: the cheapest gaps: 51 more registers known, 70% of all pairs; $45 of research

- **The wave.** `--wave unverified` (`wf_8c43ff69-b03`) took the 110 registers a research run had found but could
  not verify. One Opus 5.5 researcher per state (22) used each earlier attempt as a lead and cited a different,
  fetchable URL, and one blind Opus 5.5 reviewer per state checked it. It returned 144 findings: 98 registers, 39
  operators, 5 counts, and 2 on hosting.
- **The admission.** The usual rules applied: T1/T2, the quote found in the fetched page, and the blind
  reviewer's agreement. **51 registers were filled:** 732 of the 1,044 pairs not established as absent now have a
  known register (681 before), and 741 of 1,053 pairs are recorded (70%; 690 before). Record claims sourced rose
  to 1,618, from 1,549. The rest failed review or verification and stay as gaps with this pass counted.
- **New hosts.** 50 were classified. Five are T1: the Belgian, Lithuanian and Romanian law portals or gazettes,
  and the Finnish and Luxembourg statistics offices. 44 are T2 public bodies. `s3-eu-west-1.amazonaws.com` is T3:
  anyone can host files there, so the host cannot vouch for a government source.
- **The fact check** (`wf_b66a7125-0d9`, Fable 5.1). 66 of 68 confirmed. 2 are withheld with the checker's
  reasons: the operator of Lithuania's state PKI, and of Slovenia's water control. In each, the source names the
  body but not that it runs the system. 1,490 of 1,490 printed facts pass. The floors rose: `FACT_FLOOR` 1,490,
  records 1,618, register 741.
- **Cost, measured from the transcripts:** about **$45**, above the $15–30 estimate. Each of the 43 agents carries
  a fixed cost, and several states had only 1 or 2 gaps. The next wave should pool small states into batches, as
  the fact check does. The cost is in the run manifest.
- **The size budget was raised.** The data bundle reached 915 KB gzipped, over its 900 KB budget. It is now 1,100 KB,
  with the reason recorded in `test.sh`. Finding more data grows the bundle, and the lasting fix is a per-country
  split.

### Changed: a free retry recovers 6 registers and 26 sourced claims; the cheapest gaps go to a wave

- **The order.** The owner chose the cheapest gaps first: the 116 registers a research run had found but could not
  verify. A free pass came first, with no model cost:
  1. re-fetch every unverified claim (`research.py verify`);
  2. retry missing quotes in a rendered page (`--rendered`), which recovered 32 of 74;
  3. re-verify the vetting findings (`vetting.py verify`).

  Robots.txt refusals and 403s are recorded and never routed around.
- **The result.** 690 of 1,053 (state, class) pairs are now recorded (684 before), and 1,549 record claims are
  sourced (1,523 before). 6 of the 116 registers verified; 110 remain.
- **New hosts.** Five newly cited hosts were classified: `csam.be`, `tsl.belgium.be` and `nijz.si` as T2;
  `press.itsme-id.com` as T3 (a company); `newsbeast.gr` as T4 (press).
- **The fact check.** Fable 5.1 confirmed all 32 new and changed facts (`wf_c38b3e2e-319`). Among them, 7 printed
  values changed because a better-tier source replaced the old one. 1,424 of 1,424 printed facts pass. The floors
  rose: `FACT_FLOOR` 1,424, records 1,549, register 690.
- **The next wave.** `prepare --wave unverified` takes the remaining 110 registers. Each carries `earlier`: what
  earlier searches proposed, the URL they cited, and why it was not admitted. The researcher must cite a different,
  fetchable URL. `earlier` is never copied into a finding's question, so the blind reviewer still never sees the
  proposed value, and `tests/test_vetting.py` checks this.
- **A flaky test fixed.** One run of the 375 px visual test screenshotted "Loading the EU-27 dataset…", because the
  loading message sits inside `<main>` too. The test now waits for it to go.

### Added: research waves, and the hosting wave's pilot on the Netherlands: 12 gaps filled, $6.40

- **The mode.** A wave researches only the gaps `docs/gaps.md` lists, for one kind of field, and re-vets no printed
  fact. It runs as `python3 model/vetting.py prepare --wave hosting`, and is staged as a round, so nothing earlier is
  overwritten. Each gap names its holding's register and operator, so the search starts from the right name.
  Hosting findings also list the organisations their quote names (staging only, for #96), and an unfilled gap
  says what was searched. Runbook: `docs/vetting.md` §3f.
- **The pilot.** Run `wf_41009054-f6b`: Opus 5.5 researcher, blind Opus 5.5 reviewer. It covered the Netherlands'
  44 hosting and dependency gaps and returned 20 findings.
  - **12 admitted:** 9 hosting and 3 dependency. Among them: RDW keeps vehicle-register data in its own data
    centre; IBM manages the customs declaration system DMS; Solvinity manages the DigiD platform; Kadaster moved
    to a KPN platform; KPN runs PKIoverheid's root services.
  - **8 rejected:** 6 by the blind reviewer, and 2 because their pages could not be fetched.
  - **No source found** for the other 25 gaps. Each now has a second pass recorded in `docs/gaps.md`.
- **Two earlier findings verified.** Re-verifying the Netherlands also fetched two findings from the 2026-09-30
  vetting run that had failed to fetch then, both for the health-record exchange (the LSP). The operator is now
  printed from a higher-tier source as "VZVZ Servicecentrum".
- **The fact check.** Fable 5.1 confirmed all 14 new and changed facts (`wf_f7d14e4d-412`). 1,408 of 1,408
  printed facts pass. `FACT_FLOOR` rose to 1,408 and the record floor to 1,523.
- **Cost, measured from the transcripts.** About **$6.40**, at Opus 5.5 list prices: 17,950 output tokens,
  257,726 cache writes and 8.6M cache reads. It took 14 minutes, and the cost is recorded in the run manifest.
- **Fixed on the way:**
  - A wave description first changed the "what" text that every hosting fact's hash includes. That re-opened
    62 checked facts with no printed change, and the fact-check status caught it. The wave now has its own
    descriptions (`build_input.WAVE_KIND`).
  - A round's manifest now counts only its own run.
  - **The reproducibility check had a bug.** Rebuilding admission from scratch (`reproduce.reset_derived`) kept
    fields that an earlier admission had filled on base rows. So the pilot's Kadaster hosting, on a migrated
    row, re-admitted as "corroborated" instead of "filled". Those fields are now cleared before the rebuild, and
    all 6 registers reproduce.

### Added: `docs/gaps.md`, every missing piece of data and how hard it has been looked for

- **Why.** This is the first step of the data plan: find as much as possible, then choose the structure, then
  build the app. Until now an empty cell could mean either "searched, not found" or "never searched".
- **How.** `model/gaps.py` derives each gap's kind from the research that already ran: run 1 (holdings), run 2
  (indicators) and the vetting run. It keeps no hand-written log. The four kinds are:
  - claimed, not verified;
  - never searched;
  - searched once;
  - searched twice, not found, which is dry under the two-pass stop rule.
- **Results.** 3,440 gaps in 5,283 cells.
  - **Registers:** 675 of 1,044 (state, class) pairs are known. Of the 369 missing, 116 were found by a researcher
    but failed verification, which makes them the cheapest to close. 114 were searched once, and 139 are dry.
  - **Fields of the 675 known holdings:** hosting 71, foreign dependency 52, record count 56, data size 0,
    legal basis 259. Almost all of the rest were searched only once.
  - **Indicators:** 142 of 189 cells.
- **Where it runs.** It is regenerated by `./run.sh data` and checked by the gate's "Generated files are
  current" stage. `--csv` writes the gap list as input for a research wave. `tests/test_gaps.py` covers it.
- **Already in place.** Both research pipelines fall back to a headless-browser render when a quote is not in
  the served page (`fetch.fetch_rendered`), so the plan's rendering fetch needed no new code.

### Security: the exposed `/ask` keys are revoked, and the private findings register's entry is closed

- **The new key.** It is in the Anthropic workspace `eu27`, created 2026-10-06, and is the only key the Console
  lists there. It was set in the Vercel dashboard as a sensitive Production variable, never in a terminal or chat.
- **Proof it works.** Deploy run 37518689761 (`ac5c6af`) passed the new live `/ask` stage: 940 characters, 3
  citations.
- **It expires on 2026-11-05.** `TODO.md` holds the renewal step.

### Added: `./test.sh` checks the live `/ask` end to end, with a real API call

- **The check.** A new stage 17 (group `live`) runs `model/ask_smoke.py --require`. It asks the live
  https://eu27.cloud/api/ask one fixed question and fails unless the function runs, the key is accepted, the
  model answers, and the answer cites the corpus. It costs one request per run.
- **Where it runs.** The deploy job runs it after the deploy, against the new deploy. It is not in the gate:
  run before the deploy, a broken key would block the very redeploy that fixes it.
- **Skipping it.** `--no-live` skips it, for offline use or while the key is being replaced.
- **Shown to fail first.** On 2026-10-06, after the live key was deleted during the EU-1 key cleanup, the stage
  failed with `not_configured` and exit 1. `tests/test_workflows.py` checks that it runs after the deploy and
  never in the gate.

### Changed: the gate runs as parallel jobs, and the deploy ships the build the gate tested (#97)

- **One build, shipped as tested (optimisation 1).** The deploy job no longer rebuilds the site or recompiles the
  28 PDFs. It downloads the web app the browser tests ran against and the PDFs the PDF job inspected, packages
  them with `PREBUILT_SITE=1 vercel build` (`./run.sh site`, now `vercel.json`'s `buildCommand`), and fails
  unless `.vercel/output/static` hashes to the gate's files. The run summary records that hash.
- **Caches keyed by pins and checksums (optimisation 2).** These are cached:
  - npm, keyed by the lockfiles;
  - pip, by `requirements-dev.txt`;
  - the typst tarball, by its sha256, which is still checked on every run;
  - Playwright's browsers, by the pinned Playwright version.

  `npm ci` and `pip --require-hashes` still verify everything they install.
- **Parallel jobs (optimisation 3).** The new `.github/workflows/gate.yml` runs the stage groups at the same
  time: `model`, `web`, `pdf`, and `e2e` once per browser project (5 jobs). Pull requests (`ci.yml`) and
  deploys (`deploy.yml`) both call it. `./test.sh --only model|pdf|web|e2e [--project NAME]` runs one group;
  plain `./test.sh` is unchanged.
- **Tests.** `tests/test_workflows.py` checks that:
  - the groups cover every stage of `./test.sh`, and each group runs;
  - each Playwright project has a job with its own engine;
  - every cache key is a pin or checksum;
  - the deploy ships the gate's artifacts.
- **Verified locally.** Each group passes on its own, and `vercel build` of the prebuilt `web/dist` gives an
  identical tree hash.
- **Measured in CI.** The first run, on `d8bd0d1` with every cache cold, took **5 min 08 s** from push to live.
  The previous run, 37383861627, took about 11.5 min.

  | Job | Time |
  |---|---|
  | model | 30 s |
  | web | 39 s |
  | e2e, the 5 browser jobs | 1:07–2:12 each, starting after web |
  | pdf | 3:59, the critical path |
  | deploy, including the tree-hash check | 1:02 |

  The deploy then passed 55 of 55 smoke checks, with 1,396 of 1,396 printed facts.
- **The second run** (`747ed22`, every cache warm, 13 restored) took 4 min 54 s. The caches save about 15–20 s per
  job; the PDF job still takes about 4 min.

### Fixed: a new high-severity advisory in the web build's dependencies blocked the deploy

- **What happened.** The deploy of `2deb629` stopped at `npm audit`. GHSA-68fv-2mgg-jv7q (`source-map-js` up to
  1.2.1, an event-loop denial of service through crafted source maps) was published after the previous deploy.
- **Exposure.** None at runtime. The package is used only by the build tools (Vite, PostCSS, Tailwind, jsdom), and
  it reads only this repository's own source maps.
- **The fix.** `npm audit fix` in `web/` moves the transitive dependency to 1.2.2. Only the lockfile changes, and
  the direct pins stay exact.

### Added: the process diagram and proposed optimisations

- `docs/process.md`: the whole pipeline as a Mermaid diagram, from research through the fact check to the deploy
  and monitoring, with measured deploy timings.
- It proposes eight optimisations, each keyed by content so a stale cache cannot be used. None is implemented
  yet. Optimisations 7 and 8 change how facts are checked, so they wait for the owner and a decision entry.

### Changed: the hosting-operators work is fact-checked: 56 of 60 confirmed (#95)

- **How it got onto `main`.** The hosting-operators work, from another session, went to `main` unreviewed inside
  commit `0683d7f`, which used `git add -A`. The fact-check gate stopped its deploy.
- **The check.** The owner chose to keep it, and its 60 new `hosting` facts were checked by Fable 5.1 (run
  `wf_e9645602-884`): 56 confirmed, 4 withheld with the checker's reasons.
- **The result.** 1,396 printed facts pass, and 56 are withheld.
- **The lesson,** recorded in `docs/status.md`: commit named files only.

### Added: status and plans

- `docs/status.md`: a point-in-time snapshot.
- `docs/plans/mobile-app.md`: the React Native app in all 24 EU languages.
- `docs/plans/stichting.md`: the Dutch foundation to house the project, as planning input and not legal advice.

## 2026-10-05

### Changed: where key registers are hosted, printed and compared across the EU-27 (#95)

- **Hosting is printed.** Each country report's holdings table has a new "Hosting (as sourced)" column. 60
  admitted hosting values print as facts; they had been cited but never shown. 11 more print as gaps,
  because their quote lacks a year or number the value states.
- **A generated EU-27 overview,** "Key infrastructure and hosting":
  - It lists every holding with sourced hosting, by state, and counts per state what the printed facts say.
  - Every cell is the country report's own span, with the same source and the same fact check.
  - It appears in the EU-27 report after the ranking, in `countries/EU-INFRASTRUCTURE.md`, on the web at
    `/infrastructure` (nav: Hosting), and in `/ask`.
- **The critical-holding pages** (`/holdings/<class>`) take their column names from the document, so they
  show the hosting column too.
- **Printed facts:** 1,340 → 1,400. The 60 new facts await the cross-model fact check before deploy.
- **The methodology** (generated, in every asset) describes the overview and how its counts are made.
- **Tests:** `tests/test_evidence.py` checks that every overview fact is a span a country report prints,
  and that every printed hosting is in the overview. The book's footnote count includes the overview, and
  `/infrastructure` joins the browser, accessibility and smoke routes.
- **Visual baselines:** the two `/country/DE` baselines at 1280 px were updated, for the new nav item, the
  new counts and the wider holdings table.

### Decided: operators as entities with sourced ownership links (#96)

- **Planned, not built.** Organisations become entities, with typed hosting properties and sourced
  ownership links, so cross-country operator views are computed, and a dependency can be derived from
  sourced links and reconciled with the reviewed label.
- **Inspired by** Palantir's Ontology. The design is in
  [`docs/hosting-operators.md`](docs/hosting-operators.md).

### Found: exposure counts include withheld labels

- **What.** In 7 states (AT, CY, EL, FR, HU, IE, SE), the "Foreign-dependency exposure" section counts
  admitted dependency labels that the same report withholds. The ranking reads the same raw labels
  (`sovereignty.py:129`).
- **Status.** Recorded in #95 and `TODO.md`, not yet fixed. The new overview counts printed facts only.

## 2026-10-05

### Fixed: the Vercel project was connected to the wrong repository; Vercel no longer builds from git

- **What was wrong.** From 2026-10-02 the Vercel project that serves eu27.cloud was connected to another of the
  owner's repositories. Every push there started a production build of the wrong code, and each failed only
  because that repository has no `web/` folder.
- **The fix.** It is now connected to this repository, and `vercel.json` turns off git-triggered deploys
  (`git.deploymentEnabled: false`). Production ships only from GitHub Actions, after the full gate and the
  fact-check gate. `tests/test_vercel_config.py` keeps it that way.
- **`DEPLOYMENT.md`:** redeploy with `gh workflow run Deploy`, and set secrets in the dashboard.

## 2026-10-04

### Changed: the subtitle states the project's goal

- **The new subtitle,** on the front page and the PDF report's cover: "Toward a well-sourced plan for every EU
  member state: which critical government data to hold at home, and the sovereign data centres to hold it".
  It replaces "Each member state's critical data holdings, analysed on its own fundamentals".
- **Why "toward".** Capacity sizing stays withdrawn until each state's holdings are measured (#73), so no
  finished plan is claimed.
- **Visual baselines:** the 3 front-page baselines were updated with it.

## 2026-10-03

### Fixed: `/ask` answers on the live site

- **The fix.** `ANTHROPIC_API_KEY` is now set in Vercel (Production), and `/ask` answers with citations: the
  live check got 1,122 characters and 3 citations.
- **The cause.** The first value stored had been revoked. The `unconfigured` code added earlier the same day
  showed this from outside.
- **The daily check is now strict** (`ASK_LIVE=true`).
- **Rotate the key** (TODO). It was exposed in plain text during setup, and that is recorded as a security
  finding.

### Changed: a rejected `/ask` key is reported as such (#92)

- **What changed.** When the Anthropic API rejects the key, or none is set (HTTP 401), `/ask` now answers
  with the code `unconfigured`. Visitors see "Questions are not available right now", and nothing about the
  key is exposed.
- **Why.** The daily check, and anyone diagnosing, can now tell a key problem from a spent budget (`paused`)
  or an outage.

### Changed: a fact a second checker rejects is withheld too (#94)

- **A second stability sample.** 50 more confirmed facts, none from the first sample, went to Opus 5.5,
  which agreed on 49. Across both samples a second checker disagreed with 6 of 100 facts Fable 5.1 had
  confirmed (10% and 2%).
- **The new rule.** Those facts, and any found by later samples, are now withheld with the second checker's
  reason.
- **The result.** 1,340 printed facts pass, and 52 are withheld.

### Changed: 25 withheld facts corrected or re-sourced and confirmed; 46 remain withheld (#93)

- **The correction round.** A round re-researched the 69 facts the cross-model check had withheld
  (`vetting.py prepare --withheld`):
  - 6 research and 6 blind-review agents ran (Opus 5.5), giving 57 findings;
  - 39 were fetched and checked, with 30 exact quote matches;
  - admitted: 6 corrected values, 22 better-sourced corroborations, and 1 higher-tier supersession.
- **The fact check of the 31 changed facts.** It was run with Fable 5.1, since the round recorded Opus 5.5
  as their author: 25 confirmed and 6 withheld again.
- **The result.** 1,346 printed facts pass, and 46 remain withheld.
- **21 new source hosts classified**, among them the Irish statistics office, Czech e-Sbírka and the
  Portuguese official gazette as T1.
- **How it works.** A withheld value may be replaced only by a `corrects` finding that passes every check
  again (#93). The first vetting run's files are untouched, and admission still reproduces.

### Added: iPhone and every major browser, visual regression, Hypothesis, a mutation audit, a stability sample (#92)

- **Phones and browsers.** The browser tests now run in Chrome, Firefox, desktop Safari (WebKit), iPhone SE
  and iPhone 17 Pro: 188 tests, all passing. CI installs the browsers.
- **Three iPhone fixes:**
  - the disclaimer banner shows its first sentence on every page, with the rest one tap away;
  - the `/ask` field is 16 px, so Safari no longer zooms in;
  - navigation links are 28 px tall.
- **Visual regression.** 10 screenshot comparisons in light and dark mode, at 1280 and 375 px, against
  macOS baselines. A thicker header rule failed all 10.
- **Hypothesis.** `tests/test_hypothesis.py`, with `requirements-dev.txt` pinned with hashes. CI installs
  it; the model stays stdlib-only.
- **The mutation audit** (`tests/tools/mutation_audit.py`) on `evidence.py` killed 83 of 98 mutants. New
  tests for the gaps it found raised that to 91 of 98 (93%). The 7 survivors are listed in
  `docs/testing.md`.
- **Fact-check stability.** Opus 5.5 re-checked 50 facts Fable 5.1 had confirmed and agreed on 45 (90%).
  The 5 disagreements are in the audit file; a sample never changes a verdict.
- **The live `/ask` check** runs daily (`model/ask_smoke.py`). It reports "not configured" until the key is
  set in Vercel.

## 2026-10-02

### Added: comprehensive testing: pull requests, the live site, PDFs, generated inputs, the network layer (#92)

- **Pull requests** now run the full gate (`./test.sh --no-pdf`) and a high-severity dependency audit. Before,
  only the Python tests ran until a change reached `main`.
- **The live site.** `model/smoke.py` checks it after every deploy and every Monday (`monitor.yml`):
  - routes, all 28 PDFs and the report previews;
  - the security headers, noindex and the `www` redirect;
  - the certificate, valid for at least 14 more days;
  - that the served data is the committed data.

  The Monday run also reports new Eurostat vintages.
- **Compiled PDFs inspected** (`book/check_pdfs.py`): disclaimer, both appendices, the country named, fonts
  embedded, and a size budget.
- **Size budget:** data bundle 900 KB, JavaScript 400 KB, both gzipped.
- **Generated-input tests** (`tests/test_properties.py`): 500 seeded cases per rule, covering
  - value in quote across every EU number format;
  - the fact hash;
  - the checker rule;
  - placement ranges.
- **Fetch-layer tests** against a local HTTP server: robots, a 403 never retried, redirects, dead hosts, and
  archive host matching.
- **Web.** Component tests for `DocumentView`, `PageBand` and the theme. Browser tests now cover
  accessibility in dark mode, every route at phone width, and print: 56 browser tests and 49 unit tests.
- **The clean-room rebuild** now runs the whole gate in the fresh clone.
- **`docs/testing.md`:** every suite, where it runs and what it proves.
- **Dependencies:** `undici` 8.11.2 and `brace-expansion` 5.0.12 in `web/`, clearing the high Dependabot alerts
  there.

### Changed: the site takes the report's look; 12 more facts confirmed; the fact-check procedure documented (#87, #89, #91)

- **The theme (#91).** Every page now opens with the PDF report's cover and chapter style: an EU-blue band, a
  gold kicker and the title in the print serif (Libertinus Serif, self-hosted). Method pages use a teal band.
  Section headings and the headline figures are in the serif too. The front page shows four pages of the
  EU-27 report, rendered from the deployed PDF at build time.
- **The Slovenia rounding defect is fixed.** Population is now printed at the precision it is stored at:
  Slovenia 2.135 million, not 2.13. All 27 population figures were re-checked and confirmed (one pooled
  batch). A test keeps every Eurostat figure at its stored precision.
- **Facts behind refusing pages.** 12 facts were withheld because their pages (Estonian ministries, a Slovak
  law site) refuse automated access. They were checked again against the exact copies hashed when they were
  admitted (`factcheck.py prepare --withheld-blocked`): 11 confirmed, 1 not supported. 69 facts remain
  withheld.
- **The procedure is now documented and reproducible.** [`docs/fact-check.md`](docs/fact-check.md) gives the
  procedure. `factcheck.py replay` rebuilds the ledger from the staged runs in recorded order, and
  `./test.sh` runs it with the audit-file check. `./run.sh data` now regenerates the audit file.
- **Withheld facts' reasons** are now cut at a word, not mid-word.

### Added: eu27.cloud is live, deployed automatically from `main` (#81, #90)

- **The first automatic deploy:** `Deploy` run 37072208296 (commit `34d460c`). It ran the full gate, the
  fact-check gate, the prebuilt production deploy and the smoke test, all in CI.
- **Smoke test results:** `/`, `/country/DE`, `/fact-check`, `/methodology` and the PDFs return 200; robots
  disallows indexing and `x-robots-tag: noindex` is set; `www` redirects to the apex; the served bundle's
  hash equals the committed one.
- **Still not indexed.** The site stays out of search engines until the launch gate (#50).

### Changed: every printed fact checked by a second model; 81 withheld (#87, #89)

- **The run.** The first full cross-model fact check (`wf_da123db1-a4e`, plus the pilot) put all 1,390
  facts to Claude Fable 5.1, a different model from the one that researched them.
  - **1,309 confirmed**, and now printed with a current verdict.
  - **81 not confirmed**, now shown as disputed with the checker's reason: 48 not supported, 33 unclear.
  - Of those, 31 are register or operator names whose printed wording goes beyond the quote, 15 are
    hosting labels, and 13 are indicators. About a dozen are pages the checker could not fetch.
  - **One rounding defect:** Slovenia's population printed as 2.13 million, where the source's
    2,135,107 rounds to 2.14.
- **Where to see them:** every withheld fact is listed in `docs/fact-check-audit.md` and in each country's
  fact-check appendix.
- **Cost:** about $250–370, measured from the agents' token usage.

### Fixed: eu27.cloud DNS, and a checklist for the first automatic deploy (#90)

- **`eu27.cloud` had never resolved.** It had no nameservers: the registry listed it as *inactive*. It now
  uses Vercel's nameservers, set by the owner at iwantmyname, and `DEPLOYMENT.md` no longer claims records
  that were never there.
- **`DEPLOYMENT.md` gains a first-deploy checklist:** the Vercel token, the nameservers, the fact-check
  gate, the full test gate, the push, and the smoke test. Its deploy flow now shows the fact-check gate.

### Changed: a fact the fact check does not confirm is withheld, instead of blocking the deploy (#89)

- **Withheld, with the reason shown.** A printed fact that the second model did not confirm, or could not
  check, is now shown as **disputed**, with the checker's model, run and reason, until the fact or its
  source is corrected and checked again.
- **The gate still requires every printed fact to pass.** A withheld fact is no longer printed.
- **Where withheld facts are listed:** in the audit file, and in each country's fact-check appendix.
- **The pilot's two disagreements on Germany are withheld:** the civil-registry operator's scope, and
  whether the eID scheme is state-operated.

## 2026-10-01

### Added: the methodology in every asset, marked in a method teal (#88)

- **Briefs:** every brief now carries the full methodology appendix, beside its fact-check appendix.
- **`/ask`:** answers about the method from the generated methodology.
- **Posters:** every poster points to `/methodology` and its country's fact check.
- **The fact check:** the methodology gains a section on it.
- **One colour, teal, marks how-we-know material everywhere.** The PDF appendices open with a teal band,
  the `/methodology` and `/fact-check` pages use a teal frame, and method notes are teal. Each section
  carries the label "Method · how this was made".
- **Accessibility fix:** wide tables on the web are now keyboard-scrollable.

### Added: every printed fact is checked by the model that did not write it, before every deploy (#87)

- **The rule.** A production deploy now needs every printed fact to have a current *supported* verdict
  from a checker model that did not write it. Fable 5.1 checks what Opus 5.5 wrote and Opus 5.5 checks
  what Fable 5.1 wrote. Fable 5.1 checks facts whose author was never recorded, which today is all of
  them.
- **What a verdict covers.** It holds for the fact exactly as printed. Change the text, the quote or the
  source, and the fact must be checked again.
- **The check itself.** It runs locally with `/factcheck` (`./run.sh factcheck prepare|stage|record|audit|status|gate`).
  The deploy workflow's new **Fact-check gate** step, and `./run.sh deploy`, refuse to ship until it
  passes.
- **The audit file.** `docs/fact-check-audit.md` records status, every disagreement ever recorded,
  every run with its commit and hashes, and the steps. It is generated, and the gate fails if it is stale.
- **The appendix.** Every asset now carries a generated **fact-check appendix**: the EU-27 report and
  every country PDF ("Appendix: fact check"), every brief, the new web pages `/fact-check` and
  `/fact-check/<ISO>` (linked from the banner on every page and from each country page), and the `/ask`
  corpus. Every poster carries a one-line summary.
- **Authorship.** The vetting workflow now names its models and records which model researched each
  finding, so future facts have a recorded author.
- **Not yet run.** No fact has been checked so far, and the appendix says so (0 of 1,390). Until the first
  run is recorded, `main` cannot deploy.

### Added: citizens can source and check facts, under a two-person rule (#85)

The project is now bottom-up. Anyone in any member state can contribute through two public GitHub issue
forms, generated from the model so they can't drift from it:
- **Submit a source:** a public document that establishes a fact. It passes the same machine checks as
  agent research: fetch, hash, quote, figures in the quote, tier.
- **Check a fact:** confirm or reject a printed fact against its source. Every fact on the site and in
  the PDFs now has a **Check this fact** link, prefilled, and every country page has a **Submit a
  source** link.

A fact counts as **verified by a person** only under the two-person rule. A reviewer must be on the
public roster (`model/contrib/reviewers.csv`, added by a pull request the maintainer reviews), must not
be the submitter, must read the source's language, and must declare no conflict of interest.
- **Effects:** one confirmation makes a Strong fact **Verified**, the new top grade. One rejection makes
  a fact disputed, with the reason shown. Two withdraw it.
- **The disclaimer is now computed.** It reads exactly as before until a person verifies a fact, then
  states "N of M facts also verified by a person".
- **`./run.sh contrib audit-sample`** draws a seeded random sample of unreviewed facts. It is the human
  sampling audit the launch gate requires.
- **The evidence page has a "Help needed" table:** gaps, items the agents didn't reach, sources a
  machine couldn't fetch, and reviewers per state. Luxembourg, Lithuania, Romania, Malta and Finland need
  help most. Every state has 0 reviewers so far.

### Added: contributor terms, a reviewer guide and an editorial policy (#85, #86)

- `CONTRIBUTING.md`: pseudonymous contributions, licensed CC BY 4.0 under a DCO sign-off, with no
  copyright assignment.
- `docs/reviewing.md`: how to join the roster and what a review does.
- `docs/editorial-policy.md`: what is published, how corrections work (never silently), conflicts of
  interest, and ownership and funding. Two statements await the owner's confirmation.
- `LICENSE-DATA`: its accuracy warning, which still said nothing had been checked against primary
  sources, now describes the actual checks, and it has a contributions clause.

### Changed: agent prompts treat page and input text as data, never as instructions

Submitted quotes come from anyone, so both prompts in `workflow.js` carry the guard `/ask` already had.

### Fixed: a document cited twice was counted as two sources

The end-to-end rehearsal of a citizen submission resubmitted a fact's own source. Admission counted it as
a corroboration and overwrote the original citation's record. A finding that cites a document the fact
already cites is now `same_source`: recorded, never counted as a second source, and never overwriting.
**This corrects the 2026-09-30 vetting figures:**
- 8 of the 244 "corroborations" cited the same document, so the count is **238**;
- 2 of the 12 "disputes" were the agent reading that same document differently, so the count is **10**;
- Strong falls from 107 to **106**.

The run manifest is re-recorded with the corrected outcomes.

### Fixed: a submission now declares its document's language

The rehearsal also found that a submission recorded no language. Eligibility therefore fell back to the
state's official languages and refused a reviewer who reads the document's actual language.

### Deferred: the legal entity (#86)

A Dutch stichting is intended and not yet founded. Everything is built so it can take the project over
unchanged.

---

## 2026-09-30

A day in two halves: the morning brought the documents and deployment up to date; the rest of the day
rebuilt how the evidence is checked, graded, re-checked and reproduced (#80–#84). The vetting run's
admission, the first CI deploy and the clean-room rebuild are still to be verified; see the end of this
entry.

### Changed — every document brought in line with the rebuilt project

- **New documents.** `METHOD.md` is the reader-facing evidence pipeline: research, quote check,
  independent review, admission, rendering, and what the method does not establish. `CLAUDE.md` holds the
  exact commands and the gotchas.
- **Rewritten to the current state.** `ROADMAP.md` (in-progress work, the order of what comes next, the
  launch gate as a human sampling audit, a diagram of the plan), `PROGRESS.md`, `model/README.md` and
  `TODO.md`. `VERIFICATION.md` and `SOURCES.md` carry current figures.
- **One style guide.** `artifacts/STYLE.md`, fed by `design/tokens.json`. The per-format guides keep only
  their own rules.
- **Fixed on the way.** Posters are sized to their content again, instead of a 1,400 px fallback, and
  researched sources are labelled by publisher and title, not by a hash.

### Added — `eu27.cloud`, attached with `noindex` (#80)

Registered at iwantmyname on 2026-09-30, with its DNS kept there and pointed at Vercel. It serves `noindex`
twice: through `robots.txt` and an `X-Robots-Tag` header on every path. It is not announced.

### Added — production deploys from GitHub Actions (#81)

A push to `main` runs the full `./test.sh`. It then builds with a pinned, checksummed typst, deploys
prebuilt to Vercel and smoke-tests the live domain, including that the live data bundle is the committed
one. Actions are pinned by commit SHA. **Not yet run:** the `VERCEL_TOKEN` secret is not yet set.

### Changed — every output says the findings are machine-checked, not human-verified (#82)

One disclaimer, from `model/evidence.py`, opens the report, every country PDF, the web app, `/ask`
answers, the posters and the briefs. The list of checks each output describes is generated from what
runs. So is the ranking rule's text: `report.py` restated it by hand, and it could drift.
`tests/test_evidence.py` fails if any output drops the disclaimer or uses the old wording ("every fact
... fetched, hashed and checked"), which had been printed over five citations that were never
quote-checked.

### Changed — a fact is printed only if its figures are in its quote (#82)

The gate proved each quote is in its document. It never proved the report printed what the quote says.
- **Value in quote.** Every number and date in a printed value must now appear in the original-language
  quote, read in any EU number format. A number that is only in the English translation does not count.
- **Recorded evidence.** A citation supports nothing without a recorded quote check at the hash the
  registry holds.
- **Printed facts fell from 997 to 922.** Examples: a 10-year retention period printed as Bulgaria's
  record count; "48 million victim records" added to a French quote that says 17 million; and 68 other
  values whose numbers or dates are not in their quote. Five hand-migrated citations (#67) had no
  recorded check, and are withdrawn.
- **Names are disclosed, not required.** An abbreviation missing from the quote, often a transliteration
  (*MVR* for *МВР*), is named in the fact's checklist rather than withheld. 138 facts would otherwise
  have gone.
- **Summaries are labelled.** A value that is not a verbatim extract is labelled a machine summary of
  the quote.

### Changed — a categorical value needs the reviewer's own agreement (#79, enforced by #82)

Four indicator values had been admitted at the reviewer's *changed* value: EE K2, LU C2, PL C1 and
RO C1. They are withdrawn, and admission now enforces exact agreement. No state changed group. Estonia's
and Romania's ranges widened, as they should when a known value becomes unknown.

### Added — an evidence grade for every fact (#82)

Each fact lists the checks it passed, and a fixed rule makes it **Strong** or **Standard**. There is no
numeric score, since nothing has calibrated one. On the day it was introduced: 76 Strong, 842 Standard.
The report, the PDFs, the web and the briefs show the grade and the checks. The quote is shown in its
original language first, with the machine translation labelled.

### Added — source tiers (#83)

Every cited host is classified once, in `model/sources/authorities.csv` (247 hosts at first):
- **T1:** official law portals and gazettes, statistics offices, Eurostat;
- **T2:** public bodies and audit offices;
- **T3:** companies and other institutions;
- **T4:** unofficial statute mirrors, press and encyclopedias.

Only T1/T2 facts can be Strong, which took Strong from 76 to 59. The best source per printed fact was T1
343, T2 400, T3 9 and T4 166. 158 of the T4 facts rested on unofficial copies of statutes
(`net.jogtar.hu`, `zakonyprolidi.cz`, `zakony.judikaty.info`, `lawspot.gr`, `zakon.hr`) where the
official portal exists.

### Added — rechecks and disputed facts (#83)

`./run.sh recheck` re-fetched all 691 sources behind printed facts:
- 306 unchanged;
- 373 changed but still holding every quote;
- 3 had lost a quote, affecting 6 facts;
- 3 were gone (404: the Commission's NIFO 2024 factsheets);
- 6 refused or timed out.

A fact whose quote vanished, or whose source is gone, is now shown as **disputed**. It is not printed,
and not silently kept. A refusal changes nothing. The recheck is resumable and saves after every source.

### Fixed — 141 genuine quotes the first check could never match

The quote check decoded every page as UTF-8, so on ISO-8859-1 pages every accented letter was garbled
(`cylaw.org`, `pgdlisboa.pt`). `research.decode` reads a page in its declared charset.
- **Rendered retry.** `./run.sh retry` retries each not-found quote against the correctly decoded page,
  and renders it in a headless browser only if the text is still missing. A page that refused us is
  never retried with a browser. 177 of 251 retried quotes were found.
- **The result.** Admitted holdings rose from 416 to 472, and printed facts from 918 to 1,007.

### Added — the first vetting run across all 27 states (#83)

One researcher per state looked for a better source for every printed fact, newer information,
contradictions and filled gaps. One blind reviewer per state was shown the quote and URL, never the
proposed value.
- **Scale:** 54 agents, 6.75M tokens and 2,231 tool calls, in 64 minutes.
- **1,017 findings:** 138 upgrades, 199 corroborations, 45 newer statements, 11 contradictions and 624
  filled gaps.
- **The reviewer agreed with 862.** Of the 1,389 input items, 741 were found, 447 had no better source,
  and 201 were not reached.
- **Official portals.** The agents reached the portals the old citations lacked: 46 findings on
  `slov-lex.sk` and 45 on `e-sbirka.cz`.
- **New hosts.** 171 were tiered before admission.
- **The limit, stated.** The reviewer was the same model as the researcher. It is blind, but two
  readings by one model can share its blind spots.

The admission rules never trust the researcher's own label. A different value is decided by a published
rule: a higher tier wins, and the same authority with a later date wins. Otherwise the fact is shown as
disputed, with both sources.

**Admitted** (run `wf_1c6b8bb6-450`, manifest in `model/research/vetting/runs/`):
- 681 of the 857 fetched findings had their quote on the page.
- **363 gaps were filled**, 244 facts gained a second, independent source, and 26 values were superseded
  (23 by a higher-tier source, 3 by a later statement of the same authority).
- 12 became disputed.
- **Rejected:** 153 findings the reviewer disagreed with, 176 not verifiable on the page, 38 operators or
  counts for a register nobody established, and 5 below T2.

**The result:**
- Printed facts rose from 1,007 to **1,390**, and Strong from 58 to **107**.
- The best source behind each fact is now T1 for **635** (from 343), T2 for 633, T3 for 9 and T4 for
  **113** (from 166).
- 20 facts are shown as disputed.

### Changed — Eurostat vintages adopted; the employment column fixed (#84)

- **Newer periods.** Population 2026, renewables 2025 and land area 2026, plus Portugal's revised 2025 GDP
  (306.7 → 308.5).
- **The employment column.** Public-administration employment reproduced no Eurostat period at all
  (Sweden 420.4 against the official 245.0), so it had been withheld on every page. It is now the
  official 2024 series, printed on all 27. No column is excused any more as a "known defect".
- **Pins as data.** The pinned periods are now data, in `model/eurostat_pins.csv`, with the date and
  decision behind each. `./run.sh eurostat check` reports and writes nothing; `adopt` makes the whole
  change as one step.

### Added — reproducible from scratch (#84)

- **One command per step.** `./run.sh admit | recheck | retry | eurostat | vet | reproduce`. The agent
  step is the checked-in `/vet` skill, which runs the checked-in, hashed `workflow.js`.
- **A manifest per agent run.** It records the input, output and prompt hashes, the commit, the reviewer
  model and the tool versions.
- **Admission is a checked fixed point.** `./run.sh admit --check`, a gate stage, re-runs admission on
  the committed evidence and fails if any register would change. Admission no longer reads the clock.
- **A clean-room rebuild.** `./run.sh reproduce` rebuilds everything from a fresh clone of HEAD and
  compares it with the committed copy. `--evidence` also re-fetches every source.
- **Pinned tools.** Versions are pinned in `.tool-versions` and `.nvmrc`, `init.sh` warns on a mismatch,
  and tests hold CI to the pins. One CI workflow was on Python 3.12 while the rest ran 3.14; it is now
  aligned.

### Added — a generated methodology appendix (#84)

The EU-27 report and every country PDF end with a methodology appendix. It covers:
- sourcing, and the measured outcomes of every run;
- every check, the tiers and the grade rule;
- every calculation: the priority formula, the ranking rule and confidence, the exposure count, and each
  Eurostat series with its filters, period and unit conversion;
- how to reproduce the work, and what it does not establish.

It is generated from the constants the code runs, and a test holds each rule to its source. Each PDF
stamps the git commit and the data bundle's hash it was built from. The web `/methodology` page renders
the same document.

### Added — the gate compiles the PDFs and checks what the web shows

A typst template error had passed the whole gate this day. `./test.sh` now compiles the EU-27 report and
all 27 country PDFs (about 10 s), and checks the disclaimer in the compiled text. Four Playwright tests
check:
- the disclaimer on every page;
- the grade and checks on a fact;
- the labelled machine translation;
- that a disputed value is withheld without a footnote.

Both new checks were shown to fail when they should. One of them first passed with the disclaimer
removed, because the banner still contained it; it was tightened.

### Added — documentation

- `docs/vetting.md`, the runbook: every step as one command, the rules that must not bend, a
  record-keeping checklist, and the known limits.
- `docs/evidence.md`, generated on every build: grades, tiers, why facts are Standard, per-state charts,
  disputed facts and agent runs.
- `METHOD.md` sections 3 and 7, and decisions #82–#84.
- The README Changelog table.

### Corrections made during the day

A record of what was wrong, including in this day's own work:
- **Eurostat hashes.** The first version of #82 said the 136 Eurostat figures were never hashed. Wrong:
  their API responses are hashed in `fetch_manifest.csv`. It is corrected in #82, the docs and the code.
- **A circular tier rule.** "The operator's own domain is T1" was tried and dropped. The operator URL
  recorded for a holding is the URL the research agent cited, so the rule was true by construction, and
  it had marked 531 facts T1.
- **`cylaw.org`.** It was first classified as an official law portal. It is a non-official legal
  information institute: T4.
- **Recheck scope.** The first recheck disputed every fact on a source when only one of its quotes had
  vanished. Disputes are now per fact.
- **Admission was not reproducible.** The new check found it on its first run. Each admission started
  from the previous one's output, so a gap vetting filled read as an existing fact the next time, and
  46 register rows changed. Admission now starts from the base it never produces (Eurostat and the #67
  migrations) and rebuilds everything else from the evidence. It is a pure function of the committed
  files.
- **A mistaken `git checkout`.** Mid-work, it reset four register files. They were rebuilt from the
  evidence with identical counts: an unplanned test of the point above.
- **Two admission bugs, caught before any vetting finding was admitted.** An admitted "no central
  register" would have been flipped to "held" by a finding, instead of being treated as a contradiction.
  And any two text values without numbers counted as the same, so a finding naming a *different*
  register would have been admitted as a corroboration.
- **The `/ask` corpus.** Disputed values briefly counted as facts the site shows, which broke the corpus
  check. They count as withheld.

### Verified, and not yet

- **Verified:** `./run.sh admit --check` reports "6 of 6 registers reproduce from the committed
  evidence". `./test.sh` passes in full, including the new stages: admission, PDFs, and the evidence rules
  in the browser.
- **Verified:** `./run.sh reproduce` on commit `f62eaac`, "reproduced from scratch" in 30 s: a fresh
  clone regenerated every output identically, and admission, the PDFs, the web build and the tests all
  passed. A register cell edited by hand makes `admit --check` fail, naming the line.
- **Not yet:** `./run.sh reproduce --evidence`, the full re-fetch in a clean room; the first CI deploy
  (#81), which needs the `VERCEL_TOKEN` secret.
- **No finding has been reviewed by a person.**

---

## 2026-09-29 (evidence)

### Added — the first verified research: 416 critical holdings and 134 indicator values

Both research runs are verified and admitted.
- **Holdings.** 1,724 of 2,228 claims passed the quote check; 416 (state, class) holdings are in the
  register, each cell cited.
- **Indicators.** 240 of 288 claims passed; 134 of 189 values admitted after a downgrade-only review.

A hand spot-check found run 1's foreign-dependency labels unreliable: EU companies labelled "mixed" and
Eurosystem infrastructure treated as non-EU. Under the new rule #79, a dependency label is admitted only
when an independent reviewer agrees: 77 of 93 agreed, and 49 labels were admitted. The first ranking had
eight High-confidence "Dependent" placements; after review one remains, Ireland, spot-checked by hand
(the electoral register on a Microsoft Azure tenancy, and TETRA owned by Motorola Solutions). Italy is
*Secured in law, not yet in practice*; the other 25 are *Not demonstrated*, Low confidence.

### Fixed

On phones, the source list no longer pushes the page sideways (long hashes and claim ids now wrap).

---

## 2026-09-29 (ask)

### Added — /ask: questions answered from the sourced findings only (#78)

A question box on the site, answered by Claude Opus 5 through a Vercel Function (`api/ask.ts`). The only
material the model sees is `api/_corpus.json`, built from the content model with one block per sourced
fact or explicit gap; citations are on, and every citation resolves to its claim's quote, URL, hash and
archived copy. Questions are single-turn, at most 500 characters, and never stored. Costs are capped by a
dedicated Anthropic workspace spend limit and a Vercel Firewall rate limit. Tested with a fake client
and a recorded stream; live answers wait for the API key.

---

## 2026-09-29 (ranking)

### Added — data-sovereignty ranking by published rule (#77)

Five groups instead of a score: *Sovereign in law and in practice*, *in practice, not secured in law*,
*Secured in law, not yet in practice*, *Not demonstrated*, *Dependent on non-EU providers*. Seven sourced
indicators (`model/indicators.csv`) plus two computed from the holdings register feed the rule in
`model/sovereignty.py`. Confidence is the range of groups a state could still reach; it is shown next to
every placement. The report gains a ranking chapter; each country document opens with its placement;
the web gains `/sovereignty` with the group ladder, an EU map, a per-state explanation and a sortable
indicator grid. With no indicator researched yet, all 27 are *Not demonstrated*, Low confidence.
`.build-epoch` moves to 2026-09-29 so generated files carry today's date.

---

## 2026-09-29 (later)

### Changed — each country on its own fundamentals; Dutch-scaled figures withdrawn (#72, #73)

Every country used to be the Dutch workload table resized by population, public-administration
employment and GDP. That method is gone: `scale_workloads`, `scaling_rules.csv`, the per-country
generated CSVs, `model/eu27_results.csv` and the NL arguments of `country_data.build` are removed.
The withdrawn headline figures, for the record: ~306 MW design load, ~125k servers, ~EUR 7.2 bn
CAPEX across 86 sites. They were never measured for any state but the Netherlands. The hand-written
Dutch plan moved to `countries/NL/REFERENCE-CASE.md` as a note; `countries/NL/GOAL.md` is now
generated like the other 26.

### Added — one content model, footnoted everywhere (#74, #75)

`model/document.py` writes each country once: fundamentals (Eurostat, footnoted), critical holdings
by priority, foreign-dependency exposure, legal posture, capacity status and open research. A value
is shown only when a checked citation supports it; otherwise it is a gap. The report, 27 country
PDFs (`/report/<ISO>.pdf`), the markdown briefs, the web pages and the posters all render it.
`document.py --check` is a new `test.sh` stage.

### Added — critical holdings register and verified research (#73)

`model/holding_classes.csv` (39 classes), a widened `national_data` register with per-field
citations, and `model/research.py`, which admits a researched claim only after fetching the
document, recording its sha256, finding the quote and looking up an archived copy. Research for
all 27 states is running.

### Changed — the web app

Matrix, Workloads and Scenario are removed: they rendered the withdrawn figures and unsourced
ratings. New: country pages rendered from the document with footnotes and a source list, a sortable
Countries table, Critical holdings across all 27 states, and a Sources page. The EU theme applies
throughout (#76).

### Removed

The Chrome-printed briefing PDFs (#76), the mono typst briefs, pandoc, and the book's generated
Parts III and IV.

---

## 2026-09-29

### Added — the EU-27 country report, one PDF (#71)

`python3 book/build.py --report` builds `eu27-report.pdf`: an EU-blue cover with the circle of stars, a
clickable contents page, a provenance notice, an EU-27 summary table, then one chapter per member state in
alphabetical order. Each chapter is that country's `countries/<ISO>/GOAL.md`, converted by pandoc, so the
report cannot disagree with the files. 142 pages, about 2.8 MB. The colour template lives in
`book/templates/report.typ`; `style.typ` stays mono (#28). It is served at `/eu27-report.pdf` and linked from
the Overview page.

### Changed — prebuilt deploys; the briefs are back (#71)

`./run.sh deploy` now builds locally (`vercel build`) and uploads the output (`vercel deploy --prebuilt`),
because the PDFs need typst and pandoc. That also closes #42's open item: `/briefs/<ISO>.pdf` is served. The
SPA rewrite moved from `/` to `/index`, the path prebuilt output gives `index.html` under `cleanUrls`.

---

## 2026-09-27

### Fixed — every deep link on the live site returned 404

`vercel.json` rewrote `/(.*)` to `/index.html` while `cleanUrls` was on. Vercel 308-redirects `.html`
paths under `cleanUrls`, so the rewrite failed and `/matrix`, `/country/DE` and a refresh on any page
but `/` returned 404 from the first deploy on. The gate missed it because Playwright runs against
`vite preview`. The destination is now `/`, and `tests/test_vercel_config.py` asserts that it cannot end in
`.html`. Verified on a preview with `vercel curl` before going to production.

### Added — `DEPLOYMENT.md`, and a redeploy

The live site was the 2026-09-11 deploy (`cc242ed`), 12 commits behind, serving an `eu27.json` older
than `91c86c9`. Deploys are manual, so nothing had shipped it. `DEPLOYMENT.md` collects topology,
the deploy flow, the upload boundary, staging, a freshness check, known gaps and a deploy log. The README
"Deployment" section now points to it.

---

## 2026-09-24

### Added — the source register (#67)

`model/sources/registry.csv` (each original document once) and `citations.csv` (each claim linked to
it, with a locator and a quote, or for a dataset the value found), validated by `model/provenance.py`
and ratcheted by `tests/test_provenance.py`. `model/sources.csv` is retired; its two rows migrated and
`sources.py` reads the register. The 162 Eurostat cells are cited from their pinned series; the 26
`gov_employment_k` cells are cited but not counted, because they do not reproduce it.

- Every generated brief's key-figure table now takes its source notes from the register; the wrong
  "Eurostat LFS 2025" label is gone, and each brief says beside the employment figure that it does not
  reproduce its source. Model output byte-identical; `eu27.json` unchanged (no artefact stale).
- The launch gate widened, at the author's instruction: nothing launches until every published claim
  cites an original source (#67, `ROADMAP.md` § Sourcing plan).

### Added — the institutional map, 25 of 324 pairs (#68)

37 rows in `model/institutions.csv`, admitted by a screen in the private repo: validator, no name,
nothing the commit gate blocks, quote found on the body's page. Web routes only — the gate blocked the
first fill for its email routes, and `institutions.py` now rejects `mailto:`. `tests/test_institutions.py`.

### Added — the outreach inventory, private (#66)

In `contacts/` (the private repo): 956 seats held by 910 people across the EU institutions and 26 member
states, each with why they matter, a seat quote and an institution-published work contact; every row
fetched and checked on its page, 850 send-ready, 78 unconfirmed addresses removed. MEPs on six
committees come from the European Parliament's open-data API. This repository records counts only.

### Changed

- The NL concept poster moved to `countries/NL/assets/` (#65).
- `PROGRESS.md`, `ROADMAP.md`, `README.md`, `model/README.md`, `VERIFICATION.md`, `SOURCES.md`,
  `OUTREACH.md`, `TODO.md` brought up to date (2026-09-26).

## 2026-09-22

### Added — `DISTRIBUTION-AND-TRUST.md`, an authored note (#64)

What a sovereign estate can borrow from CDN architecture, and the encryption, accountability and
auditability that wide distribution depends on. The second authored note under #59, and joined
rather than split in two because the argument only works joined: distributing state data more
widely is a straightforward loss until encryption makes a seized replica inert and a verifiable
audit trail makes an unauthorised read detectable from outside the operator.

It names the mechanism `TIER0-TIER1-SIZING.md` item 4 was missing. That item proposed "commercially
hosted with sovereign-held keys" for the Tier 2/3 bulk and left open how that could be more than a
contractual promise; attestation-gated key release is the answer, and confidential computing was
absent from the repository entirely before this.

The note carries no figures, deliberately. The model has no term for distributed topology — #12
already records that the `min_sites` floor binds for 24 of 27 countries, making site count "mostly
a *political* parameter" — so any number would have been invented. `ROADMAP.md` gains a Planned
entry for what making it a modelled dimension would take, including the ripple through both
TypeScript type files and the golden results file.

Before this, `accountability`, `transparency`, `confidential computing` and `Schrems` appeared
nowhere in the repository, and `encryption` appeared once.

---

## 2026-09-21

### Fixed — the gate had been red for a week

`web/e2e/app.spec.ts` hardcoded `305.7 MW`, `125,089` servers and Germany's `60.4 MW`; pinning the
Eurostat vintages in `cc242ed` moved the totals to `306.4`, `125,371` and `60.7`, and nothing
updated the expectations. Failing since 2026-09-13.

The fix is not new constants. The three figures are now read from `model/eu27_results.csv` — which
the spec's own comment always claimed was where they came from — and formatted with the app's own
`mw()` and `num()`, so neither the number nor its rendering can drift independently. The parser
throws on a malformed row rather than yielding `NaN`, because a silently undefined expectation is
how this went unnoticed in the first place.

CI still cannot see this class of failure: `.github/workflows/ci.yml` runs the Python suite and
gitleaks, but no `npm run build`, no Vitest, no Playwright and no mobile suite. Recorded, not
fixed.

### Added — the critical national data register (#60)

`model/national_data.csv` records per member state which of the fifteen Tier 0/Tier 1 record
classes it holds, the national register that holds them, and the official page describing it,
with the publisher, retrieval date and a supporting quote. `model/national_data.py` validates and
reports (`./run.sh registers`); `tests/test_national_data.py` ratchets coverage from both sides,
as `tests/test_sources.py` does.

It renders as a new section in all four country renderings — `## 13.` in the generated briefs,
section 9 on the web, a subsection in the book chapter and the A4 brief, section 10 in the mobile
reader — and as a hand-written `## 21.` in `countries/NL/GOAL.md`, which the generator may not
touch (#5). A test asserts every Dutch register named in the CSV appears verbatim in that file, so
the hand-written copy cannot drift from the register.

All fifteen classes render for every country, always. **3 of 405 pairs are recorded** — the three
Dutch registers `TIER0-TIER1-SIZING.md` names as the ones to validate against: the BRP, the BRK
and the Handelsregister. Four other candidate pages 404'd or could not be quoted with confidence
and so were left unrecorded rather than guessed.

### Added — tables of contents, and country flags in the indexes (#61, #62)

Every generated brief opens with a contents list, built from the same `SECTIONS` tuple as the
headings themselves, with GitHub anchors; `countries/NL/GOAL.md` gained one by hand. The web
country page gained an on-page section index. `countries/SUMMARY.md` became a real index: each
country name links to its brief, and each row carries its flag. The web country table and the
mobile country list carry flags too.

Flags appear in indexes and navigation only, never on a poster or a briefing PDF (#47, #61). The
book's outline identifies countries as `DE · Germany` instead, because its interior is mono (#28)
and typst could only reach flag glyphs through a colour, macOS-only font — which would have made
`./run.sh book` silently render empty boxes anywhere but this machine. `tests/test_book.py` now
asserts no flag codepoint reaches the typst source.

The glyph is derived rather than stored in the bundle (#62). That kept the whole
table-of-contents change at **zero artefact churn**; only the register, which does move the
bundle, required re-rendering the 54 tracked binaries.

### Added — `artifacts/`, a style guide per representation (#63)

`artifacts/{markdown,html,pdf,png,mobile}/STYLE.md` plus a README stating the invariants that hold
across all of them. They are the working form of rules that were spread across this register and a
handful of source comments, and they cite decisions by number rather than restating them. All six
files are in `tests/test_docs.py`'s `CITING` list, so a citation that stops resolving fails the
suite.

---

## 2026-09-17

### Added — `mobile/`, an Expo reader for the same bundle

One app with the country as data rather than 27 builds: a filterable list of the member states, a
country screen following the same nine sections as `web/src/pages/Country.tsx`, and a methodology
screen carrying the not-yet-verified notice the site carries. `assets/data/eu27.json` is a copy of
`web/public/data/eu27.json`, so the app renders the whole model with no network at all, and
`__tests__/parity.test.ts` fails if the copy — or the copied `types.ts` and `format.ts` — drifts
from its original.

Local only: no EAS build, no store listing, no deploy. `.vercelignore` excludes the directory,
which matters because Vercel reads that file *instead of* `.gitignore`. Supabase is wired and idle
in `src/services/supabase.ts` — unconfigured returns `null` — for the mirror described in
[`ROADMAP.md`](ROADMAP.md), "Later — a mobile reader". No decision recorded: nothing irreversible
was decided.

### Added — security and privacy checks for a JS app in this tree

The commit gate already scans everything here for secrets and personal data. Three things it cannot
see are now asserted in `mobile/__tests__/security.test.ts`: that no `EXPO_PUBLIC_*` name is
secret-shaped (Expo inlines those into the shipped JavaScript, so a service-role key placed there
would be published to every install); that the app asks for no device capability, declares no iOS
usage strings and refuses cleartext traffic; and that every dependency is on an allowlist, which is
how analytics and crash-reporting SDKs stay out. `./run.sh test` in `mobile/` also runs
`npm audit --audit-level=high`, and every version is pinned exactly.

### Added — `gitleaks` in CI, and `tests/test_ignore_rules.py`

CI ran the model tests and nothing else; it now calls the shared reusable gitleaks workflow, which
scans full history with the shared ruleset rather than the diff. Separately, the ignore rules that
keep personal data out of git and off Vercel are now asserted rather than trusted: `**/contacts/`
and `cache/` in both files, `mobile/` in `.vercelignore`.

---

## 2026-09-13

### Added — `FEASIBILITY-RANKING.md`

An authored note ranking all 27 member states by how feasible a combined national plan for
sovereign data centers and sovereign AI models would be, in four groups (A–D). France, Germany,
Spain and Italy lead; Slovakia, Croatia, Ireland, Cyprus and Malta trail. The more useful finding
is where the two halves diverge: Estonia, Luxembourg and Latvia are easy on data centers and hard
on models, Denmark and Sweden the reverse.

The data center half reads the existing parameters. The model half is unsourced general knowledge
current to roughly May 2026, and the note says so throughout. A bounded exception to #10, recorded
as #59. `tests/test_docs.py` now checks the note's decision references too.

Builds the layer that was missing under the verification workstream: something that actually
fetches the sources. Eurostat first, then the legal corpus, then a nine-cell pilot run on top of
both. Reasoning in [`DECISIONS.md`](DECISIONS.md) #56; the arrangement is documented in the new
[`SOURCES.md`](SOURCES.md).

### Added — the fetch layer

`model/fetch.py` retrieves a document, writes it into `cache/`, and records its sha256, size,
HTTP status and retrieval date in `model/fetch_manifest.csv`. The cache is gitignored **and**
`.vercelignore`d; the manifest is tracked. Same trade as #52: the hash travels with the repository,
the megabytes do not.

Two pipelines sit on it. `./run.sh fetch eurostat` re-pulls the six Eurostat figures for all 27
(ROADMAP step 4, now closed); `./run.sh fetch legal` retrieves the legal corpus from
`model/source_urls.csv`. `tests/test_fetch.py` guards both, and passes with an empty cache, which
is what CI has.

### Found — two defects in the data, both invisible to the existing tests

**France's classification ladder was wrong.** `data_classification` read *"IGI 1300: Diffusion
Restreinte / Secret / Tres Secret"*. The instrument says, in terms, that Diffusion Restreinte
*« n'est pas un niveau de classification mais une mention de protection »* — it is a protective
marking, not a classification level. Corrected to the two levels that exist.

**Cyprus's population was Estonia's.** `population_m` held `1.370`, which is exactly Estonia's
Eurostat figure for 1 January 2025 (1,369,995). Cyprus's own is 0.983 m. Corrected. The capacity
outputs did not move, because the small-state floors already bind for Cyprus (#12).

Neither was findable by reading more carefully: a plausible number in the right format is not a
detectable error, and the classification cell reads perfectly well until you open the instrument.
That is the argument for the process, and it is the sixth and seventh entries in the #14 list.

### Found — two gaps in the verification schema itself

`covered_cells()` marks a cell sourced once **one** row exists, but the cells are free prose and
several assert more than one thing, so half a cell can read as verified. The convention is now one
row per instrument named.

Worse: **a negative claim has no primary source.** NL `certification_scheme` is *"No national cloud
scheme; BIO is the binding baseline"*, and roughly 19 of 27 states sit at `certification_strength:
baseline`. No instrument enacts the absence of a scheme, and tier 1 admits nothing but `primary`.
That is a substantial fraction of one tier-1 column with no route to being sourced under the
current rule. Recorded, not solved.

### Fixed — the fetcher's own honesty, twice

Python's `RobotFileParser.read()` treats a 403 on `robots.txt` as *disallow everything*, so the
first run reported eleven hosts as "robots-denied" when in fact they had simply blocked the
request and never served their rules. Those are different facts; `robots.txt` is now fetched
directly and its status kept. Correcting it took the corpus from 22 fetched to 25.

The opposite error surfaced immediately after: Poland's `isap.sejm.gov.pl` publishes
`Disallow: /` for all agents, but serves `robots.txt` only to browser user-agents — so the
corrected fetcher sailed straight past a real prohibition and retrieved the page. It is now marked
`forbidden` by hand and never attempted. Being *able* to fetch something is not permission to.

### Eurostat — the columns were already right; the pipeline was wrong

**Superseded later the same day. The first version of this entry reported that 98 of 162 values
differed from the CSV, "almost all of it vintage drift", and that the published OPEX was ~12%
overstated. That finding was false, and it was my measurement that was broken.** `nrg_pc_205`
band IC is 500-1,999 MWh/yr; the fetcher was requesting `MWH2000-19999`, which is band **ID**.
Against the correct band the electricity column matches at **0.00%**.

Recalibrating every column against period as well as filter gives the real picture. Each column
was taken from one specific vintage, and once pinned to it, **five of the six reproduce exactly**:

| Column | Dataset | Pinned period | Cells differing |
|---|---|---|---|
| `population_m` | `tps00001` | 2025 | 0/27 |
| `gdp_eur_bn` | `nama_10_gdp` B1GQ CP_MEUR | 2025 | 0/27 |
| `elec_price_eur_mwh` | `nrg_pc_205` band IC, X_VAT | 2025-S2 | 0/27 |
| `renewables_pct` | `nrg_ind_ren` REN_ELC | 2024 | 0/27 |
| `land_km2` | `reg_area3` L0008 | 2019 | 0/27 |
| `gov_employment_k` | `nama_10_a64_e` NACE O | 2023 | **26/27** |

So nothing needed a vintage bump. What the figures lacked was a *recorded provenance* — which is
what ROADMAP step 4 asked for all along, and what `eurostat_pull.csv` now carries. 28 cells were
nudged to match their pinned vintage exactly (mostly trailing precision; materially CZ +4.8%,
PT +5.9%, EL −2.0% population, DE +1.3% GDP). EU-27 totals move +0.23%; sites stay at 86.

**`gov_employment_k` is a provenance defect, not stale data.** It reproduces from no period at
all, and **9 of 27 values match no year of the official series within 10%** — Sweden is 40% out.
The README claims this column is "Eurostat NACE section O"; for a third of the states that is not
where the number came from. The 27 values are held unchanged pending a rebuild, and
`tests/test_fetch.py` now enforces that every *other* column reproduces from its stated source,
with this one named as a known defect so it is documented rather than silently tolerated.

The lesson is the expensive one: a measurement tool that is itself mis-specified does not fail
quietly, it manufactures confident findings. Being wrong with evidence attached is worse than
having no evidence. The periods and filters are now pinned in `SERIES` with the reasoning beside
them, and bumping a pin is a deliberate edit with a diff.

### Added — `confidence: absence`, because 39 cells assert that nothing exists

22 of the 81 tier-1 cells — 21 of the 27 `certification_scheme` cells — say some version of "No
national scheme". No instrument enacts the absence of a scheme, so under a rule admitting only
`primary` those cells could never be sourced. Tier 1 was capped at **59/81 = 72.8%**, the ledger
at 167/189, and `sources.py --strict` — the end state ROADMAP step 3 asks for — **could never
pass**. That is an unsatisfiable specification, not a research backlog.

`confidence: absence` closes it. Evidence of absence is not an instrument but an **authoritative
enumeration**: the competent authority's own register of schemes, showing the category empty. A
claim about a complete list is evidenced by the complete list.

It is also the easiest value to abuse — it would let any hard-to-find instrument be waved
through — so `sources.py` refuses an `absence` row whose cell does not actually assert an
absence, and `tests/test_sources.py` asserts that refusal. The coverage report now prints, per
column, how many cells are negative and how many were sourced that way.

No `absence` rows are recorded yet: ENISA's NCCA directory enumerates authorities, not schemes,
and inventing a weaker citation is precisely what this value exists to prevent. The mechanism is
unblocked; finding the right register per state is the next batch.

### Added — deployment as a command

`./run.sh deploy` refuses a dirty tree or a non-`main` branch, runs the full gate, checks that
`.vercelignore` still excludes `cache/`, then deploys. Deploys are manual because the Vercel GitHub
App is not installed, and a stale site was the named failure mode; a remembered incantation is a
bad defence against it. `README.md` gains the `## Deployment` and `## Verification` sections it
never had.

`./test.sh` now prints the ledger coverage as its own step and in the closing banner, and
`./init.sh` prints it on a fresh clone. The blocker should be visible to whoever is standing in
front of it.

### Still owed

The blanket "not verified against primary sources" wording in `ProvenanceBanner.tsx`,
`Methodology.tsx`, `Poster.tsx` and the generated brief §10 is still substantially true at 2 of
189, so it stands. It needs revisiting when tier 1 completes — as does the `ixp` / `threat_notes`
gap now recorded in `ROADMAP.md`.

## 2026-09-08

Closes the four findings the 2026-09-06 audit left open, and scaffolds the verification
workstream that gates everything public-facing. Reasoning in [`DECISIONS.md`](DECISIONS.md)
#51-#55; the workstream itself has its own document, [`VERIFICATION.md`](VERIFICATION.md).

### Decided — the per-country artefacts ship in the repository

Audit finding 1 asked for a decision, not a cleanup: 54 tracked binaries against a `README.md`
sentence saying nothing generated is committed. The cause turned out to be a contradiction, not
an accident. **#24 and #41 were written on the same day and say opposite things** — "per-country
PDFs, posters and the JSON bundle are tracked" against "no generated PDF is ever committed" —
and the tree followed the first while the README quoted the second.

They stay tracked (#51). #41 is scoped to the typst build directories it actually governed, and
the two pipelines are now named wherever they are described, because they were being conflated:

| Pipeline | Output | Tracked |
|---|---|---|
| `book/build.py --briefs` (typst), `./run.sh export` | `book/build/briefs/` | no |
| `model/export_artifacts.py` (Chrome), `./run.sh artefacts` | `countries/<ISO>/` poster and PDF | yes |

`./run.sh artefacts` is new. `ASSETS.md` and `ROADMAP.md` both credited `./run.sh export` with
producing the tracked artefacts; that command typesets something else, and the artefacts had no
`run.sh` entry point at all.

One thing is recorded rather than settled: #39 abandoned the Chrome PDF path on 2026-09-04 as
"weak for a document handed to a ministry", and #47 reinstated it on 2026-09-05 without that
being weighed. Both PDFs render from the same dict so no figure can diverge, but whether a
country directory should hold the web brief as printed or the typeset one is a product question.
`ROADMAP.md` now carries it under **Open questions**.

### Fixed — the PDFs are byte-reproducible, and were stale

Chrome stamps wall-clock `/CreationDate` and `/ModDate` into every PDF, so the 27 tracked
briefings were the only part of the repository that was not byte-reproducible (#15, #34). Both
fields are now rewritten to `.build-epoch` after printing, length-preserving so the
cross-reference table survives (#53).

Verified by exporting all 27 countries twice and comparing: **54 of 54 artefacts byte-identical
across two full runs.**

Re-rendering also showed the PDFs had drifted. `f03fde7` changed the bundle and re-rendered the
27 posters **but not the 27 PDFs**, which kept a provenance banner reading "Generated
2026-09-03" for three days — wrong on the artefact designed to travel without the page that
explains it, and invisible because half the artefacts had been refreshed.

### Added — `countries/ARTEFACTS.csv`, so the next drift fails a test

Each artefact's sha256 alongside the sha256 of the JSON bundle it was rendered from (#52). CI has
no Chrome and cannot re-render to check, but comparing two hashes needs no browser.
`tests/test_artifacts.py` fails when the data has moved past the binaries, when a file no longer
matches its recorded hash, or when a PDF carries a wall-clock date. A partial export carries the
untouched rows' recorded hashes over rather than certifying files it did not render.

### Added — the verification ledger

`model/sources.csv`, `model/sources.py`, `tests/test_sources.py` and `VERIFICATION.md` implement
ROADMAP steps 1-3 (#54). The ledger is **empty: 0 of 189 cells sourced**, which is the honest
starting point and now a visible number rather than a paragraph — `./run.sh sources` and
`./run.sh health` both report it.

- Schema `country,column,url,publisher,retrieved,confidence,quote`. A quote under 20 characters
  fails validation: a URL shows a page exists, not that it says what the cell claims.
- Three tier-1 columns require `confidence: primary`. Four tier-2 columns take an official
  government page. The three ordinal columns are author judgements (#10) and a source row for
  one is an error.
- `sources.py --strict` is the end-state gate and is deliberately not in CI yet. What CI enforces
  is `COVERAGE_FLOOR`, a ratchet that may only be raised.

### Fixed — DECISIONS.md had two entries numbered 38, 39, 40 and 41

For three days. `README.md` cited #41 meaning the PDF rule and `ROADMAP.md` cited #41 meaning the
domain choice, and both were right, which is the worst way for a reference to be wrong. The
second block is renumbered #47-#50 and every reference to it updated across `ASSETS.md`,
`CHANGELOG.md`, `ROADMAP.md`, `.gitignore` and `DECISIONS.md` itself.

`tests/test_docs.py` now asserts numbers are unique and contiguous and that every `#N` reference
resolves to an entry (#55).

### Changed — CI runs with `contents: read`

Audit finding 2. The job checks out, runs stdlib Python and reads a diff; it inherited the
default read/write `GITHUB_TOKEN` scope for no reason.

### The pattern, again

Three of the four audit findings were drift between what a document asserted and what the tree
did. Closing them turned up three more of the same shape: the #24/#41 contradiction, the
duplicate decision numbers, and the wrong command in two documents. None dangerous alone; all of
them the shape that hides something that is. Fourteen new tests fail on the next one.

---

## 2026-09-07

### Changed — the contacts repo now lives at `contacts/`

`sovereign-data-centers-contacts` moved from a sibling directory under `~/dev/projects/` to `contacts/`
inside this working tree. It is still a separate private repo with its own `.git` and its own remote —
nothing was merged and no file crossed between repos. Reasoning in [`DECISIONS.md`](DECISIONS.md) #46.

Verified rather than assumed, because #49 and #45 both record this exact class of assumption going wrong:

| Check | Result |
|---|---|
| `git -C contacts remote -v`, `status -sb` | private remote intact, `main` in sync, one commit `9e0270f` |
| `git status --porcelain`, `git ls-files contacts` | both empty — the outer repo sees nothing |
| `git check-ignore -v contacts/NL/list.md` | `.gitignore:38:**/contacts/` |
| `git add -f contacts/` on a scratch clone with the real files | one mode-160000 gitlink, 180 bytes; 473 distinctive tokens from `NL/list.md`, zero in the staged diff |
| `git clean -nxfd` | does **not** list `contacts/` — one `-f` refuses to remove a nested repo |
| `git clean -nxffd` | **does** list it. The one new hazard; keep the private repo pushed |
| 18 name strings from the private files vs. all 21 public commits | only `European Parliament` and `Tweede Kamer` — institutions, same result as #45's audit |
| `./test.sh --no-e2e` | passes; the generators walk `countries/` only |

The `.gitignore` rules (`**/contacts/`, `*-contacts.md`) stay, demoted to a second layer behind the
nested `.git`, and the comment block above them now says so.

### Removed — the empty `book/contacts/`

Left behind by the `paper_book/` → `book/` rename (#38) and the near miss in #49. An empty directory
called `contacts` in this repo is a trap for precisely the mistake the ignore rules exist to prevent.

---

## 2026-09-06

### Repository lineage — where the frontier note came from

The note was first published as a standalone public repo, `pieteradejong/dutch_frontier_model`, before it
was clear it belonged here. That repo is now **archived** and read-only, with its description pointing at
`countries/NL/FRONTIER-MODEL.md` so the old URL still leads somewhere useful. Nothing was deleted: the
single commit remains readable, and the local working copy was removed once the content landed here.

Archiving locks a repo immediately, so setting that forwarding description required unarchiving it for
one call and re-archiving straight after. Worth knowing before archiving anything else.

### Audited — security and privacy, round two

Second full audit, 2026-09-06, covering the working tree **and** all 21 commits rather than the current
state alone. Findings and the verification detail are in [`ROADMAP.md`](ROADMAP.md); the summary is that
nothing is disclosed and three of the four findings are documentation drift.

The audit also closed out bookkeeping the repo had been carrying: the four 2026-09-04 findings were
remediated in `f03fde7` but `ROADMAP.md` still listed them as open, and it still sent readers to
`paper_book/contacts/` for named individuals after #45 moved them into a private repo. Both corrected.

The contacts split (#45) landed the same day and was verified rather than taken on trust — the private
repo is private, is pushed and in sync with origin, and no token from it appears anywhere in this
repository's history. See ROADMAP for why the "pushed" half of that check is the one that matters.

**Open, and deliberately not fixed here:** 56 generated binaries (27 briefing PDFs, 27 infographic PNGs,
12.7 MB) are committed even though `README.md` and #41 both say they never are. That needs a decision
about intent, not a patch — see ROADMAP finding 1.

### Added — the frontier-model note (`countries/NL/FRONTIER-MODEL.md`)

An authored companion to the RijksCloud capacity plan answering "what would it take for the Netherlands
to develop its own frontier model, or at least something suitable?" — the question that comes up every
time the sovereign cloud plan is discussed. Drafted as a standalone repo, merged here because it only
makes sense next to the NL reference case. Reasoning in DECISIONS.md #44.

Three tiers, costed: sovereign *deployment* capability (€50-150M, 18 months, fits inside RijksCloud's
existing GPU envelope), sovereign mid-scale pretraining (€1.5-3B, 5 years, Eemshaven), and frontier
parity (€15-30B+, only as lead partner in an EU gigafactory consortium). Conclusion: frontier parity is
not unilaterally feasible and is the wrong goal; the binding constraints are grid capacity, a
Dutch-language corpus ~1% the size of a frontier training corpus, and training talent.

The note is deliberately framed as a **separate** ask from RijksCloud — ~150 MW against 14.2 MW, $4-6B
against €339M — because the two compete for the same Dutch grid connections and bundling them would sink
the government-cloud case.

Unlike everything else under `countries/`, this file is authored, not generated. `run.sh data` does not
write it; the name is one `generate_countries.py` never touches, like `CAPACITY_PLAN.md` and `TODO.md`.
Its cost figures are reconstructed order-of-magnitude estimates, labelled as such, and held to a lower
evidentiary standard than the model's parameters.

## 2026-09-04 (later)

### Added — the book (`book/`)

`./run.sh book` typesets an A5 print edition with typst. Structure follows DECISIONS.md #27: Parts I, II
and V are authored prose in `manuscript/`, Parts III (the 27-country gazetteer) and IV (reference tables)
are generated by `book/build.py` from `web/public/data/eu27.json` — the same dict the briefs and the web
app render from, so the book cannot drift from the model.

| Path | What it is |
|---|---|
| `book/build.py` | Renderer and CLI. Standard library only, like the rest of the model |
| `book/templates/style.typ` | Mono interior (#28), two page geometries (#40), shared table helpers |
| `book/manuscript/` | Parts I, II and V — **scaffolds**, spine only, ~24k words still to write |
| `book/build/` | Output. Gitignored (#41) |

Current output: 81 pages, 703 KB. Parts III and IV are complete; the authored parts are chapter headings
and opening paragraphs.

### Added — per-country PDF briefs

`./run.sh export` builds 27 standalone A4 briefs into `book/build/briefs/<ISO>.pdf` (1.05 MB total, about
40 KB each, ~2.5 s for all 27). Same renderer as the book's gazetteer chapter — `country_entry(c,
standalone=True)` promotes the headings and swaps the wrapper (#39).

`./run.sh build` now also writes them into `web/dist/briefs/`, served from the app at `/briefs/<ISO>.pdf`
(#42). Skipped with a warning rather than failing when typst is absent.

### Added — `OUTREACH.md`

Institutional distribution map: policy owner, operator, certification authority, procurement vehicle,
parliamentary scrutiny and press desks for all 27 member states, plus an EU-level tier and a send order.
Built on the institutional columns already in `eu27_parameters.csv`, with a provenance table marking which
rows are repo-sourced and which need verification before send (#43).

### Fixed — two bugs surfaced by rendering the briefs

1. **`seismic` is not a boolean.** It holds `"low"` / `"moderate"` / `"high"`, so a truthiness test on it
   was true for all 27 countries and every brief printed a seismic flag — including Germany, which
   `SUMMARY.md` correctly shows with none. The flag rule now matches the model's own
   (`country_data.py:125`): only `"high"` counts. Affects 6 countries, not 27.
2. **`~` is a non-breaking space in typst.** It was missing from the escape set, so "EU average ~184"
   printed as "EU average 184" — silently dropping the approximation marker from a figure. Added to
   `_SPECIAL`.

Both were invisible in the model, the JSON bundle and the web app; only typesetting the value exposed
them. Consistent with #36 — rendering it and looking at it is load-bearing.

### Changed

- **`paper_book/` → `book/`** (#38). `run.sh`, `.gitignore` and DECISIONS.md #26 updated. Both commands
  that referenced the old path had been broken since they were written.
- **`run.sh export`** now points at `book/build.py --briefs` instead of the never-written
  `model/export_artifacts.py`. Help text corrected: it builds briefs, not "reports and posters".
- **`init.sh`** no longer claims Chrome is needed for PDF export. It is needed for the Playwright E2E
  suite only; the typst warning now covers `export` as well as `book`.

## 2026-09-04

### Added — web application (`web/`)

An interactive visualization of the EU-27 dataset. React 19, Vite 8, TypeScript 6, Vitest 5, Tailwind 4,
D3 7, all exactly pinned.

| Route | What it shows |
|---|---|
| `/` | EU-27 totals, the small-state cliff, the binding-constraint finding |
| `/matrix` | Sovereignty readiness matrix — 27 × 8 diverging heatmap, sortable, cells link to source text |
| `/workloads` | Country × workload class heatmap, absolute / row-normalized toggle |
| `/scenario` | Live sandbox — six assumption sliders recompute all 27 countries in the browser |
| `/countries` | Index of all member states |
| `/country/:iso` | Full briefing: capacity, geography, legal posture, landscape, migration path |
| `/methodology` | What the model is, what it is not, and the shared assumption table |

The whole dataset is ~40 KB gzipped, so it ships client-side in one request. No API, no server.

### Added — tooling scripts

- **`init.sh`** — version-checked prerequisites, dependency install, data bundle generation. Idempotent,
  verified from a deleted `node_modules`.
- **`run.sh`** — `dev` (default), `build`, `preview`, `test`, `lint`, `format`, `type-check`, `data`,
  `export`, `book`, `clean`, `health`, `help`.
- **`test.sh`** — the full gate, eight stages, cheapest first, failing on the first problem.
- **`.build-epoch`** — the pinned generation date, read by all three scripts.

### Added — testing

- **TS/Python parity suite.** Asserts `web/src/model/capacity.ts` reproduces `model/eu27_results.csv` for
  all 27 countries. Gates the scenario sandbox. 30 assertions.
- **Playwright suite.** 15 tests: rendered-data assertions, axe accessibility on all seven routes, and a
  375 px responsive check. Drives the installed Chrome rather than downloading Chromium.
- Earlier the same week: 15 stdlib Python tests covering model invariants, CSV integrity, referential
  integrity and generator determinism.

### Added — documentation

- **`DECISIONS.md`** — 37 dated ADR-style entries.
- **`CHANGELOG.md`** — this file.

### Fixed — accessibility

- `aria-sort` moved from the sort button to the `<th>` that owns it.
- `--color-fg-muted` darkened from `#898781` to `#6f6d66`. The design-system value measures 3.21:1 against
  the page — correct for axis ticks at the 3:1 graphical threshold, failing AA as body text.
- Toggle button text changed from white on terracotta (3.12:1) to slate (4.85:1).

### Fixed — legibility

- Matrix column headers were clipped to `w-6`, rendering every dimension name as "Sov…", "Cert…", "Hyp…".
  Found by screenshotting the built page; every automated check passed while the chart was unreadable.

### Fixed — tooling

- `SOURCE_DATE_EPOCH` was a duplicated literal in two scripts and missing from `init.sh`, so initialising a
  fresh clone made the committed bundle look stale. Centralised in `.build-epoch`.
- The E2E preview server moved to port 4823 with `strictPort`. Another workspace project was serving 4173;
  Playwright silently reused it and tested a different application.
- Playwright's `channel: 'chrome'` hardcodes `/Applications/Google Chrome.app`; this machine has Chrome at
  `/Applications/Chrome.app`. The binary is now resolved explicitly, with Brave and Edge as fallbacks.

### Corrected — figures that were wrong

Both found by asserting them in tests rather than repeating them:

- **"`min_sites` binds for 26 of 27 countries"** → the real figure is **24** strictly floor-bound. Germany
  alone exceeds its floor (6 sites against 4); France and Italy tie theirs exactly at 4. The "26" came
  from an early survey that counted ties as floor-bound.
- **"Nine states fall below 1 MW per site"** → the real figure is **8**. This conflated two different
  metrics; `README.md` separately claimed nine states under 3 MW total design load, also wrong, also 8.
  The same eight countries satisfy both: SI, EE, LV, CY, MT, LU, LT, HR.

---

## 2026-09-03

### Added — legal and regulatory dataset

`model/eu27_parameters.csv` extended from 17 to 25 columns, researched for all 27 member states:
`legal_instrument`, `certification_scheme`, `data_classification`, `procurement_vehicle`,
`hyperscaler_gov_exposure`, `gov_cloud_maturity`, plus the ordinals `certification_strength` and
`hyperscaler_dependency` that the sovereignty matrix scores from.

These are **unverified research**, not sourced fact — see `DECISIONS.md` #25 for the gate that must pass
before publication.

### Added — migration phasing

`model/migration_phases.csv` maps the seven workload classes to four phases (sovereign core, security and
defense, state record, elective). `capacity_model.py` emits `countries/<ISO>/migration_phases.csv` with
servers, MW, CAPEX and cumulative share per phase. No new sizing math: it groups results the model already
computed, and phase CAPEX sums to the model's total.

### Added — country briefs extended from 9 to 12 sections

Sections 10–12 cover legal and regulatory posture, current state and provider landscape, and a costed
migration path. Prose varies on certification strength, hyperscaler dependency and government-cloud
maturity rather than reading identically 27 times.

### Added — the fact layer

- `model/country_data.py` assembles every fact about a country into one dict.
- `model/export_json.py` writes `web/public/data/eu27.json` from that same dict.
- `write_goal()` refactored into a pure dict → markdown renderer, 70 lines shorter. Verified
  behaviour-preserving: regenerating all 27 countries produced a byte-for-byte zero diff.

### Added — reproducibility

Generated files stamp their date from `SOURCE_DATE_EPOCH` when set. Previously every run rewrote 27 files
with a new date, burying real changes and making "regenerating changes nothing" untestable.

### Fixed — CSV corruption in the published output

The `IT` and `ES` rows had unquoted commas in the `ixp` field, shifting every later field. Italy's
published brief printed " Sicily" as its entire threat-notes section, and Spain's printed " Grace Hopper)
and Barcelona (2Africa". A field-count test now catches this class of defect.

### Fixed — writers disagreeing on row order

`model/eu27_results.csv` was written by both `generate_countries.py` (NL first) and
`capacity_model.py --all` (alphabetical). Any golden-file comparison would have been pure noise. Both now
sort by ISO.

### Fixed — an incorrect claim about Ireland

The exposure entry stated that all three hyperscalers anchor their principal EU regions in Dublin. AWS and
Azure do; Google's `europe-west1` is in Belgium. The existing `hyperscaler_regions_live=2` was right and
the prose was wrong.

### Added — CI

`.github/workflows/ci.yml` runs the Python suite and fails if committed generated files are stale.

---

## 2026-09-01 and earlier

The repository existed as three commits with the entire EU-27 generalization untracked: both Python
scripts, the parameter dataset, all 26 generated country directories and `SUMMARY.md`. Committing that
baseline was the prerequisite for everything above, since regenerating 27 files against an uncommitted
tree produces an unreviewable diff.

Prior history: a single-country Dutch capacity model (`GOAL.md`, an xlsx, three input CSVs, an
infographic), generalized to all 27 member states by a stdlib-only Python model.
