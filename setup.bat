@echo off
title "Installing dependencies"
py -m venv venv
call venv\Scripts\activate.bat
pip install -r requirements.txt
deactivate