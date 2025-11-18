@echo off
echo ========================================
echo  INICIO RAPIDO - Sistema E-Commerce
echo  Digit Soft - Soluciones Informaticas
echo ========================================
echo.

echo [1/4] Limpiando cache de Python...
del /s /q __pycache__ >nul 2>&1
del /s /q *.pyc >nul 2>&1

echo [2/4] Aplicando migraciones...
python manage.py makemigrations
python manage.py migrate

echo [3/4] Verificando datos...
python -c "from productos.models import Producto; print(f'Productos disponibles: {Producto.objects.filter(activo=True, disponible_web=True).count()}')"

echo [4/4] Iniciando servidor...
echo.
echo ========================================
echo  SISTEMA LISTO!
echo ========================================
echo.
echo  Abrir en navegador:
echo  http://127.0.0.1:8000/
echo.
echo  URLs principales:
echo  - Inicio: http://127.0.0.1:8000/
echo  - Productos: Ver seccion en inicio
echo  - Detalle: http://127.0.0.1:8000/productos/detalle/ID/
echo  - Checkout: http://127.0.0.1:8000/checkout/checkout/
echo.
echo  Funciones en consola del navegador (F12):
echo  - verCarrito()
echo  - vaciarCarrito()
echo  - agregarAlCarrito(id)
echo  - verDetalle(id)
echo  - limpiarLocalStorage()
echo.
echo ========================================
echo.

python manage.py runserver

