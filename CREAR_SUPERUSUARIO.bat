@echo off
chcp 65001 >nul
color 0A
cls

echo.
echo ══════════════════════════════════════════════════════════════
echo            CREAR SUPERUSUARIO - DIGIT SOFT
echo ══════════════════════════════════════════════════════════════
echo.

cd /d "%~dp0"

python crear_superusuario.py

echo.
echo ══════════════════════════════════════════════════════════════
echo.
echo ✅ Proceso completado
echo.
echo Presiona cualquier tecla para cerrar...
pause >nul

