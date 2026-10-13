# Country paths and the push rule: the working log of 2026-10-12

What was asked, what was decided, what was done and how each step was checked, in order. The decisions
themselves are in [`DECISIONS.md`](../../DECISIONS.md) (#105, #106) with their alternatives; the reader-facing
summary is in [`CHANGELOG.md`](../../CHANGELOG.md). This log is the trail between them: it names the commits,
the commands and their output, and what is still open. Planning, not data: nothing here is read by the
model, the book, the web app or `/ask`.

## 1. The ask

The owner asked for one address per member state, giving `eu27.cloud/de` as the example, then to push
everything, then for a permission rule so the assistant can push to `main` while every safety, privacy and
data-integrity rule stays in place, and for all of it to be documented in markdown.

## 2. Decisions made

| # | Decision | Where |
|---|---|---|
| 105 | A member state's page is its lower-case code as a top-level path (`/de`, `/el`), not a subdomain. `/country/<ISO>` redirects. No other two-letter top-level route. | `DECISIONS.md` #105 |
| 106 | A tracked `.claude/settings.json` allows the assistant two push forms to `main` and denies the other outward actions by name. The owner's OK in the conversation still comes first. | `DECISIONS.md` #106 |
| — | The branch's decisions #101 to #103 were renumbered to #103 to #105 because `main` had taken #101 and #102 for the landing design and the guide pages. `main`'s numbers were already published, so the branch moved. | commit `3c41351` |
| — | The appliance note (#104, then #102) and the country paths were cut as two commits, the appliance first, because #105 depends on the entry before it and `tests/test_docs.py` requires contiguous numbers. | commits `f73c24a`, `0a64633` |
| — | Other sessions' uncommitted work in the same checkout (the stichting plan, the `OUTREACH.md` change, a README deployment paragraph) was left uncommitted. Partial staging by hunk kept it out of both commits. | this log §4 |

## 3. What stays exactly as it was

The rule in #106 changes one prompt and nothing on the path to production:

- the security gate on every commit and push (`dotfiles/security/gate.sh`), which ran on each commit below;
- the `guard-git-bypass` hook, which denies `--no-verify`, the git hooks path and the bypass variable, and
  which blocked one of this session's own commands for merely mentioning the hooks path in a heredoc;
- the global denies on force pushes, `~/.ssh`, `~/.aws` and `.env` files;
- the noreply committer identity;
- the Actions gate (`./test.sh` as parallel jobs plus gitleaks, #97) and the fact-check gate (#87);
- the project rule that the owner's OK in the conversation precedes every push to `main`.

New denies, so the boundary is written down rather than implied: `git push origin --delete`,
`vercel deploy --prod`, `vercel --prod`, `gh repo edit`, `gh api` with a write method.

## 4. What was done, in order

1. **Country paths** (`0a64633` on `sovereign-appliance`). `web/src/utils/routes.ts` holds `countryPath`;
   six link sites use it; `App.tsx` adds the `:iso` route after the static ones, redirects `/country/:iso`
   and upper-case codes; `vercel.json` adds the permanent redirect. Tests: three in
   `tests/test_vercel_config.py` (the redirect exists; no two-letter source; no link built outside the
   helper), four in `web/e2e/app.spec.ts`; route lists in `model/smoke.py` and the e2e moved; the three
   `/country/DE` visual baselines renamed to `/de`.
2. **Appliance note first** (`f73c24a`). The other session's finished work, staged by file and by hunk so
   the stichting and OUTREACH changes stayed out. Verified on the staged tree alone: 362 Python tests OK,
   the note's own check 0 problems.
3. **Push of the branch.** `origin/sovereign-appliance` set as upstream.
4. **Renumbering** (`3c41351`, on `sovereign-appliance-merge`). 85 citations in 25 files moved in one pass;
   the base of the branch cites none of the three numbers.
5. **Merge of `origin/main`** (`b7f5931`). Six conflicts resolved by hand: both route groups in `App.tsx`;
   the tile map and the countries page build links with `countryPath`, the countries page keeping the
   guide's section anchor; the guide-step test and the country tests expect `/de`; `CHANGELOG.md` keeps
   both days' entries newest first; `DECISIONS.md` runs #101, #102 then #103 to #105. The helper test was
   narrowed to template paths built from an ISO code so the guides' `/for` and `/how` links pass.
6. **Full gate on the merged tree.** `./test.sh --no-live`: 18 stages, exit 0, the PDFs compiled,
   Playwright on every project, visual baselines included. Fact-check gate: 1490 of 1490 printed facts
   checked, supported, checker ≠ author.
7. **The push to `main` was refused** by Claude Code's auto-mode classifier as a production deploy. The
   owner's OK in the conversation does not reach the classifier. This is the problem #106 records.
8. **The rule** (`2ead774`). `.claude/settings.json` tracked; `CLAUDE.md`, `CHANGELOG.md` and
   `DECISIONS.md` #106. Verified: `tests/test_docs.py` OK; `./test.sh --only model`, nine checks passed.
   Writing the file into the live checkout was itself refused once as self-modification and then done
   through the `update-config` skill, which is the sanctioned route.

## 5. Verification record

| Check | Tree | Result |
|---|---|---|
| `python3 -m unittest discover -s tests` | staged appliance commit | Ran 362 tests, OK |
| same | staged country-path commit | Ran 365 tests, OK |
| `tsc`, `eslint`, `prettier --check`, `vitest` | staged country-path commit | pass, 51 tests |
| `npx playwright test e2e/app.spec.ts --project chrome` | staged country-path commit | 63 passed |
| same | merged tree | 73 passed after one guide-step URL fix |
| `./test.sh --no-live` | merged tree | 18 stages, exit 0 |
| `./run.sh factcheck status` | merged tree | 1490 of 1490 checked |
| `./test.sh --only model` | rule commit | 9 checks passed |
| live redirect, `curl -sI https://eu27.cloud/country/DE` | production | 308 to `/DE`; `/de` serves 200 (run 38334656899) |

## 6. Open

- Done: `7f265ac` pushed to `main` under the rule, Actions run 38334656899, all gate jobs green, deployed.
- The local `sovereign-appliance` branch in the working checkout is still at `0a64633`; it was left there
  so the other sessions' uncommitted files are not disturbed. Reset it to `main` once the push is done.
- Done in `dotfiles` (`893d744`, not yet pushed): policy §5 names per-project allow rules, this as the first
  example.
- Next content todo: print `eu27.cloud/<iso>` on the country PDFs and posters, which carry no address
  today. It is a content-model change, so a `label` span, a changelog entry and a `/factcheck` run.
- Still later: the mobile reader to schema 2 (`TODO.md`).
- What followed the same day (the language drafts, the pipeline hardening, the universities note, four more
  pushes to `main`) is indexed in [`2026-10-12-session-log.md`](2026-10-12-session-log.md).
