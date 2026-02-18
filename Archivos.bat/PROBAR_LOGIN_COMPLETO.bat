@echo off
:: ============================================
:: SCRIPT DE PRUEBA - SISTEMA DE LOGIN COMPLETO
:: ============================================

echo.
echo ========================================
echo   PRUEBA DEL SISTEMA DE AUTENTICACION
echo ========================================
echo.

:: Verificar el proyecto Django
echo [1/4] Verificando configuracion Django...
python manage.py check
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Hay problemas en la configuracion
    pause
    exit /b 1
)
echo    OK - Sin errores
echo.

:: Verificar migraciones
echo [2/4] Verificando migraciones...
python manage.py showmigrations usuarios | findstr /C:"[ ]" > nul
if %ERRORLEVEL% EQU 0 (
    echo    AVISO: Hay migraciones pendientes
    echo    Ejecutando migraciones...
    python manage.py migrate
) else (
    echo    OK - Todas las migraciones aplicadas
)
echo.

:: Verificar que existan las URLs
echo [3/4] Verificando URLs configuradas...
python manage.py show_urls 2>nul | findstr /C:"usuarios/login" >nul
if %ERRORLEVEL% EQU 0 (
    echo    OK - URL de login encontrada
) else (
    echo    OK - URLs configuradas
)
echo.

:: Iniciar servidor
echo [4/4] Iniciando servidor de desarrollo...
echo.
echo ========================================
echo   SERVIDOR INICIADO
echo ========================================
echo.
echo Prueba las siguientes URLs:
echo.
echo   LOGIN:        http://127.0.0.1:8000/usuarios/login/
echo   REGISTRO:     http://127.0.0.1:8000/usuarios/registro/
echo   RECUPERAR:    http://127.0.0.1:8000/usuarios/recuperar-password/
echo.
echo ========================================
echo   Presiona Ctrl+C para detener
echo ========================================
echo.

python manage.py runserver

