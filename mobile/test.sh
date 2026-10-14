#!/usr/bin/env bash
# Every check of the mobile reader in one place. Exit 0 = all green. The root gate runs it as the
# `mobile` group (`./test.sh --only mobile`, #113); `./run.sh test` runs it from here.
#
#   ./test.sh                 everything that needs no Docker and no device
#   ./test.sh --quick         static checks and unit tests only (no coverage, doctor, web export, audit)
#   ./test.sh --integration   also the live round-trip against local Supabase: the deploy's own publisher
#                             fills the bucket, anonymous reads work, anonymous writes are refused, and the
#                             app's edition store installs a good edition and rejects a tampered one
#                             (colima start; supabase start)
#   ./test.sh --offline       skip the steps that need the network (expo-doctor, npm audit)
#   ./test.sh --ci            skip the local security gate (CI runs it in its own job)
#
# Every step runs even after an earlier failure; a summary table lists them all.
set -euo pipefail
cd "$(dirname "$0")"

QUICK=0; INTEGRATION=0; OFFLINE=0; CI_MODE=0
for arg in "$@"; do
    case "$arg" in
        --quick) QUICK=1 ;;
        --integration) INTEGRATION=1 ;;
        --offline) OFFLINE=1 ;;
        --ci) CI_MODE=1 ;;
        -h|--help) sed -n '2,13p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
        *) echo "Unknown option: $arg (see ./test.sh --help)"; exit 2 ;;
    esac
done

if [ -t 1 ]; then
    GREEN='\033[0;32m'; RED='\033[0;31m'; YELLOW='\033[1;33m'; BOLD='\033[1m'; RESET='\033[0m'
else
    GREEN=''; RED=''; YELLOW=''; BOLD=''; RESET=''
fi

LOG_DIR="$(mktemp -d "${TMPDIR:-/tmp}/eu27-mobile-test.XXXXXX")"
trap 'rm -rf "$LOG_DIR"' EXIT

# Parallel indexed arrays (bash 3.2 has no associative arrays).
NAMES=(); RESULTS=(); SECONDS_TAKEN=()

record() { NAMES+=("$1"); RESULTS+=("$2"); SECONDS_TAKEN+=("$3"); }

# run_step <name> <command...>: runs the command, captures output, never aborts the script.
run_step() {
    local name="$1"; shift
    local log="$LOG_DIR/$name.log" start end rc
    printf '%b▶ %s%b\n' "$BOLD" "$name" "$RESET"
    start=$(date +%s)
    set +e
    ( "$@" ) > "$log" 2>&1
    rc=$?
    set -e
    end=$(date +%s)
    if [ "$rc" -eq 0 ]; then
        record "$name" PASS $((end - start))
        # These report per-item results worth seeing even when green.
        case "$name" in edition|audit|integration) sed 's/^/    /' "$log" ;; esac
    else
        record "$name" FAIL $((end - start))
        printf '%b  failed (exit %s) — last 40 lines:%b\n' "$RED" "$rc" "$RESET"
        tail -n 40 "$log" | sed 's/^/    /'
    fi
}

skip_step() {
    printf '%b▶ %s — skipped (%s)%b\n' "$YELLOW" "$1" "$2" "$RESET"
    record "$1" "SKIP: $2" 0
}

# --- step bodies -------------------------------------------------------------------------------

check_node() {
    local min="20.19.4" current want
    current="$(node -v | sed 's/^v//')"
    if [ "$(printf '%s\n%s\n' "$min" "$current" | sort -V | head -n1)" != "$min" ]; then
        echo "Node $current is older than $min (React Native 0.86 / Metro minimum)"; return 1
    fi
    want="$(tr -d '[:space:]v' < .nvmrc)"
    if [ "${current%%.*}" != "$want" ]; then
        echo "warning: Node $current, but .nvmrc (and CI) use $want — results may differ (try: nvm use)"
    fi
    echo "Node $current"
}

check_deps() {
    if [ ! -d node_modules ]; then
        npm ci --no-fund --no-audit
    fi
    # Exits non-zero when node_modules doesn't match package.json / package-lock.json.
    npm ls --depth=0
}

check_secrets() {
    local tracked
    tracked="$(git ls-files . | grep -E '(^|/)\.env(\..+)?$' | grep -v '\.env\.template$' || true)"
    if [ -n "$tracked" ]; then
        echo "Env files with real credentials must never be tracked:"; echo "$tracked"; return 1
    fi
    echo "no tracked env files"
}

