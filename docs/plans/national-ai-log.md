# National AI strategies: what was done and decided

A log of the work behind [`NATIONAL-AI-STRATEGIES.md`](../../NATIONAL-AI-STRATEGIES.md), newest first, in the
shape of [`stichting-log.md`](stichting-log.md). Each entry records who or what produced it, what the owner asked,
what was decided and why, what changed, how it was checked, and what is still open. The decision of record is
`DECISIONS.md` #101; this log is the working narrative behind it, not a second copy.

## 2026-10-10 — the note, its checker and the link register

**Produced by.** Claude Fable 5.1 (`claude-fable-5-1`) in Claude Code, session
`https://claude.ai/code/session_01FcnUV5xYY1w5oSz7Vnzqf2`. Seven research subagents (general-purpose, with web
search) collected the snapshots; the strategies, the cross-cutting sections, the checker and the tests were written
by the main session. Starting commit: `1d622fc` on `main`. Result: commit `8d25cc7` on branch `national-ai`, not
pushed.

**Asked by the owner.** First, in plan mode, "explore ways for european nations to develop national AI", clarified
as "i want the eu data sovereignty project to have a new section for 'national ai'", scope EU-27. Then the
redirect that fixed the deliverable: "explore for every eu27 country a strategy that would give them foundational
AI model. doesnt have to be top quality, just good enough for their citizens. document in one large markdown."
After the plan was approved: "also ensure a strong test.sh" and "document all decisions and anything relevant in a
README markdown file."

### Decisions

