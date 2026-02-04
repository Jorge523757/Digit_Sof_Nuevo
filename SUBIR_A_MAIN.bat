@echo off
chcp 65001 > nul
echo ================================================================================
echo DIGT SOFT - Subir Cambios a Main (SIN BORRAR DATOS DE MYSQL)
echo ================================================================================
echo.
echo Este script:
echo 1. Hace commit de los cambios en jorge-dev
echo 2. Cambia a la rama main
echo 3. Fusiona los cambios de jorge-dev
echo 4. Sube todo a GitHub
echo.
echo IMPORTANTE: Los datos de MySQL NO se suben (solo el código)
echo.
pause

echo.
echo [1/5] Verificando estado actual...
git status

echo.
echo [2/5] Agregando todos los archivos modificados...
git add -A

echo.
echo [3/5] Haciendo commit en jorge-dev...
git commit -m "✨ Sistema completo de órdenes de servicio mejorado - Diseño azul profesional (sin colores rosa) - Formulario completo para crear órdenes con 7 secciones - Formulario de edición con tracking de cambios - Vista de detalle con timeline visual de estados - Búsqueda avanzada con filtros de fecha - Historial completo de estados con responsables - Sistema de notificaciones automáticas - Registro de técnicos y fechas importantes - Paginación mejorada con diseño moderno - 40 órdenes de prueba generadas en MySQL - Script generador de datos (generar_datos_ordenes.py) - Documentación completa del sistema"

echo.
echo [4/5] Subiendo cambios de jorge-dev a GitHub...
git push origin jorge-dev

echo.
echo ================================================================================
echo CAMBIOS SUBIDOS A JORGE-DEV
echo ================================================================================
echo.
echo Los cambios están ahora en tu rama jorge-dev en GitHub
echo.
echo ¿Deseas fusionar con main? (S/N)
set /p RESPUESTA=
if /i "%RESPUESTA%"=="S" goto FUSIONAR
if /i "%RESPUESTA%"=="s" goto FUSIONAR
goto FIN

:FUSIONAR
echo.
echo [5a/7] Cambiando a rama main...
git checkout main

echo.
echo [5b/7] Actualizando main desde GitHub...
git pull origin main

echo.
echo [6/7] Fusionando jorge-dev con main...
git merge jorge-dev -m "Merge: Sistema completo de órdenes de servicio desde jorge-dev"

echo.
echo [7/7] Subiendo main actualizado a GitHub...
git push origin main

echo.
echo ================================================================================
echo ✅ PROCESO COMPLETADO
echo ================================================================================
echo.
echo Los cambios están ahora en:
echo - Rama jorge-dev (actualizada)
echo - Rama main (fusionada y actualizada)
echo.
echo Los datos de MySQL permanecen en tu computadora local
echo.
echo Volviendo a jorge-dev...
git checkout jorge-dev
goto FIN

:FIN
echo.
echo ================================================================================
echo Presiona cualquier tecla para salir...
pause >nul

