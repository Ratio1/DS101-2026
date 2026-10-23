@echo off
rem DS101 homework environment setup (Windows). Double-click this file.
rem It runs setup.ps1 without changing your PowerShell execution policy.
cd /d "%~dp0"
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0setup.ps1"
if errorlevel 1 (
    echo.
    echo Setup failed. Read the message above, or see homeworks\README.md - Troubleshooting.
)
pause
