@echo off
chcp 65001 > nul
cls
color 0B

echo.
echo ═══════════════════════════════════════════════════════════════════
echo   🚀 CONFIGURACIÓN AUTOMÁTICA - DIGIT SOFT
echo ═══════════════════════════════════════════════════════════════════
echo.
echo   Este script configurará automáticamente el proyecto
echo   Después de clonar el repositorio
echo.
echo ═══════════════════════════════════════════════════════════════════
echo.

pause

python setup_proyecto.py

echo.
echo ═══════════════════════════════════════════════════════════════════
echo.
echo ✅ ¡CONFIGURACIÓN COMPLETADA!
echo.
echo 📋 CREDENCIALES:
echo    Usuario: admin
echo    Contraseña: admin123
echo.
echo 🚀 PARA INICIAR:
echo    python manage.py runserver
echo.
echo ═══════════════════════════════════════════════════════════════════
echo.

pause

