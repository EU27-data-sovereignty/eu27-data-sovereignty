# Status: 2026-10-06 (updated at the end of the day)

This is a point-in-time snapshot. It is not maintained; the current state is in `TODO.md`, `CHANGELOG.md`
and `docs/fact-check-audit.md`.

## Resolved: an unreviewed feature was pushed to `main`

**Outcome: option A, chosen by the owner on 2026-10-06.** The 60 hosting facts were fact-checked by Fable 5.1
(run `wf_e9645602-884`): 56 confirmed and 4 withheld with the checker's reasons. 1,396 printed facts pass, and
56 are withheld. The account below is kept as the record.

**What happened.** Commit `0683d7f` (2026-10-05) was meant to change 4 files. It turned off Vercel's
git-triggered deploys: `vercel.json`, `tests/test_vercel_config.py`, `DEPLOYMENT.md` and `CHANGELOG.md`. The
commit used `git add -A`, so it also took **74 files of another session's in-progress work** from the working
tree, and pushed them to `main` unreviewed.

**What the extra work is.** A "hosting operators" feature:
- `docs/hosting-operators.md` and `countries/EU-INFRASTRUCTURE.md`;
- a new web page, `web/src/pages/Infrastructure.tsx`;
- changes to `model/document.py`, `model/export_json.py`, `model/generate_countries.py` and
  `model/methodology.py`;
- additions to `DECISIONS.md`, `CLAUDE.md`, `README.md`, `ROADMAP.md` and `TODO.md`;
- a regenerated bundle with **60 new `record:…:hosting` facts**.

The session names suggest the author was another Claude session working in this folder
(`sov-data` or `infrastructure-hosting-model`). That is not confirmed.

**What protected the site.** The CI gate ran `./test.sh`, which passed, and then `factcheck.py gate`, which
**failed**: 1,340 of 1,400 printed facts pass, and the 60 new ones have never been checked. The deploy was
skipped. **eu27.cloud still serves the previous good deploy (`f119e8f`).**

**The options:**

| Option | What happens | When to choose it |
|---|---|---|
| A. Keep and finish | Fact-check the 60 new facts (two pooled batches, Fable 5.1, about $10–15), record them, regenerate, run the gate, redeploy | The feature was meant to ship |
| B. Take it back off `main` | Revert the swept-in files and keep the 4-file Vercel change. The authoring session re-commits its work after review. Nothing is lost; it stays in git history | The feature was unfinished |

**The lesson.** Commit only named files (`git add <paths>`) and check `git status` before every commit.
`git add -A` must not be used when other sessions may be working in the same folder.

## What is live

