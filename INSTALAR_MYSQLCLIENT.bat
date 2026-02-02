@echo off
echo ========================================
echo DIGITSOFT - INSTALAR MYSQLCLIENT
echo ========================================
echo.
echo Este script instalara el conector de MySQL para Python
echo.
pause

echo.
echo Instalando mysqlclient...
pip install mysqlclient

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ========================================
    echo ✓ MYSQLCLIENT INSTALADO CORRECTAMENTE
    echo ========================================
    echo.
    echo Proximos pasos:
    echo 1. Crear la base de datos: CREAR_DATABASE_MYSQL.bat
    echo 2. Ejecutar migraciones: MIGRAR_MYSQL.bat
    echo.
) else (
    echo.
    echo ========================================
    echo ✗ ERROR AL INSTALAR MYSQLCLIENT
    echo ========================================
    echo.
    echo Si aparece error de compilacion, descarga e instala:
    echo https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient
    echo.
    echo O instala Visual C++ Build Tools:
    echo https://visualstudio.microsoft.com/visual-cpp-build-tools/
    echo.
)

pause

