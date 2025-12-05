@echo off
echo ========================================
echo   GENERAR DATOS FALSOS - DIGITSOFT
echo ========================================
echo.
echo Este script generara datos de prueba para:
echo   - Productos (80)
echo   - Clientes (50)
echo   - Proveedores (25)
echo   - Tecnicos (20)
echo   - Equipos (60)
echo   - Garantias (35)
echo   - Ordenes de Servicio (45)
echo   - Ventas (60)
echo   - Compras (40)
echo   - Capacitaciones (25)
echo.
echo ADVERTENCIA: Esto agregara muchos registros a tu base de datos
echo.
set /p confirmar="Deseas continuar? (S/N): "
if /i "%confirmar%" NEQ "S" (
    echo Operacion cancelada.
    pause
    exit /b
)
echo.
echo Generando datos...
echo.
python scripts\generar_datos_faker.py
echo.
echo ========================================
echo   PROCESO COMPLETADO
echo ========================================
echo.
pause