| Area | State |
|---|---|
| Site | https://eu27.cloud, `noindex`, deploy `e39228e` (run 37522504720) |
| Printed facts | 1,396, each confirmed by a second model that did not write it (#87) |
| Withheld facts | 56, shown as disputed with the checker's reason (#89, #94) |
| Fact-check runs | the pilot; the full run; populations; refused pages from hashed copies; the correction round re-check; 2 stability samples (6 of 100 rejected by the second checker) |
| `/ask` | answers with citations, on a key created 2026-10-06 and set in the Vercel dashboard. It **expires 2026-11-05**; a calendar reminder is set for 2026-11-02, 09:00 ET |
| Monitoring | weekly live smoke test plus a Eurostat vintage check; daily `/ask` check, strict (`ASK_LIVE=true`) |
| Deploys | only from GitHub Actions, prebuilt, in about 5 minutes. The gate runs as parallel jobs (`gate.yml`, #97); then the fact-check gate. The deploy ships the gate's own build, checked by tree hash, then runs the smoke test and a live `/ask` call. Vercel's own git deploys are off (`vercel.json`) |
| Pull requests | the same parallel gate without PDFs, plus `npm audit` |
| Tests | 270+ Python; 51 Vitest; 198 browser tests (Chrome, Firefox, WebKit, iPhone SE, iPhone 17 Pro, visual) |

## Today's deploys (2026-10-06)

| Run | Commit | Result | What it shipped |
|---|---|---|---|
| 37498565798 | `2deb629` | failed at `npm audit` | the 60 hosting facts checked; stopped by GHSA-68fv-2mgg-jv7q in `source-map-js` |
| 37509836013 | `437d707` | live, 13.8 min | `source-map-js` 1.2.2; `docs/process.md`; 1,396 facts; 55 of 55 smoke checks |
| 37511934214 | `d8bd0d1` | live, 5:08 | the parallel gate, shipping the tested build (#97), every cache cold |
| 37515393649 | `747ed22` | live, 4:54 | the measured timings; every cache warm (13 restored) |
| 37518689761 | `ac5c6af` | live, 5:14 | the live `/ask` stage, after the new key was set; `/ask`: 940 characters, 3 citations |
| 37522504720 | `e39228e` | live, 5:05 | the key closure, its expiry and the rotation runbook; `/ask`: 1,020 characters, 3 citations |

## Decisions recorded this period

- **#87** Every printed fact is checked by the model that did not write it before every deploy.
- **#88** The methodology is in every asset, set apart in a method teal.
- **#89** A fact the check does not confirm is withheld, not a reason to block the deploy.
- **#90** eu27.cloud uses Vercel's nameservers.
- **#91** The site takes the report's look.
- **#92** The full gate on every pull request, plus live smoke tests after each deploy and weekly.
- **#93** A withheld fact can be corrected by a later round, through every check again.
- **#94** A second checker's disagreement withholds a confirmed fact too.
- **#97** The gate runs as parallel jobs, and the deploy ships the build the gate tested.

## Security

**EU-1** (private findings register): Anthropic keys were exposed in plain text during `/ask` setup.
**Closed 2026-10-06.**
- The workspace `eu27` now holds a single key, created 2026-10-06, and set in the Vercel dashboard as a
  sensitive Production variable.
- Deploy run 37518689761 passed the live `/ask` stage (940 characters, 3 citations).
- The spend limit is set.
- **The key expires 2026-11-05.** The renewal steps are in `DEPLOYMENT.md` § `/ask` runbook.

## Waiting on the owner

1. ~~The swept-in feature~~: resolved, option A.
2. ~~Revoking the old Anthropic keys~~: done 2026-10-06, EU-1 closed. Renew the key before 2026-11-05.
3. The mobile reader: port it or drop it. Its 4 Dependabot alerts, 2 of them high, clear only that way.
4. The mobile app plan: see `docs/plans/mobile-app.md`, owner decisions 1–9.
5. The foundation plan: see `docs/plans/stichting.md`, owner decisions 1–10.

## Next steps, in order

1. ~~Resolve the swept-in feature~~: done, option A.
2. ~~Close EU-1~~: done 2026-10-06.
3. **The human sampling audit**, which unlocks launch and indexing (#25, #50):
   - recruit reviewers for the roster (`model/contrib/reviewers.csv`);
   - draw the sample (`./run.sh contrib audit-sample`);
   - measure the error rate.
4. Decide on the mobile app and the foundation. The app's store accounts and Supabase wait for the
   foundation.
5. **The data plan, step 1: find as much data as we can.** Cheapest gaps first (owner, 2026-10-06): a free
   retry pass, then a $45 wave on the registers found but not verified. Registers known: 675 → 732 of 1,044. Pairs
   recorded: 684 → 741 of 1,053 (70%). 59 registers remain "claimed, not verified". The gap list is `docs/gaps.md`. The hosting wave's
   pilot (NL) filled 12 of 44 gaps for $6.40. **The full wave** covers 1,227 hosting and dependency gaps in 27
   states. Estimated cost, scaled from the pilot: research $150–250, plus about $50 to fact-check what it
   finds. It waits for the owner's OK.
6. **Before 2026-11-05: renew the `/ask` key** (`DEPLOYMENT.md` § `/ask` runbook; calendar reminder
   2026-11-02).
7. **Optimisation 5**, a per-country PDF cache. The PDF job (about 4 min) is now the slowest part of every
   deploy (`docs/process.md`).
8. Small items:
   - a per-visitor rate limit on `/api/ask` in the Vercel firewall;
   - tests for the 3 remaining mutation-audit gaps;
   - a vetting reviewer from a different model than its researcher;
   - re-research the 52 withheld facts, or leave them withheld;
   - delete stale local branches;
   - commit the private dotfiles register.

## Where things are documented

| Topic | File |
|---|---|
| Open work | `TODO.md` |
| What changed and when | `CHANGELOG.md` |
| Why | `DECISIONS.md` |
| How facts are found and checked | `METHOD.md`, `docs/vetting.md`, `docs/fact-check.md` |
| The state of every fact | `docs/fact-check-audit.md`, generated |
| Testing | `docs/testing.md` |
| Deploying | `DEPLOYMENT.md` |
| Plans | `docs/plans/mobile-app.md`, `docs/plans/stichting.md` |
| The pipeline, its timings and the proposed speed-ups | `docs/process.md` |
| What data is missing, and how often it was searched | `docs/gaps.md`, generated |
