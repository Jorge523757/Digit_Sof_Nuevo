@echo off
:: ============================================
:: SCRIPT PARA VER EL BOTÓN DE TEMA CORRECTAMENTE
:: ============================================

echo.
echo ========================================
echo   SOLUCION: BOTON DE TEMA NO VISIBLE
echo ========================================
echo.

echo [1/3] Deteniendo servidor si esta corriendo...
taskkill /F /IM python.exe 2>nul
timeout /t 2 /nobreak >nul

echo [2/3] Limpiando cache de Django...
python manage.py clearsessions
python manage.py collectstatic --noinput --clear

echo [3/3] Iniciando servidor...
echo.
echo ========================================
echo   INSTRUCCIONES IMPORTANTES
echo ========================================
echo.
echo Para ver el boton correctamente:
echo.
echo 1. Cuando se abra el navegador, presiona:
echo    Ctrl + Shift + R (Chrome/Edge)
echo    Ctrl + F5 (Firefox)
echo.
echo 2. O bien, abre el menu del navegador:
echo    - Chrome/Edge: Menu ^> Mas herramientas ^> Borrar datos de navegacion
echo    - Firefox: Menu ^> Opciones ^> Privacidad ^> Limpiar datos
echo.
echo 3. El boton debe estar aqui:
echo    [Tienda]  [Luna/Sol]  [Campana]  [Usuario]
echo             ^^^^^^^^^^^
echo          AQUI DEBE ESTAR
echo.
echo 4. URL para probar:
echo    http://127.0.0.1:8000/dashboard/
echo    http://127.0.0.1:8000/clientes/
echo.
echo ========================================
echo   Presiona Ctrl+C para detener
echo ========================================
echo.

python manage.py runserver

