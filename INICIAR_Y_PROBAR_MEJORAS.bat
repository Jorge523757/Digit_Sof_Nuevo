@echo off
chcp 65001 >nul
color 0A
title ✅ INICIAR Y PROBAR - Nuevas Funcionalidades

echo.
echo ═══════════════════════════════════════════════════════════
echo   🎉 DIGITSOFT - NUEVAS FUNCIONALIDADES IMPLEMENTADAS
echo ═══════════════════════════════════════════════════════════
echo.
echo   ✅ 1. Filtros con deshacer individual
echo   ✅ 2. Registro de productos mejorado
echo.
echo ═══════════════════════════════════════════════════════════
echo.

:menu
echo.
echo ┌─────────────────────────────────────────────────────────┐
echo │              MENÚ DE OPCIONES                           │
echo └─────────────────────────────────────────────────────────┘
echo.
echo   [1] 🚀 Iniciar servidor Django
echo   [2] 🧪 Ver guía de pruebas
echo   [3] 📖 Abrir documentación
echo   [4] 🌐 Abrir tienda en navegador
echo   [5] 📝 Abrir formulario de productos
echo   [6] ❌ Salir
echo.
echo ═══════════════════════════════════════════════════════════
set /p opcion="Selecciona una opción (1-6): "

if "%opcion%"=="1" goto iniciar_servidor
if "%opcion%"=="2" goto ver_pruebas
if "%opcion%"=="3" goto documentacion
if "%opcion%"=="4" goto abrir_tienda
if "%opcion%"=="5" goto abrir_formulario
if "%opcion%"=="6" goto salir
echo.
echo ❌ Opción inválida. Intenta de nuevo.
timeout /t 2 >nul
cls
goto menu

:iniciar_servidor
cls
echo.
echo ═══════════════════════════════════════════════════════════
echo   🚀 INICIANDO SERVIDOR DJANGO
echo ═══════════════════════════════════════════════════════════
echo.
echo ⏳ Verificando migraciones...
python manage.py makemigrations
python manage.py migrate
echo.
echo ✅ Migraciones aplicadas
echo.
echo ═══════════════════════════════════════════════════════════
echo   📡 Servidor corriendo en: http://localhost:8000
echo ═══════════════════════════════════════════════════════════
echo.
echo   🔗 URLs importantes:
echo   ├─ Tienda: http://localhost:8000/tienda/
echo   ├─ Admin: http://localhost:8000/admin/
echo   ├─ Dashboard: http://localhost:8000/dashboard/
echo   └─ Productos: http://localhost:8000/productos/crear/
echo.
echo ═══════════════════════════════════════════════════════════
echo.
echo 💡 Presiona Ctrl+C para detener el servidor
echo.
python manage.py runserver
pause
goto menu

:ver_pruebas
cls
echo.
echo ═══════════════════════════════════════════════════════════
echo   🧪 GUÍA DE PRUEBAS
echo ═══════════════════════════════════════════════════════════
echo.
echo ╔═══════════════════════════════════════════════════════════╗
echo ║  PRUEBA 1: FILTROS CON DESHACER INDIVIDUAL               ║
echo ╚═══════════════════════════════════════════════════════════╝
echo.
echo   1️⃣ Abre: http://localhost:8000/tienda/
echo.
echo   2️⃣ Busca "laptop" en el campo de búsqueda
echo      → Debe aparecer chip azul: "🔍 Búsqueda: laptop [×]"
echo.
echo   3️⃣ Click en el botón [×] del chip
echo      → El chip desaparece con animación
echo      → La búsqueda se elimina
echo      → Aparece notificación
echo.
echo   4️⃣ Selecciona una categoría (ej: Laptops)
echo      → Aparece chip cyan: "🏷️ Categoría: Laptops [×]"
echo.
echo   5️⃣ Click en [×] del chip de categoría
echo      → Vuelve a "Todas las categorías"
echo.
echo   6️⃣ Cambia ordenamiento a "Precio: Mayor a Menor"
echo      → Aparece chip verde: "🔄 Precio: Mayor a Menor [×]"
echo.
echo   7️⃣ Aplica 3 filtros a la vez (búsqueda + categoría + orden)
echo      → Deben aparecer los 3 chips de colores
echo.
echo   8️⃣ Click en "Limpiar todo"
echo      → Todos los chips desaparecen
echo      → Vuelve al estado inicial
echo.
echo ═══════════════════════════════════════════════════════════
echo.
pause
cls
echo.
echo ╔═══════════════════════════════════════════════════════════╗
echo ║  PRUEBA 2: REGISTRO DE PRODUCTOS MEJORADO                ║
echo ╚═══════════════════════════════════════════════════════════╝
echo.
echo   1️⃣ Inicia sesión como staff o admin
echo.
echo   2️⃣ Abre: http://localhost:8000/productos/crear/
echo.
echo   3️⃣ Intenta guardar sin llenar campos
echo      → Aparece alerta roja con lista de errores
echo      → Campos con error tienen borde rojo
echo.
echo   4️⃣ Completa estos campos obligatorios:
echo      ├─ Nombre: Laptop Dell Inspiron 15
echo      ├─ SKU: TEST-DELL-001
echo      ├─ Descripción: Laptop de prueba
echo      ├─ Precio compra: 1000
echo      ├─ Precio venta: 1500
echo      ├─ Stock actual: 10
echo      ├─ Stock mínimo: 5
echo      └─ Stock máximo: 50
echo.
echo   5️⃣ Click en "Crear Producto"
echo      → Botón cambia a "Guardando..." con spinner
echo      → Aparece mensaje: "✅ Producto creado exitosamente"
echo      → Redirecciona a página de detalle
echo.
echo   6️⃣ Verifica en lista de productos
echo      → El producto "Laptop Dell Inspiron 15" debe aparecer
echo.
echo ═══════════════════════════════════════════════════════════
echo.
pause
cls
goto menu

