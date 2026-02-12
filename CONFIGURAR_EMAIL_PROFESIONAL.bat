@echo off
chcp 65001 >nul
color 0A
echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║  🔐 CONFIGURACIÓN PROFESIONAL DE EMAIL - DIGIT SOFT           ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.
echo Este script te ayudará a configurar el envío REAL de emails
echo para que los códigos lleguen al correo de los usuarios.
echo.
echo ════════════════════════════════════════════════════════════════
echo.

set SCRIPT_DIR=%~dp0
cd /d "%SCRIPT_DIR%"

echo 📧 PASO 1: Verificando configuración actual...
echo.

python -c "from decouple import config; pwd=config('EMAIL_HOST_PASSWORD', default='NO_CONFIG'); print('Estado actual: CONFIGURADO' if pwd != 'NO_CONFIG' and pwd != 'AQUI_TU_CONTRASEÑA_DE_APLICACION' else 'Estado actual: NO CONFIGURADO')" 2>nul

if errorlevel 1 (
    echo ❌ Error al verificar configuración
    echo    Instalando python-decouple...
    pip install python-decouple >nul 2>&1
)

echo.
echo ════════════════════════════════════════════════════════════════
echo.
echo 📱 PASO 2: Generar Contraseña de Aplicación de Gmail
echo.
echo Para que los emails lleguen REALMENTE, necesitas:
echo.
echo   1. Activar "Verificación en 2 pasos" en tu cuenta de Gmail
echo   2. Generar una "Contraseña de Aplicación"
echo.
echo ¿Quieres que abra las páginas necesarias? (S/N)
set /p ABRIR_PAGINAS=^>

if /i "%ABRIR_PAGINAS%"=="S" (
    echo.
    echo ✅ Abriendo página de seguridad de Google...
    start https://myaccount.google.com/security
    timeout /t 3 >nul

    echo ✅ Abriendo página de contraseñas de aplicación...
    start https://myaccount.google.com/apppasswords

    echo.
    echo 📝 INSTRUCCIONES:
    echo.
    echo   1. En la primera pestaña, activa "Verificación en 2 pasos"
    echo   2. En la segunda pestaña, genera una contraseña de aplicación
    echo   3. Selecciona: App = "Correo", Dispositivo = "Computadora Windows"
    echo   4. Copia la contraseña de 16 caracteres que aparece
    echo   5. Vuelve aquí y pégala
    echo.
)

echo.
echo ════════════════════════════════════════════════════════════════
echo.
echo 🔑 PASO 3: Ingresar Contraseña de Aplicación
echo.
echo Pega aquí la contraseña de 16 caracteres de Gmail
echo (Puedes pegarla sin espacios: abcdefghijklmnop)
echo.
set /p GMAIL_PASSWORD=Contraseña de aplicación:

if "%GMAIL_PASSWORD%"=="" (
    echo.
    echo ❌ No ingresaste ninguna contraseña
    echo    Proceso cancelado
    pause
    exit /b 1
)

echo.
echo 💾 Guardando configuración...

REM Crear archivo .env temporal
echo # CONFIGURACIÓN PROFESIONAL DE EMAIL - DIGIT SOFT > .env.tmp
echo # Configurado automáticamente el %date% %time% >> .env.tmp
echo. >> .env.tmp
echo # Backend de email (SMTP real) >> .env.tmp
echo EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend >> .env.tmp
echo. >> .env.tmp
echo # Configuración SMTP de Gmail >> .env.tmp
echo EMAIL_HOST=smtp.gmail.com >> .env.tmp
echo EMAIL_PORT=587 >> .env.tmp
echo EMAIL_USE_TLS=True >> .env.tmp
echo. >> .env.tmp
echo # Credenciales de Gmail >> .env.tmp
echo EMAIL_HOST_USER=davidcristancho160@gmail.com >> .env.tmp
echo EMAIL_HOST_PASSWORD=%GMAIL_PASSWORD% >> .env.tmp
echo. >> .env.tmp
echo # Email remitente >> .env.tmp
echo DEFAULT_FROM_EMAIL=DIGIT SOFT ^<davidcristancho160@gmail.com^> >> .env.tmp
echo. >> .env.tmp
echo # Email del administrador >> .env.tmp
echo ADMIN_EMAIL=davidcristancho160@gmail.com >> .env.tmp
echo. >> .env.tmp
echo # URL del sitio >> .env.tmp
echo SITE_URL=http://localhost:8000 >> .env.tmp
echo. >> .env.tmp
echo # Otras configuraciones >> .env.tmp
echo DEBUG=True >> .env.tmp
echo SECRET_KEY=django-insecure-digt-soft-2024-cambiar-en-produccion >> .env.tmp

