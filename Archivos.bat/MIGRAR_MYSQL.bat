@echo off
echo ========================================
echo DIGITSOFT - MIGRAR BASE DE DATOS MYSQL
echo ========================================
echo.
echo Este script ejecutara las migraciones en MySQL
echo.
pause

echo.
echo Ejecutando migraciones...
python manage.py migrate

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ========================================
    echo ✓ MIGRACIONES EJECUTADAS CORRECTAMENTE
    echo ========================================
    echo.
    echo Proximos pasos:
    echo 1. Crear superusuario: python manage.py createsuperuser
    echo 2. Iniciar servidor: python manage.py runserver
    echo.
) else (
    echo.
    echo ========================================
    echo ✗ ERROR AL EJECUTAR MIGRACIONES
    echo ========================================
    echo.
    echo Verifica que:
    echo - MySQL este corriendo
    echo - La base de datos digitsoft_db exista
    echo - mysqlclient este instalado
    echo.
)

pause

