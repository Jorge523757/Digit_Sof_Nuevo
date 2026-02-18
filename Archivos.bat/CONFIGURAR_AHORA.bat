@echo off
chcp 65001 > nul
cls
color 0E
echo.
echo ╔════════════════════════════════════════════════════════════════════════════╗
echo ║                                                                            ║
echo ║           🚀 CONFIGURACIÓN RÁPIDA DE EMAIL - 2 MINUTOS                     ║
echo ║                                                                            ║
echo ╚════════════════════════════════════════════════════════════════════════════╝
echo.
echo.
echo ✅ TU SISTEMA YA FUNCIONA - SOLO FALTA LA CONTRASEÑA
echo ════════════════════════════════════════════════════════════════════════════
echo.
echo Vi que el código se generó correctamente: 513155
echo.
echo El problema: Backend está en modo "console"
echo La solución: Configurar contraseña de Gmail (2 minutos)
echo.
echo.
echo 📝 OPCIÓN 1: CONFIGURACIÓN MANUAL RÁPIDA (1 MINUTO)
echo ════════════════════════════════════════════════════════════════════════════
echo.
echo 1. Abre: https://myaccount.google.com/apppasswords
echo    (Se abrirá automáticamente en 5 segundos)
echo.
echo 2. Genera contraseña para "Correo"
echo.
echo 3. Cópiala (16 caracteres)
echo.
echo 4. Pégala aquí abajo
echo.
echo.
timeout /t 5 >nul
start https://myaccount.google.com/apppasswords
echo.
echo ════════════════════════════════════════════════════════════════════════════
echo.
set /p password="Pega tu contraseña de aplicación aquí: "
echo.

if "%password%"=="" (
    echo ❌ No ingresaste contraseña
    echo.
    echo 💡 Si no tienes verificación en dos pasos:
    echo    1. Ve a: https://myaccount.google.com/security
    echo    2. Actívala (2 minutos)
    echo    3. Ejecuta este script de nuevo
    echo.
    pause
    exit
)

echo ⏳ Configurando...

REM Limpiar espacios
set password=%password: =%

REM Crear .env
(
echo EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
echo EMAIL_HOST=smtp.gmail.com
echo EMAIL_PORT=587
echo EMAIL_USE_TLS=True
echo EMAIL_HOST_USER=davidcristancho160@gmail.com
echo EMAIL_HOST_PASSWORD=%password%
echo DEFAULT_FROM_EMAIL=DIGITSOFT ^<davidcristancho160@gmail.com^>
echo ADMIN_EMAIL=davidcristancho160@gmail.com
echo SITE_URL=http://localhost:8000
echo DEBUG=True
echo SECRET_KEY=django-insecure-digt-soft-2024-cambiar-en-produccion
) > .env

echo.
echo ✅ Archivo .env configurado
echo.
echo 🧪 Probando conexión...
echo.

python -c "import smtplib; s = smtplib.SMTP('smtp.gmail.com', 587, timeout=10); s.starttls(); s.login('davidcristancho160@gmail.com', '%password%'); print('✅ CONEXIÓN EXITOSA'); s.quit()" 2>nul

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ════════════════════════════════════════════════════════════════════════════
    echo 🎉 ¡PERFECTO! TODO CONFIGURADO
    echo ════════════════════════════════════════════════════════════════════════════
    echo.
    echo ✅ Contraseña correcta
    echo ✅ Conexión con Gmail funciona
    echo ✅ Archivo .env configurado
    echo.
    echo.
    echo 📝 PRÓXIMO PASO (IMPORTANTE):
    echo ────────────────────────────────────────────────────────────────────────────
    echo.
    echo   REINICIA EL SERVIDOR DE DJANGO:
    echo.
    echo   1. Ve a la ventana donde corre el servidor
    echo   2. Presiona Ctrl+C para detenerlo
    echo   3. Ejecuta de nuevo: python manage.py runserver
    echo.
    echo   ¡SOLO ASÍ TOMARÁ LA NUEVA CONFIGURACIÓN!
    echo.
    echo.
    echo 🎯 DESPUÉS DE REINICIAR:
    echo ────────────────────────────────────────────────────────────────────────────
    echo.
    echo   - Ve a recuperar contraseña
    echo   - Ingresa tu email
    echo   - ¡El código llegará en 5-30 segundos!
    echo   - Revisa tu bandeja y SPAM
    echo.
    echo ════════════════════════════════════════════════════════════════════════════
    echo.
) else (
    echo.
    echo ════════════════════════════════════════════════════════════════════════════
    echo ❌ ERROR DE CONEXIÓN
    echo ════════════════════════════════════════════════════════════════════════════
    echo.
    echo Posibles causas:
    echo.
    echo 1. Contraseña incorrecta
    echo    → Verifica que copiaste la contraseña de aplicación completa
    echo    → NO uses tu contraseña normal de Gmail
    echo.
    echo 2. Falta verificación en dos pasos
    echo    → Ve a: https://myaccount.google.com/security
    echo    → Actívala y luego genera la contraseña de aplicación
    echo.
    echo 3. Problema de internet
    echo    → Verifica tu conexión
    echo.
    echo ════════════════════════════════════════════════════════════════════════════
    echo.
)

pause

