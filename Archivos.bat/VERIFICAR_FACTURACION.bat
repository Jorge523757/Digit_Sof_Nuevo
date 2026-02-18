@echo off
echo ====================================================
echo   DIGITSOFT - VERIFICAR FACTURACION AUTOMATICA
echo   Sistema Integrado: Ventas + Compras + Facturacion
echo ====================================================
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
echo ====================================================
echo   FUNCIONALIDADES IMPLEMENTADAS:
echo.
echo   Cuando se realiza una compra del carrito:
echo   1. Se crea VENTA con usuario
echo   2. Se crea FACTURA en modulo facturacion (NUEVO)
echo   3. Se crea COMPRA con usuario
echo   4. Se actualiza inventario
echo   5. Todo con transacciones atomicas
echo.
echo   Informacion de la Factura:
echo   - Numero unico: FAC-XXXXXX
echo   - Estado: EMITIDA o BORRADOR
echo   - Fecha vencimiento: 30 dias
echo   - Asociada a venta
echo   - Observaciones detalladas
echo ====================================================
echo.
echo PARA PROBAR:
echo 1. Iniciar servidor: python manage.py runserver
echo 2. Ir a la tienda: http://127.0.0.1:8000/tienda/
echo 3. Agregar productos al carrito
echo 4. Realizar checkout
echo 5. Verificar en:
echo    - Gestion de Ventas
echo    - Facturacion (NUEVO)
echo    - Gestion de Compras
echo.
echo DOCUMENTACION:
echo - FACTURACION_AUTOMATICA.md (Guia completa)
echo - MODULO_COMPRAS_MEJORADO.md (Compras)
echo.
pause

