@echo off
echo ===============================================
echo   DIGITSOFT - VERIFICAR MODULO DE COMPRAS
echo   Version Mejorada con Usuario
echo ===============================================
echo.

cd /d "%~dp0"

echo [1/2] Verificando sistema...
python manage.py check
if errorlevel 1 (
    echo.
    echo [ERROR] Hay errores en el sistema
    pause
    exit /b 1
)

echo.
echo [2/2] Sistema verificado correctamente
echo.
echo ===============================================
echo   MEJORAS IMPLEMENTADAS:
echo   - Campo usuario en Compras
echo   - Campo usuario en Ventas
echo   - Registro automatico desde carrito
echo   - Transacciones atomicas
echo   - Trazabilidad completa
echo ===============================================
echo.
echo Para probar:
echo 1. Iniciar servidor: python manage.py runserver
echo 2. Ir a la tienda: http://127.0.0.1:8000/tienda/
echo 3. Agregar productos al carrito
echo 4. Realizar checkout
echo 5. Verificar en Gestion de Compras
echo.
pause

