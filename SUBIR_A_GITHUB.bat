@echo off
chcp 65001 >nul
color 0E
cls

echo.
echo ══════════════════════════════════════════════════════════════
echo          SUBIR PROYECTO A GITHUB - DIGIT SOFT
echo ══════════════════════════════════════════════════════════════
echo.

cd /d "%~dp0"

echo ⚠️  ANTES DE CONTINUAR:
echo.
echo 1. Crea un repositorio en GitHub (si no lo hiciste)
echo    https://github.com/new
echo.
echo 2. Nombre sugerido: digit-soft
echo.
echo 3. Marca como PRIVADO (recomendado)
echo.
echo 4. NO marques "Initialize with README"
echo.
pause

echo.
echo ══════════════════════════════════════════════════════════════
echo.

set /p GITHUB_USER="Ingresa tu usuario de GitHub: "
set /p REPO_NAME="Ingresa el nombre del repositorio (digit-soft): "

if "%REPO_NAME%"=="" set REPO_NAME=digit-soft

echo.
echo [1/5] Inicializando Git...
git init
echo ✅ Git inicializado
echo.

echo [2/5] Agregando archivos...
git add .
echo ✅ Archivos agregados
echo.

echo [3/5] Creando commit inicial...
git commit -m "Initial commit: Sistema DIGIT SOFT completo con seguridad implementada"
echo ✅ Commit creado
echo.

echo [4/5] Conectando con GitHub...
git remote add origin https://github.com/%GITHUB_USER%/%REPO_NAME%.git
echo ✅ Conectado a GitHub
echo.

echo [5/5] Subiendo archivos...
echo.
echo ⏳ Esto puede tardar unos minutos...
echo.
git branch -M main
git push -u origin main

if errorlevel 1 (
    echo.
    echo ❌ Error al subir. Posibles causas:
    echo    - Credenciales incorrectas
    echo    - Repositorio no existe
    echo    - Sin conexión a internet
    echo.
    echo Intenta manualmente:
    echo    git push -u origin main
    echo.
) else (
    echo.
    echo ══════════════════════════════════════════════════════════════
    echo          ✅ PROYECTO SUBIDO EXITOSAMENTE
    echo ══════════════════════════════════════════════════════════════
    echo.
    echo Tu proyecto está en:
    echo https://github.com/%GITHUB_USER%/%REPO_NAME%
    echo.
    echo Para clonar en otra computadora:
    echo    git clone https://github.com/%GITHUB_USER%/%REPO_NAME%.git
    echo    cd %REPO_NAME%
    echo    INSTALAR.bat
    echo.
)

echo ══════════════════════════════════════════════════════════════
echo.
pause

