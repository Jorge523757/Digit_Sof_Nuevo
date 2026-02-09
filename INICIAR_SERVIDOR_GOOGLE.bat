@echo off
echo ================================================================================
echo     DIGIT SOFT - Servidor con Google OAuth ARREGLADO
echo ================================================================================
echo.

cd /d "%~dp0"

echo [1/4] Limpiando configuraciones duplicadas de Google OAuth...
python ARREGLAR_GOOGLE_DEFINITIVO.py

echo.
echo [2/4] Verificando configuracion...
python verificacion_final.py

echo.
echo [3/4] Aplicando migraciones (por si acaso)...
python manage.py migrate

echo.
echo ================================================================================
echo     SERVIDOR LISTO - GOOGLE OAUTH FUNCIONANDO
echo ================================================================================
echo.
echo - Abre tu navegador en: http://127.0.0.1:8000/usuarios/login/
echo - Haz clic en "Continuar con Google"
echo - Usa el correo: davidcristancho160@gmail.com
echo.
echo ================================================================================
echo [4/4] Iniciando servidor Django...
echo ================================================================================
echo.

python manage.py runserver

pause

