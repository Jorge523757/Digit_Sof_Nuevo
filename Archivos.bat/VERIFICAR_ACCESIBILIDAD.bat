@echo off
color 0A
title Verificación Sistema de Accesibilidad - DIGT SOFT

echo.
echo ========================================================
echo   VERIFICACION DEL SISTEMA DE ACCESIBILIDAD
echo   DIGT SOFT - Sistema de Gestion Empresarial
echo ========================================================
echo.
echo Verificando archivos de accesibilidad...
echo.

REM Verificar archivos CSS
if exist "static\css\accessibility.css" (
    echo [OK] CSS de Accesibilidad encontrado
) else (
    echo [ERROR] Falta: static\css\accessibility.css
)

REM Verificar archivos JS
if exist "static\js\accessibility.js" (
    echo [OK] JavaScript de Accesibilidad encontrado
) else (
    echo [ERROR] Falta: static\js\accessibility.js
)

REM Verificar widget HTML
if exist "templates\includes\accessibility_widget.html" (
    echo [OK] Widget HTML encontrado
) else (
    echo [ERROR] Falta: templates\includes\accessibility_widget.html
)

REM Verificar base.html
if exist "templates\base.html" (
    echo [OK] Template base.html encontrado
) else (
    echo [ERROR] Falta: templates\base.html
)

REM Verificar base_dashboard.html
if exist "templates\base_dashboard.html" (
    echo [OK] Template base_dashboard.html encontrado
) else (
    echo [ERROR] Falta: templates\base_dashboard.html
)

REM Verificar documentacion
if exist "SISTEMA_ACCESIBILIDAD_COMPLETO.md" (
    echo [OK] Documentacion completa encontrada
) else (
    echo [AVISO] Falta documentacion completa
)

if exist "GUIA_RAPIDA_ACCESIBILIDAD.md" (
    echo [OK] Guia rapida encontrada
) else (
    echo [AVISO] Falta guia rapida
)

echo.
echo ========================================================
echo   VERIFICACION COMPLETADA
echo ========================================================
echo.
echo Para probar el sistema:
echo   1. Ejecuta: python manage.py runserver
echo   2. Abre tu navegador en: http://127.0.0.1:8000/
echo   3. Busca el boton flotante (♿) en la esquina inferior derecha
echo   4. Haz clic y prueba las opciones de accesibilidad
echo.
echo Atajos de teclado:
echo   Ctrl + Alt + D = Modo Oscuro
echo   Ctrl + Alt + + = Aumentar Texto
echo   Ctrl + Alt + - = Reducir Texto
echo   Ctrl + Alt + R = Restablecer Todo
echo.
echo ========================================================
echo.
pause

