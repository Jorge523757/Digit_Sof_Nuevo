@echo off
chcp 65001 >nul
color 0E
cls

echo ╔════════════════════════════════════════════════════════════════════╗
echo ║                                                                    ║
echo ║          🔓 SOLUCIÓN: CAMPOS DE LOGIN BLOQUEADOS                  ║
echo ║                                                                    ║
echo ╚════════════════════════════════════════════════════════════════════╝
echo.

python desbloquear_campos_login.py

echo.
echo ════════════════════════════════════════════════════════════════════
echo  📌 PRÓXIMOS PASOS:
echo ════════════════════════════════════════════════════════════════════
echo.
echo  1. Abre el navegador en: http://localhost:8000/usuarios/login/
echo  2. Presiona F12 (Herramientas de desarrollador)
echo  3. Ve a la pestaña "Console"
echo  4. Pega el script mostrado arriba
echo  5. Presiona ENTER
echo  6. ¡Los campos deberían funcionar!
echo.
echo ════════════════════════════════════════════════════════════════════
echo.
pause

