@echo off
cls
echo ========================================
echo DIGIT SOFT - INICIAR SISTEMA
echo Base de Datos: SQLite (db.sqlite3)
echo ========================================
echo.
echo El sistema ahora usa SQLite (sin necesidad de MySQL)
echo.
echo Iniciando servidor Django...
echo.
echo Abre tu navegador en:
echo http://127.0.0.1:8000
echo.
echo Presiona Ctrl+C para detener el servidor
echo.
echo ========================================
echo.

cd C:\Users\jorge\OneDrive\Escritorio\Adelantando2026\Digit_Sof_Nuevo
python manage.py runserver

pause

