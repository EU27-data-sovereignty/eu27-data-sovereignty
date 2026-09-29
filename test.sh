#!/bin/bash
set -e

# =============================================================================
# EU-27 Sovereign Data Centers — full test gate
# =============================================================================
# Runs everything and stops at the first failure, cheapest checks first so a
# problem surfaces in seconds rather than minutes.
#
#   ./test.sh              everything
#   ./test.sh --no-e2e     skip the browser stage (no Chrome, or CI without one)
#
# Exit 0 = safe to publish. Anything else = do not.

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

SKIP_E2E=false
for arg in "$@"; do
    case "$arg" in
        --no-e2e) SKIP_E2E=true ;;
        --help|-h)
            sed -n '3,14p' "$0" | sed 's/^# \{0,1\}//'
            exit 0
            ;;
        *)
            echo -e "${RED}❌ Unknown option: $arg${NC}"
            exit 1
            ;;
    esac
done

STEP=0
step() {
    STEP=$((STEP + 1))
    echo
    echo -e "${BLUE}[$STEP] $1${NC}"
}
ok() { echo -e "${GREEN}    ✅ $1${NC}"; }

# The date stamped into generated files, kept in one place so init/run/test agree.
# Pinned so regeneration is byte-reproducible: a diff then shows real changes rather
# than today's date in 27 files.
export SOURCE_DATE_EPOCH="$(cat "$ROOT/.build-epoch")"

echo -e "${GREEN}Running the full test gate${NC}"

# -----------------------------------------------------------------------------
step "Python model and data integrity"
python3 -m unittest discover -s tests -q
ok "model, CSV integrity, referential integrity, determinism, ledger and fetch manifest"

# -----------------------------------------------------------------------------
step "Verification ledger"
# tests/test_sources.py already enforces this inside step 1; printing the table here
# puts the number in front of whoever runs the gate. Coverage is the project's real
# blocker (DECISIONS.md #25), and a blocker nobody sees is a blocker nobody works on.
python3 model/sources.py
ok "ledger is valid"

# -----------------------------------------------------------------------------
step "National data register"
# Same reasoning as the ledger above: the coverage number goes in front of whoever runs
# the gate. 1053 = 39 critical holding classes x 27 member states (#73).
python3 model/national_data.py | tail -4
ok "register is valid"

# -----------------------------------------------------------------------------
step "Every fact shown is sourced"
# DECISIONS.md #75: a fact in any document must carry a claim that a checked citation supports.
# An unsourced value is a gap, never a fact. This is the gate the author asked for: unimpeachable.
python3 model/document.py --check
ok "every fact in all 27 documents resolves to a checked source"

# -----------------------------------------------------------------------------
step "The /ask function type-checks against the real SDK"
# api/ask.ts proves at compile time that the request it builds is a valid SDK request (#78).
if [ ! -d "node_modules/@anthropic-ai/sdk" ]; then
    echo -e "${RED}❌ root node_modules missing. Run npm ci in the repository root.${NC}"
    exit 1
fi
web/node_modules/.bin/tsc -p tsconfig.json
ok "api/ type-checks"

# -----------------------------------------------------------------------------
step "Generated files are current"
# Regenerate with the date pinned; anything the generator *moves* is a real change
# that was not committed, which would make the published site disagree with the model.
#
# What is compared is the diff before against the diff after, not "is the tree clean".
# countries/ holds tracked binaries that are re-rendered by hand (#51), and work in
# progress under model/ is normal, so a dirty tree is not by itself a stale one --
# and a check that cries wolf on every uncommitted edit is a check people stop reading.
GENERATED_PATHS=(countries model web/public/data api/_corpus.json)
before="$(git diff -- "${GENERATED_PATHS[@]}" | shasum)"
python3 model/generate_countries.py > /dev/null
python3 model/export_json.py > /dev/null
python3 model/ask_corpus.py > /dev/null
after="$(git diff -- "${GENERATED_PATHS[@]}" | shasum)"
if [ "$before" != "$after" ]; then
    echo -e "${RED}    ❌ Generated files are stale: regenerating changed them. Run ./run.sh data and commit.${NC}"
    git diff --stat -- "${GENERATED_PATHS[@]}"
    exit 1
fi
ok "briefs, CSVs and bundle match the model"

# -----------------------------------------------------------------------------
if [ ! -d "web/node_modules" ]; then
    echo -e "${RED}❌ web/node_modules missing. Run ./init.sh first.${NC}"
    exit 1
fi
cd web

step "TypeScript types"
npm run --silent type-check
ok "tsc --noEmit clean"

step "Lint"
npm run --silent lint
ok "eslint clean"

step "Formatting"
npm run --silent format:check
ok "prettier clean"

step "Unit tests and TS/Python parity"
npm run --silent test
ok "unit tests pass"

step "Production build"
npm run --silent build
ok "build succeeded"

cd "$ROOT"

# -----------------------------------------------------------------------------
if [ "$SKIP_E2E" = true ]; then
    echo
    echo -e "${YELLOW}⚠️  Skipping browser stage (--no-e2e)${NC}"
else
    step "End-to-end, accessibility and rendered-data assertions"
    cd web
    npx playwright test
    ok "routes render real data; no accessibility violations"
    cd "$ROOT"
fi

# -----------------------------------------------------------------------------
echo
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}✅ All checks passed${NC}"
echo
echo -e "${YELLOW}Note:${NC} passing does not mean the data is verified."
echo "  $(python3 model/sources.py 2>/dev/null | tail -1)"
echo "The unsourced legal and regulatory entries are still one researcher's reading of"
echo "public policy documents — see DECISIONS.md #25 for the gate that must pass before"
echo "publishing to a custom domain or print, and VERIFICATION.md for how it is closed."
