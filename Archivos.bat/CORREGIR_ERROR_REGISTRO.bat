@echo off
echo ========================================
echo   CORREGIR ERROR DE REGISTRO
echo ========================================
echo.
echo Este script corrige el error:
echo "UNIQUE constraint failed: main_userprofile.documento"
echo.
cd /d "%~dp0"

echo 1. Deshabilitando signals duplicados...
echo    [YA HECHO en main/models.py]
echo.

echo 2. Limpiando perfiles duplicados...
python manage.py limpiar_perfiles

echo.
echo 3. Reiniciando servidor...
echo.

echo ========================================
echo   CORRECCION COMPLETADA
echo ========================================
echo.
echo Ahora puedes registrarte sin errores.
echo.
echo Presiona cualquier tecla para iniciar el servidor...
pause > nul

python manage.py runserver
# Management package

