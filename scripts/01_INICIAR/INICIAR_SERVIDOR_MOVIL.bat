@echo off
chcp 65001 > nul
color 0A
title 🚀 DigitSoft - Servidor Red Local (Móvil)

echo.
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║  🌐 DIGIT SOFT - Servidor en Red Local                        ║
echo ║  📱 Acceso desde Teléfono/Tablet habilitado                   ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.

echo 🔍 Detectando tus direcciones IP...
echo.

REM Mostrar todas las IPs disponibles
ipconfig | findstr /C:"IPv4"

echo.
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║  📱 ACCESO DESDE TU TELÉFONO:                                 ║
echo ║                                                               ║
echo ║  🔹 OPCIÓN 1 - Red Ethernet (si estás con cable):            ║
echo ║     http://192.168.1.56:8000/                                ║
echo ║                                                               ║
echo ║  🔹 OPCIÓN 2 - Red WiFi:                                     ║
echo ║     http://192.168.137.221:8000/                             ║
echo ║                                                               ║
echo ║  📱 RUTAS DISPONIBLES:                                        ║
echo ║     🏠 Inicio:     /                                         ║
echo ║     🛒 Tienda:     /tienda/                                  ║
echo ║     🛒 Carrito:    /tienda/carrito/                          ║
echo ║     📊 Dashboard:  /dashboard/                               ║
echo ║                                                               ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.

echo 💡 Acceso Local (desde esta PC):
echo    🌐 http://localhost:8000/
echo    🌐 http://127.0.0.1:8000/
echo.

echo ⚠️  IMPORTANTE:
echo    • Conecta tu teléfono a la MISMA red WiFi o red local
echo    • El firewall debe permitir el puerto 8000
echo    • No cierres esta ventana mientras uses el servidor
echo.

echo 💡 TIP: Ejecuta GUIA_CONEXION_COMPLETA.bat para más info
echo.

echo ⏳ Iniciando servidor en 3 segundos...
timeout /t 3 > nul

echo.
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║  🚀 SERVIDOR ACTIVO - Presiona CTRL+C para detener           ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.

REM Iniciar servidor
python manage.py runserver 0.0.0.0:8000

pause

