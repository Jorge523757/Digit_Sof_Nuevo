@echo off
chcp 65001 >nul
color 0A
cls

echo ════════════════════════════════════════════════════════════════════════════════
echo ✅ SERVIDOR DJANGO - INICIO LIMPIO
echo ════════════════════════════════════════════════════════════════════════════════
echo.

echo 📋 Preparando el servidor...
echo.

REM Limpiar caché de Python
echo 🗑️ Limpiando caché de Python...
for /d /r . %%d in (__pycache__) do @if exist "%%d" rd /s /q "%%d" 2>nul
del /s /q *.pyc 2>nul
echo ✅ Caché limpiado

echo.
echo 🔍 Verificando configuración de Google OAuth...
python -c "import os, django; os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings'); django.setup(); from allauth.socialaccount.models import SocialApp; apps = SocialApp.objects.filter(provider='google'); print(f'✅ Configuraciones de Google: {apps.count()}'); print('✅ OK' if apps.count() == 1 else '❌ ERROR: Deberían ser 1')"

echo.
echo ════════════════════════════════════════════════════════════════════════════════
echo 🚀 INICIANDO SERVIDOR DJANGO...
echo ════════════════════════════════════════════════════════════════════════════════
echo.
echo ⚠️ RECUERDA:
echo    • Abre el navegador en MODO INCÓGNITO: Ctrl + Shift + N
echo    • Ve a: http://127.0.0.1:8000/usuarios/login/
echo    • El login con Google debería funcionar sin errores
echo.
echo Para detener el servidor: Ctrl + C
echo.
echo ════════════════════════════════════════════════════════════════════════════════

python manage.py runserver

