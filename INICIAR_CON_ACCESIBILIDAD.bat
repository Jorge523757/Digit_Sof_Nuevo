@echo off
cd /d "%~dp0"
echo ==========================================
echo   INICIANDO SERVIDOR DJANGO
echo   con Sistema de Accesibilidad
echo ==========================================
echo.
python manage.py runserver
pause

