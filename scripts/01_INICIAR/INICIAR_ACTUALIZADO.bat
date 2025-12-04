@echo off
cls
color 0A
echo ============================================================
echo    DIGIT SOFT - Sistema Actualizado y Profesional
echo ============================================================
echo.
echo [CORRECCIONES APLICADAS]
echo  - Ventas: numero_venta automatico
echo  - Facturas: campos opcionales configurados
echo  - Capacitaciones: plantillas corregidas
echo  - Admin mejorado con fieldsets organizados
echo  - Migraciones aplicadas correctamente
echo.
echo ============================================================
echo.
echo Deteniendo procesos anteriores...
taskkill /F /IM python.exe 2>nul
timeout /t 2 /nobreak >nul
echo.
echo Activando entorno virtual...
cd /d C:\Users\jorge\OneDrive\Escritorio\DigtSoft\Digit_Sof_Nuevo
call .\venv\Scripts\activate.bat
echo.
echo Verificando sistema...
python manage.py check
echo.
echo ============================================================
echo    COMO USAR EL SISTEMA
echo ============================================================
echo.
echo 1. ADMIN PANEL: http://127.0.0.1:8000/admin/
echo    Login: admin / admin123
echo.
echo 2. AGREGAR DATOS (ORDEN RECOMENDADO):
echo    a) Clientes (ya existen 5)
echo    b) Tecnicos (ya existen 2-3)
echo    c) Productos -^> IMPORTANTE: Ver instrucciones abajo
echo    d) Proveedores
echo    e) Ventas (con productos agregados)
echo    f) Facturas (relacionadas a ventas)
echo    g) Ordenes de Servicio
echo    h) Compras
echo    i) Equipos
echo    j) Capacitaciones
echo.
echo ============================================================
echo    PARA AGREGAR PRODUCTOS (IMPORTANTE):
echo ============================================================
echo    1. Ve a Admin -^> Productos -^> Agregar producto
echo    2. Campos obligatorios:
echo       - Nombre producto: Ej "Laptop HP Pavilion"
echo       - Codigo SKU: Ej "LAP-HP-001" (unico)
echo       - Precio venta: Ej 1500000
echo       - Precio compra: Ej 1200000
echo       - Stock actual: Ej 10
echo    3. Guarda
echo.
echo ============================================================
echo    PARA AGREGAR VENTAS:
echo ============================================================
echo    1. Primero DEBES tener Productos y Clientes
echo    2. Admin -^> Ventas -^> Agregar venta
echo    3. Selecciona Cliente, Estado, Canal
echo    4. En "Detalles de venta" agrega productos
echo    5. El numero de venta se genera automaticamente
echo.
echo ============================================================
echo    INICIANDO SERVIDOR
echo ============================================================
echo.

python manage.py runserver

pause

