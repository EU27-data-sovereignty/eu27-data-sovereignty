#!/usr/bin/env bash
#
# One-time setup: dependencies, and an .env.local the app does not actually need.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

GREEN='\033[0;32m'; NC='\033[0m'

echo -e "${GREEN}Installing dependencies${NC} (exact pins, from package-lock.json)"
if [ -f package-lock.json ]; then npm ci; else npm install; fi

if [ ! -f .env.local ]; then
    cp .env.template .env.local
    echo -e "${GREEN}Wrote .env.local${NC} from the template. It is gitignored, and empty is fine:"
    echo "  the app renders the whole model from assets/data/eu27.json and makes no network calls."
fi

echo
echo -e "${GREEN}Ready${NC}. ./run.sh web   (or ios / android)"
