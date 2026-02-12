@echo off
chcp 65001 >nul
color 0B
cls

echo ╔════════════════════════════════════════════════════════════════════╗
echo ║                                                                    ║
echo ║        🎯 CREAR MIGRACIONES - SISTEMA DE ÓRDENES DE SERVICIO      ║
echo ║                                                                    ║
echo ╚════════════════════════════════════════════════════════════════════╝
echo.
echo Este script creará las migraciones para los nuevos modelos.
echo.
pause

cls
echo.
echo ════════════════════════════════════════════════════════════════════
echo  📦 CREANDO MIGRACIONES...
echo ════════════════════════════════════════════════════════════════════
echo.

echo [1/4] Creando migraciones para ordenes...
python manage.py makemigrations ordenes

echo.
echo [2/4] Creando migraciones para tecnicos...
python manage.py makemigrations tecnicos

echo.
echo [3/4] Creando migraciones para notificaciones...
python manage.py makemigrations notificaciones

echo.
echo [4/4] Creando migraciones para reportes_dano...
python manage.py makemigrations reportes_dano

echo.
echo ════════════════════════════════════════════════════════════════════
echo  ✅ MIGRACIONES CREADAS
echo ════════════════════════════════════════════════════════════════════
echo.
echo ¿Deseas aplicar las migraciones ahora? (S/N)
set /p aplicar=

if /i "%aplicar%"=="S" (
    cls
    echo.
    echo ════════════════════════════════════════════════════════════════════
    echo  🚀 APLICANDO MIGRACIONES...
    echo ════════════════════════════════════════════════════════════════════
    echo.

    python manage.py migrate

    echo.
    echo ════════════════════════════════════════════════════════════════════
    echo  ✅ MIGRACIONES APLICADAS EXITOSAMENTE
    echo ════════════════════════════════════════════════════════════════════
    echo.
) else (
    echo.
    echo ℹ️ Migraciones creadas pero no aplicadas.
    echo    Para aplicarlas manualmente ejecuta: python manage.py migrate
    echo.
)

pause

