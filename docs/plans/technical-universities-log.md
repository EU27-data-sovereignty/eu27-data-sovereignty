# The technical universities: what was done and decided

A log of the work behind [`TECHNICAL-UNIVERSITIES.md`](../../TECHNICAL-UNIVERSITIES.md), newest first, in the shape
of [`national-ai-log.md`](national-ai-log.md) and [`sovereign-appliance-log.md`](sovereign-appliance-log.md). Each
entry records who or what produced it, what the owner asked, what was decided and why, what changed, how it was
checked, and what is still open. The decision of record is `DECISIONS.md` #108; this log is the working narrative
behind it, not a second copy. Planning, not data: nothing here is read by the model, the book, the web app or `/ask`.

## 2026-10-12 to 2026-10-13 — the note written, reviewed twice, registered, pushed

**Produced by.** Claude Fable 5.1 (`claude-fable-5-1`) in Claude Code, session
`https://claude.ai/code/session_01JzrUgU5ZozYWCPBXUD2b5w`, on branch `sovereign-appliance-merge` from `3fe96b5`.
Three subagents: a `claude-opus-5-5` agent drafted the note and fetched every cited page; a second `claude-opus-5-5`
agent reviewed it in a separate session; a `claude-fable-5-1` agent ran the cross-model check. Commits `79fdf01`,
`96991e6`, `6747558`, all on `main`.

**Asked by the owner.** "I want you to identify the top technical schools in every eu27 country and add those to a
appropriate named markdown file", then "Include everything In test.sh and make sure it does not become bloated".

### Decisions

