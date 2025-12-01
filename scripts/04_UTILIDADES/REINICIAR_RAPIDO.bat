@echo off
title REINICIAR SERVIDOR RAPIDO
color 0B
cls
echo.
echo ========================================
echo   REINICIANDO SERVIDOR DJANGO
echo ========================================
echo.

cd /d "%~dp0"

echo [1/2] Deteniendo servidor...
taskkill /F /IM python.exe 2>nul
timeout /t 2 /nobreak >nul

echo [2/2] Iniciando servidor...
echo.
start "" python manage.py runserver 0.0.0.0:8000

timeout /t 3 /nobreak >nul

echo.
echo ========================================
echo   SERVIDOR REINICIADO
echo   http://127.0.0.1:8000
echo ========================================
echo.
echo Presiona CTRL+F5 en el navegador
echo para recargar sin cache
echo.
pause

