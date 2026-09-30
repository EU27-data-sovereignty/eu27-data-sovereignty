# TODO (EU-27)

Cross-country work, as a checklist. Why and in what order: [`ROADMAP.md`](ROADMAP.md). How the evidence is
produced: [`METHOD.md`](METHOD.md).

## Publish
- [ ] Production deploy of the current build (author's OK), then push
- [ ] `/ask`: dedicated Anthropic workspace with a spend limit and `ANTHROPIC_API_KEY` in Vercel
      (author), then the 12-question eval (with approval), then the Vercel Firewall rate limit

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
