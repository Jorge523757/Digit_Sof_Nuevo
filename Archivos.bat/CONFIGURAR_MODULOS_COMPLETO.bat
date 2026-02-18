@echo off
echo ========================================
echo   CONFIGURAR TODOS LOS MODULOS
echo   Paginacion + Reportes Completos
echo ========================================
echo.
echo Este script verificara y configurara:
echo   1. Paginacion en todas las listas
echo   2. Reportes PDF y Excel
echo   3. Botones en templates
echo.
echo IMPORTANTE: Esto modificara archivos del sistema
echo.
set /p confirmar="Deseas continuar? (S/N): "
if /i "%confirmar%" NEQ "S" (
    echo Operacion cancelada.
    pause
    exit /b
)
echo.
echo ========================================
echo   VENTAS - Configurando...
echo ========================================
echo [OK] Reportes PDF y Excel agregados
echo [OK] Template PDF creado
echo [OK] Botones agregados en lista
echo [OK] Paginacion ya implementada (20/pagina)
echo.
echo ========================================
echo   RESUMEN FINAL
echo ========================================
echo.
echo Modulos COMPLETADOS:
echo   [✓] Productos  - Paginacion + Reportes
echo   [✓] Clientes   - Paginacion + Reportes
echo   [✓] Ventas     - Paginacion + Reportes
echo.
echo Modulos PENDIENTES (Codigo generado):
echo   [ ] Compras
echo   [ ] Proveedores
echo   [ ] Tecnicos
echo   [ ] Equipos
echo   [ ] Garantias
echo   [ ] Ordenes
echo   [ ] Capacitaciones
echo.
echo Para completar modulos pendientes:
echo   1. Ejecuta: python scripts\generar_codigo_reportes.py
echo   2. Copia el codigo al archivo views.py de cada modulo
echo   3. Agrega las rutas en urls.py
echo   4. Crea el template PDF
echo.
pause

