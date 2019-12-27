@echo off
title Installing dependencies

echo Creating virtual environment...
py -m venv venv
echo Virtual environment created.

echo.

echo Activating virtual environment...
call venv\Scripts\activate.bat
echo Virtual environment activated

echo.

echo Installing requirements...
pip install -r requirements.txt
echo Requirements installed

echo.
echo First part of setup completed.
echo.

py Scripts\setup.py

echo.
echo Setup completed.
pause

deactivate