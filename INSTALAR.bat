@echo off
chcp 65001 >nul
color 0B
cls

echo.
echo ══════════════════════════════════════════════════════════════
echo          INSTALACIÓN COMPLETA - DIGIT SOFT
echo ══════════════════════════════════════════════════════════════
echo.

cd /d "%~dp0"

echo [1/6] Verificando Python...
python --version
if errorlevel 1 (
    echo ❌ Python no está instalado
    pause
    exit /b 1
)
echo ✅ Python encontrado
echo.

echo [2/6] Creando entorno virtual...
if exist venv (
    echo ⚠️  Entorno virtual ya existe, omitiendo...
) else (
    python -m venv venv
    echo ✅ Entorno virtual creado
)
echo.

echo [3/6] Activando entorno virtual...
call venv\Scripts\activate.bat
echo ✅ Entorno activado
echo.

echo [4/6] Instalando dependencias...
pip install -r requirements.txt
echo ✅ Dependencias instaladas
echo.

echo [5/6] Aplicando migraciones...
python manage.py migrate
echo ✅ Base de datos configurada
echo.

echo [6/6] Creando superusuario...
python crear_superusuario.py
echo.

echo ══════════════════════════════════════════════════════════════
echo          ✅ INSTALACIÓN COMPLETADA
echo ══════════════════════════════════════════════════════════════
echo.
echo Para iniciar el servidor:
echo    python manage.py runserver
echo.
echo Luego accede a: http://127.0.0.1:8000
echo.
echo Usuario: admin
echo Contraseña: admin123
echo.
echo ══════════════════════════════════════════════════════════════
echo.
pause

