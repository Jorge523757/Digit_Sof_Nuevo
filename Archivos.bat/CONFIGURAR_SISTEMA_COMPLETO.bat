@echo off
chcp 65001 >nul
color 0A
title CONFIGURAR SISTEMA COMPLETO - DIGIT SOFT

echo.
echo ========================================================================
echo    🚀 CONFIGURANDO SISTEMA COMPLETO CON RECAPTCHA Y RECUPERACIÓN
echo ========================================================================
echo.

echo [1/5] Limpiando configuraciones de Google OAuth duplicadas...
python LIMPIAR_GOOGLE_OAUTH.py
if errorlevel 1 (
    echo ❌ Error al limpiar Google OAuth
    pause
    exit /b 1
)

echo.
echo [2/5] Ejecutando migraciones de base de datos...
python manage.py makemigrations
python manage.py migrate
if errorlevel 1 (
    echo ❌ Error en migraciones
    pause
    exit /b 1
)

echo.
echo [3/5] Recolectando archivos estáticos...
python manage.py collectstatic --noinput
if errorlevel 1 (
    echo ⚠️  Advertencia en archivos estáticos (no crítico)
)

echo.
echo [4/5] Verificando configuración final...
python verificacion_final.py
if errorlevel 1 (
    echo ⚠️  Advertencia en verificación (revisa los mensajes)
)

echo.
echo ========================================================================
echo    ✅ CONFIGURACIÓN COMPLETADA
echo ========================================================================
echo.
echo 📋 CARACTERÍSTICAS IMPLEMENTADAS:
echo    ✅ reCAPTCHA (No soy un robot) en login
echo    ✅ Recuperación de contraseña con código por email (30 min)
echo    ✅ Login con Google OAuth corregido
echo    ✅ Validaciones mejoradas
echo.
echo 🔐 SISTEMA DE RECUPERACIÓN:
echo    Paso 1: Ingresa tu email + reCAPTCHA
echo    Paso 2: Código de 6 dígitos (expira en 30 min)
echo    Paso 3: Nueva contraseña segura
echo.
echo 🚀 Para iniciar el servidor:
echo    python manage.py runserver
echo.
echo 🌐 Luego visita:
echo    http://127.0.0.1:8000/usuarios/login/
echo.
echo 📧 Para recuperar contraseña:
echo    http://127.0.0.1:8000/usuarios/recuperar/
echo.
echo ========================================================================
pause

