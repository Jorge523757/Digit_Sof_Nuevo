@echo off
echo ============================================================
echo DIGITSOFT - Verificación de Sistema de Notificaciones
echo ============================================================
echo.

echo [1/3] Verificando que existan notificaciones en la BD...
python crear_notificaciones_test.py
echo.

echo [2/3] Verificando archivos del sistema...
echo Archivo notificaciones.js:
if exist "static\js\notificaciones.js" (
    echo    [OK] Encontrado
) else (
    echo    [ERROR] No encontrado
)

echo Archivo click-fix-critical.css:
if exist "static\css\click-fix-critical.css" (
    echo    [OK] Encontrado
) else (
    echo    [ERROR] No encontrado
)

echo Template base_dashboard.html:
if exist "templates\base_dashboard.html" (
    echo    [OK] Encontrado
) else (
    echo    [ERROR] No encontrado
)
echo.

echo [3/3] Iniciando servidor...
echo.
echo ============================================================
echo INSTRUCCIONES:
echo 1. El servidor se iniciará en http://127.0.0.1:8000
echo 2. Abre el navegador y ve al dashboard
echo 3. Presiona F12 para abrir la consola del navegador
echo 4. Busca los mensajes que empiecen con [Notificaciones]
echo 5. Haz clic en el botón de la campana (notificaciones)
echo 6. Deberías ver el dropdown con tus notificaciones
echo ============================================================
echo.
pause

python manage.py runserver