check_shell() {
    local f rc=0
    for f in *.sh scripts/*.sh; do
        [ -f "$f" ] || continue
        bash -n "$f" || rc=1
        /bin/bash -n "$f" || rc=1   # macOS bash 3.2 — the committed-script baseline
    done
    if command -v shellcheck > /dev/null 2>&1; then
        shellcheck -S warning ./*.sh || rc=1
    else
        echo "shellcheck not installed — syntax-checked only (brew install shellcheck)"
    fi
    return $rc
}

# Tool versions that live outside package.json: the Supabase CLI the deploy's gate installs
# (../.github/workflows/gate.yml) is an exact x.y.z and the one README.md names; no EAS anywhere.
check_tooling() {
    local rc=0 supa readme
    supa="$(sed -n -E 's/^[[:space:]]*version:[[:space:]]*(.*)$/\1/p' ../.github/workflows/gate.yml | tr -d "'\"" | sort -u)"
    if ! printf '%s' "$supa" | grep -qE '^[0-9]+\.[0-9]+\.[0-9]+$'; then
        echo "gate.yml: Supabase CLI version must be one exact x.y.z (found: ${supa:-none})"; rc=1
    else
        readme="$(grep -oE 'Supabase CLI [0-9]+\.[0-9]+\.[0-9]+' README.md | head -n1 | sed 's/Supabase CLI //')"
        if [ "$readme" != "$supa" ]; then
            echo "README.md names Supabase CLI ${readme:-none}, gate.yml installs $supa"; rc=1
        else
            echo "Supabase CLI $supa in gate.yml and README.md"
        fi
    fi
    if grep -qE 'eas-cli|eas build|eas update' run.sh init.sh README.md package.json app.json; then
        echo "EAS is not used: no eas-cli, eas build or eas update may appear (no store release, #109)"; rc=1
    fi
    return $rc
}

# Every dependency is an exact x.y.z (repo-standards; the gate enforces it on commit too).
check_pins() {
    node -e '
const pkg = require("./package.json");
const all = { ...pkg.dependencies, ...pkg.devDependencies };
const bad = Object.entries(all).filter(([, v]) => !/^\d+\.\d+\.\d+$/.test(v));
if (bad.length) { console.log("Not exact pins:"); bad.forEach(([k, v]) => console.log(`  ${k} ${v}`)); process.exit(1); }
console.log(`${Object.keys(all).length} dependencies, all exact x.y.z`);
'
}

# This app is itself, not a copy of the template with the template's identifiers.
check_identity() {
    local rc=0
    grep -q '"slug": "eu27-data-sovereignty"' app.json || { echo "app.json: slug is not eu27-data-sovereignty"; rc=1; }
    grep -q '"scheme": "eu27"' app.json || { echo "app.json: scheme is not eu27"; rc=1; }
    if grep -qE 'rn-supabase|rnsupabaseapp|yourcompany' app.json package.json supabase/config.toml; then
        echo "a template placeholder is still present (rn-supabase, rnsupabaseapp, yourcompany)"; rc=1
    fi
    grep -q '^project_id = "eu27-data-sovereignty-mobile"$' supabase/config.toml || { echo "config.toml: project_id is not eu27-data-sovereignty-mobile"; rc=1; }
    [ "$rc" -eq 0 ] && echo "app.json, package.json and supabase/config.toml name this project"
    return $rc
}

# Every EXPO_PUBLIC_* variable the code reads has a line in .env.template. Names only, never values.
check_env_keys() {
    local used declared missing="" unused="" k
    used="$(grep -rhoE 'process\.env\.EXPO_PUBLIC_[A-Z0-9_]+' app src | sed 's/process\.env\.//' | sort -u)"
    declared="$(grep -oE '^EXPO_PUBLIC_[A-Z0-9_]+=' .env.template | tr -d '=' | sort -u)"
    for k in $used; do printf '%s\n' "$declared" | grep -qx "$k" || missing="$missing $k"; done
    for k in $declared; do printf '%s\n' "$used" | grep -qx "$k" || unused="$unused $k"; done
    [ -n "$unused" ] && echo "warning: in .env.template but never read:$unused"
    if [ -n "$missing" ]; then echo "Read by the code but missing from .env.template:$missing"; return 1; fi
    echo "$(printf '%s\n' "$used" | wc -l | tr -d ' ') EXPO_PUBLIC_* keys read by the code, all in .env.template"
}

# The scripts' contracts: help exits 0 with no side effects, unknown input exits non-zero.
check_scripts() {
    local rc=0
    ./run.sh help > /dev/null || { echo "./run.sh help should exit 0"; rc=1; }
    if ./run.sh no-such-command > /dev/null 2>&1; then echo "./run.sh <unknown> should exit non-zero"; rc=1; fi
    ./init.sh --help > /dev/null || { echo "./init.sh --help should exit 0"; rc=1; }
    if ./init.sh --no-such-flag > /dev/null 2>&1; then echo "./init.sh <unknown flag> should exit non-zero"; rc=1; fi
    ./test.sh --help > /dev/null || { echo "./test.sh --help should exit 0"; rc=1; }
    if ./test.sh --no-such-flag > /dev/null 2>&1; then echo "./test.sh <unknown flag> should exit non-zero"; rc=1; fi
    [ "$rc" -eq 0 ] && echo "run.sh, init.sh, test.sh: --help exits 0, unknown input exits non-zero"
    return $rc
}

# The 28 parts are generated from the committed bundle (#110): regenerate them, so the checks below run on
# the tree as a fresh checkout would have it.
check_parts() {
    python3 ../model/export_json.py --split --from ../web/public/data/eu27.json
}

# The parts on disk match the manifest, the manifest is the committed bundle's, and the site's copy is the
# app's (model/edition.py check).
check_edition() {
    python3 ../model/edition.py check --dir assets/data --bundle ../web/public/data/eu27.json \
        --site-manifest ../web/public/data/manifest.json
}

# src/constants/Colors.ts is generated by design/build_tokens.py: it must be the current tokens.
check_tokens() {
    python3 ../design/build_tokens.py --check && echo "src/constants/Colors.ts is current"
}

check_web_build() {
    npx expo export --platform web --output-dir "$LOG_DIR/web-dist"
}

require_local_supabase() {
    if ! command -v supabase > /dev/null 2>&1; then
        echo "Supabase CLI not found"; return 1
    fi
    if ! supabase status > /dev/null 2>&1; then
        echo "Local Supabase isn't running: colima start && supabase start"; return 1
    fi
}

check_integration() {
    require_local_supabase || return 1
    node scripts/integration-test.mjs
}

# --- run -----------------------------------------------------------------------------------------

printf '%bEU-27 Data Sovereignty — the mobile reader, test suite%b\n\n' "$GREEN" "$RESET"

run_step node check_node
run_step deps check_deps

if git rev-parse --is-inside-work-tree > /dev/null 2>&1; then
    run_step secrets check_secrets
else
    skip_step secrets "not a git repo"
fi

run_step shell check_shell
run_step tooling check_tooling
run_step pins check_pins
run_step identity check_identity
run_step env-keys check_env_keys
run_step scripts check_scripts
run_step format npm run format:check
run_step lint npm run lint
run_step types npm run type-check
run_step parts check_parts
run_step edition check_edition
run_step tokens check_tokens

if [ "$QUICK" -eq 1 ]; then
    run_step unit npx jest
else
    run_step unit npm run test:coverage
fi
run_step parity npx jest __tests__/parity.test.ts __tests__/security.test.ts

if [ "$QUICK" -eq 1 ]; then
    skip_step doctor "--quick"
    skip_step web-build "--quick"
    skip_step audit "--quick"
else
    if [ "$OFFLINE" -eq 1 ]; then skip_step doctor "--offline"; else run_step doctor npm run doctor; fi
    run_step web-build check_web_build
    if [ "$OFFLINE" -eq 1 ]; then skip_step audit "--offline"; else run_step audit node scripts/check-audit.mjs; fi
fi

GATE="$HOME/dev/dotfiles/security/gate.sh"
if [ "$CI_MODE" -eq 1 ]; then
    skip_step gate "--ci (CI runs the gate in its security job)"
elif [ ! -x "$GATE" ]; then
    skip_step gate "security gate not installed"
elif ! git rev-parse --is-inside-work-tree > /dev/null 2>&1; then
    skip_step gate "not a git repo"
else
    run_step gate "$GATE" scan-tree
fi

if [ "$INTEGRATION" -eq 1 ]; then
    run_step integration check_integration
else
    skip_step integration "pass --integration"
fi

# --- summary -------------------------------------------------------------------------------------

failed=0
printf '\n%b%-13s %-6s %s%b\n' "$BOLD" "STEP" "TIME" "RESULT" "$RESET"
i=0
while [ "$i" -lt "${#NAMES[@]}" ]; do
    case "${RESULTS[$i]}" in
        PASS) color="$GREEN" ;;
        FAIL) color="$RED"; failed=$((failed + 1)) ;;
        *) color="$YELLOW" ;;
    esac
    printf '%-13s %-6s %b%s%b\n' "${NAMES[$i]}" "${SECONDS_TAKEN[$i]}s" "$color" "${RESULTS[$i]}" "$RESET"
    i=$((i + 1))
done

if [ "$failed" -gt 0 ]; then
    printf '\n%b%s step(s) failed%b\n' "$RED" "$failed" "$RESET"
    exit 1
fi
printf '\n%bAll checks passed%b\n' "$GREEN" "$RESET"
