# National AI strategies: what was done and decided

A log of the work behind [`NATIONAL-AI-STRATEGIES.md`](../../NATIONAL-AI-STRATEGIES.md), newest first, in the
shape of [`stichting-log.md`](stichting-log.md). Each entry records who or what produced it, what the owner asked,
what was decided and why, what changed, how it was checked, and what is still open. The decision of record is
`DECISIONS.md` #103; this log is the working narrative behind it, not a second copy. The note was recorded as
#101 until commit `3c41351` of 2026-10-12 renumbered it to #103, so the three commits of 2026-10-10 cite #101 in
their messages; the 2026-10-13 entry says why.

## 2026-10-13 — renumbered to #103, merged into `main`, deployed; the record brought up to date

**Produced by.** Claude Fable 5.1 (`claude-fable-5-1`) in Claude Code, the session that wrote the two entries below,
`https://claude.ai/code/session_01FcnUV5xYY1w5oSz7Vnzqf2`, after a context reset. The owner asked: "ensure everything is
documented in markdown files". Nothing in the note, the checker, the tests or the link register changed in this entry;
only this log.

### What happened between the entries

All of it by concurrent sessions on this machine; their own narratives are [`country-paths-log.md`](country-paths-log.md)
§2, [`sovereign-appliance-log.md`](sovereign-appliance-log.md) and the session index
[`2026-10-12-session-log.md`](2026-10-12-session-log.md).

- **Renumbered** in `3c41351` on 2026-10-12: `main` had meanwhile taken #101 and #102 for the landing design and the
  guide pages, so this note's decision is #103 (the appliance note #104, the country paths #105). For this note the
  commit moved the two citations in `NATIONAL-AI-STRATEGIES.md`, the `DECISION` constant in `model/national_ai_note.py`,
  `tests/test_national_ai.py`, `tests/test_docs.py`, the header of the fact-check report, this log, and the entries in
  `CHANGELOG.md`, `README.md`, `ROADMAP.md`, `TODO.md` and `FEASIBILITY-RANKING.md`. The three commits of 2026-10-10
  (`8d25cc7`, `5537135`, `f321d78`) keep #101 in their messages; history is not rewritten.
- **Merged into `main`.** `b7f5931` merged `origin/main` into the branch that carried this note and the appliance note;
  `7f265ac` was pushed to `main` on 2026-10-12 under the permission rule of #106: Actions run 38334656899, conclusion
  success, every gate job green, deployed. The note has been on `main` since. It is still never rendered, so nothing
  on the site changed because of it.
- **The checker now runs through the notes register.** `79fdf01` added `model/notes.py`, one `test.sh` stage that runs
  every authored note's checker; `python3 model/notes.py check` lists this note as one of four (#103, #104, #108 and
  the language drafts).
- `origin/national-ai` (`f321d78`) is an ancestor of `main` and can be deleted by the owner; the assistant may not
  delete branches.

### What this session did on resuming

- Found the owner's checkout on `sovereign-appliance`, 28 commits behind `main`, with other sessions' uncommitted
  files (`CHANGELOG.md`, `OUTREACH.md`, `README.md`, the three stichting files); left all of it untouched, as before.
- Checked every markdown file on `origin/main` that names the note for a citation left at #101: none. The `#101`
  that remain in `README.md`, `CHANGELOG.md` and `DECISIONS.md` are the landing design's.
- Found that this log carried the new number but did not say it had been renumbered, merged or deployed; those facts
  were only in the other sessions' logs, and the "Still open" list of the entry below still called the merge an open
  item. Wrote this entry, added the sentence in the header, and marked that item done in place.

### Decisions

1. **This log is amended, not rewritten.** The header gains one sentence on the numbering; the merge item in the
   2026-10-10 "Still open" list gains a pointer to this entry; the entries themselves stay as written. A reader of the
   2026-10-10 commits sees #101 and finds here why the record says #103.
2. **The entry is written on a branch from `origin/main`, in a worktree, not in the checkout.** The checkout holds
   other sessions' uncommitted work on a branch behind `main`. The branch is `national-ai-log`, pushed to origin;
   `main` is the owner's to fast-forward (`git push origin national-ai-log:main`), since #106 wants the owner's OK in
   the conversation before each push there.
3. **No changelog entry.** A log entry changes no behaviour and no printed fact; `CHANGELOG.md` already records the
   note under 2026-10-10, and the renumbering is in the concurrent session's record.

### Verification

In the worktree at `origin/main` (`fcf0b65`) plus this entry, 2026-10-13:

```
./run.sh national-ai check   → 27 states, 467 URLs (462 answered at the last link check), 175 unverified marks, 38,429 words, 0 problems
python3 model/notes.py check → ok  the national-AI note (#103)  (and the three other notes ok)
python3 -m unittest tests.test_national_ai tests.test_docs → Ran 19 tests, OK
gh run view 38334656899      → conclusion success, head 7f265ac, event push
git merge-base --is-ancestor f321d78 origin/main → true
```

### Still open

- Unchanged: 130 cells the reviewers could not source, kept marked; four `gov.ie` pages refuse automated fetches; the
  sourced follow-on in `ROADMAP.md` § "Then — national AI as reviewed indicators", not started.
- Owner: fast-forward `main` to `national-ai-log`; delete `origin/national-ai` once satisfied.

### Where everything is recorded

