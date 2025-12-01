@echo off
echo ====================================================================
echo   SOLUCION AUTOMATICA - Acceso desde Movil a DigitSoft
echo ====================================================================
echo.
echo Este script va a:
echo 1. Configurar el Firewall de Windows para permitir el puerto 8000
echo 2. Iniciar el servidor Django en modo red local
echo.
echo IMPORTANTE: Debes ejecutar esto como ADMINISTRADOR
echo (Click derecho sobre el archivo - Ejecutar como administrador)
echo.
pause

echo.
echo ====================================================================
echo   PASO 1: Configurando Firewall de Windows
echo ====================================================================
echo.

REM Eliminar regla anterior si existe
netsh advfirewall firewall delete rule name="Django DigitSoft Port 8000" >nul 2>&1

REM Crear nueva regla para permitir conexiones entrantes en puerto 8000
echo Creando regla de firewall para puerto 8000...
netsh advfirewall firewall add rule name="Django DigitSoft Port 8000" dir=in action=allow protocol=TCP localport=8000

if %errorlevel% equ 0 (
    echo [OK] Regla de firewall creada exitosamente
) else (
    echo [ERROR] No se pudo crear la regla. Ejecuta como Administrador.
    echo.
    echo Como ejecutar como Administrador:
    echo 1. Click derecho sobre este archivo .bat
    echo 2. Selecciona "Ejecutar como administrador"
    echo 3. Acepta el dialogo de UAC
    pause
    exit /b 1
)

echo.
echo ====================================================================
echo   PASO 2: Verificando configuracion de red
echo ====================================================================
echo.

echo Tus direcciones IP disponibles:
ipconfig | findstr "IPv4"

echo.
echo ====================================================================
echo   PASO 3: Iniciando servidor Django
echo ====================================================================
echo.

echo Servidor iniciando en modo red local...
echo.
echo ACCESO DESDE TU MOVIL:
echo.
echo   URL Principal: http://192.168.137.221:8000/
echo   Tienda:        http://192.168.137.221:8000/tienda/
echo   Carrito:       http://192.168.137.221:8000/tienda/carrito/
echo.
echo IMPORTANTE:
echo   - Tu movil debe estar en el MISMO WiFi
echo   - No cierres esta ventana
echo   - Presiona CTRL+C para detener el servidor
echo.
echo ====================================================================
echo   SERVIDOR ACTIVO
echo ====================================================================
echo.

python manage.py runserver 0.0.0.0:8000

pause

