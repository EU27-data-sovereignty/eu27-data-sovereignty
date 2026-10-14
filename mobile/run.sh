#!/usr/bin/env bash
#
# The mobile reader of the EU-27 report: an Expo app that ships the fact-checked edition and reads it
# offline (#109, #110). There is no build, no store listing and no EAS here: a public release is gated on
# the verification work (DECISIONS.md #25, #50), exactly as indexing and the custom domain are.
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
    echo "  help         This message"
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
    *)          echo -e "${RED}Unknown command: $1${NC}" >&2; echo; usage; exit 1 ;;
esac
