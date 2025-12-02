@echo off
REM ====================================================
REM DIAGNÓSTICO RÁPIDO DEL DASHBOARD
REM ====================================================

echo.
echo ====================================================
echo  DIAGNÓSTICO DEL DASHBOARD
echo ====================================================
echo.

cd /d "%~dp0"

echo [1/3] Verificando archivos CSS...
if exist "static\css\dashboard-content.css" (
    echo [OK] dashboard-content.css existe
) else (
    echo [ERROR] dashboard-content.css NO existe
)

if exist "staticfiles\css\dashboard-content.css" (
    echo [OK] dashboard-content.css en staticfiles existe
) else (
    echo [ERROR] dashboard-content.css NO está en staticfiles
)

echo.
echo [2/3] Verificando template...
if exist "templates\dashboard\dashboard.html" (
    echo [OK] dashboard.html existe
) else (
    echo [ERROR] dashboard.html NO existe
)

echo.
echo [3/3] Verificando proyecto Django...
python manage.py check

echo.
echo ====================================================
echo  INSTRUCCIONES:
echo ====================================================
echo.
echo 1. Abre el navegador en: http://127.0.0.1:8000/dashboard/
echo 2. Presiona Ctrl + F5 para recargar
echo 3. DESPLAZATE HACIA ABAJO con la rueda del mouse
echo 4. Busca las secciones "Actividad Reciente" y "Tareas Pendientes"
echo.
echo ====================================================
echo  SEGÚN LOS LOGS, EL DASHBOARD ESTÁ FUNCIONANDO
echo  Solo necesitas hacer SCROLL HACIA ABAJO
echo ====================================================
echo.

pause

