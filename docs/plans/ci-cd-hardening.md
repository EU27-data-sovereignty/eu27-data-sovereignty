# CI/CD hardening: the list, what is done, what is yours to run

2026-10-12. The owner asked whether the pipeline is strong enough, then for the actions that add the least
friction to one writer, then to do all of them. The decision is [`DECISIONS.md`](../../DECISIONS.md) #107;
this is the working list.

## The assessment, in one paragraph

The deploy path was already strong: a push to `main` runs the full gate as parallel jobs, the fact-check
gate, ships the exact artifacts the gate tested from an environment that only `main` can read, and
smoke-tests the live domain afterwards; actions are pinned by SHA, typst is checksummed, pip uses hashes.
The repository around it was loose: no branch protection, secret scanning off, no rollback, a floating
runner image, and nothing watching the pins for vulnerabilities.

## The seven actions

| # | Action | Friction | Status |
|---|---|---|---|
| 1 | Secret scanning and push protection on the repository | none | **yours**, command A |
| 2 | Pin every workflow to `ubuntu-24.04` | none | done, `tests/test_workflows.py` |
| 3 | Ruleset on `main`: no force push, no deletion | none | **yours**, command B (file in tree) |
| 4 | Dependabot security updates on, version updates off | none | file done; **yours**, command C |
| 5 | Keep the fact-check gate at deploy time only | none | unchanged, by design (#87) |
| 6 | Roll back a deploy that fails its post-deploy checks | one smoke test | done, `deploy.yml` |
| 7 | Required fast checks on `main`; `ci.yml` on every branch push | ~5 min per push to `main` | done in tree; applied by command B |

Rejected, because each would slow one writer for no check: required reviews, a staging environment, visual
regression in CI. Reasons in #107.

## The three commands (repository settings, outside the tree)

The assistant's own permission rule (#106) denies `gh api` writes and `gh repo edit`, so these are typed by
the owner. Each is idempotent: running it twice changes nothing the second time.

**A. Secret scanning and push protection**

```
gh api -X PATCH repos/EU27-data-sovereignty/eu27-data-sovereignty \
  --input - <<'EOF'
{"security_and_analysis":{"secret_scanning":{"status":"enabled"},"secret_scanning_push_protection":{"status":"enabled"}}}
EOF
```

**B. The ruleset for `main`** (the file is `.github/rulesets/main.json`; to update it later, `-X PUT` on
`rulesets/<id>` with the same input)

```
gh api -X POST repos/EU27-data-sovereignty/eu27-data-sovereignty/rulesets --input .github/rulesets/main.json
```

**C. Dependabot alerts and security updates**

```
gh api -X PUT repos/EU27-data-sovereignty/eu27-data-sovereignty/vulnerability-alerts
gh api -X PUT repos/EU27-data-sovereignty/eu27-data-sovereignty/automated-security-fixes
```

**Check, read-only, after all three:**

```
gh api repos/EU27-data-sovereignty/eu27-data-sovereignty/rulesets --jq '.[].name'
gh api repos/EU27-data-sovereignty/eu27-data-sovereignty --jq '.security_and_analysis'
```

## What changes in the daily loop after command B

Push the branch, wait for the four fast checks (about five minutes), then push it to `main`. A push to `main`
of a commit whose checks have not run is refused with the names of the missing checks. Nothing else changes:
the gate, the fact-check gate, the deploy and the smoke test run as before, and the deploy now rolls itself
back if the smoke test or the live `/ask` check fails.
