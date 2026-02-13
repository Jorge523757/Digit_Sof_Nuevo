@echo off
chcp 65001 > nul
cls
color 0C

echo.
echo ═══════════════════════════════════════════════════════════════════
echo   🔧 REPARAR REGISTROS DUPLICADOS Y ERRORES DE GOOGLE OAUTH
echo ═══════════════════════════════════════════════════════════════════
echo.
echo   Este script solucionará:
echo.
echo   ✅ Error de UNIQUE constraint (clientes.numero_documento)
echo   ✅ Registros duplicados en la base de datos
echo   ✅ Perfiles sin cliente asociado
echo   ✅ Problemas de Google OAuth
echo.
echo ═══════════════════════════════════════════════════════════════════
echo.

pause

echo.
echo 🔄 Ejecutando reparación...
echo.

python reparar_registros_duplicados.py

echo.
echo ═══════════════════════════════════════════════════════════════════
echo.
echo ✅ REPARACIÓN COMPLETADA
echo.
echo ═══════════════════════════════════════════════════════════════════
echo.
echo 📋 PRÓXIMOS PASOS:
echo.
echo 1. Intenta registrarte de nuevo como cliente
echo 2. O inicia sesión con Google
echo.
echo El sistema ahora debería funcionar correctamente.
echo.
echo ═══════════════════════════════════════════════════════════════════
echo.

pause

