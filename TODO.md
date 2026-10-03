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
- [ ] 10 Dependabot alerts on `main` (2 high, 5 moderate, 3 low), reported by GitHub on the push
- [ ] Fix the `security` workflow, which fails on every push because its reusable workflow is only in the
      unpushed local dotfiles (pushing dotfiles needs the owner's OK)
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
- [ ] Resolve the 81 withheld facts (owner decides; never edit a verdict). All are listed in
      `docs/fact-check-audit.md` § Withheld. By kind: 31 register or operator names worded beyond their quote,
      15 hosting labels, 13 indicators, about 12 pages the checker could not fetch. Most affected: IE 10,
      EE 10, HU 9, PT 7, SK 6
- [x] Rounding defect fixed (population printed at its stored 3 decimals; test keeps every Eurostat figure at
      its stored precision); 27 populations re-checked and confirmed
- [x] Retry route for facts whose pages refused the checker: `prepare --withheld-blocked`, from the hashed
      copy; 11 of 12 confirmed. 69 facts remain withheld
- [x] Correction round (#93): 69 withheld facts re-researched, 25 corrected or re-sourced and confirmed
- [ ] 46 facts still withheld: no T1/T2 quote found, reviewer disagreed, or the check rejected the correction
- [ ] Stability sample: Opus 5.5 disagreed with 5 of 50 Fable-confirmed facts (audit file § Stability); decide
      whether a second-checker disagreement should withhold a fact
- [ ] Owner: ANTHROPIC_API_KEY in Vercel (dedicated workspace, spend limit), then repository variable ASK_LIVE=true
- [ ] Owner: port the mobile reader to schema 2, or drop it (its 4 Dependabot alerts need one or the other)
- [ ] Six Slovak facts cite `zakony.judikaty.info`, an unofficial mirror (T4); find the official text (slov-lex.sk)
- [x] Dependabot in `web/`: `undici` 8.11.2, `brace-expansion` 5.0.12; `npm audit --audit-level=high` clean, now a CI step
- [ ] Dependabot in `mobile/` (stale reader): `node-forge` (no fix), `braces`; port the reader to schema 2 or drop it
- [ ] Testing items that wait for the owner's OK (docs/testing.md § Not yet in place): live `/ask` check,
      mutation testing / `hypothesis`, fact-check stability sampling, visual baselines, Firefox/WebKit,
      weekly source link check, pushing dotfiles to fix the red `security` workflow
- [ ] Two of the withheld facts, from the pilot:
  - [ ] `record:DE:civil_registry:operator`: the printed text says "national personal identification
        number … for every natural person"; §139b AO only says the BZSt stores these data on natural
        persons. Bring the printed text back to the quote
  - [ ] `indicator:DE:K2` (eID operated by the state): printed Yes, but no cited page says Bundesdruckerei
        is the designated operator. Find that source (e.g. the Bundesanzeiger designation) or set unknown
- [x] `gate` prints `1309 of 1309` and exits 0; `Verified:` lines of #87 and #89 filled in
- [ ] Merge `feat/citizen-review` and `feat/fact-check` into `main` (owner's OK; a push to `main` deploys)
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
- [ ] Decide how classified holdings (defence, intelligence) count in the ranking: exclusion or unknown
- [ ] Rendering fetch for JavaScript pages (FI, PT, LT, CY) and a retry route for refused sites
      (LU, LV, RO, IE)
- [ ] Re-run the thin run-1 states: AT, BE, EE
- [ ] Record counts and data sizes per holding, for capacity (#73)
- [ ] `gov_employment_k`: source it or drop it (withheld today)
- [ ] Human sampling audit with a measured error rate: the launch gate (#25, #67)

## Outputs
- [ ] Mobile reader to schema 2 (content model), with the two Dependabot alerts fixed on the way
- [ ] Print book: country parts rendered from the content model; write Parts I, II and V
- [ ] Capacity from measured holdings, once enough are measured (#73)

## Testing
- [ ] Put the web suites in CI. `ci.yml` runs the Python suite and gitleaks only; Vitest, Playwright
      and the API type-check run in `./test.sh` locally.

## Federation (deferred by decision, Sept 2026)
- [ ] Out-of-country reserve for frontline and micro states (EE data-embassy pattern)
- [ ] Pooled sovereign capacity for small states
- [ ] Mutual DR pairs and treaty basis

## Outreach (waits on the launch gate)
- [x] People inventory, private (`contacts/people.csv`): 956 rows, 850 send-ready (2026-09-24)
- [ ] Second research pass: MT (none), CY, HU, HR, EL, SI (five rows or fewer)
- [ ] Re-research the 77 rows whose seat quote was not found on its page, and the ~30 unreachable
- [ ] Institutional map beyond 25/324: contact *pages* for the email-routed bodies (#68)
