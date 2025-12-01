@echo off
title RECARGA COMPLETA - Servidor Django
color 0A
echo.
echo ========================================
echo   RECARGA COMPLETA DEL SERVIDOR
echo ========================================
echo.
echo [1/3] Matando procesos de Python...
taskkill /F /IM python.exe 2>nul
timeout /t 2 /nobreak >nul

echo [2/3] Limpiando archivos temporales...
cd /d "%~dp0"
if exist __pycache__ rmdir /s /q __pycache__
if exist "*.pyc" del /f /q *.pyc

echo [3/3] Iniciando servidor en puerto 8000...
echo.
echo ========================================
echo   SERVIDOR LISTO EN:
echo   http://127.0.0.1:8000
echo ========================================
echo.
echo Presiona Ctrl+C para detener el servidor
echo.

python manage.py runserver 0.0.0.0:8000

pause

