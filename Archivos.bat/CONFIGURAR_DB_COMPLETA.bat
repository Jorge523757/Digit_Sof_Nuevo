@echo off
chcp 65001 > nul
echo ================================================================================
echo DIGT SOFT - Configuración Completa de Base de Datos
echo ================================================================================
echo.
echo Este script:
echo    1. Aplica las migraciones de Django
echo    2. Crea un superusuario automáticamente (si no existe)
echo.
pause

echo.
echo [1/2] Aplicando migraciones...
echo.
python manage.py migrate

echo.
echo [2/2] Creando superusuario...
echo.
python inicializar_db.py

echo.
echo ================================================================================
echo ✅ Configuración completada
echo ================================================================================
echo.
echo Credenciales de acceso:
echo    Usuario: admin
echo    Contraseña: admin123
echo.
echo Para iniciar el servidor:
echo    python manage.py runserver
echo.
echo Panel de administración:
echo    http://localhost:8000/admin/
echo.
pause

