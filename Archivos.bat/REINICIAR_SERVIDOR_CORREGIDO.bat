@echo off
echo ============================================
echo  SOLUCION: Error currency_filters
echo ============================================
echo.
echo El error ha sido corregido:
echo.
echo 1. Se agrego 'utils' a INSTALLED_APPS
echo 2. Se crearon los archivos necesarios:
echo    - utils/__init__.py
echo    - utils/apps.py
echo.
echo ============================================
echo  REINICIANDO SERVIDOR...
echo ============================================
echo.
echo Presiona Ctrl+C para detener el servidor anterior
echo Luego ejecuta este script nuevamente
echo.
pause
echo.
echo Iniciando servidor Django...
python manage.py runserver

