@echo off
chcp 65001 >nul
color 0C
echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║  ⚠️  ERROR: VERIFICACIÓN EN 2 PASOS NO ACTIVADA               ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.
echo El email NO puede enviarse porque Google rechaza las credenciales.
echo.
echo ════════════════════════════════════════════════════════════════
echo.
echo 🔴 PROBLEMA DETECTADO:
echo.
echo    La cuenta: davidcristancho160@gmail.com
echo    NO tiene la Verificación en 2 Pasos activada correctamente
echo.
echo ════════════════════════════════════════════════════════════════
echo.
echo ✅ SOLUCIÓN (5 MINUTOS):
echo.
echo    PASO 1: Activa Verificación en 2 Pasos
echo    ────────────────────────────────────────
echo.
echo    1. Abre: https://myaccount.google.com/security
echo    2. Busca: "Verificación en dos pasos"
echo    3. Haz clic en "Comenzar"
echo    4. Sigue el asistente (usa tu teléfono)
echo    5. Completa la activación
echo.
echo    PASO 2: Genera Nueva Contraseña de Aplicación
echo    ───────────────────────────────────────────────
echo.
echo    1. Abre: https://myaccount.google.com/apppasswords
echo    2. Escribe: DIGIT SOFT
echo    3. Haz clic en "Crear"
echo    4. Copia la contraseña de 16 caracteres SIN espacios
echo.
echo    PASO 3: Ejecuta Este Script de Nuevo
echo    ────────────────────────────────────────
echo.
echo    Vuelve a ejecutar: CONFIGURAR_EMAIL_PROFESIONAL.bat
echo    Y pega la NUEVA contraseña cuando te la pida
echo.
echo ════════════════════════════════════════════════════════════════
echo.
echo ¿Quieres que abra las páginas necesarias? (S/N)
set /p ABRIR=^>

if /i "%ABRIR%"=="S" (
    echo.
    echo ✅ Abriendo páginas de Google...
    start https://myaccount.google.com/security
    timeout /t 2 >nul
    start https://myaccount.google.com/apppasswords
    echo.
    echo 📝 SIGUE ESTOS PASOS:
    echo.
    echo    1. En la primera pestaña: Activa "Verificación en 2 pasos"
    echo    2. En la segunda pestaña: Genera contraseña de aplicación
    echo    3. Copia la contraseña SIN espacios
    echo    4. Ejecuta de nuevo: CONFIGURAR_EMAIL_PROFESIONAL.bat
    echo.
)

echo.
echo Presiona cualquier tecla para cerrar...
pause >nul

