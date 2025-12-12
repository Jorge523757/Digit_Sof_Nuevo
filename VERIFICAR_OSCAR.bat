@echo off
echo ================================================================
echo VERIFICACION DE OSCAR ALVAREZ
echo ================================================================
echo.
echo Este script verificara si Oscar Alvarez fue creado correctamente
echo como tecnico en la base de datos.
echo.
echo ================================================================
echo.

cd /d "%~dp0"

python manage.py shell < verificar_oscar.py

echo.
echo ================================================================
echo VERIFICACION COMPLETADA
echo ================================================================
echo.
pause

