@echo off
chcp 65001 >nul
cls
echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║        DIGITSOFT - DIAGNÓSTICO Y CONFIGURACIÓN MYSQL         ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.

echo [1/4] Verificando si MySQL está instalado...
echo.
mysql --version 2>nul
if %ERRORLEVEL% EQU 0 (
    echo ✓ MySQL está instalado
    echo.
) else (
    echo ✗ MySQL NO está instalado
    echo.
    echo NECESITAS INSTALAR MYSQL:
    echo 1. Ve a: https://dev.mysql.com/downloads/mysql/
    echo 2. Descarga MySQL Community Server
    echo 3. Instala y configura una password de root
    echo 4. Vuelve a ejecutar este script
    echo.
    pause
    exit /b 1
)

echo [2/4] Verificando si el servicio MySQL está corriendo...
echo.
sc query MySQL80 2>nul | find "RUNNING" >nul
if %ERRORLEVEL% EQU 0 (
    echo ✓ MySQL está corriendo
    echo.
) else (
    echo ⚠ MySQL no está corriendo o tiene otro nombre
    echo.
    echo Intentando ver todos los servicios MySQL...
    sc query state= all | find "mysql" /I
    echo.
    echo Si ves un servicio MySQL arriba, puedes iniciarlo con:
    echo net start [NOMBRE_DEL_SERVICIO]
    echo.
)

echo [3/4] Verificando si mysqlclient está instalado...
echo.
pip show mysqlclient >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo ✓ mysqlclient está instalado
    pip show mysqlclient | findstr "Version"
    echo.
) else (
    echo ✗ mysqlclient NO está instalado
    echo.
    echo Intentando instalar mysqlclient...
    pip install mysqlclient
    echo.
    if %ERRORLEVEL% NEQ 0 (
        echo ✗ Error al instalar mysqlclient
        echo.
        echo SOLUCIONES:
        echo 1. Instala Visual C++ Build Tools
        echo    https://visualstudio.microsoft.com/visual-cpp-build-tools/
        echo.
        echo 2. O descarga el wheel precompilado:
        echo    https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient
        echo.
        pause
        exit /b 1
    ) else (
        echo ✓ mysqlclient instalado correctamente
        echo.
    )
)

echo [4/4] Verificando versión de Python...
echo.
python --version
echo.

echo ════════════════════════════════════════════════════════════════
echo RESUMEN:
echo ════════════════════════════════════════════════════════════════
echo.
mysql --version 2>nul && echo ✓ MySQL instalado || echo ✗ MySQL NO instalado
pip show mysqlclient >nul 2>&1 && echo ✓ mysqlclient instalado || echo ✗ mysqlclient NO instalado
echo.
echo ════════════════════════════════════════════════════════════════
echo PRÓXIMOS PASOS:
echo ════════════════════════════════════════════════════════════════
echo.
echo Si todo está ✓:
echo   1. Ejecuta: CREAR_DATABASE_MYSQL.bat
echo   2. Ejecuta: MIGRAR_MYSQL.bat
echo   3. Crea superusuario: python manage.py createsuperuser
echo   4. Inicia servidor: python manage.py runserver
echo.
echo Si algo está ✗:
echo   - Instala MySQL desde: https://dev.mysql.com/downloads/mysql/
echo   - Instala mysqlclient: pip install mysqlclient
echo.
pause