1. **One authored markdown, not a rendered section.** The owner asked for one large document and an exploration
   first. `NATIONAL-AI-STRATEGIES.md` sits at the root beside `FEASIBILITY-RANKING.md` and is held to the
   `countries/NL/FRONTIER-MODEL.md` standard (#44): authored, never generated, never read by the model, the book,
   the web app or `/ask`.
   - *Alternatives:* render it through the content model (every value would then need a quote-checked citation and
     an independent review before anything prints, which is the follow-on, not the exploration); extend
     `FEASIBILITY-RANKING.md` (superseded by #77 because it ranked and was unsourced); one file per state under
     `countries/<ISO>/` (the cross-state sections need one place, and the owner asked for one file).
   - *Verified:* `tests/test_national_ai.py` fails if `model/`, `book/`, `api/`, `web/src/` or `mobile/` names the
     note. Recorded as `DECISIONS.md` #101.
2. **"Good enough for citizens" is six testable properties, none of them frontier parity.** B1 every official
   and recognised language; B2 deployable by public services under national and EU law; B3 continuity that does
   not depend on one foreign vendor (open weights, escrow or co-ownership); B4 data provenance the state can
   defend; B5 an annual cost the state can carry indefinitely; B6 evaluation owned nationally. Every strategy
   argues against this bar, so the entries are comparable without being ranked.
3. **Four routes, generalised from FRONTIER-MODEL §4 without the Dutch figures.** R1 adapt an open-weight base on
   a national corpus; R2 pool with the language community or an EU vehicle; R3 build a national mid-scale
   programme; R4 procure frontier access with terms. A route's cost and time band is given once, in section 2,
   labelled **[reconstructed]**; no state's entry carries a cost figure, and nothing is scaled from the
   Netherlands (#72, #73).
   - *Verified:* the checker's MONEY regex refuses a currency figure in any entry's strategy subsections, and
     `**[reconstructed]**` is allowed in section 2 only.
4. **The note ranks nothing.** States are grouped by recommended route in section 6, alphabetical within a
   group, with the line that the groups are a recommendation and not a ranking (#10, #77).
   - *Verified:* the checker's RANK regex refuses ordering language outside four allowed sentences; the
     route-group test refuses a non-alphabetical group or a state listed twice or not at all.
5. **Every factual claim carries a URL and an access date, or the mark `**[unverified]**`.** The
   `docs/plans/stichting.md` convention. Nothing is printed from memory. Press is cited as "(press)" and only as
   a pointer.
   - *Verified:* the checker refuses a snapshot cell with neither; the count of marks is printed by
     `./run.sh national-ai check`.
6. **The link register is committed, and a dead link must sit on a marked line.** `./run.sh national-ai links`
   fetches every cited URL once into `docs/national-ai-strategies-links.csv` (url, status, error, checked);
   a URL that did not answer 2xx or 3xx must be on a line carrying `**[unverified]**`, or the gate fails.
   Per the project rule: commit the evidence rather than relying on it.
   - *Alternatives:* a scratchpad link check with no trace (nothing for a third party to audit); marking
     unanswered URLs automatically (the author should see each one).
7. **The strategies are the author's analysis and say so.** The header and section 7 state that the
   recommendations are judgement, current to the access dates, and that no machine check covers them.
8. **A mechanical contract, not a review, is what `./test.sh` can enforce on prose.** The gate checks what it can
   refuse (decisions 1, 3, 4, 5 and 6 above, plus the header wording, exactly one `### Name (ISO)` entry per state
   alphabetical by English name from `model/eu27_parameters.csv`, the six fixed subsections, the eleven snapshot
   rows, at least three sources per entry, and the link register being current). The second-model review of the
   claims against their pages is a separate, costed step left to the owner.
9. **Decision references of one to three digits.** `tests/test_docs.py` `REFERENCE` was `#(\d{1,2})` and would
   have skipped #101; widened to `#(\d{1,3})` with the hex-colour guard kept. Closes the `TODO.md` item.
10. **Bookkeeping in the same commit.** `DECISIONS.md` #101 with all seven parts; `CHANGELOG.md` entry; a README
    section and Changelog-table row; `CLAUDE.md` command and gotcha; `ROADMAP.md` § Planned for the sourced
    follow-on; `FEASIBILITY-RANKING.md` status rows pointing at the note; `docs/testing.md` listing the new
    test module.

### How the research ran

| Step | What happened |
|---|---|
| EU-level brief | One agent: EuroHPC AI Factories and antennas, the supercomputers, the AI Gigafactory call, OpenEuroLLM, EUROPA, ALT-EDIC, access modes, the Cloud and AI Development Act, Apply AI and the Data Union strategy. Official EuroHPC JU and Commission pages first. |
| Country snapshots | Six agents in parallel, one per cluster: Nordic and Baltic; DACH and Benelux; France, Iberia and Italy; Visegrád with Slovenia and Croatia; Bulgaria, Romania and the south-east; Greece, Cyprus and Ireland (Malta with the south-west). Each filled the eleven-row snapshot per state with a URL and access date per claim, and wrote no strategy. |
| What went wrong | The agents' shared web-search quota ran out mid-run. Later cells were filled from directly fetched pages or marked unverified. This is why the note carries 223 marks: the gaps are visible, not silent. |
| Writing | The bar, the routes, the building blocks, the 27 strategies and the cross-cutting sections were written in the main session from the agents' snapshots, FRONTIER-MODEL §3–5 for the reasoning pattern, and `model/eu27_parameters.csv` where a fundamental is cited as "this repository's fundamentals". Assembled from per-state fragments by a scratchpad script. |
| Link check | Every cited URL fetched once with a browser user agent, retried as curl on 403, with a curl subprocess fallback where the system Python's TLS stack failed (three hosts). EUR-Lex answers 202 and 308, so 2xx and 3xx count as answered. |

### What changed (commit `8d25cc7`, 15 files)

| File | Change |
|---|---|
| `NATIONAL-AI-STRATEGIES.md` | New. Header, contents, §1 the bar, §2 the routes with the reconstructed band table, §3 building blocks, §4 EU vehicles as of October 2026, §5 one entry per state in the fixed template, §6 cross-cutting (five findings, language clusters, route groups, four first moves), §7 caveats, §8 status. 2,334 lines. |
| `model/national_ai_note.py` | New. The contract checker and link fetcher behind `./run.sh national-ai check\|links`. |
| `tests/test_national_ai.py` | New. The contract on the real note, and unit tests of each refusal on a synthetic note. |
| `docs/national-ai-strategies-links.csv` | New. The link register. |
| `test.sh`, `run.sh` | A step "The national-AI note keeps its contract" in the model group; the `national-ai` command. |
| `tests/test_docs.py` | Three-digit decision references; the note listed among the citing files. |
| `DECISIONS.md` | #101. |
| `CHANGELOG.md`, `README.md` | The 2026-10-10 entry; the section "National AI strategies" with its decisions table, how it was made, what the gate checks and what it is not; the Layout line and Changelog-table row. |
| `CLAUDE.md`, `ROADMAP.md`, `FEASIBILITY-RANKING.md`, `TODO.md`, `docs/testing.md` | Command and gotcha; the planned follow-on; status rows; the ticked regex item; the test module listed. |

Not changed: the bundle, the web app, the PDFs, `/ask`, the posters. The note is not rendered, so nothing a
reader of `eu27.cloud` sees is different. The owner's uncommitted README deployment edits and the three stichting
plan files were left unstaged and untouched.

### The route groups, as written in §6

Alphabetical within a group; a recommendation, not a ranking.

| Group | States |
|---|---|
| R1, institutionalise a model line that exists | Bulgaria, Denmark, Estonia, France, Germany, Greece, Hungary, Italy, Netherlands, Poland, Portugal, Romania, Slovenia, Sweden |
| R1, start on an open base | Czechia, Ireland, Latvia, Lithuania, Malta |
| R2, pool with the language community or a factory | Austria, Belgium, Croatia, Cyprus, Luxembourg, Slovakia |
| R3, mid-scale pretraining achieved; keep it funded | Finland, Spain |

Every group pairs its route with R4, frontier access procured with terms.

### Verification

Run on 2026-10-10 against commit `8d25cc7`:

```
./test.sh --only model
  All checks in the model group passed (346 tests)
./run.sh national-ai check
  NATIONAL-AI-STRATEGIES.md: 27 states, 393 URLs (387 answered at the last link check),
  223 unverified marks, 36,795 words, 0 problems
```

| Count | Value |
|---|---|
| Cited URLs | 393 |
| Answered (2xx or 3xx) | 387 |
| Did not answer, all on marked lines | 6 (four `gov.ie` pages refusing automated requests, two pages gone) |
| `**[unverified]**` marks | 223 |
| Words | 36,795 |

The commit passed the security gate. No email-shaped string is in the note or the register.

### Problems met on the way

- The checker found what the author missed: currency figures inside the French, Italian and Portuguese strategies,
  "top five" in the German snapshot, "ahead of most" in the Bulgarian entry. All reworded.
- The RANK regex first matched the word "behind" in ordinary prose; removed from the pattern.
- The first link check counted EUR-Lex's 202 and 308 responses as failures, choked on one non-ASCII URL, and
  failed TLS on three hosts under the system Python 3.9 that `python3` resolved to in the session shell. Fixed in
  the fetcher rather than by hand-editing the register.
- `tests/test_repeatability.py` requires every test module to be listed in `docs/testing.md`; added.
- The README held the owner's unstaged deployment edits, so only the three new hunks were staged, by patch.

### Still unverified

- The 223 marked cells. Most are speaker counts, minority-language recognition, funding amounts and strategy
  texts that the agents could not fetch after the search quota ran out. They are facts a later pass can fill; none
  is load-bearing for a route recommendation, which the entry's "main blocker" line says where it matters.
- The strategies themselves. They are judgement, and no second model has read them against the cited pages.

### Follow-ups for the owner (not done here)

Each needs the owner's OK; none was done in this session.
1. **Push `national-ai`.** A push to `main` is a production deploy (#81). The note is not rendered, so the deploy
   would change nothing a reader sees, but the gate runs in full in Actions.
2. **The second-model review.** One Opus agent per cluster re-reads each entry's claims against its cited URLs and
   writes `docs/plans/national-ai-strategies-factcheck-<date>.md` in the stichting pattern; claims it does not
   confirm get the mark. Roughly seven agent runs.
3. **The sourced follow-on.** Five reviewed yes/partial/no indicators with `dimension=ai`, kept out of the ranking,
   a per-state section, a copied-span overview and a `/national-ai` page, as planned in `ROADMAP.md` § Planned.
   The note's snapshot tables become that run's seed.
4. **A later pass on the unverified cells**, once the search budget allows, with `./run.sh national-ai links`
   rerun afterwards so the register matches.
