@echo off
python --version > nul 2>&1
if %errorlevel% equ 0 (
    echo Python 3 is installed
) else (
    echo Python 3 is not installed Please download the python3 from https://www.python.org/downloads/
)
pause
