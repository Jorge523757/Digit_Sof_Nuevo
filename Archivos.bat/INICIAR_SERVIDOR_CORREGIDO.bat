@echo off
echo ================================================
echo     DIGITSOFT - INICIAR SERVIDOR
echo     Visualizacion Corregida - Version 1.0
echo ================================================
echo.

cd /d "%~dp0"

echo [1/3] Verificando sistema...
python manage.py check
if errorlevel 1 (
    echo.
    echo [ERROR] Se encontraron errores en el sistema.
    pause
    exit /b 1
)

echo.
echo [2/3] Recopilando archivos estaticos...
python manage.py collectstatic --noinput

echo.
echo [3/3] Iniciando servidor Django...
echo.
echo ================================================
echo     SERVIDOR INICIADO
echo     Accede a: http://127.0.0.1:8000
echo     Presiona CTRL+C para detener
echo ================================================
echo.

python manage.py runserver

pause

