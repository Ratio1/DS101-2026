#!/usr/bin/env bash
# Start Jupyter Lab in the DS101 homework environment (Linux / macOS).
set -euo pipefail

cd "$(dirname "$0")"

if ! command -v uv >/dev/null 2>&1; then
  echo "uv was not found. Run ./setup.sh first, then open a new terminal."
  exit 1
fi

uv run jupyter lab
