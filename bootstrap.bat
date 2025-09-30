@echo off
REM Create the virtual environment if it doesn't exist
if not exist .venv (
    echo Creating virtual environment ".venv"...
    python -m venv .venv
)

REM Activate the virtual environment
echo Activating virtual environment ".venv"...
cd .venv\Scripts

activate.bat

cd ..\..

REM You can add further commands here to run within the activated environment
REM For example, to install packages from a requirements file:

pip install -r requirements.txt

echo Virtual environment ".venv" is now active.
pause