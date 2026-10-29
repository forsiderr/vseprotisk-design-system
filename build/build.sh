#!/usr/bin/env bash
# Build + contract test: tokens -> _variables.scss -> compile check.
set -euo pipefail
cd "$(dirname "$0")/.."

echo "[1/3] generate _variables.scss from tokens…"
python3 build/generate.py

echo "[2/3] compile-check SCSS (dart-sass if available)…"
if node_modules/.bin/sass >/dev/null 2>&1 || [ -x node_modules/.bin/sass ]; then
  node_modules/.bin/sass dist/_variables.scss dist/_contract.check.css --no-source-map
  rm -f dist/_contract.check.css
  echo "      ok — SCSS is syntactically valid"
else
  echo "      (dart-sass not installed; run: npm i -D sass)" >&2
fi

echo "[3/3] done. Paste dist/_variables.scss into the Upgates custom-variables slot."
