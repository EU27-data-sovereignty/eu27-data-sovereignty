# TODO (EU-27)

Cross-country work, as a checklist. Why and in what order: [`ROADMAP.md`](ROADMAP.md). How the evidence is
produced: [`METHOD.md`](METHOD.md).

## Publish (first automatic deploy to eu27.cloud; checklist in `DEPLOYMENT.md`)
- [x] **Owner:** create a Vercel token (https://vercel.com/account/tokens, scope `pieteradejongs-projects`),
      then `gh secret set VERCEL_TOKEN --env production` and paste it
- [x] **Owner:** at iwantmyname, set the nameservers for `eu27.cloud` to `ns1.vercel-dns.com` and
      `ns2.vercel-dns.com` (#90); verify with `dig +short NS eu27.cloud`
- [x] Full fact check recorded; `factcheck.py gate` exits 0 at 1,309 of 1,309 (2026-10-02)
- [x] Fast-forwarded `main` to `feat/fact-check` and pushed (2026-10-02); `Deploy` run 37072208296 green;
      live at https://eu27.cloud (noindex); recorded in `DEPLOYMENT.md`
- [ ] Dependabot: 4 open (2 high, 2 moderate), all in `mobile/package-lock.json` (2026-10-05); `web/` is
      clean. The rebuilt lockfile (#109) carries the same four Expo-toolchain transitives, allowlisted with reasons
      in `mobile/audit-allowlist.json`; **owner:** dismiss them in the Security tab with those reasons
- [x] `security` workflow green on every push since 2026-10-03 (calls the shared workflow, `71d84ba`)
- [ ] `/ask`: dedicated Anthropic workspace with a spend limit and `ANTHROPIC_API_KEY` in Vercel
      (author), then the 12-question eval (with approval), then the Vercel Firewall rate limit

## Fact check and methodology (#87, #88)
Every printed fact is checked by the model that did not write it before a deploy. Status:
`./run.sh factcheck status`. Audit file: [`docs/fact-check-audit.md`](docs/fact-check-audit.md).
Runbook: `/factcheck` (`.claude/skills/factcheck/SKILL.md`).

Done
- [x] Fact-check machinery: `model/factcheck.py`, the checker workflow, a fact hash per verdict, refusal of
      a wrong or self-checking model, the deploy gate in CI and `./run.sh deploy` (commit `4a7d51c`)
- [x] Generated audit file and a fact-check appendix in every asset (PDFs, briefs, web, `/ask`, posters)
- [x] Vetting workflow names its models and records `researcher_model`, so future facts have an author
- [x] Pilot (2026-10-01, run `wf_074137f6-b8e`): DE batch of 30 facts, Fable 5.1 confirmed from the API.
      28 supported, 2 not supported. Measured cost about $4–6 per 30 facts
- [x] Methodology in every asset, including full appendices in the briefs, the generated text in `/ask`,
      and a poster line; a fact-check section in the methodology (#88)
- [x] Method teal (`method` token, AA contrast) for how-we-know material in the PDFs, web and posters (#88)
- [x] Wide web tables keyboard-scrollable (accessibility)

Open
- [x] Commit the #88 methodology and style work and the pilot results (`9e1ddb2`)
- [x] Full run decided (2026-10-02): Fable 5.1, about $185–280, for the remaining 1,362 facts
- [x] A disagreement withholds the fact (shown as disputed with the checker's reason) instead of blocking
      the deploy (#89)
- [x] Full run `wf_da123db1-a4e` (2026-10-02): 1,309 confirmed and 81 withheld (48 not supported, 33 unclear);
      measured cost about $250–370
- [x] (Superseded by the 52 below.) Resolve the 81 withheld facts (owner decides; never edit a verdict). All are listed in
      `docs/fact-check-audit.md` § Withheld. By kind: 31 register or operator names worded beyond their quote,
      15 hosting labels, 13 indicators, about 12 pages the checker could not fetch. Most affected: IE 10,
      EE 10, HU 9, PT 7, SK 6
- [x] Rounding defect fixed (population printed at its stored 3 decimals; test keeps every Eurostat figure at
      its stored precision); 27 populations re-checked and confirmed
- [x] Retry route for facts whose pages refused the checker: `prepare --withheld-blocked`, from the hashed
      copy; 11 of 12 confirmed. 69 facts remain withheld
- [x] Correction round (#93): 69 withheld facts re-researched, 25 corrected or re-sourced and confirmed
- [ ] 52 facts still withheld (2026-10-04): 46 left after the correction round (no T1/T2 quote found,
      reviewer disagreed, or the check rejected the correction) plus 6 a second checker rejected (#94).
      Listed in `docs/fact-check-audit.md` § Withheld
- [x] Stability samples: Opus 5.5 disagreed with 6 of 100 Fable-confirmed facts; a second-checker
      disagreement now withholds the fact (#94)
- [x] ANTHROPIC_API_KEY set in Vercel (Production), 2026-10-03
- [x] **Security: rotate ANTHROPIC_API_KEY** (done 2026-10-06; the private findings register's entry is closed).
      A new key in the `eu27` workspace, set in the Vercel dashboard as a sensitive Production variable. Deploy run
      37518689761: `/ask: ok (940 characters, 3 citations)`. The Console lists only that key. The spend limit is set
- [ ] **Before 2026-11-05: renew the `/ask` key.** The current key expires that day, and `/ask` stops with it.
      Create a key in the `eu27` workspace, paste it in the Vercel dashboard (`ANTHROPIC_API_KEY`, Production),
      then push or run `gh workflow run Deploy`. The deploy's live `/ask` stage confirms it. Then delete the old key.
      The daily monitor would catch a lapse, but only after `/ask` is down. A calendar reminder is set for
      2026-11-02, 09:00 ET, with these steps
- [x] Live `/ask` answers with citations (`ask_smoke.py --require`: 1122 characters, 3 citations, 2026-10-03);
      repository variable ASK_LIVE=true, so the daily check now fails if it stops
- [x] Owner: port the mobile reader to schema 2, or drop it: rebuilt on the content model (#109, 2026-10-14)
- [ ] **Owner:** the edition channel (#111, #112): create the Supabase project in an EU-27 region, apply
      `mobile/supabase/migrations/` (`cd mobile && supabase link --project-ref <ref> && supabase db push`),
      `gh variable set SUPABASE_URL --body https://<ref>.supabase.co`, and
      `pbpaste | gh secret set SUPABASE_SERVICE_ROLE_KEY --env production`; until then the deploy's `edition` job is
      skipped. Then confirm the app identifiers `cloud.eu27.reader`, and read the app on a device
- [ ] **Owner:** the three repository-settings commands in `docs/plans/ci-cd-hardening.md` (#107): A secret
      scanning and push protection; B the ruleset for `main` from `.github/rulesets/main.json`; C Dependabot
      alerts and security updates. Until B runs, a push to `main` is not held to the fast checks. Checked
      2026-10-14 (`docs/plans/ci-cd-status-2026-10-14.md`): none of the three applied yet
- [ ] **Owner:** the weekly recheck of Monday 2026-10-12 (Monitor run 38269792964) found 27 sources newly disputing
      their facts, 18 of them `finlex.fi` pages served with HTTP 200 and the quote not found. `./run.sh recheck`
      (`./run.sh retry` if the host now needs the rendered route), `./run.sh data`, review, commit
- [x] Push `dotfiles` commit `893d744` (policy §5, the per-project allow rule): on its `origin/main`, checked 2026-10-14
- [ ] **Owner:** the stichting files from `sovereign-appliance` are committed on `plans/stichting-refresh` (`1e1c713`,
      `dff7967`, 2026-10-14; the stash that carried them is kept as `stash@{0}`). Push that branch and
      `ci/status-2026-10-14`, then each to `main`; then `git branch -D sovereign-appliance`, `git worktree prune`,
      `git stash drop`
- [ ] **Owner:** read `TECHNICAL-UNIVERSITIES.md` (#108) and a language draft or two; no person has read either
- [ ] Six Slovak facts cite `zakony.judikaty.info`, an unofficial mirror (T4); find the official text (slov-lex.sk)
- [x] Dependabot in `web/`: `undici` 8.11.2, `brace-expansion` 5.0.12; `npm audit --audit-level=high` clean, now a CI step
- [ ] Dependabot in `mobile/`: `node-forge` (no fix), `braces` (no fix), `decode-uri-component`, `uuid`: allowlisted with
      reasons (#113); owner to dismiss with those reasons
- [x] Testing items (b89f03c, 1e52404): live `/ask` check, mutation testing, `hypothesis`, fact-check
      stability sampling, visual baselines, Firefox/WebKit, iPhone
- [x] Weekly source link check: the `sources` job of `monitor.yml` re-fetches every cited source on Mondays (#98);
      first run 2026-10-12
- [ ] Two of the withheld facts, from the pilot:
  - [ ] `record:DE:civil_registry:operator`: the printed text says "national personal identification
        number … for every natural person"; §139b AO only says the BZSt stores these data on natural
        persons. Bring the printed text back to the quote
  - [ ] `indicator:DE:K2` (eID operated by the state): printed Yes, but no cited page says Bundesdruckerei
        is the designated operator. Find that source (e.g. the Bundesanzeiger designation) or set unknown
- [x] `gate` prints `1309 of 1309` and exits 0; `Verified:` lines of #87 and #89 filled in
- [x] `feat/citizen-review` and `feat/fact-check` merged into `main` (both in `git branch --merged main`)
- [ ] Optional: make the vetting reviewer cross-model too (it is still Opus 5.5 reviewing Opus 5.5)
- [ ] Optional: credit the cross-model check in the evidence grades (`evidence.assess`); a decision of
      its own
- [ ] Fix the vetting manifest's prompt hash, which `manifest()` records at write time and not at run
      time, so the committed run shows a later hash
- [ ] Checker politeness: the pilot fetched pages with a browser User-Agent string; decide whether
      the prompt should forbid that, as `/vet` forbids browser retries

## Evidence (raise confidence)
- [x] Critical-holdings register widened to 39 classes (#73); research run 1 for all 27: 416 admitted
- [x] Ranking indicators (#77); research run 2 with downgrade-only review: 134 of 189 admitted
- [x] Every dependency label independently reviewed (#79): 77 of 93 agreed
- [ ] Hosting pass: where each verified tier 0/1 holding runs (procurement, audit offices, parliament),
      then #79 review. About 86% are unknown today
- [x] Hosting printed per holding, and a generated EU-27 overview in every output (#95, 2026-10-05)
- [ ] `/factcheck` the 60 hosting facts #95 printed; the deploy gate blocks `main` until then
- [ ] `/vet` the 11 hosting values that print as gaps: their quote lacks a year or number they state
      (BG land_property, five DK rows, EL tax and health_records, IT facial_biometric, SE vehicle_licensing)
- [ ] Exposure counts and the ranking read withheld dependency labels: `document.exposure_section` and
      `sovereignty.py:129` count the raw label, so 7 states (AT, CY, EL, FR, HU, IE, SE) count labels their
      report withholds. Count printed facts only, diff the placements, and record the decision
- [ ] Operators as entities (#96, `docs/hosting-operators.md`): schema, staging, review and admission;
      then the backfill from the 71 hosting quotes, computed operator views and the derived dependency
- [x] **Done 2026-10-10** — the decision-reference regex in `tests/test_docs.py` matches 1–3 digits (#103)
- [ ] Decide how classified holdings (defence, intelligence) count in the ranking: exclusion or unknown
- [ ] Rendering fetch for JavaScript pages (FI, PT, LT, CY) and a retry route for refused sites
      (LU, LV, RO, IE)
- [ ] Re-run the thin run-1 states: AT, BE, EE
- [ ] Record counts and data sizes per holding, for capacity (#73)
- [ ] `gov_employment_k`: source it or drop it (withheld today)
- [ ] Human sampling audit with a measured error rate: the launch gate (#25, #67)

## Outputs
- [x] Mobile reader to schema 2 (content model): rebuilt, #109–#113 (2026-10-14)
- [ ] Mobile reader: a signed manifest (ed25519) so the channel proves authorship, not only integrity (#111)
- [ ] Mobile reader: add `Gate / Mobile reader (./test.sh --only mobile)` to `main`'s ruleset after two weeks of timings (#113)
- [ ] Print `eu27.cloud/<iso>` on the country PDFs and posters, which carry no address today (#105): a `label`
      span in the content model, a changelog entry, `/factcheck` before the push
- [ ] Localisation stage 1 (`docs/plans/localisation-plan.md`): apply the 42 `fix` cells, a native reading per
      language, then the decision entry the plan reserves
- [ ] Print book: country parts rendered from the content model; write Parts I, II and V
- [ ] PDF tables: a long compound word (e.g. "Identitätsdokumentenregister") runs into the next column;
      allow hyphenation or breaking in table cells
- [ ] Capacity from measured holdings, once enough are measured (#73)

## Testing
- [x] Web suites in CI: `ci.yml` runs `./test.sh --no-pdf` on pull requests (Vitest, Playwright, API
      type-check); `deploy.yml` runs the full `./test.sh`

## Federation (deferred by decision, Sept 2026)
- [ ] Out-of-country reserve for frontline and micro states (EE data-embassy pattern)
- [ ] Pooled sovereign capacity for small states
- [ ] Mutual DR pairs and treaty basis

## Outreach (waits on the launch gate)
- [x] People inventory, private (`contacts/people.csv`): 956 rows, 850 send-ready (2026-09-24)
- [ ] Second research pass: MT (none), CY, HU, HR, EL, SI (five rows or fewer)
- [ ] Re-research the 77 rows whose seat quote was not found on its page, and the ~30 unreachable
- [ ] Institutional map beyond 25/324: contact *pages* for the email-routed bodies (#68)
