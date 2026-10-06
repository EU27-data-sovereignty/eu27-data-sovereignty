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
#   ./test.sh --no-pdf     skip compiling the PDFs (no typst); without it, missing typst fails
#   ./test.sh --only GROUP one group: model, pdf, web or e2e (CI runs them as parallel jobs)
#   ./test.sh --only e2e --project NAME   one Playwright project (CI runs one job each)
#   PDF_OUT=dir ./test.sh  keep the compiled PDFs in dir (CI deploys exactly these)
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
SKIP_PDF=false
ONLY=""
PROJECT=""
while [ $# -gt 0 ]; do
    case "$1" in
        --no-e2e) SKIP_E2E=true ;;
        --no-pdf) SKIP_PDF=true ;;
        --only)
            ONLY="$2"; shift
            case "$ONLY" in model|pdf|web|e2e) ;; *) echo -e "${RED}❌ --only takes model, pdf, web or e2e${NC}"; exit 1 ;; esac
            ;;
        --project) PROJECT="$2"; shift ;;
        --help|-h)
            sed -n '3,18p' "$0" | sed 's/^# \{0,1\}//'
            exit 0
            ;;
        *)
            echo -e "${RED}❌ Unknown option: $1${NC}"
            exit 1
            ;;
    esac
    shift
done

# A stage runs when no group is chosen, or when it is in the chosen one. The groups partition the
# stages: running all four is exactly ./test.sh, which tests/test_workflows.py checks.
in_group() { [ -z "$ONLY" ] || [ "$ONLY" = "$1" ]; }

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

if in_group model; then
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
fi

if in_group web; then
# -----------------------------------------------------------------------------
step "The /ask function type-checks against the real SDK"
# api/ask.ts proves at compile time that the request it builds is a valid SDK request (#78).
if [ ! -d "node_modules/@anthropic-ai/sdk" ]; then
    echo -e "${RED}❌ root node_modules missing. Run npm ci in the repository root.${NC}"
    exit 1
fi
web/node_modules/.bin/tsc -p tsconfig.json
ok "api/ type-checks"
fi

if in_group model; then
# -----------------------------------------------------------------------------
step "Generated files are current"
# Regenerate with the date pinned; anything the generator *moves* is a real change
# that was not committed, which would make the published site disagree with the model.
#
# What is compared is the diff before against the diff after, not "is the tree clean".
# countries/ holds tracked binaries that are re-rendered by hand (#51), and work in
# progress under model/ is normal, so a dirty tree is not by itself a stale one --
# and a check that cries wolf on every uncommitted edit is a check people stop reading.
GENERATED_PATHS=(countries model web/public/data api/_corpus.json docs/evidence.md)
before="$(git diff -- "${GENERATED_PATHS[@]}" | shasum)"
python3 model/generate_countries.py > /dev/null
python3 model/export_json.py > /dev/null
python3 model/ask_corpus.py > /dev/null
python3 model/evidence_report.py > /dev/null
after="$(git diff -- "${GENERATED_PATHS[@]}" | shasum)"
if [ "$before" != "$after" ]; then
    echo -e "${RED}    ❌ Generated files are stale: regenerating changed them. Run ./run.sh data and commit.${NC}"
    git diff --stat -- "${GENERATED_PATHS[@]}"
    exit 1
fi
ok "briefs, CSVs and bundle match the model"

# -----------------------------------------------------------------------------
step "Admission reproduces the committed registers"
# Research then vetting admission, re-run on the committed evidence, must change nothing: the
# registers a reader sees follow from the staged findings, verification rows and tier table (#84).
python3 model/reproduce.py admit-check
ok "registers reproduce from the committed evidence"

step "Fact-check ledger and audit file reproduce"
# The fact-check ledger must rebuild from the committed staged verdicts, run by run in recorded order,
# and docs/fact-check-audit.md from the ledger (#87). Whether every printed fact passes is the deploy
# gate's job (factcheck.py gate), not this one's, so a branch with unchecked changes still passes here.
python3 model/factcheck.py replay
python3 model/factcheck.py audit --check
ok "fact-check ledger reproduces from the staged runs; audit file current"
fi

if { in_group web || in_group e2e; } && [ ! -d "web/node_modules" ]; then
    echo -e "${RED}❌ web/node_modules missing. Run ./init.sh first.${NC}"
    exit 1
