# The sovereign appliance: what was done and decided

A log of the work behind [`SOVEREIGN-APPLIANCE.md`](../../SOVEREIGN-APPLIANCE.md), newest first, in the shape of
[`national-ai-log.md`](national-ai-log.md). Each entry records who or what produced it, what the owner asked, what was
decided and why, what changed, how it was checked, and what is still open. The decision of record is `DECISIONS.md`
#102; this log is the working narrative behind it, not a second copy.

## 2026-10-13 — committed, and the record brought up to date

**Produced by.** Claude Fable 5.1 (`claude-fable-5-1`) in Claude Code, the same session as the entry below,
`https://claude.ai/code/session_01BH4A8Do1xnsJ2M9GbUAFJG`, after a context reset. The owner asked: "document all
decisions and changes in markdown". Nothing in the note, the checker or the tests changed in this entry; only this log.

### What happened between the entries

- **The work was committed by the concurrent session, not this one.** The session editing the checkout for #103
  committed this work first, as `f73c24a` on 2026-10-12 at 17:38 (local), from the staged tree alone, and #103 on top
  of it one minute later as `0a64633`. Its session URL is the `Claude-Session` trailer on both commits
  (`session_01JzrUgU5ZozYWCPBXUD2b5w`); the entry below names the session that wrote the note. Both URLs are therefore
  part of the trail: one produced the content, the other the commits.
- **The separation went the other way round from the follow-up's suggestion**, #102 first and #103 after, which is
  the cleaner order: the #102 commit holds exactly the sixteen files in the table below and nothing of #103's, and
  the gate ran on each commit. `f73c24a` records its own verification in the message: `python3 -m unittest discover
  -s tests`: 362 tests, OK, and the checker's `13 sections, 8 URLs, 0 problems`. The entry below records 364 from
  `./test.sh --only model`; the difference between the two counting commands was not traced. Neither number includes
  #103's tests, which came later.
- **Committer identity** is the GitHub noreply address on both commits, as the workspace rule requires.
- **The branch `sovereign-appliance` has no upstream.** Nothing has been pushed; `main` is a production deploy (#81).

### Decisions

8. **#102 is committed before #103, each from its own staged set, with the gate on both.** The alternatives were a
   single commit of both sessions' work (rejected: two unrelated changes under one message and one decision trail)
   and separating the hunks by writing trees around the hook (forbidden by the workspace rule that every commit
   passes the gate). The order was the concurrent session's call; it is recorded here because it is the order the
   history now shows.
9. **This log stays the narrative of record and is corrected rather than rewritten.** The heading "not yet
   committed" in the entry below is amended in place with a pointer to this entry, and the commit follow-up is marked
   resolved, so a reader of the earlier entry is not misled and the earlier wording is still visible in history.
   `DECISIONS.md` #102 and the `CHANGELOG.md` entry are unchanged: both already describe what was committed, and
   neither records commit hashes by convention.

### State of the tree at this entry

- Modified and untracked: the stichting files (`CHANGELOG.md`, `OUTREACH.md`, `README.md`, `docs/plans/stichting.md`,
  `docs/plans/stichting-factcheck-2026-10-08.md`, `docs/plans/stichting-log.md`), untouched by either session and
  never staged by this one.
- Untracked `.claude/settings.json`: a Claude Code permissions file allowing `git push origin main` and two variants
  and denying force pushes, branch deletes and direct production deploys. It was not written by this session and is
  not committed here; whether it is checked in is the owner's call, since it widens what an assistant may do without
  asking.

### Verification

On `0a64633`, 2026-10-13:

- `./run.sh appliance check`: `13 sections, 8 URLs (7 answered at the last link check), 4 unverified marks, 4,165
  words, 0 problems`.
- `python3 -m unittest tests.test_sovereign_appliance tests.test_national_ai tests.test_docs`: 35 tests, OK.

### Still unverified

Unchanged from the entry below: the second-model review of the eight quotations; the Riigi Teataja page, cited and
not read; whether the agreement's inviolability clauses can be reproduced for a cage in a commercial facility.

### Where everything is recorded

| What | Where |
|---|---|
| The note | `SOVEREIGN-APPLIANCE.md` (its status table carries the open review) |
| The decision of record, with alternatives and *Verified:* | `DECISIONS.md` #102 |
| The reader-facing change entry | `CHANGELOG.md`, 2026-10-12, "Added" |
| The contract and how it is checked | `model/sovereign_appliance_note.py`, `tests/test_sovereign_appliance.py`, the `test.sh` step, `./run.sh appliance` |
| The link register | `docs/sovereign-appliance-links.csv` |
| Where the note is pointed to | `README.md` (layout, item 4, its section), `ROADMAP.md` item 6, `CLAUDE.md` (command and gotcha), `docs/hosting-operators.md` (`colocated_appliance`), `docs/testing.md` |
| The commit | `f73c24a`, sixteen files, verification in its message |
| The working narrative and the open items | this file |

### Follow-ups for the owner (not done here)

- Run the second-model review over the eight quotations, then update the note's status table and #102's *Verified:*.
- Decide whether `.claude/settings.json` is committed, ignored or removed.
- Decide whether the box becomes the unit when distribution is modelled (`ROADMAP.md`, item 6 of that block).
- Push and merge: `main` is a production deploy (#81); the owner's OK first.

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
   member-state names and no test; the box needs sizing figures, a quoted treaty and a checker. Recorded as #102
   with the rejected alternatives.
2. **The #101 contract shape, stricter in two places.** A checker, a committed link register, a gate step and a test,
   as for `NATIONAL-AI-STRATEGIES.md`. Stricter: no currency figure anywhere (the #101 note allows bands in one
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
5. **Reuse the #101 checker's generic parts rather than copy them.** `load_links` and `write_links` in
   `model/national_ai_note.py` took `path` and `note` parameters with the old defaults; the ranking and money
   patterns, the URL probe and `states()` are imported. The #101 tests pass unchanged.
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

### What changed (committed the same day as `f73c24a`; see the 2026-10-13 entry)

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
| `DECISIONS.md`, `CHANGELOG.md`, `README.md`, `ROADMAP.md` | #102; the entry; the layout line, item 4 and a section; the distribution item's unit |

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
  note's status table and #102 say so.
- The Riigi Teataja page: cited, not read.
- Whether the agreement's inviolability clauses could be reproduced for a cage in a commercial facility is a legal
  question the note leaves open (caveat 4).

### Follow-ups for the owner (not done here)

- Commit. When this entry was written another session was editing the same checkout for #103 (the `/de` route),
  with staged renames in the index and its own hunks in `CHANGELOG.md`, `DECISIONS.md`, `CLAUDE.md` and
  `README.md` next to this work's. A plain commit would take both; the gate must run on whatever is committed, so
  the two are separated by hand (or #103 is committed first and this work on top of it). *Resolved the same day;
  the 2026-10-13 entry records how.*

- Run the second-model review (`/factcheck`'s rule, by hand for prose) over the eight quotations.
- Decide whether the box becomes the unit when distribution is modelled (`ROADMAP.md`, item 6 of that block).
- Push and merge are the owner's call: `main` is a production deploy (#81).
