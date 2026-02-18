@echo off
chcp 65001 >nul
echo.
echo ============================================================
echo 🔐 OBTENIENDO TU CÓDIGO DE RECUPERACIÓN
echo ============================================================
echo.

cd /d "%~dp0"
python obtener_codigo.py

echo.
echo ============================================================
echo.
echo Presiona cualquier tecla para cerrar...
pause >nul

