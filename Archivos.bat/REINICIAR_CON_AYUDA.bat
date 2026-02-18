@echo off
chcp 65001 >nul
color 0A
cls

echo.
echo ══════════════════════════════════════════════════════════════
echo          REINICIAR SERVIDOR - DIGIT SOFT
echo ══════════════════════════════════════════════════════════════
echo.
echo ✅ Módulo de AYUDA agregado al sidebar de clientes y técnicos
echo.
echo Presiona Ctrl+C para detener el servidor actual
echo Luego ejecuta este archivo para reiniciar
echo.
echo ══════════════════════════════════════════════════════════════
echo.

cd /d "%~dp0"

echo [1/2] Verificando sistema...
python manage.py check
if errorlevel 1 (
    echo.
    echo ❌ Error en el sistema
    pause
    exit /b 1
)
echo ✅ Sistema sin errores
echo.

echo [2/2] Iniciando servidor...
echo.
echo ══════════════════════════════════════════════════════════════
echo          SERVIDOR INICIADO
echo ══════════════════════════════════════════════════════════════
echo.
echo Accede a: http://127.0.0.1:8000
echo.
echo Usuario de prueba: Teodoro12
echo.
echo ✅ NUEVO: Módulo de Ayuda disponible en el sidebar
echo    Sección "Soporte" → "Ayuda y Soporte"
echo.
echo Para detener: Presiona Ctrl+C
echo ══════════════════════════════════════════════════════════════
echo.

python manage.py runserver

