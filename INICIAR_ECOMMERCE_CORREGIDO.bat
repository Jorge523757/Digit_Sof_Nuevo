@echo off
echo =====================================
echo   INICIAR E-COMMERCE - DIGIT SOFT
echo =====================================
echo.

cd /d "%~dp0"

echo [1/3] Verificando ambiente...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no esta instalado
    pause
    exit /b 1
)
echo OK: Python instalado

echo.
echo [2/3] Verificando base de datos...
if not exist "db.sqlite3" (
    echo Base de datos no encontrada. Ejecutando migraciones...
    python manage.py migrate
)
echo OK: Base de datos lista

echo.
echo [3/3] Iniciando servidor Django...
echo.
echo ======================================
echo   SERVIDOR INICIADO
echo ======================================
echo.
echo Abre tu navegador en:
echo.
echo    http://127.0.0.1:8000/tienda/
echo.
echo Para detener el servidor presiona Ctrl+C
echo.
echo ======================================
echo.

python manage.py runserver 0.0.0.0:8000

