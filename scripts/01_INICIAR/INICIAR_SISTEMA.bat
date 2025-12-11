@echo off
echo ============================================================
echo    DIGIT SOFT - Sistema de Gestion Empresarial
echo    Verificacion y Ejecucion del Sistema
echo ============================================================
echo.

cd /d C:\Users\jorge\OneDrive\Escritorio\DigtSoft\Digit_Sof_Nuevo

echo [1/4] Activando entorno virtual...
call .\venv\Scripts\activate.bat

echo.
echo [2/4] Verificando sistema...
python manage.py check --deploy 2>nul
if %errorlevel% neq 0 (
    echo.
    echo Verificacion basica...
    python manage.py check
)

echo.
echo [3/4] Aplicando migraciones pendientes...
python manage.py migrate --no-input

echo.
echo [4/4] Iniciando servidor de desarrollo...
echo.
echo ============================================================
echo    SISTEMA LISTO!
echo ============================================================
echo.
echo  Panel de Administracion:
echo  URL: http://127.0.0.1:8000/admin/
echo  Usuario: admin
echo  Contrasena: admin123
echo.
echo  Modulos disponibles:
echo  - Clientes:    http://127.0.0.1:8000/clientes/
echo  - Tecnicos:    http://127.0.0.1:8000/tecnicos/
echo  - Productos:   http://127.0.0.1:8000/productos/
echo  - Proveedores: http://127.0.0.1:8000/proveedores/
echo  - Ventas:      http://127.0.0.1:8000/ventas/
echo  - Ordenes:     http://127.0.0.1:8000/ordenes/
echo  - Garantias:   http://127.0.0.1:8000/garantias/
echo  - Dashboard:   http://127.0.0.1:8000/dashboard/
echo.
echo ============================================================
echo  Presiona Ctrl+C para detener el servidor
echo ============================================================
echo.

python manage.py runserver

pause

