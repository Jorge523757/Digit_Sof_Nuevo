@echo off
pause

)
    echo.
    echo - La password de root sea correcta
    echo - MySQL este corriendo
    echo - MySQL este instalado
    echo Verifica que:
    echo.
    echo ========================================
    echo ✗ ERROR AL CREAR LA BASE DE DATOS
    echo ========================================
    echo.
) else (
    echo.
    echo 3. Crear superusuario: python manage.py createsuperuser
    echo 2. Ejecutar migraciones: python manage.py migrate
    echo 1. Instalar mysqlclient: pip install mysqlclient
    echo Proximos pasos:
    echo.
    echo - Puerto: 3306
    echo - Host: localhost
    echo - Password: digitsoft2024
    echo - Usuario: digitsoft_user
    echo - Base de datos: digitsoft_db
    echo Datos de conexion:
    echo.
    echo ========================================
    echo ✓ BASE DE DATOS CREADA EXITOSAMENTE
    echo ========================================
    echo.
if %ERRORLEVEL% EQU 0 (

mysql -u root -p < crear_database_mysql.sql
echo Ejecutando script SQL...
echo.

pause
echo.
echo - MySQL debe estar corriendo
echo - MySQL debe estar instalado
echo Requisitos:
echo.
echo Este script creara la base de datos en MySQL
echo.
echo ========================================
echo DIGITSOFT - CREAR BASE DE DATOS MYSQL
echo ========================================

