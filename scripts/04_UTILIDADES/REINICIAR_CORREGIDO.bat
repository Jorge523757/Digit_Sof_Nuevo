@echo off
cls
color 0A
echo ============================================================
echo    REINICIANDO SERVIDOR - ERRORES CORREGIDOS
echo ============================================================
echo.
echo Deteniendo procesos Python anteriores...
taskkill /F /IM python.exe 2>nul
timeout /t 2 /nobreak >nul
echo.
echo Activando entorno virtual...
cd /d C:\Users\jorge\OneDrive\Escritorio\DigtSoft\Digit_Sof_Nuevo
call .\venv\Scripts\activate.bat
echo.
echo Verificando sistema...
python manage.py check
echo.
echo ============================================================
echo    INICIANDO SERVIDOR CON CORRECCI ONES
echo ============================================================
echo.
echo CAMBIOS APLICADOS:
echo  - Eliminado FormDummy en ordenes/views.py
echo  - Limpiado capacitaciones/lista.html
echo  - Todas las funciones duplicadas eliminadas
echo.
echo URLS DISPONIBLES:
echo  http://127.0.0.1:8000/ordenes/
echo  http://127.0.0.1:8000/ventas/
echo  http://127.0.0.1:8000/capacitaciones/
echo  http://127.0.0.1:8000/compras/
echo  Y todos los demas modulos...
echo.
echo ============================================================
echo  Presiona Ctrl+C para detener el servidor
echo ============================================================
echo.

python manage.py runserver

pause

