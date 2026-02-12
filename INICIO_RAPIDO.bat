@echo off
chcp 65001 >nul
color 0A
cls

echo.
echo ╔════════════════════════════════════════════════════════════════════════╗
echo ║                                                                        ║
echo ║              ⚡ INICIO RÁPIDO - DIGIT SOFT ⚡                           ║
echo ║                                                                        ║
echo ╚════════════════════════════════════════════════════════════════════════╝
echo.
echo.
echo 🚀 Este script va a:
echo    1. Limpiar Google OAuth
echo    2. Ejecutar migraciones
echo    3. Verificar sistema
echo    4. Iniciar servidor
echo.
echo ⏱️  Esto tomará aproximadamente 1-2 minutos
echo.
pause

cls
echo.
echo ═══════════════════════════════════════════════════════════════════════
echo  [1/4] Limpiando configuración de Google OAuth...
echo ═══════════════════════════════════════════════════════════════════════
echo.
python LIMPIAR_GOOGLE_OAUTH.py
if errorlevel 1 (
    echo.
    echo ❌ Error al limpiar Google OAuth
    pause
    exit /b 1
)

echo.
echo.
echo ═══════════════════════════════════════════════════════════════════════
echo  [2/4] Ejecutando migraciones de base de datos...
echo ═══════════════════════════════════════════════════════════════════════
echo.
python manage.py makemigrations
python manage.py migrate
if errorlevel 1 (
    echo.
    echo ❌ Error en migraciones
    pause
    exit /b 1
)

echo.
echo.
echo ═══════════════════════════════════════════════════════════════════════
echo  [3/4] Verificando sistema completo...
echo ═══════════════════════════════════════════════════════════════════════
echo.
python verificar_sistema_completo.py

echo.
echo.
echo ═══════════════════════════════════════════════════════════════════════
echo  [4/4] Iniciando servidor de desarrollo...
echo ═══════════════════════════════════════════════════════════════════════
echo.
echo ✅ Configuración completada!
echo.
echo 🌐 Abriendo navegador en: http://127.0.0.1:8000/usuarios/login/
echo.
echo ⚠️  IMPORTANTE - EMAILS EN DESARROLLO:
echo    Los códigos de recuperación aparecen en ESTA CONSOLA
echo    NO se envían a tu email real
echo.
echo 📋 Para probar:
echo    • Login normal: Usuario + contraseña + reCAPTCHA
echo    • Recuperar contraseña: Email + reCAPTCHA (código en consola)
echo    • Login con Google: davidcristancho160@gmail.com
echo.
echo ═══════════════════════════════════════════════════════════════════════
echo.
echo Presiona Ctrl+C para detener el servidor
echo.

REM Abrir navegador
start http://127.0.0.1:8000/usuarios/login/

REM Iniciar servidor
python manage.py runserver

