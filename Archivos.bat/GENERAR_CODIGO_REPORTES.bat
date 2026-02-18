@echo off
chcp 65001 > nul
echo ========================================
echo   GENERAR CODIGO DE REPORTES
echo ========================================
echo.
echo Este script generara el codigo completo de reportes
echo para TODOS los modulos pendientes:
echo.
echo   - Compras
echo   - Proveedores
echo   - Tecnicos
echo   - Equipos
echo   - Garantias
echo   - Ordenes de Servicio
echo   - Capacitaciones
echo.
echo El codigo se guardara en: CODIGO_REPORTES_COMPLETO.txt
echo.
pause
echo.
echo Generando codigo...
python scripts\generar_codigo_reportes_auto.py > CODIGO_REPORTES_COMPLETO.txt
echo.
if %ERRORLEVEL% EQU 0 (
    echo [OK] Codigo generado exitosamente
    echo.
    echo Archivo creado: CODIGO_REPORTES_COMPLETO.txt
    echo Tamanio:
    dir CODIGO_REPORTES_COMPLETO.txt | findstr "CODIGO_REPORTES"
    echo.
    echo Para usar el codigo:
    echo 1. Abre CODIGO_REPORTES_COMPLETO.txt
    echo 2. Busca el modulo que quieres implementar
    echo 3. Copia el codigo de views.py
    echo 4. Copia las rutas de urls.py
    echo 5. Copia los botones para el template
    echo 6. Crea el template PDF
    echo.
    set /p abrir="Deseas abrir el archivo ahora? (S/N): "
    if /i "%abrir%" == "S" (
        notepad CODIGO_REPORTES_COMPLETO.txt
    )
) else (
    echo [ERROR] Hubo un error al generar el codigo
)
echo.
pause

