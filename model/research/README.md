# Research staging

Agent research lands here before anything is admitted. **Nothing in this directory is rendered or
counted.** A claim reaches the source register only through `model/research.py`, which fetches the
cited document, records its SHA-256, finds the quote in the extracted text and looks up an archived
copy (DECISIONS.md #73, #75).

| Path | What | Produced by |
|---|---|---|
| `<ISO>.json` | Critical holdings: 39 classes per state, claims with verbatim quotes | Research run 1, 2026-09-29 |
| `indicators/<ISO>.json` | The seven data-sovereignty indicators (#77), with the reviewer's verdict per value | Research run 2, 2026-09-29 |
| `dependency_review/<ISO>.json` | An independent reviewer's verdict on every foreign-dependency classification from run 1 (#79) | Review run, 2026-09-29 |
| `recheck.csv` | One row per source behind a printed fact: re-fetched, hash before/now, whether every quote is still there (`claims_missing`) | `research.py recheck` (#83) |
| `vetting/<ISO>.json` | Vetting run: findings (upgrade, corroborate, supersede, contradict, fill gap), each with its blind review; the reviewer's model and the workflow's sha256 | `model/research/vetting/workflow.js` via `vetting.py stage` |
| `vetting/verification.csv`, `outcomes.csv`, `disputes.csv` | The mechanical check of each finding; what admission did with it; disagreements no rule settles | `vetting.py verify`, `admit` |
| `verification.csv` | One row per (state, class or indicator, field, URL): HTTP status, content type, sha256, match result, archived copy | `research.py verify` |

## How the runs were made

**Run 1: holdings.** One agent per member state, 27 in parallel.
- Each agent was given `model/holding_classes.csv` and asked to find, per class: the official name,
  operator, legal basis, hosting and foreign dependency, record count and data size.
- Each claim needed a verbatim quote of 8–60 words from the exact URL.
- "Not held" needs an authoritative statement; silence means "unknown".

**Run 2: indicators.** Two stages per state, pipelined.
1. **Research.** The agent gets the yes/partial/no definitions from `model/indicators.csv`, a source
   priority (legislation portals, the competent authority, audit offices, procurement, the eIDAS trusted
   list and notified eID schemes), and a self-check: fetch every cited URL and confirm the quote before
   returning.
2. **Review.** A separate skeptic re-reads each cited page and judges whether the quote *establishes*
   the value under the definition.
   - It may keep a value, downgrade yes → partial, or downgrade anything → unknown. It may never upgrade.
   - **Staging rule:** the reviewed value is used when it is the same or a downgrade. Any other
     disagreement, or a value with no review, becomes "unknown".
   - Both values and the reviewer's reason are kept under `review` in each indicator.

Outcome of run 2's review: 19 of 189 values changed. After review, 119 are yes, 27 partial, 2 no and
41 unknown, all still subject to mechanical verification.

## Known limits

- **Machine-checked, not human-checked.** The quote check proves the words are in the fetched document.
  The review stage (run 2 only) judges whether they support the value. Neither is a human expert
  reading the statute.
- **Unchecked translations.** Values and English glosses are agent translations; the quote in the
  original language is the evidence.
- **Pages that defeat the check.** Pages that render their text with JavaScript, sit behind a login or
  refuse automated requests fail verification even when the quote is genuine. They are recorded as
  failures and stay out.

## Results, 2026-09-29

- **Holdings (run 1).** 2,228 claims; 1,724 passed the quote check (77%). 416 (state, class) holdings
  admitted.
  - Failures cluster in two places: pages whose text is rendered by JavaScript (FI, PT, LT, CY) and sites
    that refused automated requests (LU, LV, RO, IE).
- **Dependency review (#79).** 93 classifications reviewed, 77 agreed, 16 disputed. Admitted: 43
  national, 4 EU provider, 2 non-EU provider.
- **Indicators (run 2).** 288 claims; 240 passed. 134 of 189 indicator values admitted.
