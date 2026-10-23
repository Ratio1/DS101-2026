#!/usr/bin/env bash
# DS101 homework environment setup (Linux / macOS).
# Creates homeworks/.venv with uv and registers a "DS101" Jupyter kernel.
set -euo pipefail

cd "$(dirname "$0")"

if ! command -v uv >/dev/null 2>&1; then
  echo "uv is not installed."
  read -r -p "Install uv now from https://astral.sh/uv ? [y/N] " answer
  if [[ "${answer}" =~ ^[Yy]$ ]]; then
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.local/bin:$PATH"
    if ! command -v uv >/dev/null 2>&1; then
      echo "uv was installed but is not on PATH yet. Open a new terminal and rerun ./setup.sh."
      exit 1
    fi
  else
    echo "Install uv manually (https://docs.astral.sh/uv/) and rerun this script."
    exit 1
  fi
fi

echo "Creating the environment in $(pwd)/.venv ..."
uv sync

echo "Registering the Jupyter kernel 'ds101' ..."
uv run python -m ipykernel install --user --name ds101 --display-name "DS101 (uv)"

echo
echo "Done. Start Jupyter with:"
echo "  cd $(pwd) && uv run jupyter lab"
echo "In VS Code, pick the kernel 'DS101 (uv)' or the interpreter .venv/bin/python."
