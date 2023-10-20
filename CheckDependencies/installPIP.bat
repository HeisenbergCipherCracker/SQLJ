@echo off
set "get_pip_script=get-pip.py"

rem Download get-pip.py
curl https://bootstrap.pypa.io/get-pip.py -o %get_pip_script% >nul 2>&1

rem Install pip
python %get_pip_script% >nul 2>&1

rem Check if pip is installed
python -m pip --version >nul 2>&1
if %errorlevel% equ 0 (
    echo pip is installed
) else (
    echo pip installation failed
)

rem Clean up get-pip.py
del %get_pip_script%