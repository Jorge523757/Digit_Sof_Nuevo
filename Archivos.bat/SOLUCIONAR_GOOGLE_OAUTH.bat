@echo off
chcp 65001 >nul
color 0E
cls

echo ════════════════════════════════════════════════════════════════════════════════
echo 🔧 SOLUCIÓN DEFINITIVA - ERROR GOOGLE OAUTH
echo ════════════════════════════════════════════════════════════════════════════════
echo.

echo 📋 PASO 1: Limpiando configuración de Google OAuth...
echo.
python limpieza_total_google.py

echo.
echo ════════════════════════════════════════════════════════════════════════════════
echo 📋 PASO 2: Verificando que solo haya 1 configuración...
echo.
python diagnostico_google_completo.py

echo.
echo ════════════════════════════════════════════════════════════════════════════════
echo 📋 PASO 3: Limpiando archivos de caché de Python...
echo.

echo Eliminando archivos __pycache__...
for /d /r . %%d in (__pycache__) do @if exist "%%d" rd /s /q "%%d"
echo ✅ Caché de Python limpiado

echo.
echo Eliminando archivos .pyc...
del /s /q *.pyc 2>nul
echo ✅ Archivos .pyc eliminados

echo.
echo ════════════════════════════════════════════════════════════════════════════════
echo 🎯 INSTRUCCIONES FINALES
echo ════════════════════════════════════════════════════════════════════════════════
echo.
echo ⚠️ IMPORTANTE: Debes seguir estos pasos AHORA:
echo.
echo 1. ❌ DETÉN el servidor Django si está corriendo (Ctrl+C en la terminal)
echo.
echo 2. ✅ INICIA el servidor nuevamente:
echo    python manage.py runserver
echo.
echo 3. 🌐 LIMPIA el caché del navegador:
echo    - Chrome/Edge: Ctrl+Shift+Delete (Eliminar "Cookies" e "Imágenes en caché")
echo    - O usa modo incógnito: Ctrl+Shift+N
echo.
echo 4. 🔄 RECARGA la página de login:
echo    http://127.0.0.1:8000/usuarios/login/
echo.
echo 5. ✅ INTENTA login con Google
echo.
echo ════════════════════════════════════════════════════════════════════════════════
echo 💡 ¿Por qué el error persiste?
echo ════════════════════════════════════════════════════════════════════════════════
echo.
echo El servidor Django guarda en memoria la configuración antigua. Por eso aunque
echo en la base de datos solo hay 1 configuración, el servidor sigue viendo la vieja.
echo.
echo LA SOLUCIÓN: Reiniciar el servidor (no solo refrescar la página)
echo.
echo ════════════════════════════════════════════════════════════════════════════════
pause

