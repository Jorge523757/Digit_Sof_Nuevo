@echo off
echo ============================================
echo   PRUEBAS AUTOMATICAS - API DE BUSQUEDA
echo ============================================
echo.
echo [!] IMPORTANTE: El servidor debe estar corriendo
echo [!] URL: http://localhost:8000
echo.
pause
echo.
echo [+] Ejecutando pruebas...
echo.

python test_api_busqueda.py

echo.
echo ============================================
pause

