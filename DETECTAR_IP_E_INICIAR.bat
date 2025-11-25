@echo off
chcp 65001 > nul
color 0E
title 🌐 DigitSoft - Detectar IP y Configurar Acceso Móvil

echo.
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║                                                               ║
echo ║     🌐 DETECTOR AUTOMÁTICO DE IP - DIGIT SOFT                ║
echo ║                                                               ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.

echo IMPORTANTE: Ejecutar como ADMINISTRADOR
echo.
pause

echo.
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║  🔍 DETECTANDO CONFIGURACIÓN DE RED                          ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.

REM Detectar IP activa
for /f "tokens=2 delims=:" %%a in ('ipconfig ^| findstr /C:"IPv4" ^| findstr /V "127.0.0.1"') do (
    set IP_RAW=%%a
    set IP_RAW=!IP_RAW:~1!

    REM Verificar si es una IP válida de red local
    echo !IP_RAW! | findstr /R "^192\.168\.[0-9]*\.[0-9]*$" >nul
    if !errorlevel! equ 0 (
        echo ✅ IP DETECTADA: !IP_RAW!
        set IP_ACTIVA=!IP_RAW!
    )
)

if not defined IP_ACTIVA (
    echo ❌ ERROR: No se detectó ninguna IP de red local activa
    echo.
    echo Tu configuración actual:
    ipconfig | findstr /C:"IPv4"
    echo.
    echo PROBLEMA DETECTADO:
    echo Tu PC no está conectada a ninguna red WiFi o Ethernet
    echo.
    echo SOLUCIONES:
    echo 1. Conecta tu PC a una red WiFi
    echo 2. O conecta un cable Ethernet
    echo 3. O activa el hotspot móvil en tu PC
    echo.
    pause
    exit /b 1
)

echo.
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║  ✅ CONFIGURACIÓN DE RED DETECTADA                           ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.

REM Mostrar toda la información de red
ipconfig | findstr /C:"Adaptador" /C:"IPv4" /C:"Puerta de enlace"

echo.
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║  🔧 CONFIGURANDO FIREWALL                                     ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.

REM Limpiar reglas anteriores
netsh advfirewall firewall delete rule name="Django DigitSoft Port 8000" >nul 2>&1
netsh advfirewall firewall delete rule name="Django DigitSoft Port 8000 Out" >nul 2>&1
netsh advfirewall firewall delete rule name="Python Django Server" >nul 2>&1

echo Limpiando reglas antiguas...
timeout /t 1 > nul

REM Crear reglas de firewall
echo.
echo Creando reglas de firewall para puerto 8000...

netsh advfirewall firewall add rule name="Django DigitSoft Port 8000" dir=in action=allow protocol=TCP localport=8000 profile=any
if %errorlevel% equ 0 (
    echo [OK] Regla de entrada creada
) else (
    echo [ERROR] No se pudo crear regla - Ejecuta como ADMINISTRADOR
    pause
    exit /b 1
)

netsh advfirewall firewall add rule name="Django DigitSoft Port 8000 Out" dir=out action=allow protocol=TCP localport=8000 profile=any >nul 2>&1

REM Permitir Python
where python >nul 2>&1
if %errorlevel% equ 0 (
    for /f "delims=" %%i in ('where python') do (
        netsh advfirewall firewall add rule name="Python Django Server" dir=in action=allow program="%%i" enable=yes profile=any >nul 2>&1
    )
)

echo [OK] Firewall configurado correctamente

echo.
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║  📱 INFORMACIÓN PARA TU MÓVIL                                 ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.
echo TU IP ACTIVA ES: !IP_ACTIVA!
echo.
echo ┌─────────────────────────────────────────────────────────────┐
echo │                                                             │
echo │  🌐 ACCEDE DESDE TU MÓVIL A:                                │
echo │                                                             │
echo │     http://!IP_ACTIVA!:8000/                                │
echo │                                                             │
echo │  📱 URLs COMPLETAS:                                         │
echo │                                                             │
echo │     Inicio:    http://!IP_ACTIVA!:8000/                     │
echo │     Tienda:    http://!IP_ACTIVA!:8000/tienda/              │
echo │     Carrito:   http://!IP_ACTIVA!:8000/tienda/carrito/      │
echo │     Dashboard: http://!IP_ACTIVA!:8000/dashboard/           │
echo │                                                             │
echo └─────────────────────────────────────────────────────────────┘
echo.
echo ⚠️  IMPORTANTE:
echo    • Tu móvil debe estar en el MISMO WiFi/Red que tu PC
echo    • Usa http:// NO https://
echo    • Incluye el puerto :8000
echo.

REM Crear archivo con la URL para referencia
echo http://!IP_ACTIVA!:8000/ > URL_PARA_MOVIL.txt
echo http://!IP_ACTIVA!:8000/tienda/ >> URL_PARA_MOVIL.txt
echo. >> URL_PARA_MOVIL.txt
echo Creado: URL_PARA_MOVIL.txt con las URLs >> URL_PARA_MOVIL.txt

echo.
echo ✅ Se creó el archivo "URL_PARA_MOVIL.txt" con las URLs
echo.

echo ╔═══════════════════════════════════════════════════════════════╗
echo ║  🚀 INICIANDO SERVIDOR DJANGO                                ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.

echo Iniciando servidor en 0.0.0.0:8000...
echo (Aceptará conexiones desde cualquier IP de la red)
echo.
echo PRESIONA CTRL+C PARA DETENER EL SERVIDOR
echo.

REM Iniciar servidor
python manage.py runserver 0.0.0.0:8000

echo.
echo Servidor detenido.
pause

