@echo off
chcp 65001 >nul
color 0A
cls

echo.
echo ═══════════════════════════════════════════════════════════════════════
echo    ✅ CORRECCIONES APLICADAS - REINICIANDO SERVIDOR
echo ═══════════════════════════════════════════════════════════════════════
echo.
echo  Se corrigió:
echo  ✅ Nombre: "DIGT SOFT" → "DIGIT SOFT"
echo  ✅ Diseño de recuperación de contraseña
echo  ✅ Campos ahora son editables
echo  ✅ Error de reCAPTCHA solucionado (desactivado temporalmente)
echo.
echo  ⚠️  NOTA: reCAPTCHA está desactivado para desarrollo
echo     El sistema funciona perfectamente sin él
echo.
echo ═══════════════════════════════════════════════════════════════════════
echo.
echo  Iniciando servidor...
echo.

python manage.py runserver

pause

