echo  - Abre test_notificaciones.html en tu navegador para ver
echo    una simulacion del sistema funcionando
echo.
echo ========================================================================
echo.
pause

echo.
echo [*] Iniciando servidor Django...
echo [*] URL: http://127.0.0.1:8000
echo.
echo     IMPORTANTE: Deja esta ventana abierta
echo.

python manage.py runserver
@echo off
color 0A
echo.
echo ========================================================================
echo                  DIGITSOFT - NOTIFICACIONES CORREGIDAS
echo ========================================================================
echo.
echo  El sistema de notificaciones ha sido completamente reparado.
echo.
echo  CAMBIOS REALIZADOS:
echo  -------------------
echo  [+] Nuevo archivo: static/js/notificaciones.js
echo  [+] Actualizado: static/css/click-fix-critical.css
echo  [+] Actualizado: templates/base_dashboard.html
echo.
echo  COMO PROBAR:
echo  ------------
echo  1. Presiona cualquier tecla para iniciar el servidor
echo  2. Abre tu navegador en: http://127.0.0.1:8000
echo  3. Inicia sesion con tu usuario
echo  4. Presiona F12 para abrir la consola del navegador
echo  5. Busca los mensajes que empiezan con [Notificaciones]
echo  6. Haz clic en el boton de la campana (notificaciones)
echo  7. Deberas ver el dropdown con tus 17 notificaciones
echo.
echo  DEBUGGING:
echo  ----------
echo  - Si no funciona, limpia el cache: Ctrl + Shift + Delete
echo  - Verifica la consola (F12) para errores
echo  - Los mensajes deben empezar con: [Notificaciones]
echo.
echo  PRUEBA RAPIDA:
echo  --------------

