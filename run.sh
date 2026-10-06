#!/bin/bash
set -e

# =============================================================================
# EU-27 Sovereign Data Centers — development runner
# =============================================================================

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

print_info()    { echo -e "${BLUE}ℹ️  $1${NC}"; }
print_success() { echo -e "${GREEN}✅ $1${NC}"; }
print_warning() { echo -e "${YELLOW}⚠️  $1${NC}"; }
print_error()   { echo -e "${RED}❌ $1${NC}"; }

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

# The date stamped into generated files, kept in one place so init/run/test agree.
# Pinned so regeneration is byte-reproducible: a diff then shows real changes rather
# than today's date in 27 files.
export SOURCE_DATE_EPOCH="$(cat "$ROOT/.build-epoch")"

check_deps() {
    if [ ! -d "$ROOT/web/node_modules" ]; then
        print_error "Dependencies not installed. Run ./init.sh first."
        exit 1
    fi
}

show_help() {
    echo -e "${GREEN}EU-27 Sovereign Data Centers${NC}"
    echo
    echo "Usage: ./run.sh [command]"
    echo
    echo -e "${GREEN}Develop${NC}"
    echo "  dev, start       Start the dev server (default)"
    echo "  build            Production build"
    echo "  preview          Serve the production build"
    echo "  site             What vercel build runs (vercel.json); PREBUILT_SITE=1 ships the gate's build"
    echo
    echo -e "${GREEN}Quality${NC}"
    echo "  test             Full test gate (delegates to ./test.sh)"
    echo "  test:watch       Vitest in watch mode"
    echo "  lint             ESLint"
    echo "  lint:fix         ESLint with auto-fix"
    echo "  format           Prettier write"
    echo "  format:check     Prettier check"
    echo "  type-check       tsc --noEmit"
    echo
    echo -e "${GREEN}Data and artefacts${NC}"
    echo "  data             Regenerate country CSVs, briefs and the JSON bundle"
    echo "  artefacts        Re-render the tracked posters and briefing PDFs (needs Chrome)"
    echo "  export           EU-27 report + 27 country PDFs (book/build/, from the content model)"
    echo "  book             Typeset the paper book"
    echo "  sources          Verification-ledger coverage report"
    echo "  registers        Critical national data register coverage report"
    echo "  fetch [what]     Fetch source documents into cache/ (eurostat | legal | all)"
    echo
    echo -e "${GREEN}Evidence (docs/vetting.md; each step is one command)${NC}"
    echo "  admit [--check]  Admit verified research, then vetting; --check proves the registers reproduce"
    echo "  recheck          Re-fetch every source behind a printed fact (resumable)"
    echo "  retry            Retry not-found quotes (served page in its charset, then rendered), then admit"
    echo "  eurostat check   Pull at the pinned periods and report; writes nothing"
    echo "  eurostat adopt COL=PERIOD ...   Move pins, apply, register the vintage"
    echo "  vet prepare|stage|hosts|verify|admit|report   The vetting run (the agent step is /vet)"
    echo "  contrib forms|ingest|status|audit-sample   Citizen submissions and the two-person rule"
    echo "  factcheck prepare|stage|record|audit|status|gate   Cross-model fact check (agent step: /factcheck)"
    echo "  reproduce [--evidence]   Rebuild everything in a fresh clone and compare"
    echo
    echo -e "${GREEN}Deployment${NC}"
    echo "  deploy           Run the full gate, then deploy to Vercel production"
    echo
    echo -e "${GREEN}Housekeeping${NC}"
    echo "  clean            Remove build artefacts"
    echo "  health           Versions, data freshness, tool availability"
    echo "  help             This message"
}

regen_data() {
    # The same pinned date the gate uses (#34), so `data` and `./test.sh` agree byte for byte.
    # Bump .build-epoch deliberately when a release should carry a new date.
    export SOURCE_DATE_EPOCH="$(cat "$ROOT/.build-epoch")"
    print_info "Regenerating model outputs..."
    python3 model/generate_countries.py > /dev/null
    python3 model/export_json.py
    python3 model/ask_corpus.py > /dev/null
    python3 model/evidence_report.py > /dev/null
    python3 model/gaps.py > /dev/null                 # what is missing, and how hard it was looked for
    python3 model/factcheck.py audit > /dev/null      # reads the bundle just written (#87)
    print_success "Country files, briefs, bundle, /ask corpus, docs/evidence.md, docs/gaps.md and docs/fact-check-audit.md regenerated"
}

