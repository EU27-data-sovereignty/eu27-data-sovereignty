---
name: factcheck
description: Fact-check every printed fact that is due, as printed, with the model that did not write it (Fable 5.1 or Opus 5.5), and record it in the audit file and every asset's appendix. Use before any push to main (a production deploy), when the owner asks to fact-check or re-check the report, or when `./run.sh factcheck status` shows facts not passing.
---

# /factcheck: the cross-model fact check that gates every deploy (#87)

A push to `main` deploys to production, and the deploy refuses to run unless `factcheck.py gate`
passes. The gate requires every printed fact to have a current verdict of *supported* from a checker
model that did not write it, and requires `docs/fact-check-audit.md` to be current. This skill is the
order of operations. Follow it exactly: a check only means something if every run is made the same way.

## Before starting

- `git status` must be clean, on a branch other than `main`.
- Run `./run.sh factcheck status` to see how many facts are not passing, and why.

## Steps

1. **Prepare.** Run `./run.sh factcheck prepare`, or add `--all` to re-check every printed fact. It
   prints:
   - the run id;
   - the facts due, per checker model;
   - the number of batches, one agent each;
   - the path of `args.json`.

   State what the run will cost, then **wait for the owner's OK**. For scale, the vetting run of
   2026-09-30 used 54 agents for 1,017 findings.
2. **Run the workflow.** Call the Workflow tool with
   `scriptPath: model/research/factcheck/workflow.js` and `args` set to the contents of that
   `args.json`, as a JSON array.
   - Use the checked-in script, never an edited copy. `prepare` recorded its sha256.
   - The script sets each agent's model from its batch. Never let a checker inherit the session model.
3. **Stage.** Run `./run.sh factcheck stage <task output file> --run <workflow run id> --prepared <run id from prepare>`.
   - It refuses any batch whose checker reported a different model than the one asked for, or that
     wrote a fact in the batch.
   - Report every refusal to the owner. Re-run the refused batches only; never edit their output.
4. **Record.** Run `./run.sh factcheck record --run <workflow run id> --output <task output file> --agents N --tokens N --duration T`,
   taking those figures from the workflow's usage. It writes:
   - the ledger;
   - the run manifest;
   - `docs/fact-check-audit.md`.
5. **Disagreements.** Run `./run.sh factcheck status`.
   - For every fact *not supported* or *unclear*, show the owner the claim, the printed text, the
     checker's reason and the URL.
   - **The owner decides.** Typically that means a better source through `/vet`, or withdrawing the
     fact. A changed fact is due again, so the next run checks it.
   - Never edit the ledger, a register or a verdict to make the gate pass.
6. **Build.** Run `./run.sh data`, then `./run.sh artefacts`. This refreshes the fact-check appendix
   in the bundle, the briefs, the PDFs, the web page and the poster footers.
7. **Gate.** `./test.sh` must pass in full, and `./run.sh factcheck gate` must exit 0. The gate
   prints `N of N printed facts checked, supported, checker ≠ author`.
8. **Record the decision.**
   - Update the `Verified:` line of DECISIONS #87, or of the decision the run verifies, with the date,
     the run id and the gate's output.
   - Add a `CHANGELOG.md` entry (newest first) with facts checked, per model and per verdict.
9. **Commit** the ledger, the staged run, the manifest, the audit file and the regenerated outputs,
   all together. **Never push without the owner's explicit OK.** A push to `main` is a production deploy.

## Never

- Never let a model check a fact it wrote. Never relabel a verdict's model.
- Never resolve a disagreement by judgement or by editing a file. It stays on the record in the audit
  file even after a later check supersedes it.
- Never describe the result as human-verified. It is a check by a second model.
