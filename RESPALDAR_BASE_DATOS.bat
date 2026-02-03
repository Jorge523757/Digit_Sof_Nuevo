@echo off
REM ================================================================
REM HACER RESPALDO DE LA BASE DE DATOS ANTES DE SUBIR A GIT
REM ================================================================

echo.
echo ========================================
echo RESPALDO DE BASE DE DATOS
echo ========================================
echo.

cd /d C:\Users\jorge\OneDrive\Escritorio\Adelantando2026\Digit_Sof_Nuevo

REM Crear carpeta de respaldos si no existe
if not exist "respaldos" mkdir respaldos

REM Obtener fecha y hora para el nombre del respaldo
for /f "tokens=2 delims==" %%I in ('wmic os get localdatetime /value') do set datetime=%%I
set fecha=%datetime:~0,8%
set hora=%datetime:~8,6%
set timestamp=%fecha%_%hora%

echo.
echo Creando respaldo...
echo Fecha: %fecha:~0,4%-%fecha:~4,2%-%fecha:~6,2%
echo Hora: %hora:~0,2%:%hora:~2,2%:%hora:~4,2%
echo.

REM Copiar base de datos
copy db.sqlite3 "respaldos\db_backup_%timestamp%.sqlite3" >nul

if %ERRORLEVEL% EQU 0 (
    echo ✓ Respaldo creado exitosamente
    echo.
    echo Archivo: respaldos\db_backup_%timestamp%.sqlite3
    echo Tamaño:
    dir /s "respaldos\db_backup_%timestamp%.sqlite3" | findstr "db_backup"
    echo.
    echo ========================================
    echo RESPALDOS EXISTENTES:
    echo ========================================
    echo.
    dir /b respaldos\*.sqlite3
    echo.
    echo ✓ Ahora puedes subir a Git sin preocupaciones
    echo.
) else (
    echo ✗ Error al crear respaldo
    echo Verifica que el archivo db.sqlite3 exista
    echo.
)

pause

