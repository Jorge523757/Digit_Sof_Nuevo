@echo off
chcp 65001 > nul
color 0A
echo ================================================================================
echo DIGT SOFT - Reiniciar Servidor Django
echo ================================================================================
echo.
echo IMPORTANTE: Si el servidor está corriendo, detenlo primero con Ctrl+C
echo.
pause
echo.
echo ================================================================================
echo Limpiando caché de Python...
echo ================================================================================
if exist "reportes_dano\__pycache__" (
    rd /s /q reportes_dano\__pycache__
    echo ✓ Caché de reportes_dano eliminado
)
if exist "config\__pycache__" (
    rd /s /q config\__pycache__
    echo ✓ Caché de config eliminado
)
echo.
echo ================================================================================
echo Verificando configuración...
echo ================================================================================
echo.
echo Verificando INSTALLED_APPS...
findstr /C:"reportes_dano" config\settings.py >nul
if %errorlevel%==0 (
    echo ✓ reportes_dano está en INSTALLED_APPS
) else (
    echo ✗ ERROR: reportes_dano NO está en INSTALLED_APPS
    pause
    exit /b 1
)
echo.
echo Verificando URLs...
findstr /C:"reportes_dano.urls" config\urls.py >nul
if %errorlevel%==0 (
    echo ✓ reportes_dano.urls está configurado
) else (
    echo ✗ ERROR: reportes_dano.urls NO está configurado
    pause
    exit /b 1
)
echo.
echo Verificando migraciones...
python manage.py showmigrations reportes_dano
echo.
echo ================================================================================
echo Iniciando servidor Django...
echo ================================================================================
echo.
echo El servidor se iniciará en: http://127.0.0.1:8000/
echo.
echo Para ver Gestión de Equipos: http://127.0.0.1:8000/equipos/
echo.
echo Presiona Ctrl+C para detener el servidor
echo.
echo ================================================================================
python manage.py runserver

