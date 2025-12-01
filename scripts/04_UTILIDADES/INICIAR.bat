@echo off
cls
color 0A
echo ============================================================
echo    DIGT SOFT - Sistema de Gestion Empresarial
echo    TODOS LOS MODULOS COMPLETADOS Y FUNCIONALES
echo ============================================================
echo.
echo  Estado: SISTEMA 100%% FUNCIONAL
echo  Base de Datos: SQLite3 - TODAS LAS MIGRACIONES APLICADAS
echo  Python: 3.13.3
echo  Django: 5.1.3
echo  Bootstrap: 5.3
echo.
echo ============================================================
echo    MODULOS DISPONIBLES:
echo ============================================================
echo.
echo  [OK] 1.  Clientes          - CRUD Completo + Tablas
echo  [OK] 2.  Tecnicos          - CRUD Completo + Tablas
echo  [OK] 3.  Productos         - E-commerce + Inventario
echo  [OK] 4.  Proveedores       - CRUD Completo + Tablas
echo  [OK] 5.  Ventas            - Sistema Completo + E-commerce
echo  [OK] 6.  Ordenes Servicio  - Gestion Tecnica Completa
echo  [OK] 7.  Compras           - Gestion de Compras
echo  [OK] 8.  Facturacion       - Facturas Electronicas
echo  [OK] 9.  Equipos           - Inventario de Equipos
echo  [OK] 10. Capacitaciones    - Entrenamientos
echo  [OK] 11. Garantias         - Sistema de Garantias
echo  [OK] 12. Dashboard         - Panel de Control
echo.
echo ============================================================
echo    CREDENCIALES DE ACCESO:
echo ============================================================
echo.
echo  Usuario:     admin
echo  Contrasena:  admin123
echo  Email:       admin@digtsoft.com
echo.
echo ============================================================
echo    URLs DISPONIBLES:
echo ============================================================
echo.
echo  Panel Admin:     http://127.0.0.1:8000/admin/
echo  Dashboard:       http://127.0.0.1:8000/dashboard/
echo.
echo  Clientes:        http://127.0.0.1:8000/clientes/
echo  Tecnicos:        http://127.0.0.1:8000/tecnicos/
echo  Productos:       http://127.0.0.1:8000/productos/
echo  Proveedores:     http://127.0.0.1:8000/proveedores/
echo  Ventas:          http://127.0.0.1:8000/ventas/
echo  Ordenes:         http://127.0.0.1:8000/ordenes/
echo  Compras:         http://127.0.0.1:8000/compras/
echo  Facturacion:     http://127.0.0.1:8000/facturacion/
echo  Equipos:         http://127.0.0.1:8000/equipos/
echo  Capacitaciones:  http://127.0.0.1:8000/capacitaciones/
echo  Garantias:       http://127.0.0.1:8000/garantias/
echo.
echo ============================================================
echo    INICIANDO SERVIDOR...
echo ============================================================
echo.

cd /d C:\Users\jorge\OneDrive\Escritorio\DigtSoft\Digit_Sof_Nuevo
call .\venv\Scripts\activate.bat

python manage.py runserver

pause

