@echo off
setlocal
cd /d "%~dp0"
python chibi_warlords_game.py
if errorlevel 1 (
  py chibi_warlords_game.py
)
endlocal
