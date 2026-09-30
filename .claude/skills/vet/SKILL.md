---
name: vet
description: Run a vetting pass over every printed fact in the EU-27 report — find better and newer sources, fill gaps, blind-review, verify mechanically, admit, and record the run. Use when the owner asks to vet, re-vet, refresh or re-check the report's evidence, or before anything is published outward.
---

# /vet: a reproducible vetting run

The procedure and its rules are in `docs/vetting.md`, and METHOD.md section 7 states the rules. This
skill is the order of operations. Follow it exactly: a vetting run is only reproducible if every run
is made the same way.

## Before starting

- `git status` must be clean, on a branch other than `main`: `git switch -c data/vetting-<date>`.
- Say what this will cost before launching. The 2026-09-30 run used 54 agents, 6.75M tokens and 64
  minutes. Launch only after the owner agrees.

## Steps

1. **Prepare the input.** `./run.sh vet prepare`, or add `--iso XX` for a subset. It prints the run id and
   the path of `args.json`.
2. **Run the workflow.** Call the Workflow tool with
   `scriptPath: model/research/vetting/workflow.js` and `args` set to the contents of that `args.json`,
   as a JSON array. Use the checked-in script, never an edited copy: its sha256 is how the run
   identifies its prompts. To change the prompts, edit `workflow.js` in a commit of its own, first.
3. **Stage.** `./run.sh vet stage <task output file> --run <workflow run id>`. Pass the task's output
   file as written.
4. **Tier new hosts.**
   - `./run.sh vet hosts` writes a stub with a suggested tier for each unclassified host.
   - Correct it against the table in `docs/vetting.md`. Show the owner every T1 call and every T3/T4
     call, and ask them to confirm.
   - Copy the confirmed stub into `cache/vetting/<run>/`, then `./run.sh vet hosts --apply <stub>`.
5. **Verify.** Run `./run.sh vet verify` in the background with the maximum timeout. It's resumable:
   if it's interrupted, run it again.
6. **Admit.** `./run.sh admit` runs research, then vetting, always both. Then `./run.sh vet report`.
7. **Build and gate.**
   - `./run.sh data`, then `./run.sh artefacts`.
   - Raise the floors the tests ask for: `FLOORS`, `NATIONAL_DATA_FLOOR` and `FACT_FLOOR`. Lowering
     one needs the reason written beside it.
   - `./run.sh admit --check` must print "6 of 6 registers reproduce".
   - `./test.sh` must pass in full.
8. **Record the run.** Write the run manifest (`python3 model/vetting.py manifest --run <id> --output
   <task output file>`). Update the `Verified:` line of the DECISIONS entry the run verifies with the
   date, the run id and the `vet report` totals. Add the run to `CHANGELOG.md` (newest first): what was
   found, admitted, disputed and not reached, citing the decision.
9. **Commit** on the branch. The commit message carries the report totals. **Never push without the
   owner's explicit OK.** A push to `main` is a production deploy.

## Never

- Never edit a register by hand to make a finding fit. Admission decides.
- Never resolve a disputed fact by judgement. Only the two published rules resolve it: a higher tier
  wins, and the same authority with a later date wins.
- Never retry a page that refused (403, robots) with a browser.
- Never describe the result as human-verified.
