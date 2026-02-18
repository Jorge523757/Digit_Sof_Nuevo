chcp 65001 > nul
cls
color 0A
echo.
echo ╔════════════════════════════════════════════════════════════════════════════╗
echo ║                                                                            ║
echo ║              🚀 ACTIVAR ENVÍO REAL DE EMAILS - DIGITSOFT                   ║
echo ║                                                                            ║
echo ╚════════════════════════════════════════════════════════════════════════════╝
echo.
echo.
echo 📧 CONFIGURACIÓN DE GMAIL PARA ENVÍO REAL DE CÓDIGOS
echo ════════════════════════════════════════════════════════════════════════════
echo.
echo Ya he creado el archivo .env con tu email: davidcristancho160@gmail.com
echo.
echo Ahora solo necesitas completar la CONTRASEÑA DE APLICACIÓN.
echo.
echo.
echo ⚠️  IMPORTANTE: NO uses tu contraseña normal de Gmail
echo    Debes usar una "Contraseña de Aplicación" (16 caracteres)
echo.
echo.
echo 🔐 CÓMO OBTENER TU CONTRASEÑA DE APLICACIÓN:
echo ════════════════════════════════════════════════════════════════════════════
echo.
echo PASO 1: Abre esta URL en tu navegador
echo         👉 https://myaccount.google.com/apppasswords
echo.
echo PASO 2: Inicia sesión con tu cuenta de Gmail
echo         (davidcristancho160@gmail.com)
echo.
echo PASO 3: Si no tienes verificación en dos pasos:
echo         - Te pedirá activarla primero
echo         - Sigue las instrucciones (toma 2 minutos)
echo.
echo PASO 4: Genera una contraseña de aplicación:
echo         - Selecciona "Correo" como aplicación
echo         - Selecciona "Windows Computer" como dispositivo
echo         - Haz clic en "Generar"
echo.
echo PASO 5: Copia la contraseña de 16 caracteres que aparece
echo         - Ejemplo: abcd efgh ijkl mnop
echo         - Puedes copiarla con o sin espacios
echo.
echo.
pause
echo.
echo.
echo ════════════════════════════════════════════════════════════════════════════
echo 🎯 AHORA VAMOS A CONFIGURAR LA CONTRASEÑA
echo ════════════════════════════════════════════════════════════════════════════
echo.
set /p password="Pega aquí tu contraseña de aplicación (16 caracteres): "
echo.

if "%password%"=="" (
    echo.
    echo ❌ No ingresaste ninguna contraseña
    echo.
    pause
    exit
)

echo.
echo ⏳ Configurando...
echo.

REM Limpiar espacios de la contraseña
set password=%password: =%

REM Crear el archivo .env con la contraseña
(
echo # CONFIGURACIÓN DE EMAIL - DIGITSOFT
echo # Generado automáticamente
echo.
echo # Backend de email
echo EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
echo.
echo # Configuración SMTP de Gmail
echo EMAIL_HOST=smtp.gmail.com
echo EMAIL_PORT=587
echo EMAIL_USE_TLS=True
echo.
echo # Credenciales de Gmail
echo EMAIL_HOST_USER=davidcristancho160@gmail.com
echo EMAIL_HOST_PASSWORD=%password%
echo.
echo # Email remitente
echo DEFAULT_FROM_EMAIL=DIGITSOFT ^<davidcristancho160@gmail.com^>
echo.
echo # Email del administrador
echo ADMIN_EMAIL=davidcristancho160@gmail.com
echo.
echo # URL del sitio
echo SITE_URL=http://localhost:8000
echo.
echo # Otras configuraciones
echo DEBUG=True
echo SECRET_KEY=django-insecure-digt-soft-2024-cambiar-en-produccion
) > .env

echo.
echo ✅ ¡Archivo .env configurado correctamente!
echo.
echo.
echo ════════════════════════════════════════════════════════════════════════════
echo 🧪 PROBANDO CONEXIÓN CON GMAIL...
echo ════════════════════════════════════════════════════════════════════════════
echo.

python -c "import smtplib; server = smtplib.SMTP('smtp.gmail.com', 587, timeout=10); server.starttls(); server.login('davidcristancho160@gmail.com', '%password%'); print('✅ CONEXIÓN EXITOSA'); server.quit()" 2>nul

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ════════════════════════════════════════════════════════════════════════════
    echo 🎉 ¡CONFIGURACIÓN COMPLETADA EXITOSAMENTE!
    echo ════════════════════════════════════════════════════════════════════════════
    echo.
    echo ✅ La contraseña es correcta
    echo ✅ Conexión con Gmail funciona perfectamente
    echo ✅ El archivo .env está configurado
    echo.
    echo.
    echo 📝 PRÓXIMOS PASOS:
    echo ────────────────────────────────────────────────────────────────────────────
    echo.
    echo 1. REINICIA el servidor de Django:
    echo    - Cierra el servidor actual (Ctrl+C^)
    echo    - Vuelve a ejecutar: python manage.py runserver
    echo.
    echo 2. PRUEBA la recuperación de contraseña:
    echo    - Ve a la página de login
    echo    - Haz clic en "¿Olvidaste tu contraseña?"
    echo    - Ingresa cualquier email registrado
    echo    - ¡El código llegará por email en 5-30 segundos!
    echo.
    echo 3. REVISA tu bandeja de entrada
    echo    - También revisa la carpeta de SPAM
    echo    - El email vendrá de: DIGITSOFT ^<davidcristancho160@gmail.com^>
    echo.
    echo.
    echo ════════════════════════════════════════════════════════════════════════════
    echo.
) else (
    echo.
    echo ════════════════════════════════════════════════════════════════════════════
    echo ❌ ERROR: No se pudo conectar con Gmail
    echo ════════════════════════════════════════════════════════════════════════════
    echo.
    echo Posibles causas:
    echo.
    echo 1. La contraseña es incorrecta
    echo    - Asegúrate de usar la contraseña de aplicación (16 caracteres^)
    echo    - NO uses tu contraseña normal de Gmail
    echo.
    echo 2. No tienes verificación en dos pasos activada
    echo    - Ve a: https://myaccount.google.com/security
    echo    - Actívala primero
    echo.
    echo 3. Problema de conexión a internet
    echo    - Verifica tu conexión
    echo.
    echo.
    echo 💡 SOLUCIÓN: Ejecuta este script de nuevo y verifica:
    echo    - Que copiaste bien la contraseña de aplicación
    echo    - Que tienes verificación en dos pasos activada
    echo.
    echo ════════════════════════════════════════════════════════════════════════════
    echo.
)

pause