case "${1:-dev}" in
    dev|start)
        check_deps
        print_info "Starting dev server on http://localhost:5173"
        cd web && npm run dev
        ;;
    build)
        check_deps
        regen_data
        (cd web && npm run build)
        # Briefs go into dist/, never into web/public/ — public/ is committed and these
        # are regenerable binaries. Skipped rather than fatal when typst is absent.
        if command -v typst &> /dev/null; then
            python3 book/report.py -o web/dist > /dev/null
            print_success "Built to web/dist/ (EU-27 report and 27 country PDFs at /report/<ISO>.pdf)"
        else
            print_warning "typst missing — built without the PDFs"
            print_success "Built to web/dist/"
        fi
        ;;
    site)
        # vercel.json's buildCommand: what `vercel build` runs to produce web/dist (#71, #81). The root
        # node_modules are for api/ (the /ask function). In deploy.yml PREBUILT_SITE=1: web/dist is then
        # the build the gate tested, with the 28 PDFs its PDF job compiled and inspected, so it is checked
        # and shipped, never rebuilt (docs/process.md, optimisation 1).
        npm ci
        if [ "${PREBUILT_SITE:-}" = 1 ]; then
            if [ ! -f web/dist/index.html ]; then
                print_error "PREBUILT_SITE=1, but web/dist has no index.html"
                exit 1
            fi
            pdfs=$(find web/dist -name '*.pdf' -size +1k | wc -l | tr -d ' ')
            if [ "$pdfs" != 28 ]; then
                print_error "PREBUILT_SITE=1, but web/dist has $pdfs PDFs, not 28"
                exit 1
            fi
            print_success "Shipping the gate's build: web/dist with 28 PDFs"
        else
            (cd web && npm ci && npm run build)
            python3 book/report.py -o web/dist
        fi
        ;;
    preview)
        check_deps
        cd web && npm run preview
        ;;
    test)
        exec "$ROOT/test.sh" "${@:2}"
        ;;
    test:watch)
        check_deps
        cd web && npm run test:watch
        ;;
    lint)         check_deps; cd web && npm run lint ;;
    lint:fix)     check_deps; cd web && npm run lint:fix ;;
    format)       check_deps; cd web && npm run format ;;
    format:check) check_deps; cd web && npm run format:check ;;
    type-check)   check_deps; cd web && npm run type-check ;;
    data)
        regen_data
        ;;
    artefacts)
        # The tracked countries/<ISO>/ infographic poster (#24, #51). The Chrome briefing PDF
        # is retired (#76); the per-country PDF comes from `export`.
        check_deps
        python3 model/export_artifacts.py "${@:2}"
        ;;
    export)
        # The EU-27 report and the 27 country PDFs from the content model (#74, #75).
        python3 book/report.py "${@:2}" && python3 book/report.py --countries "${@:2}"
        ;;
    sources)
        python3 model/sources.py "${@:2}"
        ;;
    registers)
        # The critical national data register: which Tier 0/Tier 1 records each state holds
        # and the official page describing each. Stdlib only, like `sources` -- no check_deps.
        python3 model/national_data.py "${@:2}"
        ;;
    fetch)
        # Stdlib only, like `sources` -- no check_deps. Writes into cache/, which is
        # gitignored AND .vercelignored; only the manifest and the pull are tracked.
        case "${2:-all}" in
            eurostat) python3 model/fetch_eurostat.py "${@:3}" ;;
            legal)    python3 model/fetch_sources.py "${@:3}" ;;
            all)
                python3 model/fetch_eurostat.py
                echo
                python3 model/fetch_sources.py
                ;;
            *) print_error "fetch: expected eurostat, legal or all"; exit 1 ;;
        esac
        ;;
    admit)
        # Always both, in this order: vetting may supersede or dispute what research admitted.
        if [ "${2:-}" = "--check" ]; then
            python3 model/reproduce.py admit-check
        else
            python3 model/reproduce.py admit      # from the base, research then vetting (#84)
        fi
        ;;
    recheck)
        python3 model/research.py recheck "${@:2}"
        ;;
    retry)
        python3 model/research.py verify --rendered && python3 model/reproduce.py admit
        ;;
    eurostat)
        case "${2:-check}" in
            check) python3 model/fetch_eurostat.py --check ;;
            adopt) python3 model/fetch_eurostat.py --adopt "${@:3}" ;;
            *) print_error "usage: ./run.sh eurostat check | adopt COL=PERIOD ..."; exit 1 ;;
        esac
        ;;
    vet)
        python3 model/vetting.py "${@:2}"
        ;;
    contrib)
        # Citizen submissions and reviews (#85): forms | ingest | status | audit-sample
        python3 model/contrib.py "${@:2}"
        ;;
    factcheck)
        # Every printed fact checked by the model that did not write it (#87):
        # prepare | stage | record | audit | status | gate
        python3 model/factcheck.py "${@:2}"
        ;;
    reproduce)
        python3 model/reproduce.py clean-room "${@:2}"
        ;;
    deploy)
        # The manual fallback. Normally a push to main deploys through
        # .github/workflows/deploy.yml (#81); this does the same from this machine.
        # It refuses to ship anything that is not the committed state of main and
        # has not passed the gate.
        if [ -n "$(git status --porcelain)" ]; then
            print_error "Working tree is dirty. Commit first — deploy ships the tree, not the last commit."
            git status --short
            exit 1
        fi
        branch="$(git rev-parse --abbrev-ref HEAD)"
        if [ "$branch" != "main" ]; then
            print_error "On branch '$branch'. Production deploys come from main."
            exit 1
        fi
        if ! command -v vercel &> /dev/null; then
            print_error "The Vercel CLI is not installed. Install with: npm i -g vercel"
            exit 1
        fi
        print_info "Running the full gate before deploying..."
        "$ROOT/test.sh" "${@:2}"
        echo
        # Every printed fact needs a current, agreeing verdict from the model that did not
        # write it, and docs/fact-check-audit.md must be current (#87). Run /factcheck first.
        print_info "Fact-check gate..."
        python3 model/factcheck.py gate
        echo
        # cache/ can be hundreds of MB of fetched gazettes. .vercelignore excludes it,
        # but .vercelignore is read INSTEAD of .gitignore, so the rule is easy to lose.
        if [ -d "$ROOT/cache" ] && ! grep -q '^cache/$' "$ROOT/.vercelignore"; then
            print_error ".vercelignore does not exclude cache/ — the fetched corpus would upload."
            exit 1
        fi
        # Built here, uploaded prebuilt: the PDFs need typst, which Vercel's build image
        # does not have (DECISIONS.md #71). vercel build runs vercel.json's buildCommand
        # locally into .vercel/output; only that output is uploaded.
        for tool in typst; do
            if ! command -v "$tool" &> /dev/null; then
                print_error "$tool is not installed — the PDFs cannot be built. brew install $tool"
                exit 1
            fi
        done
        print_info "Building for production..."
        vercel build --prod --yes
        print_info "Deploying to production..."
        vercel deploy --prebuilt --prod
        print_success "Deployed. robots.txt still disallows indexing until the verification gate passes."
        ;;
    book)
        if ! command -v typst &> /dev/null; then
            print_error "typst is not installed. Install with: brew install typst"
            exit 1
        fi
        print_info "Typesetting the book..."
        python3 book/build.py "${@:2}"
        ;;
    clean)
        print_info "Cleaning build artefacts..."
        rm -rf web/dist web/coverage web/test-results web/playwright-report
        find . -name '__pycache__' -type d -prune -exec rm -rf {} + 2>/dev/null || true
        print_success "Clean"
        ;;
    health)
        echo -e "${GREEN}Environment${NC}"
        echo "  python3   $(python3 --version 2>&1 | awk '{print $2}')"
        echo "  node      $(node -v 2>/dev/null || echo 'missing')"
        echo "  npm       $(npm -v 2>/dev/null || echo 'missing')"
        echo "  typst     $(typst --version 2>/dev/null | awk '{print $2}' || echo 'missing (book only)')"
        echo
        echo -e "${GREEN}Data${NC}"
        if git diff --quiet -- countries model web/public/data 2>/dev/null; then
            print_success "No uncommitted changes under countries/, model/ or the bundle"
        else
            # Not necessarily stale: re-rendered artefacts and work in progress look
            # the same here. ./test.sh distinguishes them by regenerating and seeing
            # whether anything moves.
            print_warning "Uncommitted changes present — ./test.sh says whether they are stale"
        fi
        echo "  countries $(find countries -maxdepth 1 -mindepth 1 -type d | wc -l | tr -d ' ')"
        echo "  bundle    $(du -h web/public/data/eu27.json 2>/dev/null | cut -f1 || echo 'missing')"
        echo
        echo -e "${GREEN}Verification${NC} (the gate on indexing, the domain and the book)"
        python3 model/sources.py 2>/dev/null | tail -1 | sed 's/^/  /' 
        ;;
    help|--help|-h)
        show_help
        ;;
    *)
        print_error "Unknown command: $1"
        echo
        show_help
        exit 1
        ;;
esac
