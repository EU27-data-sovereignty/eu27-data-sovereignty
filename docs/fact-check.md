# The cross-model fact check: procedure

Every printed fact is checked, exactly as printed, by a second model that did not write it. No production
deploy happens unless every printed fact has a current *supported* verdict. A fact the check does not
confirm is withheld as disputed, with the checker's reason, instead of printed.

- **The rules:** [`DECISIONS.md`](../DECISIONS.md) #87 and #89.
- **The method in prose:** [`METHOD.md`](../METHOD.md) §9.
- **The state of every fact:** [`docs/fact-check-audit.md`](fact-check-audit.md), generated.

This file is the procedure. Follow it exactly: a check only means something if every run is made the same way.
The `/factcheck` skill (`.claude/skills/factcheck/SKILL.md`) runs these same steps.

## The rule

| Fact written by | Checked by |
|---|---|
| `claude-opus-5-5` | `claude-fable-5-1` |
| `claude-fable-5-1` | `claude-opus-5-5` |
| anything else: unrecorded, a person, or a program | `claude-fable-5-1` |

The rule is `factcheck.RULE`, and `factcheck.checker_for` applies it. The author comes from the files:
- a vetting finding records `researcher_model` (#87 on);
- a citizen's finding records the person (`person:<handle>`);
- a Eurostat value was read by a program (`program:fetch_eurostat.py`);
- everything admitted earlier is `unrecorded`.

## What a verdict covers

A verdict is for one fact *as printed*. `fact_sha256` is the SHA-256 of the canonical JSON of the following,
built by `factcheck.fact_record` and `citation_record`:
- the claim id;
- the question it answers;
- the printed text;
- whether it is categorical;
- every citation: source id, URL, archived URL, Eurostat API URL, fetched-document hash, locator, original
  quote, English quote, and the value as found.

The bundle and the content model share these functions, so both compute the same hash. A test checks this for
every fact. Change any part of a fact and its verdict lapses: the fact must be checked again before the next
deploy. Nothing else voids a verdict, so a re-run checks only what changed.

## Running a check

All commands run from the repository root. `./run.sh factcheck <cmd>` is `python3 model/factcheck.py <cmd>`.

1. **See what is due.** `./run.sh factcheck status` lists every printed fact that is not passing, and why:
   never checked, changed since it was checked, or checked by its own author.
2. **Prepare.** `./run.sh factcheck prepare`. It prints the run id, the facts due per checker model, the
   number of batches, and the path of `args.json`.
   - `--all` re-checks every printed fact.
   - `--pool` batches across states. Use it for a few facts spread over many states, such as one figure per
     country: one agent instead of one per state.
   - `--withheld-blocked` re-checks withheld facts whose checker could not read the source (a refusal, a
     block, a timeout). It sends no fetch: each fact goes with a plain-text copy of the exact document the
     pipeline fetched and hashed when the fact was admitted, found in `cache/` by its SHA-256.
   - The input goes to `cache/factcheck/<run>/in/`. Its hash and the workflow's hash are recorded here, at
     prepare time.
   - **State the cost and get the owner's OK.** Measured on 2026-10-02: about $4–6 for a batch of 30 facts
     with Fable 5.1. The workflow's own token count leaves out cache tokens. Sum `message.usage` in the agent
     transcripts for the real figure.
3. **Run the workflow.** Call the Workflow tool with `scriptPath: model/research/factcheck/workflow.js` and
   `args` set to the contents of `args.json`.
   - The script sets each checker's model from its batch; nothing inherits the session's model.
   - Change prompts only in `workflow.js`, in a commit of its own.
   - If agents fail on a session or rate limit, resume with the same script, args and
     `resumeFromRunId`: finished batches replay from cache.
4. **Stage.** `./run.sh factcheck stage <task output file> --run <workflow run id> --prepared <run id from prepare>`.
   It refuses, as a whole, any batch whose checker:
   - reported a different model than the one asked for;
   - is an author of a fact in the batch;
   - answered for a fact it was not given;
   - gave an invalid verdict.

   A fact left without a verdict is recorded as *unclear*. Email addresses in a checker's text are removed.
5. **Record.** `./run.sh factcheck record --run <id> --output <task output file> --agents N --tokens N --duration T`.
   This writes:
   - the ledger;
   - the run manifest, `model/research/factcheck/runs/<run>.json`: sequence, input, workflow and output
     hashes, commit, bundle hash, counts;
   - the audit file.
6. **Rebuild the outputs.** `./run.sh data`, then `./run.sh artefacts`. This updates:
   - the withheld facts in the documents;
   - the fact-check appendix in every PDF, brief, web page and the `/ask` corpus;
   - the posters.
7. **Gate.** `./test.sh` must pass. `./run.sh factcheck gate` must print `N of N printed facts checked, supported,
   checker ≠ author` and exit 0.
8. **Record the decision and commit.**
   - Update the `Verified:` line of the decision the run verifies, and add a `CHANGELOG.md` entry.
   - Commit the staged run, the ledger, the manifest, the audit file and the regenerated outputs together.
   - A push to `main` is a production deploy: get the owner's OK.

## Resolving a withheld fact

Never by editing a verdict, the ledger or a register. A withheld fact comes back only as a *changed* fact:
- a better source, through `/vet`;
- or printed wording that its quote supports.

Either way the hash changes, the old verdict withholds nothing, and the next run checks the new fact. A
source that refused the checker can be re-checked from its hashed copy (`--withheld-blocked`). Every verdict
stays on the record in the audit file, including those a later run superseded.

## Files

| File | Committed | What it is |
|---|---|---|
| `model/factcheck.py` | yes | the rule, the hash, prepare / stage / record / audit / status / gate / replay |
| `model/research/factcheck/workflow.js` | yes | the checker's prompt and schema; its SHA-256 is in each run's manifest |
| `model/research/factcheck/staged/<run>/<batch>.json` | yes | every verdict as staged: the evidence the ledger is built from |
| `model/research/factcheck/runs/<run>.json` | yes | one manifest per run |
| `model/research/factcheck/ledger.csv` | yes | the current verdict per claim |
| `docs/fact-check-audit.md` | yes | generated: status, withheld facts, every disagreement, runs, steps |
| `model/factcheck_appendix.py` | yes | the appendix every asset carries |
| `cache/factcheck/<prepared>/` | no (`cache/`) | the workflow input, its hashes, and the gzipped raw output |

## What is reproducible, and how to check it

- **The ledger, from the staged verdicts.** `python3 model/factcheck.py replay` applies every staged run in
  recorded order and compares the result with the committed ledger. It is a stage of `./test.sh`.
- **The audit file, from the ledger and the bundle.** `python3 model/factcheck.py audit --check`, also in
  `./test.sh`. The gate fails if the file is stale.
- **The appendix in every asset, from the ledger.** `./run.sh data` is byte-reproducible under the pinned build
  date, and `./test.sh` checks the generated files are current.
- **Which facts are due, and the checker for each.** `prepare` is deterministic given the bundle and the
  ledger. The run id includes the hash of its input.
- **Which model checked.** Each manifest names the model. The staged batch records the model the script asked
  for and the one the checker reported, and `stage` refuses a mismatch. The agent transcripts carry the API's
  own model field.
- **Not reproducible: the verdicts themselves.** A model asked again may answer differently. To test that,
  run `prepare --all` on the same bundle and compare the new staged verdicts with the old ones; the
  manifests record both runs.

The clean-room rebuild (`./run.sh reproduce`) clones HEAD, regenerates every output and runs `./test.sh
--no-e2e` in the clone, so a fresh clone proves the ledger replay and the audit file too.

## Known limits

- **A check by a second model, not by a person.** It narrows one model's blind spots. It does not remove
  those that models share.
- **The checker may send a browser-like User-Agent** when it fetches pages itself.
- **Unclear is withheld.** A true fact behind a page that refuses automated access stays withheld until a
  hashed copy confirms it, or a person does.
