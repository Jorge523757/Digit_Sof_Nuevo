@echo off
REM ===================================================
REM REINICIO COMPLETO DEL SERVIDOR CON LIMPIEZA
REM ===================================================

echo.
echo ===============================================
echo  DIGIT SOFT - Reinicio Completo
echo ===============================================
echo.

cd /d "%~dp0"

echo [1/4] Limpiando cache de Python...
del /s /q __pycache__\*.pyc 2>nul
del /s /q *.pyc 2>nul

echo.
echo [2/4] Limpiando y recopilando archivos estaticos...
python manage.py collectstatic --clear --noinput

echo.
echo [3/4] Verificando proyecto...
python manage.py check

echo.
echo [4/4] Iniciando servidor...
echo.
echo ===============================================
echo  IMPORTANTE: Presiona Ctrl+F5 en el navegador
echo  para limpiar la cache y recargar el CSS
echo ===============================================
echo.
echo Dashboard: http://localhost:8000/dashboard/
echo.

python manage.py runserver

pause

