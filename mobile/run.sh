#!/usr/bin/env bash
#
# The mobile reader of the EU-27 report: an Expo app that ships the fact-checked edition and reads it
# offline (#109, #110). It is built, sent to TestFlight and uploaded to App Store Connect by the release
# workflow on EAS (.eas/workflows/release.yml, #114), which the deploy's `app` job starts after the site's
# gate; the commands below run the same steps by hand with the pinned CLI in node_modules. "Submit for
# Review" and "Release" stay clicks in App Store Connect: the launch gate (DECISIONS.md #25, #67).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

GREEN='\033[0;32m'; YELLOW='\033[1;33m'; RED='\033[0;31m'; NC='\033[0m'

check_deps() {
    if [ ! -f package.json ] || [ ! -d node_modules ]; then
        echo -e "${RED}node_modules/ is missing. Run ./init.sh first.${NC}" >&2
        exit 1
    fi
}

# The 28 parts are generated from the committed bundle and gitignored (#110): Metro cannot bundle
# the app until they exist. Cheap (about a second) and idempotent.
ensure_parts() {
    if [ ! -f assets/data/eu27.core.json ]; then
        echo -e "${YELLOW}Generating the split edition into assets/data/ ...${NC}"
        python3 ../model/export_json.py --split --from ../web/public/data/eu27.json
    fi
}

# Only the commands that start the app read .env.local, and only the URL's shape: the anon key is never
# read or printed. No .env.local is fine: the app then reads its bundled edition and makes no request.
check_env_file() {
    if [ ! -f .env.local ]; then
        echo -e "${YELLOW}No .env.local: the app runs with no edition channel (offline, bundled edition only).${NC}"
        return 0
    fi
    local url
    url="$(sed -n -E 's/^EXPO_PUBLIC_SUPABASE_URL=["'"'"']?([^"'"'"']*).*/\1/p' .env.local | head -n1)"
    case "$url" in
        "") echo -e "${YELLOW}EXPO_PUBLIC_SUPABASE_URL is empty in .env.local: no edition channel.${NC}" ;;
        *supabase.com/dashboard*)
            echo -e "${RED}EXPO_PUBLIC_SUPABASE_URL is a dashboard URL. The app needs the API URL:${NC}"
            echo -e "   https://<project-ref>.supabase.co, or http://127.0.0.1:54321 for the local stack"
            exit 1 ;;
        http://127.0.0.1*|http://localhost*)
            if ! curl -s -f "${url%/}/storage/v1/version" > /dev/null 2>&1 && ! supabase status > /dev/null 2>&1; then
                echo -e "${YELLOW}.env.local points at the local stack, which is not running (colima start; supabase start).${NC}"
            fi ;;
    esac
}

usage() {
    echo -e "${GREEN}Usage${NC}: ./run.sh [command]"
    echo
    echo "  start        Expo dev server (default)"
    echo "  ios          Open in the iOS simulator"
    echo "  android      Open in the Android emulator"
    echo "  web          Open in a browser (react-native-web)"
    echo "  prod         Dev server with a production JS bundle (minified, no dev tools)"
    echo "  debug        Dev server with verbose Expo logging"
    echo "  parts        Regenerate the 28 parts of the edition from ../web/public/data/eu27.json"
    echo "  test         Every check (test.sh; add --quick, --integration, --offline)"
    echo "  lint         ESLint and the Prettier check"
    echo "  format       Prettier --write and ESLint --fix"
    echo "  type-check   tsc --noEmit"
    echo "  doctor       expo-doctor"
    echo "  supabase     The local stack's status"
    echo
    echo "  release              Run the release workflow on EAS (.eas/workflows/release.yml); owner approval in the dashboard"
    echo "  release record <id>  Append an EAS build to releases.csv (model/release.py)"
    echo "  build ios|android    One production build on EAS, by hand (eas build --profile production)"
    echo "  update <message>     Publish the JavaScript to the production channel (eas update)"
    echo "  metadata push|pull   The App Store listing (store.config.json); push needs EAS_REVIEW_EMAIL and EAS_REVIEW_PHONE"
    echo "  eas <args>           The pinned EAS CLI (eas.json cli.version), e.g. ./run.sh eas login, ./run.sh eas credentials"
    echo "  help                 This message"
}

