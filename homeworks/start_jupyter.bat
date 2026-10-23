@echo off
rem Start Jupyter Lab in the DS101 homework environment (Windows). Double-click this file.
cd /d "%~dp0"
where uv >nul 2>nul
if errorlevel 1 (
    echo uv was not found. Run setup.bat first, then open a new terminal or double-click again.
    pause
    exit /b 1
)
uv run jupyter lab
if errorlevel 1 pause