:documentacion
cls
echo.
echo ═══════════════════════════════════════════════════════════
echo   📖 DOCUMENTACIÓN DISPONIBLE
echo ═══════════════════════════════════════════════════════════
echo.
echo   📄 1. MEJORAS_FILTROS_Y_PRODUCTOS.md
echo      → Documentación técnica completa
echo      → Código y ejemplos
echo.
echo   📖 2. GUIA_RAPIDA_NUEVAS_FUNCIONALIDADES.md
echo      → Guía de usuario
echo      → Instrucciones paso a paso
echo.
echo   🧪 3. PROBAR_MEJORAS_FILTROS_PRODUCTOS.bat
echo      → Script de pruebas
echo      → Checklist de verificación
echo.
echo   ✅ 4. RESUMEN_IMPLEMENTACION_COMPLETA.md
echo      → Resumen ejecutivo
echo      → Métricas y resultados
echo.
echo ═══════════════════════════════════════════════════════════
echo.
echo ¿Qué documento deseas abrir?
echo.
echo [1] Documentación técnica
echo [2] Guía de usuario
echo [3] Script de pruebas
echo [4] Resumen completo
echo [5] Volver al menú
echo.
set /p doc="Selecciona (1-5): "

if "%doc%"=="1" start MEJORAS_FILTROS_Y_PRODUCTOS.md
if "%doc%"=="2" start GUIA_RAPIDA_NUEVAS_FUNCIONALIDADES.md
if "%doc%"=="3" start PROBAR_MEJORAS_FILTROS_PRODUCTOS.bat
if "%doc%"=="4" start RESUMEN_IMPLEMENTACION_COMPLETA.md
if "%doc%"=="5" goto menu

timeout /t 2 >nul
goto menu

:abrir_tienda
cls
echo.
echo ═══════════════════════════════════════════════════════════
echo   🌐 ABRIENDO TIENDA EN NAVEGADOR
echo ═══════════════════════════════════════════════════════════
echo.
echo   URL: http://localhost:8000/tienda/
echo.
echo   ⚠️  Asegúrate de que el servidor esté corriendo
echo.
echo   💡 Prueba los filtros con deshacer individual:
echo      ├─ Buscar productos
echo      ├─ Filtrar por categoría
echo      ├─ Cambiar ordenamiento
echo      └─ Eliminar filtros individualmente
echo.
start http://localhost:8000/tienda/
echo   ✅ Navegador abierto
echo.
timeout /t 3 >nul
goto menu

:abrir_formulario
cls
echo.
echo ═══════════════════════════════════════════════════════════
echo   📝 ABRIENDO FORMULARIO DE PRODUCTOS
echo ═══════════════════════════════════════════════════════════
echo.
echo   URL: http://localhost:8000/productos/crear/
echo.
echo   ⚠️  Debes estar autenticado como staff/admin
echo.
echo   💡 Prueba la validación mejorada:
echo      ├─ Intenta guardar sin datos
echo      ├─ Observa mensajes de error
echo      ├─ Completa campos obligatorios
echo      └─ Verifica el guardado exitoso
echo.
start http://localhost:8000/productos/crear/
echo   ✅ Navegador abierto
echo.
timeout /t 3 >nul
goto menu

:salir
cls
echo.
echo ═══════════════════════════════════════════════════════════
echo   👋 GRACIAS POR USAR DIGITSOFT
echo ═══════════════════════════════════════════════════════════
echo.
echo   ✅ Nuevas funcionalidades implementadas:
echo      ├─ Filtros con deshacer individual
echo      └─ Registro de productos mejorado
echo.
echo   📚 Consulta la documentación para más información
echo.
echo ═══════════════════════════════════════════════════════════
echo.
timeout /t 3 >nul
exit