fi

# -----------------------------------------------------------------------------
if ! in_group pdf; then
    :
elif [ "$SKIP_PDF" = true ]; then
    echo
    echo -e "${YELLOW}⚠️  Skipping the PDF stage (--no-pdf)${NC}"
else
    step "The EU-27 report and 27 country PDFs compile"
    # Exactly what the deploy builds (vercel.json buildCommand), so a template error fails here and
    # not halfway through a production deploy (#81). A typst error passed the whole gate once.
    if ! command -v typst &> /dev/null; then
        echo -e "${RED}    ❌ typst is not installed (brew install typst), or pass --no-pdf${NC}"
        exit 1
    fi
    if [ -n "$PDF_OUT" ]; then
        PDF_DIR="$PDF_OUT"
        mkdir -p "$PDF_DIR"
    else
        PDF_DIR="$(mktemp -d)"
        trap 'rm -rf "$PDF_DIR"' EXIT
    fi
    python3 book/report.py -o "$PDF_DIR" > /dev/null
    pdfs=$(find "$PDF_DIR" -name '*.pdf' -size +1k | wc -l | tr -d ' ')
    if [ "$pdfs" != 28 ]; then
        echo -e "${RED}    ❌ expected 28 PDFs, found $pdfs${NC}"
        exit 1
    fi
    # The compiled PDFs, not just their source (#82, #88, #92): disclaimer, both appendices, the country
    # named, every font embedded, a size budget, and the report previews. Needs poppler (CI installs it).
    if command -v pdftotext &> /dev/null && command -v pdffonts &> /dev/null; then
        python3 book/check_pdfs.py "$PDF_DIR"
    else
        echo -e "${YELLOW}    ⚠️  poppler (pdftotext, pdffonts) not installed: compiled PDFs not inspected${NC}"
    fi
    ok "28 PDFs compiled and inspected: disclaimer, appendices, fonts, size; 4 previews"
fi

if in_group web; then
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

step "Size budget"
# What a reader downloads, gzipped (#92): the data bundle (826 KB on 2026-10-02) and all JavaScript (342 KB,
# 236 KB of it the map outline). Raising a budget is a decision with its reason, like a coverage floor.
python3 - <<'PY'
import gzip, pathlib, sys
budget = {"data bundle": (pathlib.Path("public/data/eu27.json"), 900_000),
          "JavaScript": (sorted(pathlib.Path("dist/assets").glob("*.js")), 400_000)}
over = []
for name, (paths, limit) in budget.items():
    paths = paths if isinstance(paths, list) else [paths]
    size = sum(len(gzip.compress(p.read_bytes(), 9)) for p in paths)
    print(f"    {name}: {size / 1000:.0f} KB gzipped of {limit / 1000:.0f} KB")
    if size > limit:
        over.append(name)
sys.exit(1 if over else 0)
PY
ok "data bundle and JavaScript within their gzipped budgets"

cd "$ROOT"
fi

# -----------------------------------------------------------------------------
if ! in_group e2e; then
    :
elif [ "$SKIP_E2E" = true ]; then
    echo
    echo -e "${YELLOW}⚠️  Skipping browser stage (--no-e2e)${NC}"
else
    step "End-to-end, accessibility and rendered-data assertions"
    cd web
    if [ -n "$PROJECT" ]; then
        npx playwright test --project "$PROJECT"
    else
        npx playwright test
    fi
    ok "routes render real data; no accessibility violations"
    cd "$ROOT"
fi

# -----------------------------------------------------------------------------
echo
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
if [ -n "$ONLY" ]; then
    echo -e "${GREEN}✅ All checks in the ${ONLY}${PROJECT:+ ($PROJECT)} group passed${NC}"
    exit 0
fi
echo -e "${GREEN}✅ All checks passed${NC}"
echo
echo -e "${YELLOW}Note:${NC} passing does not mean the data is verified."
echo "  $(python3 model/sources.py 2>/dev/null | tail -1)"
echo "The unsourced legal and regulatory entries are still one researcher's reading of"
echo "public policy documents — see DECISIONS.md #25 for the gate that must pass before"
echo "the site is indexed or announced, and VERIFICATION.md for how it is closed."
