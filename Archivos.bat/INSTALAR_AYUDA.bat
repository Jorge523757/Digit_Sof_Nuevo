@echo off
chcp 65001 >nul
cls
color 0B
echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║  📚 MÓDULO DE AYUDA Y SOPORTE - DIGIT SOFT                    ║
echo ║  Instalación Rápida                                           ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

cd /d "%~dp0"

echo ✅ Módulo de ayuda listo para instalar
echo.
echo 📋 Se creará:
echo    - Sistema de tickets de ayuda
echo    - Base de conocimientos (FAQs)
echo    - Panel de administración
echo    - 6 categorías iniciales
echo    - 10 preguntas frecuentes
echo.
pause
echo.

echo ════════════════════════════════════════════════════════════════
echo 📋 PASO 1: Aplicando migraciones...
echo ════════════════════════════════════════════════════════════════
echo.

python manage.py makemigrations
python manage.py migrate

echo.
echo ════════════════════════════════════════════════════════════════
echo 📋 PASO 2: Creando datos iniciales...
echo ════════════════════════════════════════════════════════════════
echo.

python crear_datos_ayuda.py

echo.
echo ════════════════════════════════════════════════════════════════
echo ✅ INSTALACIÓN COMPLETADA
echo ════════════════════════════════════════════════════════════════
echo.
echo 🎉 El módulo de ayuda está listo!
echo.
echo 🌐 URLs disponibles:
echo    http://127.0.0.1:8000/ayuda/              - Centro de ayuda
echo    http://127.0.0.1:8000/ayuda/faqs/         - Preguntas frecuentes
echo    http://127.0.0.1:8000/ayuda/tickets/      - Mis tickets
echo.
echo 💡 Próximo paso:
echo    Inicia el servidor: python manage.py runserver
echo.
pause

