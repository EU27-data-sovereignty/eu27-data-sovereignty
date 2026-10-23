# The Draghi report: what was done and decided

A log of the work behind [`DRAGHI-REPORT.md`](../../DRAGHI-REPORT.md), newest first, in the shape of
[`technical-universities-log.md`](technical-universities-log.md). Each entry records:
- who or what produced it;
- what the owner asked;
- each choice made, the trade-off it accepted, and what changed;
- how it was checked, and what is still open.

`DECISIONS.md` #118 is the decision of record. This log is the working narrative behind it and does not repeat its
alternatives. It is planning, not data: nothing here is read by the model, the book, the web app, the reader or `/ask`.

## 2026-10-23: the report archived, read against the 27 states, committed and pushed to a branch

**Produced by.** Claude Opus 5.5 (`claude-opus-5-5`) in Claude Code, session
`https://claude.ai/code/session_01MUUAhb26VaVC6gAQF4hshd`, on the new branch `notes/draghi-report`, cut from
`mobile/rebuild` at `def3390`. Two `general-purpose` subagents on the same model extracted quotations:
- one took every passage naming a member state: 324 records, about 142k subagent tokens;
- one took Part B's defence, space, innovation, competition and governance chapters: 259 records, about 244k.

Both token figures exclude cache (see the agent-run cost memory). Commits: `d8b87af` (pushed) and `009b819` (local,
records a CI finding in TODO).

**Asked by the owner**, verbatim:
1. "find and download the mario draghi report on europe"
2. "can you verify the report doenst yet exist in the eu27 project repo"
3. "goal for this session: analyze the draghi report and think about implications for this project, with emohasis on
   per nation. also, save the pdf somewhere on an asssets folder"
4. "always ensure test.sh is comprehensive"
5. "comnmit and push all, presuming secrutity and privacy"
6. "status?"
7. "log all decisions and tradefofs on markdown"

Two choices went to the owner as questions and came back answered: a gitignored `assets/` folder with a tracked
manifest, and an authored note with a checker. The rest were the assistant's, and are listed below with what each one
cost.

### Decisions about the source

1. **Checked for an existing copy before downloading.**
   - Searched filenames, every text file including gitignored ones, every branch's history, and
     `model/sources/*.csv`.
   - Ran `pdftotext` on all 342 PDFs under `cache/` and `.vercel/output/static/`: 0 hits for "Draghi" or the report's
     title.
   - *Trade-off:* raw `grep` cannot read compressed PDF text, so the text extraction was the only part of the check
     that could have found a copy filed under a hashed name.
2. **Took the two English parts and nothing else.**
   - Archived: Part A (73 pages) and Part B (328 pages), from the Commission's own download URLs.
   - Left out: the German and French translations of Part A, and Draghi's address to the European Parliament.
   - *Trade-off:* a reader of a translation has to map pages. The note quotes English only, so nothing else was needed.
