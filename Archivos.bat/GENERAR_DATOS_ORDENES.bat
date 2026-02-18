@echo off
chcp 65001 > nul
echo ================================================================================
echo DIGT SOFT - Generar Datos de Órdenes de Servicio
echo ================================================================================
echo.
echo Este script genera órdenes de servicio de prueba en la base de datos MySQL
echo.
echo IMPORTANTE: Los datos se guardarán permanentemente en MySQL
echo.
pause

echo.
echo Ejecutando generador de órdenes...
echo.

python generar_datos_ordenes.py

echo.
echo ================================================================================
echo Proceso completado
echo ================================================================================
echo.
pause

