@echo off
chcp 65001 >nul
cls
echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║        DIGITSOFT - CREAR BASE DE DATOS MYSQL                 ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.

set MYSQL_PATH=C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe

echo Verificando MySQL...
if exist "%MYSQL_PATH%" (
    echo ✓ MySQL encontrado
    echo.
) else (
    echo ✗ MySQL no encontrado en la ruta predeterminada
    echo.
    echo Por favor, ingresa la ruta completa de mysql.exe
    echo Ejemplo: C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe
    echo.
    set /p MYSQL_PATH="Ruta de mysql.exe: "
)

echo.
echo Creando base de datos digitsoft_db...
echo.
echo Por favor ingresa la password de root de MySQL:
echo.

"%MYSQL_PATH%" -u root -p < crear_database_mysql.sql

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ╔══════════════════════════════════════════════════════════════╗
    echo ║        ✓ BASE DE DATOS CREADA EXITOSAMENTE                  ║
    echo ╚══════════════════════════════════════════════════════════════╝
    echo.
    echo Datos de conexión:
    echo ───────────────────────────────────────────────────────────────
    echo Base de datos: digitsoft_db
    echo Usuario:       digitsoft_user
    echo Password:      digitsoft2024
    echo Host:          localhost
    echo Puerto:        3306
    echo.
    echo ╔══════════════════════════════════════════════════════════════╗
    echo ║        PRÓXIMOS PASOS                                        ║
    echo ╚══════════════════════════════════════════════════════════════╝
    echo.
    echo 1. Ejecutar migraciones:
    echo    python manage.py migrate
    echo.
    echo 2. Crear superusuario:
    echo    python manage.py createsuperuser
    echo.
    echo 3. Iniciar servidor:
    echo    python manage.py runserver
    echo.
) else (
    echo.
    echo ╔══════════════════════════════════════════════════════════════╗
    echo ║        ✗ ERROR AL CREAR LA BASE DE DATOS                    ║
    echo ╚══════════════════════════════════════════════════════════════╝
    echo.
    echo Verifica que:
    echo - MySQL esté corriendo (services.msc)
    echo - La password de root sea correcta
    echo - El usuario root tenga permisos
    echo.
)

pause