# The EAS CLI is not a project dependency (expo-doctor refuses that); it runs as `npx eas-cli@<exact>`, the
# one version pinned in eas.json's cli.version, which the CLI itself enforces, as the Vercel CLI does in
# ../.github/workflows/deploy.yml (#114).
EAS="eas-cli@$(node -p 'require("./eas.json").cli.version')"
eas() { npx --yes "$EAS" "$@"; }

# Every EAS command needs an account: a login session (eas login) or EXPO_TOKEN in the environment (CI).
require_eas_account() {
    if [ -z "${EXPO_TOKEN:-}" ] && ! eas whoami > /dev/null 2>&1; then
        echo -e "${RED}Not logged in to EAS: run './run.sh eas login', or set EXPO_TOKEN (CI).${NC}" >&2
        exit 1
    fi
}

require_review_contact() {
    if [ -z "${EAS_REVIEW_EMAIL:-}" ] || [ -z "${EAS_REVIEW_PHONE:-}" ]; then
        echo -e "${RED}EAS_REVIEW_EMAIL and EAS_REVIEW_PHONE must be set: Apple's review contact, never in the tree.${NC}" >&2
        exit 1
    fi
}

case "${1:-start}" in
    help|-h|--help) usage; exit 0 ;;
esac
check_deps

case "${1:-start}" in
    start)      check_env_file; ensure_parts; npx expo start ;;
    ios)        check_env_file; ensure_parts; npx expo start --ios ;;
    android)    check_env_file; ensure_parts; npx expo start --android ;;
    web)        check_env_file; ensure_parts; npx expo start --web ;;
    prod)       check_env_file; ensure_parts; npx expo start --no-dev --minify ;;
    debug)      check_env_file; ensure_parts; EXPO_DEBUG=1 npx expo start ;;
    parts)      python3 ../model/export_json.py --split --from ../web/public/data/eu27.json ;;
    test)       shift; exec ./test.sh "$@" ;;
    lint)       npm run lint; npx prettier --check . ;;
    format)     npm run format; npm run lint -- --fix ;;
    type-check) npm run type-check ;;
    doctor)     npm run doctor ;;
    supabase)   supabase status ;;
    release)
        shift
        case "${1:-run}" in
            run)    require_eas_account; eas workflow:run .eas/workflows/release.yml ;;
            record) [ -n "${2:-}" ] || { echo -e "${RED}Usage: ./run.sh release record <eas-build-id>${NC}" >&2; exit 1; }
                    require_eas_account; python3 ../model/release.py record --dir . --ledger releases.csv --build "$2" ;;
            *)      echo -e "${RED}Unknown release command: $1${NC}" >&2; exit 1 ;;
        esac ;;
    build)
        case "${2:-}" in
            ios|android) require_eas_account; eas build --platform "$2" --profile "${3:-production}" ;;
            *) echo -e "${RED}Usage: ./run.sh build ios|android [profile]${NC}" >&2; exit 1 ;;
        esac ;;
    update)
        [ -n "${2:-}" ] || { echo -e "${RED}Usage: ./run.sh update <message>${NC}" >&2; exit 1; }
        require_eas_account; eas update --channel production --message "$2" ;;
    metadata)
        case "${2:-}" in
            push) require_eas_account; require_review_contact; eas metadata:push --profile production ;;
            pull) require_eas_account; eas metadata:pull --profile production ;;
            lint) EAS_REVIEW_EMAIL="$(printf 'lint%sexample.invalid' @)" EAS_REVIEW_PHONE='+00 0' eas metadata:lint --profile production ;;
            *) echo -e "${RED}Usage: ./run.sh metadata push|pull|lint${NC}" >&2; exit 1 ;;
        esac ;;
    eas)        shift; eas "$@" ;;
    *)          echo -e "${RED}Unknown command: $1${NC}" >&2; echo; usage; exit 1 ;;
esac
