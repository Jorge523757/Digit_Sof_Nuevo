@echo off
chcp 65001 > nul
cls
echo.
echo ╔════════════════════════════════════════════════════════════════════════════╗
echo ║                                                                            ║
echo ║           ⚡ SOLUCIÓN RÁPIDA - CÓDIGO DE RECUPERACIÓN                      ║
echo ║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝
echo.
echo.
echo 🔍 PROBLEMA:
echo ═══════════════════════════════════════════════════════════════════════════
echo   No te llega el email con el código de 6 dígitos para recuperar contraseña
echo.
echo.
echo ✅ SOLUCIONES:
echo ═══════════════════════════════════════════════════════════════════════════
echo.
echo   OPCIÓN 1: VER EL CÓDIGO EN LA CONSOLA DE DJANGO (RÁPIDO)
echo   ──────────────────────────────────────────────────────────────────────
echo   1. Asegúrate de que el servidor Django esté corriendo
echo   2. En la consola donde corre Django, verás algo como:
echo.
echo      ══════════════════════════════════════════════════════════════
echo      ✅ EMAIL DE RECUPERACIÓN ENVIADO
echo      ══════════════════════════════════════════════════════════════
echo      Para: tu_email@gmail.com
echo      Usuario: tu_usuario
echo.
echo          🔢 CÓDIGO DE VERIFICACIÓN: 123456
echo.
echo      ⏰ Válido hasta: 14:30:00
echo      ══════════════════════════════════════════════════════════════
echo.
echo   3. Copia ese código de 6 dígitos
echo   4. Pégalo en la página de recuperación
echo.
echo.
echo   OPCIÓN 2: CONFIGURAR GMAIL PARA ENVÍO REAL (RECOMENDADO)
echo   ──────────────────────────────────────────────────────────────────────
echo   1. Ejecuta: CONFIGURAR_EMAIL_GMAIL.bat
echo   2. Sigue las instrucciones para obtener contraseña de aplicación
echo   3. El script configurará todo automáticamente
echo   4. Los códigos llegarán por email en segundos
echo.
echo.
echo   OPCIÓN 3: RECUPERAR CÓDIGO DESDE BASE DE DATOS
echo   ──────────────────────────────────────────────────────────────────────
echo   1. Ejecuta: python ver_codigos_recuperacion.py
echo   2. Verás todos los códigos activos con sus emails
echo   3. Busca tu email y usa el código más reciente
echo.
echo.
echo 📝 PASOS DETALLADOS PARA OPCIÓN 1 (LA MÁS RÁPIDA):
echo ═══════════════════════════════════════════════════════════════════════════
echo.
echo   1. Abre otra ventana de PowerShell/CMD
echo   2. Ve a la carpeta del proyecto:
echo      cd "C:\Users\jorge\OneDrive\Escritorio\Adelantando2026\Digit_Sof_Nuevo"
echo.
echo   3. Activa el entorno virtual (si usas uno):
echo      .\venv\Scripts\activate
echo.
echo   4. Inicia el servidor:
echo      python manage.py runserver
echo.
echo   5. En tu navegador, ve a la página de recuperación de contraseña
echo.
echo   6. Ingresa tu email y solicita el código
echo.
echo   7. MIRA LA CONSOLA donde corre Django
echo      ¡Ahí aparecerá el código de 6 dígitos!
echo.
echo   8. Copia ese código y úsalo en la página
echo.
echo.
echo 🚀 ¿QUIERES QUE LOS EMAILS LLEGUEN DE VERDAD?
echo ═══════════════════════════════════════════════════════════════════════════
echo.
echo   Ejecuta: CONFIGURAR_EMAIL_GMAIL.bat
echo.
echo   Esto configurará Gmail para que:
echo   ✅ Los códigos lleguen por email en 5-30 segundos
echo   ✅ No necesites ver la consola
echo   ✅ Funcione como cualquier sistema profesional
echo.
echo.
pause

