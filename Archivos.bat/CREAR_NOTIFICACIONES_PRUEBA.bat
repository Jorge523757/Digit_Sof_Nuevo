@echo off
chcp 65001 >nul
title DIGITSOFT - Crear Notificaciones de Prueba
color 0B

echo.
echo ═══════════════════════════════════════════════════════════════════
echo  DIGITSOFT - CREAR NOTIFICACIONES DE PRUEBA
echo ═══════════════════════════════════════════════════════════════════
echo.
echo Este script creará notificaciones de prueba para visualizar
echo el sistema de notificaciones en funcionamiento.
echo.
echo ═══════════════════════════════════════════════════════════════════
echo.

python crear_notificaciones_prueba.py

echo.
echo ═══════════════════════════════════════════════════════════════════
echo.
echo Presiona cualquier tecla para cerrar...
pause >nul

