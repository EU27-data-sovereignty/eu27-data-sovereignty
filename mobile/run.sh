#!/usr/bin/env bash
#
# The Expo reader, local only. There is no build, no store listing and no deploy here:
# `build`, `update` and the EAS commands the template ships were removed rather than left
# to rot, because a public release is gated on the verification work (DECISIONS.md #25)
# exactly as indexing and the custom domain are. See ROADMAP.md, "Later — a mobile reader".
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

GREEN='\033[0;32m'; NC='\033[0m'

check_deps() {
    if [ ! -d node_modules ]; then
        echo "node_modules/ is missing. Run ./init.sh first." >&2
        exit 1
    fi
}

usage() {
    echo -e "${GREEN}Usage${NC}: ./run.sh [command]"
    echo
    echo "  start        Expo dev server (default)"
    echo "  ios          Open in the iOS simulator"
    echo "  android      Open in the Android emulator"
    echo "  web          Open in a browser (react-native-web)"
    echo "  test         Jest, plus the dependency audit"
    echo "  lint         ESLint"
    echo "  type-check   tsc --noEmit"
    echo "  format       Prettier --write"
    echo "  help         This message"
}

case "${1:-start}" in
    start)      check_deps; npx expo start ;;
    ios)        check_deps; npx expo start --ios ;;
    android)    check_deps; npx expo start --android ;;
    web)        check_deps; npx expo start --web ;;
    test)
        check_deps
        npx jest "${@:2}"
        # The allowlist in __tests__/security.test.ts keeps the dependency set small; this
        # keeps the small set current. Pinned versions are what make the result meaningful.
        npm audit --audit-level=high
        ;;
    lint)       check_deps; npx expo lint ;;
    type-check) check_deps; npx tsc --noEmit ;;
    format)     check_deps; npx prettier --write . ;;
    help|-h|--help) usage ;;
    *)          echo "Unknown command: $1" >&2; echo; usage; exit 1 ;;
esac
