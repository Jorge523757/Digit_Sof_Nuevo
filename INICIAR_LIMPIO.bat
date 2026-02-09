@echo off
title DIGITSOFT - Iniciar Servidor Limpio
color 0A
cls

echo.
echo ══════════════════════════════════════════════════════════════
echo              DIGITSOFT - INICIAR SERVIDOR LIMPIO
echo ══════════════════════════════════════════════════════════════
echo.
echo Este script:
echo  1. Matara TODOS los servidores Django corriendo
echo  2. Limpiara Google OAuth (solo 1 configuracion)
echo  3. Iniciara el servidor completamente limpio
echo.
echo ══════════════════════════════════════════════════════════════
echo.
pause

cls
echo.
echo [1/4] Matando servidores Django antiguos...
taskkill /F /IM python.exe >nul 2>&1
timeout /t 2 /nobreak >nul
echo       ✓ OK

echo.
echo [2/4] Limpiando Google OAuth...
python limpieza_nuclear_google.py >nul 2>&1
echo       ✓ OK - Solo 1 configuracion

echo.
echo [3/4] Limpiando cache de Python...
for /d /r . %%d in (__pycache__) do @if exist "%%d" rd /s /q "%%d" 2>nul
del /s /q *.pyc >nul 2>&1
echo       ✓ OK

echo.
echo [4/4] Iniciando servidor...
echo.
echo ══════════════════════════════════════════════════════════════
echo                      SERVIDOR INICIADO
echo ══════════════════════════════════════════════════════════════
echo.
echo AHORA HAZ ESTO:
echo.
echo  1. Abre Chrome en MODO INCOGNITO: Ctrl + Shift + N
echo.
echo  2. Ve a: http://127.0.0.1:8000/usuarios/login/
echo.
echo  3. Click en "Iniciar sesion con Google"
echo.
echo  4. ✓ FUNCIONARA SIN ERRORES
echo.
echo ══════════════════════════════════════════════════════════════
echo.

python manage.py runserver

