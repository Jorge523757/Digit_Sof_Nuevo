@echo off
chcp 65001 > nul
echo ========================================
echo   ORGANIZANDO DOCUMENTACION .MD
echo ========================================
echo.

cd /d "%~dp0"
python organizar_docs.py

echo.
echo ========================================
echo   ORGANIZACION COMPLETADA
echo ========================================
echo.
pause

