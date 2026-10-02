# TODO (EU-27)

Cross-country work, as a checklist. Why and in what order: [`ROADMAP.md`](ROADMAP.md). How the evidence is
produced: [`METHOD.md`](METHOD.md).

## Publish
- [ ] Production deploy of the current build (author's OK), then push. Blocked by the fact-check gate (#87)
      until all 1,390 printed facts pass; see below
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
- [ ] **Commit** the #88 methodology and style work and the pilot results (uncommitted on `feat/fact-check`)
- [ ] **Decide the full run** for the remaining 1,360 facts (57 batches, about 45–60 min):
      Fable 5.1, about $185–280 (the rule as chosen), or Opus 5.5, about $75–110 (reverses that choice)
- [ ] Run it with `/factcheck`; stage, record, `./run.sh data`, `./run.sh artefacts`, `./test.sh`, gate
- [ ] Resolve every disagreement (owner decides; never edit a verdict). From the pilot:
  - [ ] `record:DE:civil_registry:operator`: the printed text says "national personal identification
        number … for every natural person"; §139b AO only says the BZSt stores these data on natural
        persons. Bring the printed text back to the quote
  - [ ] `indicator:DE:K2` (eID operated by the state): printed Yes, but no cited page says Bundesdruckerei
        is the designated operator. Find that source (e.g. the Bundesanzeiger designation) or set unknown
- [ ] `gate` prints `1390 of 1390` and exits 0; fill in the `Verified:` line of #87
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
