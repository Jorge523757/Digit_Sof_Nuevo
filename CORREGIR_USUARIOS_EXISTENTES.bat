@echo off
echo ================================================================
echo CORRECCION DE USUARIOS EXISTENTES
echo ================================================================
echo.
echo Este script corregira los usuarios que fueron creados antes
echo de la actualizacion del sistema.
echo.
echo Creara los registros faltantes en las tablas:
echo  - clientes
echo  - tecnicos
echo  - proveedores
echo.
echo Y actualizara los permisos de administradores.
echo.
echo ================================================================
echo.

cd /d "%~dp0"

echo Ejecutando script de correccion...
echo.

python corregir_usuarios_existentes.py

echo.
echo ================================================================
echo PROCESO COMPLETADO
echo ================================================================
echo.
pause

