@echo off
chcp 65001 >nul
title E-commerce Digit Soft - Servidor
color 0A

echo.
echo ═══════════════════════════════════════════════
echo   🛒 DIGIT SOFT - E-COMMERCE
echo ═══════════════════════════════════════════════
echo.

cd /d "%~dp0"

echo [1/4] Verificando Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ ERROR: Python no está instalado
    pause
    exit /b 1
)
echo ✅ Python instalado correctamente
echo.

echo [2/4] Verificando base de datos...
if not exist "db.sqlite3" (
    echo ⚠️  Base de datos no encontrada
    echo Ejecutando migraciones...
    python manage.py migrate
    if errorlevel 1 (
        echo ❌ Error al crear la base de datos
        pause
        exit /b 1
    )
)
echo ✅ Base de datos lista
echo.

echo [3/4] Limpiando archivos temporales...
if exist "*.pyc" del /S /Q "*.pyc" >nul 2>&1
if exist "__pycache__" rd /S /Q "__pycache__" >nul 2>&1
echo ✅ Limpieza completada
echo.

echo [4/4] Iniciando servidor Django...
echo.
echo ═══════════════════════════════════════════════
echo   ✅ SERVIDOR INICIADO
echo ═══════════════════════════════════════════════
echo.
echo 📍 URL del E-commerce:
echo    http://127.0.0.1:8000/tienda/
echo.
echo 📍 URL del Dashboard:
echo    http://127.0.0.1:8000/dashboard/
echo.
echo 📍 URL del Admin:
echo    http://127.0.0.1:8000/admin/
echo.
echo ⚠️  IMPORTANTE: NO CIERRES ESTA VENTANA
echo    El servidor debe estar corriendo para que funcione
echo.
echo 🛑 Para detener el servidor: Ctrl+C
echo ═══════════════════════════════════════════════
echo.

:: Abrir el navegador automáticamente después de 2 segundos
timeout /t 2 /nobreak >nul
start http://127.0.0.1:8000/tienda/

:: Iniciar el servidor
python manage.py runserver 0.0.0.0:8000

pause