| What | Where |
|---|---|
| The note | `NATIONAL-AI-STRATEGIES.md` (§8 is its status table) |
| The decision of record, with alternatives and *Verified:* | `DECISIONS.md` #103 |
| The reader-facing change entry | `CHANGELOG.md`, 2026-10-10, "Added … (#103)" |
| The contract and how it is checked | `model/national_ai_note.py`, `tests/test_national_ai.py`, `./run.sh national-ai check` and `links`, the `test.sh` stage through `model/notes.py` |
| The link register | `docs/national-ai-strategies-links.csv` |
| The second-model review, verbatim | `docs/plans/national-ai-strategies-factcheck-2026-10-10.md` |
| Where the note is pointed to | `README.md` (layout and its section), `ROADMAP.md` (the Done bullet and the follow-on), `TODO.md`, `FEASIBILITY-RANKING.md`, `CLAUDE.md`, `docs/testing.md` |
| The renumbering, the merge and the push to `main` | `3c41351`, `b7f5931`, `7f265ac`; narrative in `country-paths-log.md` §2 and `2026-10-12-session-log.md` |
| The working narrative and the open items | this file |

## 2026-10-10, later — the second-model review, applied

**Produced by.** The same Claude Fable 5.1 session. Six Claude Opus 5.5 (`claude-opus-5-5`) subagents did the
checking, one per cluster of entries and one for sections 2, 4 and 6; the writing session applied their verdicts.
Starting commit `5537135`; the branch had been pushed to `origin/national-ai` just before.

**Asked by the owner.** "push", then "actually just do it all", then "ensure proper security and privacy checks".

### Decisions

1. **Push the branch, not `main`.** The branch went to `origin/national-ai` over SSH after the gate in strict CI
   mode, gitleaks and a scan of every added line for email addresses, phone numbers, IP addresses, credentials and
   local paths all came back clean. The remote was switched from HTTPS to SSH because no HTTPS credential was
   stored and every sibling repo uses SSH. `main` is untouched: a push there is a production deploy (#81).
2. **Run the second-model review now, with Opus 5.5.** The rule of #87 (a fact is checked by the model that did
   not write it) applied to an authored note: Fable 5.1 wrote it, so Opus 5.5 checked it. Six agents in parallel,
   each told to fetch, to quote at most 25 words, never to supply a fact from memory, and to edit nothing.
3. **Apply every verdict in the note, and commit the reports verbatim.** A NOT CONFIRMED claim was corrected
   where the reviewer found the fact on an official page, reworded to what the page says where it was overstated,
   or removed and marked where it had no source. A FOUND cell was filled with the fact, the URL and the access
   date. Each edit was asserted to match exactly one place in the note. The reports are
   [`national-ai-strategies-factcheck-2026-10-10.md`](national-ai-strategies-factcheck-2026-10-10.md).
4. **Absence stays absence.** Where a reviewer could only show that no contract, bid or page exists, the cell
   says so and keeps its mark.

### What the review found

| Part | Claims | Confirmed | Not confirmed | Unclear | Unverified cells | Found |
|---|---|---|---|---|---|---|
| All six parts | 1,086 | 987 | 50 | 49 | 222 | 92 |

Of the 50 not confirmed, 19 were true on an uncited official page and 31 were wrong, overstated or unsourced. The
ones that changed a recommendation's premise: MeluXina-AI has 1,008 GPUs, not over 2,100; Gefion is funded by a
foundation and the state's investment fund, not privately; Silo AI has been part of AMD since August 2024 and
Poro 2 is under a Llama licence; the Dutch cabinet wrote in March 2026 that the budget has no room for the
Gigafactory commitment; the Lithuanian factory's EU share is EUR 65 million; the Romanian models were trained on a
slice of the corpus, not all of it; the AI Continent Action Plan's EUR 10 billion is a total, not a commitment to
factories; OpenEuroLLM's Leonardo hours were for a dataset project. No route group changed.

### Verification

```
./run.sh national-ai links  → 467 URLs, 462 answered, 5 did not
./run.sh national-ai check  → 27 states, 467 URLs (462 answered), 175 unverified marks, 38,429 words, 0 problems
```

| Count | Before the review | After |
|---|---|---|
| Cited URLs | 393 | 467 |
| Did not answer | 6 | 5 (four `gov.ie` pages, one page gone) |
| Unverified marks | 223 | 175 |
| Words | 36,795 | 38,429 |

### Still open

- 130 cells the reviewers could not source, kept marked.
- The sourced follow-on (reviewed indicators and a `/national-ai` page) is designed in `ROADMAP.md` and not
  started: it adds about 135 printed facts that each need a fetched quote, an independent review and the
  cross-model check before a deploy.
- Merging `national-ai` into `main` is a production deploy and is the owner's call. *Done by a concurrent session:
  merged in `b7f5931`, pushed to `main` as `7f265ac` on 2026-10-12, Actions run 38334656899 green; see the
  2026-10-13 entry.*

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
     note. Recorded as `DECISIONS.md` #103.
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
   have skipped #103; widened to `#(\d{1,3})` with the hex-colour guard kept. Closes the `TODO.md` item.
10. **Bookkeeping in the same commit.** `DECISIONS.md` #103 with all seven parts; `CHANGELOG.md` entry; a README
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
| `DECISIONS.md` | #103. |
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
