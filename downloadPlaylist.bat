@echo off

echo Activating virtual environment...
call venv\Scripts\activate.bat
echo Virtual environment activated.

echo.

echo Running playlist.py...
py Scripts\playlist.py

pause
deactivate