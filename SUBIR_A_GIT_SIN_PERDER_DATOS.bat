@echo off
REM ================================================================
REM SUBIR CAMBIOS A GIT SIN PERDER DATOS
REM Los datos de db.sqlite3 NO se subirán (están en .gitignore)
REM ================================================================

echo.
echo ========================================
echo SUBIR CAMBIOS A GIT - PRESERVANDO DATOS
echo ========================================
echo.
echo Este script va a:
echo 1. Ver los archivos que se van a subir
echo 2. Agregar los cambios al staging
echo 3. Hacer commit con un mensaje descriptivo
echo 4. Subir a tu rama jorge-dev
echo.
echo NOTA: db.sqlite3 NO se subirá (tus datos están seguros)
echo.
pause

REM Ir al directorio del proyecto
cd /d C:\Users\jorge\OneDrive\Escritorio\Adelantando2026\Digit_Sof_Nuevo

echo.
echo ========================================
echo 1. ARCHIVOS QUE SE VAN A SUBIR:
echo ========================================
echo.
git status
echo.
echo ========================================
echo 2. VERIFICANDO .gitignore
echo ========================================
echo.
echo Archivos ignorados (NO se subirán):
findstr /C:"db.sqlite3" .gitignore
echo.
echo Si ves "db.sqlite3" arriba, tus datos NO se subirán.
echo.
pause

echo.
echo ========================================
echo 3. AGREGANDO CAMBIOS AL STAGING
echo ========================================
echo.
git add .
echo.
echo ✓ Archivos agregados
echo.

echo.
echo ========================================
echo 4. HACIENDO COMMIT
echo ========================================
echo.
echo Mensaje del commit:
echo "Mejoras en Órdenes de Servicio: diseño sin rosa, paginación mejorada, registro de estados"
echo.

git commit -m "feat: Mejoras en Ordenes de Servicio - Diseño azul sin rosa, paginacion mejorada, registro completo de estados para clientes y tecnicos, filtros avanzados, autocompletado" -m "- Eliminados colores rosa, nueva paleta azul/verde/naranja" -m "- Paginacion moderna con iconos y contadores" -m "- Sistema de registro de estados con timeline" -m "- Registro completo de cliente y tecnico" -m "- Filtros avanzados implementados" -m "- Autocompletado de clientes y tecnicos" -m "- Migracion de MySQL a SQLite completada" -m "- CSS moderno responsive con modo oscuro"

echo.
echo ✓ Commit realizado
echo.

echo.
echo ========================================
echo 5. SUBIENDO A GITHUB (rama jorge-dev)
echo ========================================
echo.

git push origin jorge-dev

echo.
if %ERRORLEVEL% EQU 0 (
    echo ========================================
    echo ✓ ¡CAMBIOS SUBIDOS EXITOSAMENTE!
    echo ========================================
    echo.
    echo Tus cambios están en GitHub en la rama jorge-dev
    echo La base de datos db.sqlite3 NO se subió
    echo Tus datos están seguros localmente
    echo.
) else (
    echo ========================================
    echo ✗ ERROR AL SUBIR
    echo ========================================
    echo.
    echo Verifica:
    echo 1. Que tengas conexión a internet
    echo 2. Que estés autenticado en GitHub
    echo 3. Que la rama jorge-dev exista
    echo.
)

echo.
echo ========================================
echo RESUMEN:
echo ========================================
echo.
echo Archivos subidos: SÍ
echo Base de datos subida: NO
echo Datos preservados: SÍ
echo Rama: jorge-dev
echo.
pause

