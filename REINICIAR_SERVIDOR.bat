@echo off
echo ========================================
echo   REINICIANDO SERVIDOR DJANGO
echo ========================================
echo.
cd /d "%~dp0"
echo Limpiando cache...
python manage.py collectstatic --noinput --clear
echo.
echo Iniciando servidor en http://127.0.0.1:8000
echo Presiona Ctrl+C para detener el servidor
echo.
python manage.py runserver
pause

