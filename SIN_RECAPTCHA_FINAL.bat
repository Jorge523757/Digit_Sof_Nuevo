@echo off
chcp 65001 >nul
color 0C
cls

echo.
echo ╔════════════════════════════════════════════════════════════════════════╗
echo ║                                                                        ║
echo ║          🔧 SOLUCIÓN FINAL - reCAPTCHA COMPLETAMENTE ELIMINADO          ║
echo ║                                                                        ║
echo ╚════════════════════════════════════════════════════════════════════════╝
echo.
echo.
echo ═══════════════════════════════════════════════════════════════════════
echo  ✅ CAMBIOS APLICADOS
echo ═══════════════════════════════════════════════════════════════════════
echo.
echo  ✅ Vista simplificada (sin formulario Django)
echo  ✅ Template con campo HTML simple
echo  ✅ NO se valida reCAPTCHA
echo  ✅ Solo requiere email válido
echo.
echo ═══════════════════════════════════════════════════════════════════════
echo  🎯 CÓMO FUNCIONA AHORA
echo ═══════════════════════════════════════════════════════════════════════
echo.
echo  1. Ingresas tu email
echo  2. Click en "Enviar Código"
echo  3. ¡Funciona! Sin validación de reCAPTCHA
echo  4. Código aparece en la consola
echo.
echo ═══════════════════════════════════════════════════════════════════════
echo  🚀 INICIANDO SERVIDOR
echo ═══════════════════════════════════════════════════════════════════════
echo.
timeout /t 2 >nul

echo  Abriendo navegador en 3 segundos...
timeout /t 3 >nul

start http://127.0.0.1:8000/usuarios/recuperar/

echo.
echo  ✅ Navegador abierto
echo  📧 Ingresa: davidcristancho160@gmail.com
echo  🔍 Código aparecerá en ESTA CONSOLA
echo.
echo ═══════════════════════════════════════════════════════════════════════
echo  SERVIDOR CORRIENDO
echo ═══════════════════════════════════════════════════════════════════════
echo.

python manage.py runserver

pause

