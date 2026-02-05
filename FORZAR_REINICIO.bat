@echo off
color 0C
cls
echo ================================================================================
echo                  ATENCION: SERVIDOR NO ESTA REINICIADO
echo ================================================================================
echo.
echo El error persiste porque el servidor Django sigue corriendo con configuracion
echo antigua (antes de agregar reportes_dano).
echo.
echo DEBES HACER ESTO MANUALMENTE:
echo.
echo 1. Ve a la ventana donde corre "python manage.py runserver"
echo 2. Presiona Ctrl + C para detenerlo
echo 3. Vuelve a ejecutar: python manage.py runserver
echo.
echo ================================================================================
echo.
echo Presiona cualquier tecla para FORZAR cierre de Python y reiniciar...
pause >nul

echo.
echo [1/3] Cerrando todos los procesos de Python...
taskkill /F /IM python.exe 2>nul
if errorlevel 1 (
    echo No habia procesos Python corriendo
) else (
    echo Procesos Python cerrados
)

timeout /t 2 >nul

echo.
echo [2/3] Esperando 3 segundos...
timeout /t 3 >nul

echo.
echo [3/3] Iniciando servidor Django...
echo.
python manage.py runserver

