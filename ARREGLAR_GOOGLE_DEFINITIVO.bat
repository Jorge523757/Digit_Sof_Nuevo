@echo off
chcp 65001 >nul
color 0C
cls

echo ════════════════════════════════════════════════════════════════════════════════
echo 🚨 SOLUCION DEFINITIVA - MATAR TODO Y REINICIAR LIMPIO
echo ════════════════════════════════════════════════════════════════════════════════
echo.

echo Este script va a:
echo    1. MATAR todos los procesos de Python/Django
echo    2. LIMPIAR completamente la base de datos de Google OAuth
echo    3. REINICIAR el servidor limpio
echo.

pause

echo.
echo ════════════════════════════════════════════════════════════════════════════════
echo PASO 1: MATANDO PROCESOS DE PYTHON...
echo ════════════════════════════════════════════════════════════════════════════════
echo.

taskkill /F /IM python.exe 2>nul
if %ERRORLEVEL% EQU 0 (
    echo OK: Procesos de Python detenidos
) else (
    echo OK: No habia procesos de Python corriendo
)

timeout /t 2 /nobreak >nul

echo.
echo ════════════════════════════════════════════════════════════════════════════════
echo PASO 2: LIMPIEZA NUCLEAR DE GOOGLE OAUTH...
echo ════════════════════════════════════════════════════════════════════════════════
echo.

python limpieza_nuclear_google.py

echo.
echo ════════════════════════════════════════════════════════════════════════════════
echo PASO 3: LIMPIANDO CACHE DE PYTHON...
echo ════════════════════════════════════════════════════════════════════════════════
echo.

for /d /r . %%d in (__pycache__) do @if exist "%%d" rd /s /q "%%d" 2>nul
echo OK: Cache limpiado

echo.
echo ════════════════════════════════════════════════════════════════════════════════
echo PASO 4: INICIANDO SERVIDOR LIMPIO...
echo ════════════════════════════════════════════════════════════════════════════════
echo.
echo TODO LISTO
echo.
echo IMPORTANTE - AHORA HAZ ESTO:
echo    1. Abre el navegador en MODO INCOGNITO (Ctrl + Shift + N)
echo    2. Ve a: http://127.0.0.1:8000/usuarios/login/
echo    3. Click en Iniciar sesion con Google
echo    4. DEBE FUNCIONAR sin el error MultipleObjectsReturned
echo.
echo ════════════════════════════════════════════════════════════════════════════════
echo Iniciando servidor...
echo.

python manage.py runserver

