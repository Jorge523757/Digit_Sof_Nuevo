@echo off
chcp 65001 >nul
color 0C
cls

echo.
echo ╔════════════════════════════════════════════════════════════════════════╗
echo ║                                                                        ║
echo ║          🔧 SOLUCIÓN DEFINITIVA - ERROR RECAPTCHA RESUELTO              ║
echo ║                                                                        ║
echo ╚════════════════════════════════════════════════════════════════════════╝
echo.
echo.
echo ═══════════════════════════════════════════════════════════════════════
echo  📋 PROBLEMA RESUELTO
echo ═══════════════════════════════════════════════════════════════════════
echo.
echo  ❌ Error anterior:
echo     PlantillaNoExiste: django_recaptcha/widget_v2_checkbox.html
echo.
echo  ✅ Solución aplicada:
echo     • reCAPTCHA desactivado temporalmente
echo     • Template comentado correctamente
echo     • Formularios funcionan sin reCAPTCHA
echo.
echo ═══════════════════════════════════════════════════════════════════════
echo  🔧 CAMBIOS REALIZADOS
echo ═══════════════════════════════════════════════════════════════════════
echo.
echo  ✅ usuarios/forms.py - reCAPTCHA desactivado
echo  ✅ templates/usuarios/login.html - Campo oculto
echo  ✅ templates/usuarios/recuperar_paso1.html - Campo oculto
echo  ✅ "DIGT SOFT" → "DIGIT SOFT" corregido
echo.
echo ═══════════════════════════════════════════════════════════════════════
echo  🚀 INICIANDO SERVIDOR LIMPIO
echo ═══════════════════════════════════════════════════════════════════════
echo.
echo  El servidor se iniciará en unos segundos...
echo  Luego prueba: http://127.0.0.1:8000/usuarios/recuperar/
echo.
echo  ⚠️  IMPORTANTE:
echo     • NO hay reCAPTCHA (desactivado para desarrollo)
echo     • Campos son editables
echo     • Códigos aparecen en esta consola
echo.
timeout /t 3 >nul

echo  Limpiando archivos temporales...
python manage.py clean_pyc 2>nul

echo  Iniciando servidor Django...
echo.
echo ═══════════════════════════════════════════════════════════════════════
echo.

python manage.py runserver

pause