1. **"Top" became membership of a named published list.** The project ranks nothing (#10, #77), and a list of the
   schools the assistant thinks best is an opinion no reader can check. Three bases, each on the row: C1, member
   of CESAER; C2, member of the EuroTech Universities Alliance; C3, the state's technical university or polytechnic
   cited from a fetched page, used only where C1 and C2 give fewer than two. "Leading" is defined in the note as
   being on one of those lists; the order within a state is alphabetical; the checker refuses a ranking word
   anywhere else. Recorded as #108 with the rejected alternatives (league tables, the model's own judgment).
2. **The CESAER list is cited from the Internet Archive capture of 2026-04-13**, because cesaer.org did not resolve
   from the drafting machine on 2026-10-12. The row date is the day the capture was read; membership is as of the
   capture. On 2026-10-13 the cross-model checker reached the live page: the same 44 EU-state members, one entry
   renamed ("Grenoble INP – UGA" for "Université Grenoble Alpes"). The note keeps the capture as its cited source
   and says so in the Criteria line.
3. **A state with no technical university says so; a general university is not a stand-in.** The first draft listed
   the University of Luxembourg and the University of Ljubljana. The second review called them claims known to be
   wrong, not unverified ones. Both became a single `(none found) | — | — | none: searched 2026-10-12` row, a shape
   the checker now requires to be the state's only row.
4. **One `test.sh` stage for every note and draft set, through a register.** The gate had reached twenty stages, one
   per note. `model/notes.py` holds `CHECKERS`, a module-to-label map; `test.sh` runs it once as "Authored notes and
   agent drafts keep their contracts"; `tests/test_notes.py` fails on a `model/*_note.py` or `i18n_drafts.py` that
   is not registered and on a checker run by its own stage. Eighteen stages, and a new note is one line.
5. **The checker reuses the #103 helpers rather than copying them.** `load_links`, `urls` and `write_links` are
   imported from `model/national_ai_note.py`; the link register `docs/technical-universities-links.csv` has the
   same columns as the other two.
6. **Register labels name no note file.** The #103 and #104 checkers grep `model/` for their own filename and
   refuse a module that names it; the first labels did, and both failed. Labels now say "the national-AI note
   (#103)" and so on.
7. **A homepage URL is a bare origin, `https://www.tugraz.at`, no trailing slash**, so the register's one URL per
   row matches the row exactly; the checker enforces the shape.

### How the research ran

- The drafting agent fetched the archived CESAER members page, the EuroTech about page and each C3 page it cited,
  and wrote the row from what the page names. IP Paris is on both lists and is counted once, as C1. EPFL and
  Technion (C2, non-EU) and the non-EU C1 members are out of scope.
- C3 is the note's choice, not the page's: a cited page shows that the institution exists and what it calls itself;
  no page was found that names it *the* state's technical institution. The Method section says so.
- Two institutions were not added for lack of a fetched page that says so: LUT University (FI) and a second
  Hungarian institution.
- `links` on 2026-10-12: 73 URLs, 67 answered. `tugraz.at`, `kuleuven.be` and `rwth-aachen.de` did not resolve from
  this machine; `ucd.ie`, `taltech.ee` and `rtu.lv` refused (403); `uni.lu` answered 202. The Estonian row cites
  the rectors' conference page instead of taltech.ee; the Latvian row is **[unverified]**.
- Cities and homepage URLs are not separately sourced; the note says so.

### What changed

| File | Change | Commit |
|---|---|---|
| `TECHNICAL-UNIVERSITIES.md` | new: review-status line, Criteria, 27 state sections, Method; 61 rows (44 C1, 3 C2, 11 C3, 1 unverified, 2 none) | `79fdf01`, `96991e6`, `6747558` |
| `docs/technical-universities-links.csv` | new, written by `python3 model/technical_universities_note.py links` | `79fdf01`, `96991e6` |
| `model/technical_universities_note.py` | new checker, `check` and `links` | `79fdf01`, `96991e6` |
| `model/notes.py` | new: the register and the one stage | `79fdf01`, `96991e6` |
| `tests/test_notes.py` | new: every checker registered, run once, no per-note stage | `79fdf01`, `96991e6` |
| `tests/test_permissions.py` | new: the shape of `.claude/settings.json` (#106), carried here because it was due | `79fdf01` |
| `test.sh` | three note stages replaced by one; 18 stages | `79fdf01` |
| `tests/test_sovereign_appliance.py` | expects the register, not its own stage | `79fdf01` |
| `docs/testing.md` | the stages renumbered | `79fdf01` |
| `CLAUDE.md` | commands for the checker and the register; the gotchas | `79fdf01`, `96991e6` |
| `DECISIONS.md` | #108 | `96991e6`, `6747558` |
| `CHANGELOG.md` | the two entries under 2026-10-12 | `79fdf01`, `96991e6`, `6747558` |
| `docs/plans/localisation-plan.md` | the drafts' checker cited through the register | `96991e6` |

### The reviews

1. **Second agent, same model** (`claude-opus-5-5`, separate session, before the push). Read the 44 C1 rows against
   the archived list, the C2 rows against the EuroTech page and six C3 rows against their cited pages (BG, HR, EE,
   MT, IE, CY): all confirmed. Found: the two general-university rows (decision 3 above); no decision entry (#108
   written); the ranking-word list missing "ranked" and "ranking"; a C1 date that read as the capture date; the C3
   choice stated as the page's; the register's headline line picked by position, not by content; the `-f` deny
   regex in `tests/test_permissions.py`; a blank line in a table. Applied in `96991e6`.
2. **The label was wrong.** The note and #108 had called that review "second-model". The owner's standard (#87) is
   the model that did not write it; a second agent on the same model is not that. Corrected in `6747558`, and the
   cross-model check run.
3. **Cross-model check** (`claude-fable-5-1` agent, 2026-10-13). Fetched the archived CESAER page and confirmed all
   44 C1 rows and that no EU-state member is missing; the EuroTech page and the three C2 rows; all eleven C3 pages,
   each naming its institution; found nothing contradicting the RTU row or the two "none found" rows; no ranking
   language. Zero discrepancies. It also reached the live cesaer.org page (decision 2).

### Verification

| Check | Result |
|---|---|
| `python3 model/technical_universities_note.py check` | 27 states, 61 rows (C1 44, C2 3, C3 11, [unverified] 1, none 2), 73 URLs (67 answered at the last link check), 0 problems |
| `python3 model/notes.py check` | four checkers, all `ok` |
| `python3 -m unittest tests.test_notes tests.test_permissions tests.test_docs` | OK |
| `./test.sh --no-live` on `6747558` | 18 stages, exit 0 |
| Actions, branch `sovereign-appliance-merge` | 22 checks green before the push to `main` |
| Actions deploy run 38345425553 (`6747558`) | every gate job and the deploy green; the record and promote steps ran, the rollback step was skipped |

### Still unverified

- No person has read the note. The review-status line and #108 say so.
- The Riga Technical University row: cited, not read (403).
- cesaer.org itself: reached once, on 2026-10-13, by the cross-model checker; the Criteria line still cites the
  capture. `links` from this machine has not reached it.
- Cities and homepages, by design.

### Open

- A reading by the owner.
- If institutions ever become entities in the hosting model (#96), this note is the seed of a sourced register and
  stops being authored; #108 says when that would change.
