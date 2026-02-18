@echo off
echo ============================================
echo  DIGITSOFT - Verificacion de Validaciones
echo ============================================
echo.
echo Iniciando servidor y verificando modulos...
echo.

cd /d "%~dp0"

echo [1/3] Verificando archivos de validaciones...
if exist "usuarios\validators.py" (
    echo    OK - Validadores de usuario creados
) else (
    echo    ERROR - Falta archivo validators.py
)

if exist "usuarios\forms.py" (
    echo    OK - Formularios de usuario actualizados
) else (
    echo    ERROR - Falta archivo forms.py
)

echo.
echo [2/3] Verificando configuracion...
findstr /C:"ValidadorLongitudMinima" config\settings.py >nul
if %errorlevel%==0 (
    echo    OK - Validadores configurados en settings.py
) else (
    echo    ADVERTENCIA - Validadores no encontrados en settings
)

echo.
echo [3/3] Iniciando servidor Django...
echo.
echo ============================================
echo  El servidor se iniciara en unos segundos
echo ============================================
echo.
echo Prueba las siguientes funcionalidades:
echo.
echo 1. Login: http://localhost:8000/usuarios/login/
echo 2. Registro: http://localhost:8000/usuarios/registro/
echo 3. Productos: http://localhost:8000/productos/
echo 4. Clientes: http://localhost:8000/clientes/
echo 5. Ventas: http://localhost:8000/ventas/
echo 6. Compras: http://localhost:8000/compras/
echo.
echo ============================================
echo  Presiona Ctrl+C para detener el servidor
echo ============================================
echo.

python manage.py runserver 0.0.0.0:8000

pause

