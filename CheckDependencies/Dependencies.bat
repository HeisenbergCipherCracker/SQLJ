@echo off

rem Check if Python 3 is installed
python -c "import sys" >nul 2>&1
if %errorlevel% neq 0 (
    echo Python 3 is not installed,please downlaod from: https://www.python.org/downloads/
    rem Add code to install Python 3 here, such as downloading the installer and running it
)

rem Check if pip is installed
python -m pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo pip is not installed, installing...
    rem Add code to install pip here, such as downloading get-pip.py and running it
)

rem Check if required libraries are installed
set "missing_libraries="
for %%i in (colorama re asyncio math requests os sys time) do (
    python -c "import %%i" >nul 2>&1
    if %errorlevel% neq 0 (
        set "missing_libraries=!missing_libraries! %%i"
    )
)

if "%missing_libraries%"=="" (
    echo All libraries are installed
) else (
    echo Missing libraries:%missing_libraries%
)