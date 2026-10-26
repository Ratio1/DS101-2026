# DS101 homeworks

There is one folder per lecture. Each folder has a homework notebook, a solution notebook and the data they use.

| Folder | Topic |
|---|---|
| `lecture_2/` | Data, EDA and the Pharma-style RFM case: inspection, data quality, RFM features, k-means, t-SNE, text features, embeddings preview |

All notebooks share one Python environment. [uv](https://docs.astral.sh/uv/) creates it in
`homeworks/.venv` from `pyproject.toml` and `uv.lock`. You set it up once.

## Windows

### Quick setup

1. Open the `homeworks` folder in File Explorer.
2. Double-click **`setup.bat`**.
   - If uv is missing, the script asks whether to install it. Type `y` and press Enter.
   - If it then says *"uv was installed but is not on PATH yet"*, close the window and double-click `setup.bat` again.
3. Wait for **Done**. The first run downloads Python packages and can take a few minutes.

### Start Jupyter

Double-click **`start_jupyter.bat`**. Jupyter Lab opens in your browser.
Open `lecture_2/practice.ipynb`. Keep the black window open while you work. Close it to stop Jupyter.

### Manual setup (PowerShell)

```powershell
# 1. Install uv (one time)
powershell -ExecutionPolicy Bypass -c "irm https://astral.sh/uv/install.ps1 | iex"
# 2. Close and reopen PowerShell, then:
cd path\to\DS101-2026\homeworks
uv sync
uv run python -m ipykernel install --user --name ds101 --display-name "DS101 (uv)"
# 3. Start Jupyter
uv run jupyter lab
```

## Linux / macOS

### Quick setup

```bash
cd homeworks
./setup.sh
```

The script installs uv if you agree, runs `uv sync`, and registers the Jupyter kernel **DS101 (uv)**.

### Start Jupyter

```bash
cd homeworks
./start_jupyter.sh      # same as: uv run jupyter lab
```

### Manual setup

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh    # 1. install uv, then open a new terminal
cd homeworks
uv sync                                            # 2. create .venv
uv run python -m ipykernel install --user --name ds101 --display-name "DS101 (uv)"
uv run jupyter lab                                 # 3. start Jupyter
```

## VS Code

1. Install the **Python** and **Jupyter** extensions.
2. Run the setup above once.
3. Open a notebook and click **Select Kernel** in the top-right corner.
4. Choose **DS101 (uv)**, or choose the Python interpreter
   `homeworks/.venv/bin/python` (Linux/macOS) or `homeworks\.venv\Scripts\python.exe` (Windows).

## How to work on a homework

1. Open `lecture_N/practice.ipynb`. The walkthrough cells already show their outputs.
2. Run the notebook from the top (**Run > Run All Cells**). Your outputs should match the saved ones.
3. Solve the tasks in the **Homework** section at the end.
4. Compare with `practice_solution.ipynb` only after you have tried each task yourself.

## Troubleshooting

| Problem | Fix |
|---|---|
| `uv` is not recognized / command not found | Close and reopen the terminal after installing uv. On Windows, double-click `setup.bat` again. |
| *"running scripts is disabled on this system"* | Use `setup.bat` instead of `setup.ps1`. It bypasses the policy for this one script only. |
| Notebook says `ModuleNotFoundError` | The wrong kernel is selected. Choose **DS101 (uv)** (see VS Code above), or start Jupyter with `start_jupyter`. |
| Download fails on a university or company network | Set the proxy first, then run setup **in the same window**: `set HTTPS_PROXY=http://proxy:port` then `setup.bat` (Windows cmd), `$env:HTTPS_PROXY="http://proxy:port"` then `.\setup.bat` (PowerShell), or `export HTTPS_PROXY=http://proxy:port` (Linux/macOS). Double-clicking `setup.bat` does not see the proxy. |
| `FileNotFoundError: data/...` | Open the notebook from its own `lecture_N` folder. Jupyter runs each notebook from its folder. |
| Something is broken and you want a clean start | Delete `homeworks/.venv` and run setup again. |

## For instructors: add a package

```bash
cd homeworks
uv add <package>
```

This updates `pyproject.toml` and `uv.lock`. Commit both files.
