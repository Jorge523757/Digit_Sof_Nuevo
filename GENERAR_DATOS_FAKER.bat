@echo off
chcp 65001 >nul
title DIGIT SOFT - Generador de Datos Faker
color 0B

echo.
echo ═══════════════════════════════════════════════════════════════════
echo  DIGIT SOFT - GENERADOR DE DATOS DE PRUEBA
echo ═══════════════════════════════════════════════════════════════════
echo.
echo Este script generará datos falsos para TODOS los módulos:
echo.
echo   ✓ Clientes
echo   ✓ Productos y Categorías
echo   ✓ Proveedores
echo   ✓ Equipos
echo   ✓ Técnicos
echo   ✓ Ventas
echo   ✓ Órdenes de Servicio
echo   ✓ Garantías
echo   ✓ Compras
echo   ✓ Capacitaciones
echo.
echo ═══════════════════════════════════════════════════════════════════
echo.

echo Verificando instalación de Faker...
python -c "import faker" 2>nul
if errorlevel 1 (
    echo.
    echo ⚠️  Faker no está instalado. Instalando...
    echo.
    pip install faker
    if errorlevel 1 (
        echo.
        echo ❌ Error al instalar Faker
        pause
        exit /b 1
    )
    echo.
    echo ✅ Faker instalado correctamente
)

echo.
echo ═══════════════════════════════════════════════════════════════════
echo  INICIANDO GENERACIÓN DE DATOS...
echo ═══════════════════════════════════════════════════════════════════
echo.

python generar_datos_faker.py

echo.
echo ═══════════════════════════════════════════════════════════════════
echo.
echo Presiona cualquier tecla para cerrar...
pause >nul

