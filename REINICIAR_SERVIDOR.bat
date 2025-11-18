@echo off
echo ================================================
echo   REINICIANDO SERVIDOR DJANGO - DIGIT SOFT
echo ================================================
echo.

echo [1/3] Deteniendo procesos de Python...
taskkill /F /IM python.exe 2>nul
timeout /t 2 /nobreak >nul

echo [2/3] Limpiando cache de Python...
del /s /q *.pyc 2>nul
for /d /r . %%d in (__pycache__) do @if exist "%%d" rd /s /q "%%d"

echo [3/3] Iniciando servidor...
echo.
echo ================================================
echo   SERVIDOR INICIANDO EN http://127.0.0.1:8000
echo ================================================
echo.

python manage.py runserver

