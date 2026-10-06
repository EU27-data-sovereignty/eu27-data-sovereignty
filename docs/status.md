# Status: 2026-10-06

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
| Site | https://eu27.cloud, `noindex`, deploy `f119e8f` |
| Printed facts | 1,396, each confirmed by a second model that did not write it (#87) |
| Withheld facts | 56, shown as disputed with the checker's reason (#89, #94) |
| Fact-check runs | the pilot; the full run; populations; refused pages from hashed copies; the correction round re-check; 2 stability samples (6 of 100 rejected by the second checker) |
| `/ask` | answers with citations, on the new key, set in the Vercel dashboard (2026-10-05) |
| Monitoring | weekly live smoke test plus a Eurostat vintage check; daily `/ask` check, strict (`ASK_LIVE=true`) |
| Deploys | only from GitHub Actions, prebuilt, after `./test.sh` and the fact-check gate. Vercel's own git deploys are off (`vercel.json`) |
| Pull requests | full `./test.sh --no-pdf` plus `npm audit` |
| Tests | 270+ Python; 51 Vitest; 198 browser tests (Chrome, Firefox, WebKit, iPhone SE, iPhone 17 Pro, visual) |

## Decisions recorded this period

- **#87** Every printed fact is checked by the model that did not write it before every deploy.
- **#88** The methodology is in every asset, set apart in a method teal.
- **#89** A fact the check does not confirm is withheld, not a reason to block the deploy.
- **#90** eu27.cloud uses Vercel's nameservers.
- **#91** The site takes the report's look.
- **#92** The full gate on every pull request, plus live smoke tests after each deploy and weekly.
- **#93** A withheld fact can be corrected by a later round, through every check again.
- **#94** A second checker's disagreement withholds a confirmed fact too.

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
5. Small items:
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
