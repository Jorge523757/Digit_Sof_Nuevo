@echo off
echo ============================================
echo   DIGITSOFT - TIENDA CON BUSQUEDA DINAMICA
echo ============================================
echo.
echo [+] Iniciando servidor Django...
echo [+] URL: http://localhost:8000/tienda/
echo.
echo ============================================
echo   NUEVAS FUNCIONALIDADES:
echo ============================================
echo [✓] Busqueda dinamica en tiempo real
echo [✓] Filtros por categoria (sin recargar)
echo [✓] Ordenamiento dinamico
echo [✓] API endpoint: /tienda/api/buscar/
echo.
echo Presiona Ctrl+C para detener el servidor
echo ============================================
echo.

python manage.py runserver

pause

