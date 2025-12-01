@echo off
echo ================================================
echo   INSTALANDO DEPENDENCIAS - DIGIT SOFT
echo ================================================
echo.

echo [1/2] Instalando ReportLab para PDFs...
pip install reportlab

echo.
echo [2/2] Reiniciando servidor...
echo.

taskkill /F /IM python.exe 2>nul
timeout /t 2 /nobreak >nul

del /s /q *.pyc 2>nul
for /d /r . %%d in (__pycache__) do @if exist "%%d" rd /s /q "%%d"

echo ================================================
echo   SERVIDOR INICIANDO EN http://127.0.0.1:8000
echo ================================================
echo.

python manage.py runserver

