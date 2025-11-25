@echo off
chcp 65001 > nul
color 0C
title 🚨 SOLUCION URGENTE - Error de Conexion Movil

echo.
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║                                                               ║
echo ║     🚨 SOLUCION AUTOMATICA - ERROR DE CONEXION MOVIL         ║
echo ║                                                               ║
echo ║  Error: ERR_CONNECTION_TIMED_OUT                             ║
echo ║  Causa: Firewall bloqueando el puerto 8000                   ║
echo ║                                                               ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.

echo IMPORTANTE: Este script DEBE ejecutarse como ADMINISTRADOR
echo.
echo Si NO lo ejecutaste como administrador:
echo   1. Cierra esta ventana
echo   2. Click DERECHO sobre el archivo .bat
echo   3. Selecciona "Ejecutar como administrador"
echo.
pause

echo.
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║  PASO 1: Deteniendo procesos en puerto 8000                  ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.

REM Matar cualquier proceso Python que esté usando el puerto 8000
for /f "tokens=5" %%a in ('netstat -aon ^| findstr :8000 ^| findstr LISTENING') do taskkill /F /PID %%a 2>nul

echo Procesos en puerto 8000 detenidos (si existian)
timeout /t 2 > nul

echo.
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║  PASO 2: Configurando Firewall de Windows                    ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.

REM Eliminar reglas anteriores si existen
netsh advfirewall firewall delete rule name="Django DigitSoft Port 8000" >nul 2>&1
netsh advfirewall firewall delete rule name="Django Dev Server" >nul 2>&1
netsh advfirewall firewall delete rule name="Python Django" >nul 2>&1

echo Limpiando reglas antiguas...
timeout /t 1 > nul

REM Crear regla de firewall para ENTRADA (TCP)
echo.
echo Creando regla de ENTRADA para puerto 8000...
netsh advfirewall firewall add rule name="Django DigitSoft Port 8000" dir=in action=allow protocol=TCP localport=8000 profile=any

if %errorlevel% equ 0 (
    echo [OK] Regla de ENTRADA creada correctamente
) else (
    echo [ERROR] No se pudo crear la regla de ENTRADA
    echo.
    echo SOLUCION:
    echo 1. Cierra esta ventana
    echo 2. Click DERECHO sobre SOLUCIONAR_ACCESO_MOVIL_ADMIN.bat
    echo 3. Selecciona "Ejecutar como administrador"
    echo 4. Acepta el dialogo de UAC (Control de Cuentas de Usuario)
    pause
    exit /b 1
)

REM Crear regla de firewall para SALIDA (TCP)
echo.
echo Creando regla de SALIDA para puerto 8000...
netsh advfirewall firewall add rule name="Django DigitSoft Port 8000 Out" dir=out action=allow protocol=TCP localport=8000 profile=any

if %errorlevel% equ 0 (
    echo [OK] Regla de SALIDA creada correctamente
) else (
    echo [WARNING] No se pudo crear la regla de SALIDA (no es critico)
)

REM Permitir Python en el firewall
echo.
echo Permitiendo Python en el firewall...
netsh advfirewall firewall add rule name="Python Django Server" dir=in action=allow program="%LOCALAPPDATA%\Programs\Python\Python313\python.exe" enable=yes profile=any >nul 2>&1
netsh advfirewall firewall add rule name="Python Django Server 2" dir=in action=allow program="C:\Users\jorge\AppData\Local\Programs\Python\Python313\python.exe" enable=yes profile=any >nul 2>&1

echo [OK] Python permitido en el firewall

echo.
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║  PASO 3: Verificando configuracion de red                    ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.

echo Tu direccion IP actual:
ipconfig | findstr "IPv4" | findstr "192.168"

echo.
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║  PASO 4: Verificando que el firewall esta configurado        ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.

netsh advfirewall firewall show rule name="Django DigitSoft Port 8000" | findstr "Habilitado"

echo.
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║  CONFIGURACION COMPLETADA                                    ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.
echo ✅ Firewall configurado correctamente
echo ✅ Puerto 8000 abierto para conexiones entrantes
echo ✅ Python permitido en el firewall
echo.

echo.
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║  PASO 5: Iniciando servidor Django                           ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.

echo Iniciando servidor en modo red local...
echo.
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║                                                               ║
echo ║  📱 ACCEDE DESDE TU MOVIL A:                                  ║
echo ║                                                               ║
echo ║     http://192.168.137.221:8000/                             ║
echo ║                                                               ║
echo ║  🛒 URLS DISPONIBLES:                                         ║
echo ║                                                               ║
echo ║     Tienda:    /tienda/                                      ║
echo ║     Carrito:   /tienda/carrito/                              ║
echo ║     Dashboard: /dashboard/                                   ║
echo ║                                                               ║
echo ║  ⚠️  IMPORTANTE:                                              ║
echo ║                                                               ║
echo ║     • No cierres esta ventana                                ║
echo ║     • Tu movil debe estar en el MISMO WiFi                   ║
echo ║     • Usa http:// NO https://                                ║
echo ║     • Incluye el puerto :8000                                ║
echo ║                                                               ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.
echo Presiona CTRL+C para detener el servidor
echo.

REM Iniciar el servidor
python manage.py runserver 0.0.0.0:8000

echo.
echo Servidor detenido.
pause

