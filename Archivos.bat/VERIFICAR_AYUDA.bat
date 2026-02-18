@echo off
chcp 65001 >nul
cls
color 0B
echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║  🔍 VERIFICAR Y ACCEDER AL MÓDULO DE AYUDA                    ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

cd /d "%~dp0"

echo 📋 Verificando módulo de ayuda...
echo.

python verificar_ayuda.py

echo.
echo ════════════════════════════════════════════════════════════════
echo.
echo 🌐 Para acceder al módulo de ayuda:
echo.
echo    1. Asegúrate de que el servidor esté corriendo:
echo       python manage.py runserver
echo.
echo    2. Abre tu navegador en:
echo       http://127.0.0.1:8000/ayuda/
echo.
echo ════════════════════════════════════════════════════════════════
echo.
pause

