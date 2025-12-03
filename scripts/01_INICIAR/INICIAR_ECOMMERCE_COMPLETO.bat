@echo off
echo ========================================
echo   INICIANDO SISTEMA DE E-COMMERCE
echo   CARRITO Y FACTURACION COMPLETO
echo ========================================
echo.

cd /d "%~dp0"

echo Verificando servidor Django...
python manage.py check

if errorlevel 1 (
    echo.
    echo ERROR: Hay problemas con la configuracion
    pause
    exit /b 1
)

echo.
echo ========================================
echo   Servidor iniciando en:
echo   http://127.0.0.1:8000
echo.
echo   URLs principales:
echo   - Tienda: http://127.0.0.1:8000/tienda/
echo   - Carrito: http://127.0.0.1:8000/tienda/carrito/
echo   - Dashboard: http://127.0.0.1:8000/dashboard/
echo ========================================
echo.

python manage.py runserver

pause

