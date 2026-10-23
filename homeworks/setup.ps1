# DS101 homework environment setup (Windows PowerShell).
# Creates homeworks\.venv with uv and registers a "DS101" Jupyter kernel.
# Run from PowerShell:  powershell -ExecutionPolicy Bypass -File setup.ps1
$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
    Write-Host "uv is not installed."
    $answer = Read-Host "Install uv now from https://astral.sh/uv ? [y/N]"
    if ($answer -match '^[Yy]$') {
        powershell -ExecutionPolicy Bypass -c "irm https://astral.sh/uv/install.ps1 | iex"
        $env:Path = "$env:USERPROFILE\.local\bin;$env:Path"
        if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
            Write-Host "uv was installed but is not on PATH yet. Close and reopen the terminal, then rerun setup."
            exit 1
        }
    } else {
        Write-Host "Install uv manually (https://docs.astral.sh/uv/) and rerun this script."
        exit 1
    }
}

Write-Host "Creating the environment in $PSScriptRoot\.venv ..."
uv sync

Write-Host "Registering the Jupyter kernel 'ds101' ..."
uv run python -m ipykernel install --user --name ds101 --display-name "DS101 (uv)"

Write-Host ""
Write-Host "Done. Start Jupyter with:"
Write-Host "  cd $PSScriptRoot; uv run jupyter lab"
Write-Host "In VS Code, pick the kernel 'DS101 (uv)' or the interpreter .venv\Scripts\python.exe."
