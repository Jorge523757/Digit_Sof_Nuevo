@echo off
chcp 65001 >nul
echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║           DIGITSOFT - CONFIGURACIÓN MYSQL                    ║
echo ║                GUÍA DE INSTALACIÓN                           ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.
echo ═══════════════════════════════════════════════════════════════
echo 📋 PASOS PARA CONFIGURAR MYSQL
echo ═══════════════════════════════════════════════════════════════
echo.
echo PASO 1: INSTALAR MYSQL
echo ────────────────────────────────────────────────────────────────
echo Si no tienes MySQL instalado:
echo 1. Descarga MySQL Community Server:
echo    https://dev.mysql.com/downloads/mysql/
echo 2. Instala MySQL
echo 3. Anota la password de root que configuraste
echo.
echo PASO 2: VERIFICAR QUE MYSQL ESTÉ CORRIENDO
echo ────────────────────────────────────────────────────────────────
echo - Abre Servicios de Windows (services.msc)
echo - Busca "MySQL80" o similar
echo - Verifica que esté "En ejecución"
echo - Si no, haz clic derecho ^> Iniciar
echo.
echo PASO 3: INSTALAR MYSQLCLIENT PARA PYTHON
echo ────────────────────────────────────────────────────────────────
echo Ejecuta:
echo    INSTALAR_MYSQLCLIENT.bat
echo.
echo O manualmente:
echo    pip install mysqlclient
echo.
echo PASO 4: CREAR LA BASE DE DATOS
echo ────────────────────────────────────────────────────────────────
echo Ejecuta:
echo    CREAR_DATABASE_MYSQL.bat
echo.
echo O manualmente:
echo    mysql -u root -p ^< crear_database_mysql.sql
echo.
echo PASO 5: EJECUTAR MIGRACIONES
echo ────────────────────────────────────────────────────────────────
echo Ejecuta:
echo    MIGRAR_MYSQL.bat
echo.
echo O manualmente:
echo    python manage.py migrate
echo.
echo PASO 6: CREAR SUPERUSUARIO
echo ────────────────────────────────────────────────────────────────
echo Ejecuta:
echo    python manage.py createsuperuser
echo.
echo PASO 7: INICIAR EL SERVIDOR
echo ────────────────────────────────────────────────────────────────
echo Ejecuta:
echo    python manage.py runserver
echo.
echo ═══════════════════════════════════════════════════════════════
echo 🔧 SOLUCIÓN DE PROBLEMAS
echo ═══════════════════════════════════════════════════════════════
echo.
echo ❌ ERROR: "mysqlclient install failed"
echo ────────────────────────────────────────────────────────────────
echo SOLUCIÓN 1: Instalar Visual C++ Build Tools
echo    https://visualstudio.microsoft.com/visual-cpp-build-tools/
echo.
echo SOLUCIÓN 2: Descargar wheel precompilado
echo    https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient
echo    pip install mysqlclient-X.X.X-cpXX-cpXX-win_amd64.whl
echo.
echo ❌ ERROR: "Access denied for user"
echo ────────────────────────────────────────────────────────────────
echo - Verifica usuario y password en config/settings.py
echo - Usuario: digitsoft_user
echo - Password: digitsoft2024
echo.
echo ❌ ERROR: "Can't connect to MySQL server"
echo ────────────────────────────────────────────────────────────────
echo - Verifica que MySQL esté corriendo
echo - Abre services.msc y busca MySQL80
echo - Inicia el servicio si está detenido
echo.
echo ═══════════════════════════════════════════════════════════════
echo 📊 DATOS DE CONEXIÓN
echo ═══════════════════════════════════════════════════════════════
echo Base de datos: digitsoft_db
echo Usuario:       digitsoft_user
echo Password:      digitsoft2024
echo Host:          localhost
echo Puerto:        3306
echo Charset:       utf8mb4
echo ═══════════════════════════════════════════════════════════════
echo.
pause

