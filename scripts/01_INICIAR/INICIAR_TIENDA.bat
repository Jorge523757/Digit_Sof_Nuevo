@echo off
echo ========================================
echo   INICIANDO TIENDA DIGIT SOFT
echo   Vista Estilo E-commerce
echo ========================================
echo.

REM Verificar que estamos en el directorio correcto
if not exist "manage.py" (
    echo ERROR: No se encuentra manage.py
    echo Por favor ejecuta este script desde el directorio del proyecto
    pause
    exit /b 1
)

echo [1/3] Verificando archivos necesarios...
if exist "templates\ecommerce\productos_estilo_exito.html" (
    echo   ✓ Template HTML encontrado
) else (
    echo   ✗ Template HTML no encontrado
)

if exist "static\css\productos-exito.css" (
    echo   ✓ CSS encontrado
) else (
    echo   ✗ CSS no encontrado
)

if exist "static\js\productos-exito.js" (
    echo   ✓ JavaScript encontrado
) else (
    echo   ✗ JavaScript no encontrado
)

if exist "ecommerce_views.py" (
    echo   ✓ Vistas encontradas
) else (
    echo   ✗ Vistas no encontradas
)

echo.
echo [2/3] Recolectando archivos estáticos...
python manage.py collectstatic --noinput --clear

echo.
echo [3/3] Iniciando servidor de desarrollo...
echo.
echo ========================================
echo   SERVIDOR INICIADO
echo ========================================
echo.
echo   URL Principal: http://localhost:8000/
echo   Tienda Nueva:  http://localhost:8000/ecommerce/tienda/
echo.
echo   Presiona Ctrl+C para detener el servidor
echo.
echo ========================================
echo.

REM Iniciar el servidor
python manage.py runserver

pause

