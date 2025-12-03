echo.
echo 6. Abre el carrito (icono superior derecha)
echo.
echo 7. Verifica:
echo    - 🎨 Renderizando item...
echo    - ✅ Carrito renderizado
echo.
echo 8. RESULTADO: Debes ver la IMAGEN del producto
echo.
echo ========================================
echo.
pause
@echo off
echo ========================================
echo  PROBANDO SISTEMA DE IMAGENES CARRITO
echo ========================================
echo.
echo 1. Limpiando carrito anterior...
echo.

REM El navegador puede acceder a localStorage, pero no lo limpiamos aquí
REM ya que lo haremos desde la consola del navegador

echo 2. Iniciando servidor Django...
echo.
cd /d "%~dp0"
python manage.py runserver

echo.
echo ========================================
echo INSTRUCCIONES PARA PROBAR:
echo ========================================
echo.
echo 1. Abre: http://localhost:8000/ecommerce/productos/
echo.
echo 2. Presiona F12 para abrir la consola
echo.
echo 3. Busca estos mensajes:
echo    - 🚀 Sistema de imágenes del carrito v3.0 iniciado
echo    - ✅ X imágenes de productos mapeadas
echo.
echo 4. Haz clic en "Agregar" en cualquier producto
echo.
echo 5. Verifica en consola:
echo    - 🛒 Agregando producto...
echo    - ✅ Producto nuevo agregado al carrito

