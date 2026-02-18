@echo off
echo ========================================
echo   DIGITSOFT - Iniciar Servidor
echo   Version 2.0 - Con Reportes
echo ========================================
echo.
echo Verificando sistema...
python manage.py check
echo.
if %ERRORLEVEL% EQU 0 (
    echo [OK] Sistema sin errores
    echo.
    echo Iniciando servidor en http://localhost:8000/
    echo.
    echo Presiona Ctrl+C para detener el servidor
    echo ========================================
    echo.
    python manage.py runserver
) else (
    echo [ERROR] Hay errores en el sistema
    echo Por favor revisa los mensajes arriba
    echo.
    pause
)

