@echo off
chcp 65001 > nul
echo ================================================================================
echo DIGT SOFT - Crear Superusuario Automáticamente
echo ================================================================================
echo.
echo Este script crea un superusuario predeterminado si no existe.
echo.
echo Credenciales por defecto:
echo    Usuario: admin
echo    Email: admin@digitsoft.com
echo    Contraseña: admin123
echo.
echo ⚠️  IMPORTANTE: Cambia la contraseña después del primer login!
echo.
pause

echo.
echo Creando superusuario...
echo.

python manage.py crear_superusuario

echo.
echo ================================================================================
echo Proceso completado
echo ================================================================================
echo.
echo Para acceder al panel de administración:
echo    1. Inicia el servidor: python manage.py runserver
echo    2. Visita: http://localhost:8000/admin/
echo    3. Usuario: admin
echo    4. Contraseña: admin123
echo.
pause

