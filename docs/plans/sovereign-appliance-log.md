# The sovereign appliance: what was done and decided

A log of the work behind [`SOVEREIGN-APPLIANCE.md`](../../SOVEREIGN-APPLIANCE.md), newest first, in the shape of
[`national-ai-log.md`](national-ai-log.md). Each entry records who or what produced it, what the owner asked, what was
decided and why, what changed, how it was checked, and what is still open. The decision of record is `DECISIONS.md`
#104; this log is the working narrative behind it, not a second copy.

## 2026-10-12 — the note written, checked and registered

**Produced by.** Claude Fable 5.1 (`claude-fable-5-1`) in Claude Code, session
`https://claude.ai/code/session_01BH4A8Do1xnsJ2M9GbUAFJG`. One Explore subagent read the repository's authored-note
conventions; the writing session fetched the sources itself. Starting commit `f321d78` on `national-ai`, on a new
branch `sovereign-appliance`.

**Asked by the owner.** "are you familiar with netflix's strategy of installing data boxes in data centers?", then
"what i like about these boxes is that they can be fit into existing data centers, which are already everywhere.
they can be custom made for our purposes, i think national public data, at least in the first phase, is just text,
identity, numbers. everything secure, obviously." Asked which facilities: "anything connected to the national
internet infra". Asked what to produce: a new authored note.

### Decisions

1. **A new note, not an extension of `DISTRIBUTION-AND-TRUST.md`.** That note's own caveats are no numbers, no
   member-state names and no test; the box needs sizing figures, a quoted treaty and a checker. Recorded as #104
   with the rejected alternatives.
2. **The #103 contract shape, stricter in two places.** A checker, a committed link register, a gate step and a test,
   as for `NATIONAL-AI-STRATEGIES.md`. Stricter: no currency figure anywhere (the #103 note allows bands in one
   section), and no member state named outside `## Precedents` and `## Sources`, where each paragraph or list item
   naming one must carry a URL with an access date or **[unverified]**. The name match is a prefix with a left word
   boundary, so "Estonian" and "Luxembourgish" count.
3. **Name the precedent.** #64 named no state. The one government instance of owner hardware in another party's
   facility is a bilateral agreement with a published text; describing it without the names would be less
   checkable. The constraint is that the name sits only where the source does.
4. **Quote the agreement from the Luxembourg parliamentary dossier.** Every Estonian page tried (Riigi Teataja, the
   government's agenda page, the Riigikogu press release, RIA, e-Estonia, ERR) answered 403 to both the project's
   user agent and a plain `curl` one. Luxembourg's Chamber of Deputies publishes the consolidated dossier 7185 as a
   PDF with the agreement's English text annexed, and the Conseil d'État publishes its opinion. The Legilux page is
   rendered by script and holds no text for a fetcher. The Riigi Teataja URL is cited as the Estonian publication and
   marked **[unverified]**, with the sentence saying the quotations are from the dossier.
5. **Reuse the #103 checker's generic parts rather than copy them.** `load_links` and `write_links` in
   `model/national_ai_note.py` took `path` and `note` parameters with the old defaults; the ranking and money
   patterns, the URL probe and `states()` are imported. The #103 tests pass unchanged.
6. **Record `colocated_appliance` in the #96 design, build nothing.** One value in the planned `model` enum of
   `docs/hosting-operators.md`, with the note as the argument behind it.
7. **No figure of the note's own.** Every number is quoted from `TIER0-TIER1-SIZING.md` or a cited page. The
   streaming company's URLs stay out of `model/sources/`, as #64 did with its vendor pages.

### How the research ran

- The Open Connect overview PDF was fetched and read with `pdftotext`; the partner and appliances pages were read
  through the fetch tool. The embedded-deployment guide PDF exceeded the fetch tool's size limit and was not used.
- The Luxembourg dossier (2.6 MB PDF) and the Conseil d'État opinion (18 KB PDF) were downloaded with `curl` into
  the session scratchpad and read with `pdftotext`; Articles 1 to 8 of the agreement were quoted from the dossier's
  annex, which reproduces the Mémorial A 1029 text of 6 December 2017.
- RFC 9334 and RFC 9162 were read through the fetch tool for the two definitions quoted.
- No browser session was available (the Chrome extension was not connected), so no page was read interactively.

### What changed (on branch `sovereign-appliance`, not yet committed)

| File | Change |
|---|---|
| `SOVEREIGN-APPLIANCE.md` | new, 4,165 words, 13 sections, 8 URLs |
| `docs/sovereign-appliance-links.csv` | new, written by `./run.sh appliance links` |
| `model/sovereign_appliance_note.py` | new checker, `check` and `links` |
| `tests/test_sovereign_appliance.py` | new, 16 tests |
| `model/national_ai_note.py` | `load_links(path)`, `write_links(note, path)`; defaults unchanged |
| `tests/test_docs.py`, `docs/testing.md` | the note among the citing files; the test module listed |
| `test.sh`, `run.sh` | the gate step "The sovereign-appliance note keeps its contract"; `appliance check\|links` |
| `CLAUDE.md` | the command and the gotcha |
| `docs/hosting-operators.md` | `colocated_appliance` in the planned `model` enum |
| `DECISIONS.md`, `CHANGELOG.md`, `README.md`, `ROADMAP.md` | #104; the entry; the layout line, item 4 and a section; the distribution item's unit |

### Verification

- `./run.sh appliance links`: 8 URLs, 7 answered, 1 did not (403, Riigi Teataja).
- `./run.sh appliance check`: `13 sections, 8 URLs (7 answered at the last link check), 4 unverified marks, 4,165
  words, 0 problems`.
- `./test.sh --only model`: 364 tests, OK; every step green including the new one.
- Three wordings the checker refused during drafting were fixed before the first passing run: "ahead of demand"
  (the ranking pattern matches "ahead of"), "the Estonian gazette" in a caveat, and the **[unverified]** mark sitting
  on the line after its URL in two places.

### Still unverified

- The second-model review of the quotations against their pages (#87's rule applied to prose) has not run. The
  note's status table and #104 say so.
- The Riigi Teataja page: cited, not read.
- Whether the agreement's inviolability clauses could be reproduced for a cage in a commercial facility is a legal
  question the note leaves open (caveat 4).

### Follow-ups for the owner (not done here)

- Commit. When this entry was written another session was editing the same checkout for #105 (the `/de` route),
  with staged renames in the index and its own hunks in `CHANGELOG.md`, `DECISIONS.md`, `CLAUDE.md` and
  `README.md` next to this work's. A plain commit would take both; the gate must run on whatever is committed, so
  the two are separated by hand (or #105 is committed first and this work on top of it).

- Run the second-model review (`/factcheck`'s rule, by hand for prose) over the eight quotations.
- Decide whether the box becomes the unit when distribution is modelled (`ROADMAP.md`, item 6 of that block).
- Push and merge are the owner's call: `main` is a production deploy (#81).
