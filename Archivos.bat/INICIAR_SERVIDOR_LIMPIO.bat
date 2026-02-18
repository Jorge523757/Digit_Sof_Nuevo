@echo off
cls
echo ========================================
echo   REINICIANDO SERVIDOR - DIGT SOFT
echo ========================================
echo.
echo Deteniendo procesos de Python...
taskkill /F /IM python.exe 2>nul
timeout /t 2 >nul

cd /d "%~dp0"

echo.
echo Verificando el proyecto...
python manage.py check

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: Hay problemas en el proyecto.
    echo Revisa los errores arriba.
    pause
    exit /b 1
)

echo.
echo ========================================
echo   INICIANDO SERVIDOR
echo ========================================
echo.
echo Servidor iniciado en: http://127.0.0.1:8000
echo.
echo URLs importantes:
echo   - Login:      http://127.0.0.1:8000/usuarios/login/
echo   - Dashboard:  http://127.0.0.1:8000/dashboard/
echo   - Admin:      http://127.0.0.1:8000/admin/
echo   - Usuarios:   http://127.0.0.1:8000/usuarios/gestionar/
echo.
echo Presiona Ctrl+C para detener el servidor
echo ========================================
echo.

python manage.py runserver

pause