3. **Stored outside git under a hash manifest** (owner's choice).
   - Gitignored: `assets/reports/**/*.pdf`, in both ignore files.
   - Tracked: `assets/reports/MANIFEST.csv`, with URL, size and sha256 for each part.
   - *Trade-off:* the copies are not backed up by git or by the `~/dev` backup. Restoring them depends on the
     Commission's URLs staying up.
   - No Internet Archive copy was made. The manifest hash would prove an archived copy identical, so making one
     remains an option if the Commission URLs ever move.
4. **No backup entry.** The files can be rebuilt from public URLs, which is the workspace rule's "ignore it" case.

### Decisions about the note's form

5. **The branch was cut from `mobile/rebuild`, not `main`.**
   - *Why:* the decision number follows #117 without a collision.
   - *Trade-off:* the branch carries the unmerged reader work (#109–#117), so it cannot reach `main` on its own.
6. **Citations use the PDF page, not the printed folio.** Part A's cover and colophon carry no folio, so its
   disclaimer (A p. 2) would otherwise have no page.
   - *Trade-off:* a reader of the printed Part A has to subtract two.
   - Part B's folios match the PDF pages.
7. **The quote register is generated, never kept by hand.**
   - The first version seeded rows from the note, then re-proved them. Mid-session, `quotes` was changed to rebuild
     the whole register from the note's citations, and a test compares the two.
   - *Why:* a hand-kept register drifts from the note. A generated one cannot.
8. **Quotations are compared with whitespace collapsed and nothing else.** Line-break hyphens are not undone, and the
   citation pattern cannot hold a double quote inside a quotation.
   - *Trade-off:* every span the note quotes was chosen to avoid inner double quotes. One sentence was rephrased to
     put the page right after the closing mark: "the demand for” (A p. 36) what it calls sovereign cloud solutions".
9. **A state's facts are cited as claim id plus printed text, compared with the bundle.**
   - Only spans with the role `fact` count, so a withheld (disputed, #89) or gap value cannot be cited.
   - *Trade-off:* any upstream change to a cited text fails `check`, and the entry must be re-read. That is
     deliberate, because a quiet mismatch is the failure being prevented.
10. **Only long quotations must be anchored.** A quotation of 40 characters or more needs a page or a claim id.
    Shorter quoted terms, such as “home affairs”, are not checked.
    - *Trade-off:* a short misquotation could pass. A rule for short spans would have flagged every scare quote.
11. **Ranking and money reuse the national-AI checker's patterns, with quotations exempt.**
    - Draghi's “top ten worldwide” stays quoted.
    - The assistant's own comparatives went too, although no pattern caught them: "the most national hosting", "the
      clearest case", "the state the report names least", "named more often than any other". Each was rewritten as a
      count or a plain statement (#10, #77).
12. **The approved plan's per-state Sources subsection was dropped.** Every citation in an entry is either a PDF page
    backed by the register or a claim id backed by the bundle, so a Sources list would only repeat them. The plan
    file's version had it; the note does not.

### Decisions about the analysis

13. **One reading lens: the B p. 84 proposals, applied per state.**
    - **The exception:** defence, home affairs and justice.
    - **Gold-plating:** passporting against the indicators L1 and L3.
    - **The floor:** EU control of security and encryption, read against C1 and C2.
    - *Trade-off:* Draghi's energy, pharma and industry material is left out of the state entries. It bears on the
      economy, not on hosting state data.
14. **The exception is read through the operator the project already prints.**
    - "Home affairs" is decided by which ministry runs the identity register, so no new research was needed.
    - *Trade-off:* it covers only the states with a printed operator. BG, LT and MT have none, and LU has one only for
      its eID. Those entries say so, and the sourcing is a TODO item.
15. **"Plausibly" is used throughout.** The report defines the exception only by example, so no reading can be more
    certain than that.
    - Two calls go a step past the printed text, and the entries say so: Cyprus's Civil Registry and Migration
      Department and Latvia's Office of Citizenship and Migration Affairs are read as home affairs from the word
      "migration" in their names.
    - Portugal's IRN was not placed under any ministry, because nothing printed names one.
16. **"Where Draghi names it" quotes the mention that bears most on data.**
    - For 22 states that is the GDPR age-of-consent footnote (B p. 319). It names 26 of the 27.
    - Slovenia's closest mention is a nuclear-generation footnote (B p. 20), quoted and labelled as not about data.
    - The `none: searched` form was not needed, since all 27 states are named somewhere.
17. **EU-wide figures stay EU-wide.** The hyperscaler share, the 90% data value loss and the 80% digital dependence
    are quoted in section 2 and used for no state.

### Decisions about checking, the gate and publishing

18. **The quotations were extracted by two subagents and checked mechanically.** Each agent returned verbatim spans
    with page numbers and no conclusions, verified its own output (324/324 and 259/259), and the assistant re-proved
    every quote the note uses (58/58).
    - *Trade-off:* the extractors and the analyst are the same model. The mechanical check covers the quotes, not the
      reading of them.
19. **The test.sh rule was met through the existing register.** The checker runs through `model/notes.py`, with no new
    stage, and `check` re-finds every quotation in the PDFs when they are on disk.
    - Where they are not, as in CI, the headline says `re-proving SKIPPED (no PDF here; run fetch)`.
    - *Trade-off:* CI does not download the PDFs, so it relies on the committed register's `found` column. Fetching
      them would make every CI run depend on commission.europa.eu being reachable.
    - The rule was saved as the memory `test-sh-comprehensive`. The gate's own `test_repeatability` caught one omission
      the same hour: `test_draghi_note` was missing from `docs/testing.md`.
20. **The full gate ran with `--no-live`.** The live `/ask` check makes a real, paid call to production, and nothing
    here touches `/ask`.
    - *Trade-off:* the run was not the complete gate, and the summary said so.
21. **Committed although `./test.sh` failed in `mobile/`.** `doctor` failed on Expo SDK 58 patch releases above the
    pins, and `audit` on a stale `braces` allowlist row. Both come from upstream changes since `def3390`, and nothing
    in `mobile/` was changed.
    - *Trade-off:* fixing them here would have mixed a dependency bump into a documentation change. It went to TODO,
      to be done in its own change.
22. **Pushed the branch, not `main`.** "Push all" was read as this work's branch. A push to `main` is a production
    deploy (#81) and needs its own OK.
    - The security gate passed on commit and on push. Its "origin is PUBLIC" line is the banner for strict mode
      (`dotfiles/security/gate.sh` line 550), not a finding.
23. **The web audit failure found in CI was recorded, not fixed.** Branch CI run `40009608303` failed
    `npm audit --audit-level=high --prefix web` on `vite` 8.2.x (high) and `vitest` 5.0.x (moderate), both dev
    dependencies.
    - Local `./test.sh --only web` does not run that audit, so the gate passed here and failed there.
    - That gap contradicts decision 19's rule. It is a TODO item, and commit `009b819` is not yet pushed.

### How it was checked

- `python3 model/draghi_note.py fetch`: both parts `ok` against the manifest.
- `python3 model/draghi_note.py quotes`: 58 quotations, 58 found on their page.
- `python3 model/draghi_note.py check`: 27 states, 58 quotations (58 re-found in the hashed PDFs), 89 claim ids,
  1 URL, 0 problems.
- `./test.sh --only model`: 455 tests OK, every stage green.
- `./test.sh --no-live`: model, PDF and web stages green; `mobile/test.sh` failed `doctor` and `audit` (decision 21).
- Branch CI: security green and model green; web and mobile failed (decisions 21 and 23).
- `doc-dupes` ran clean on every markdown file written in the session, this log included.

### Still open

Every open item is in `TODO.md`, under "The Draghi note (#118)" and "Testing". In short:
- the cross-model review, and a person's reading;
- what became of the B p. 84 proposals;
- the 5G-toolbox states and the "secure cloud" programmes;
- operators still to source for five states;
- the two upstream failures in mobile and web;
- the push of `009b819`.
