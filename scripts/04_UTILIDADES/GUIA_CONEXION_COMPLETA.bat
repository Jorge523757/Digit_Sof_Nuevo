@echo off
chcp 65001 > nul
color 0B
title 🌐 DigitSoft - Guía de Conexión Completa

echo.
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║           🌐 DIGIT SOFT - GUÍA DE CONEXIÓN                   ║
echo ║        Cómo conectar desde cualquier dispositivo             ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.

echo 📍 TUS DIRECCIONES IP DISPONIBLES:
echo.
echo    1️⃣  CONEXIÓN ETHERNET (Cable):
echo        IP: 192.168.1.56
echo        Red: 192.168.1.x
echo.
echo    2️⃣  CONEXIÓN WiFi:
echo        IP: 192.168.137.221
echo        Red: 192.168.137.x
echo.
echo    3️⃣  LOCALHOST (solo esta PC):
echo        IP: 127.0.0.1 o localhost
echo.

echo ╔═══════════════════════════════════════════════════════════════╗
echo ║  🖥️  ACCESO DESDE ESTA COMPUTADORA:                           ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.
echo    🌐 http://localhost:8000/
echo    🌐 http://127.0.0.1:8000/
echo    🌐 http://192.168.1.56:8000/  (Ethernet)
echo    🌐 http://192.168.137.221:8000/  (WiFi)
echo.

echo ╔═══════════════════════════════════════════════════════════════╗
echo ║  📱 ACCESO DESDE TELÉFONO/TABLET:                            ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.
echo    OPCIÓN 1 - Red Ethernet (192.168.1.x):
echo    ───────────────────────────────────────
echo    🔹 Asegúrate que tu teléfono esté en la misma red
echo    🔹 Abre el navegador
echo    🔹 Accede a:
echo.
echo       🏠 Inicio:     http://192.168.1.56:8000/
echo       🛒 Tienda:     http://192.168.1.56:8000/tienda/
echo       🛒 Carrito:    http://192.168.1.56:8000/tienda/carrito/
echo       📊 Dashboard:  http://192.168.1.56:8000/dashboard/
echo       🔐 Login:      http://192.168.1.56:8000/usuarios/login/
echo.
echo.
echo    OPCIÓN 2 - Red WiFi (192.168.137.x):
echo    ────────────────────────────────────
echo    🔹 Conecta tu teléfono a la misma WiFi
echo    🔹 Abre el navegador
echo    🔹 Accede a:
echo.
echo       🏠 Inicio:     http://192.168.137.221:8000/
echo       🛒 Tienda:     http://192.168.137.221:8000/tienda/
echo       🛒 Carrito:    http://192.168.137.221:8000/tienda/carrito/
echo       📊 Dashboard:  http://192.168.137.221:8000/dashboard/
echo       🔐 Login:      http://192.168.137.221:8000/usuarios/login/
echo.

echo ╔═══════════════════════════════════════════════════════════════╗
echo ║  💻 ACCESO DESDE OTRA COMPUTADORA EN LA RED:                 ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.
echo    Si la PC está en la red Ethernet (192.168.1.x):
echo       → http://192.168.1.56:8000/
echo.
echo    Si la PC está en la red WiFi (192.168.137.x):
echo       → http://192.168.137.221:8000/
echo.

echo ╔═══════════════════════════════════════════════════════════════╗
echo ║  ⚙️  CONFIGURACIÓN Y REQUISITOS:                              ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.
echo    ✅ Servidor debe estar corriendo:
echo       python manage.py runserver 0.0.0.0:8000
echo.
echo    ✅ Firewall de Windows:
echo       • Debe permitir conexiones entrantes en puerto 8000
echo       • Ve a: Panel de Control ^> Firewall ^> Configuración avanzada
echo       • Crea regla entrante para puerto 8000
echo.
echo    ✅ Dispositivos en la misma red:
echo       • Teléfono/Tablet debe estar en la MISMA WiFi
echo       • O en la misma red Ethernet si es posible
echo.
echo    ✅ ALLOWED_HOSTS configurado:
echo       • Ya está configurado para aceptar todas las conexiones
echo.

echo ╔═══════════════════════════════════════════════════════════════╗
echo ║  🔧 COMANDOS ÚTILES:                                          ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.
echo    Ver tus IPs:
echo       ipconfig
echo.
echo    Iniciar servidor (red local):
echo       python manage.py runserver 0.0.0.0:8000
echo.
echo    Verificar puerto 8000 abierto:
echo       netstat -an ^| findstr :8000
echo.
echo    Crear regla de firewall (como Admin):
echo       netsh advfirewall firewall add rule name="Django Dev Server" ^
echo       dir=in action=allow protocol=TCP localport=8000
echo.

echo ╔═══════════════════════════════════════════════════════════════╗
echo ║  🆘 SOLUCIÓN DE PROBLEMAS:                                    ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.
echo    ❌ "No se puede conectar":
echo       1. Verifica que el servidor esté corriendo
echo       2. Verifica la IP con 'ipconfig'
echo       3. Intenta con la otra IP (Ethernet o WiFi)
echo       4. Desactiva temporalmente el firewall para probar
echo       5. Asegúrate que estén en la misma red
echo.
echo    ❌ "Bad Request (400)":
echo       1. El servidor ya está configurado para aceptar conexiones
echo       2. Reinicia el servidor (CTRL+C y vuelve a iniciar)
echo.
echo    ❌ "Timeout" o "No se puede alcanzar":
echo       1. Verifica el firewall de Windows
echo       2. Prueba haciendo ping: ping 192.168.1.56
echo       3. Conecta el dispositivo a la misma red
echo.

echo ╔═══════════════════════════════════════════════════════════════╗
echo ║  📝 RESUMEN RÁPIDO:                                           ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.
echo    Para conectar desde tu teléfono:
echo.
echo    1️⃣  Abre tu navegador móvil
echo    2️⃣  Escribe: http://192.168.1.56:8000/
echo    3️⃣  Si no funciona, prueba: http://192.168.137.221:8000/
echo    4️⃣  ¡Listo! Ya puedes usar la tienda desde tu teléfono
echo.

echo.
echo ═══════════════════════════════════════════════════════════════
echo.
echo 💡 TIP: Guarda esta ventana abierta como referencia
echo.
echo Presiona cualquier tecla para cerrar...
pause > nul