REM Hacer backup del .env actual
if exist .env (
    echo 📦 Creando backup de .env actual...
    copy /Y .env .env.backup.%date:~-4,4%%date:~-10,2%%date:~-7,2%_%time:~0,2%%time:~3,2%%time:~6,2% >nul 2>&1
)

REM Reemplazar .env con el nuevo
move /Y .env.tmp .env >nul 2>&1

echo ✅ Configuración guardada en .env
echo.

echo ════════════════════════════════════════════════════════════════
echo.
echo 🧪 PASO 4: Probando envío de email...
echo.

python -c "import os; os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings'); import django; django.setup(); from django.core.mail import send_mail; from django.conf import settings; print('📧 Enviando email de prueba...'); result = send_mail('Prueba - DIGIT SOFT', 'Este es un email de prueba del sistema DIGIT SOFT. Si recibes este mensaje, la configuración es correcta.', settings.DEFAULT_FROM_EMAIL, ['davidcristancho160@gmail.com'], fail_silently=False); print('✅ Email enviado correctamente!' if result else '❌ Error al enviar email')" 2>nul

if errorlevel 1 (
    echo.
    echo ❌ Error al enviar email de prueba
    echo.
    echo Posibles causas:
    echo   - La contraseña de aplicación es incorrecta
    echo   - La verificación en 2 pasos no está activada
    echo   - Hay un problema de conexión a internet
    echo.
    echo Revisa la configuración y vuelve a intentar
    pause
    exit /b 1
)

echo.
echo ════════════════════════════════════════════════════════════════
echo.
echo ✅ CONFIGURACIÓN COMPLETADA
echo ════════════════════════════════════════════════════════════════
echo.
echo 🎉 El sistema está configurado correctamente
echo.
echo Ahora los códigos de recuperación llegarán al email:
echo    davidcristancho160@gmail.com
echo.
echo 📝 Próximos pasos:
echo.
echo   1. Reinicia el servidor Django
echo   2. Prueba el sistema de recuperación de contraseña
echo   3. Verifica que el email llegue a la bandeja de entrada
echo.
echo 💡 Nota: El email puede tardar algunos segundos en llegar
echo    Si no lo ves, revisa la carpeta de SPAM
echo.
echo ════════════════════════════════════════════════════════════════
echo.
echo ¿Quieres reiniciar el servidor Django ahora? (S/N)
set /p REINICIAR=^>

if /i "%REINICIAR%"=="S" (
    echo.
    echo 🔄 Deteniendo servidor actual...
    taskkill /F /IM python.exe >nul 2>&1
    timeout /t 2 >nul

    echo ✅ Servidor detenido
    echo.
    echo 🚀 Iniciando servidor con nueva configuración...
    start "DIGIT SOFT Server" cmd /k "cd /d %SCRIPT_DIR% && python manage.py runserver"

    timeout /t 3 >nul
    echo.
    echo ✅ Servidor iniciado
    echo.
    echo 🌐 Accede a: http://127.0.0.1:8000
    echo.
)

echo.
echo Presiona cualquier tecla para cerrar...
pause >nul

