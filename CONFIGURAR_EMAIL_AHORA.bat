@echo off
chcp 65001 > nul
color 0B
cls

echo.
echo ═══════════════════════════════════════════════════════════════════════════
echo.
echo           ⚡ CONFIGURAR ENVÍO DE EMAILS - 2 MINUTOS ⚡
echo.
echo ═══════════════════════════════════════════════════════════════════════════
echo.
echo.
echo   Este script te guiará paso a paso para configurar el envío de emails.
echo.
echo   Después de configurar:
echo.
echo   ✅ Los códigos de recuperación llegarán automáticamente al email
echo   ✅ Funciona para TODOS los usuarios (100, 1000, 10000+)
echo   ✅ Totalmente automático - sin intervención manual
echo.
echo ═══════════════════════════════════════════════════════════════════════════
echo.
pause
echo.

python CONFIGURAR_EMAIL_SIMPLE.py

echo.
echo ═══════════════════════════════════════════════════════════════════════════
echo.
pause
