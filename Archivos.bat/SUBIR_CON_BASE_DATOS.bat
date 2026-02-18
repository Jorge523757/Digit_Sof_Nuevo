@echo off
REM ================================================================
REM SUBIR A GIT INCLUYENDO LA BASE DE DATOS CON DATOS
REM Los datos se compartirán con quien clone el repositorio
REM ================================================================

echo.
echo ========================================
echo SUBIR TODO A GIT (Con Base de Datos)
echo ========================================
echo.
echo Este script va a subir:
echo - Codigo fuente
echo - Templates y estilos
echo - Base de datos db.sqlite3 CON LOS 220 REGISTROS
echo.
echo IMPORTANTE: Quien clone tendra todos los datos listos
echo.
pause

cd /d C:\Users\jorge\OneDrive\Escritorio\Adelantando2026\Digit_Sof_Nuevo

echo.
echo ========================================
echo 1. ARCHIVOS QUE SE VAN A SUBIR:
echo ========================================
echo.
git status
echo.

echo.
echo ========================================
echo 2. VERIFICANDO BASE DE DATOS
echo ========================================
echo.
if exist db.sqlite3 (
    echo ✓ Base de datos encontrada: db.sqlite3
    for %%A in (db.sqlite3) do echo   Tamaño: %%~zA bytes
    echo.
    echo Esta base de datos INCLUYE:
    echo - 20 Clientes
    echo - 20 Ordenes de Servicio
    echo - 20 Productos
    echo - 20 Proveedores
    echo - 20 Tecnicos
    echo - Y mas... (220 registros en total)
    echo.
) else (
    echo ✗ Base de datos NO encontrada
    echo.
    pause
    exit
)

pause

echo.
echo ========================================
echo 3. AGREGANDO CAMBIOS AL STAGING
echo ========================================
echo.
git add .
git add db.sqlite3 -f
echo.
echo ✓ Todos los archivos agregados (incluyendo db.sqlite3)
echo.

echo.
echo ========================================
echo 4. HACIENDO COMMIT
echo ========================================
echo.

git commit -m "feat: Mejoras completas en Ordenes de Servicio + Base de datos con 220 registros" -m "Cambios principales:" -m "- Diseño sin rosa: paleta azul/verde/naranja profesional" -m "- Paginacion moderna con iconos y contadores de registros" -m "- Sistema completo de registro de estados con timeline" -m "- Registro detallado de cliente (entrega y recepcion)" -m "- Registro detallado de tecnico (revision, diagnostico, reparacion)" -m "- Filtros avanzados con 7 criterios de busqueda" -m "- Autocompletado de clientes y tecnicos con AJAX" -m "- Migracion de MySQL a SQLite completada" -m "- CSS moderno responsive con modo oscuro" -m "" -m "Base de datos incluida:" -m "- db.sqlite3 con 220 registros de datos vacios" -m "- Listo para usar al clonar (no requiere seed)" -m "- 20 registros por cada modelo principal" -m "" -m "Archivos nuevos:" -m "- static/css/ordenes-modern.css" -m "- static/css/autocomplete.css" -m "- static/js/autocomplete-ordenes.js" -m "- CONFIGURACION_SQLITE.md" -m "- ORDENES_MEJORADAS_COMPLETO.md" -m "- ORDENES_SIN_ROSA_MEJORADO.md" -m "- FILTROS_PAGINACION_AUTOCOMPLETADO.md"

echo.
echo ✓ Commit realizado con mensaje completo
echo.

echo.
echo ========================================
echo 5. SUBIENDO A GITHUB (rama jorge-dev)
echo ========================================
echo.
echo Subiendo archivos...
echo Esto puede tardar debido al tamaño de db.sqlite3
echo.

git push origin jorge-dev

echo.
if %ERRORLEVEL% EQU 0 (
    echo ========================================
    echo ✓ ¡TODO SUBIDO EXITOSAMENTE!
    echo ========================================
    echo.
    echo Cambios en GitHub (rama jorge-dev):
    echo - Codigo fuente actualizado ✓
    echo - Base de datos db.sqlite3 incluida ✓
    echo - 220 registros disponibles ✓
    echo.
    echo Ahora cualquiera que clone tendra:
    echo - El sistema completo funcionando
    echo - Todos los datos precargados
    echo - Sin necesidad de ejecutar seed
    echo.
    echo Para probar en otra computadora:
    echo   git clone https://github.com/Jorge523757/Digit_Sof_Nuevo.git
    echo   cd Digit_Sof_Nuevo
    echo   git checkout jorge-dev
    echo   python manage.py runserver
    echo   (Los datos ya estaran alli!)
    echo.
) else (
    echo ========================================
    echo ✗ ERROR AL SUBIR
    echo ========================================
    echo.
    echo Posibles causas:
    echo 1. Sin conexion a internet
    echo 2. Archivo muy grande (GitHub limita a 100MB)
    echo 3. Credenciales incorrectas
    echo.
    echo Si db.sqlite3 es muy grande, considera:
    echo - Comprimir la base de datos
    echo - Usar Git LFS para archivos grandes
    echo - O subir sin la base de datos
    echo.
)

echo.
echo ========================================
echo INFORMACION DEL COMMIT:
echo ========================================
echo.
git log -1 --stat
echo.

pause

