@echo off
echo ============================================
echo   PRUEBAS - FILTROS Y REGISTRO DE PRODUCTOS
echo ============================================
echo.
echo [!] IMPORTANTE: El servidor debe estar corriendo
echo [!] URL: http://localhost:8000
echo.
echo ============================================
echo   PRUEBAS AUTOMATICAS
echo ============================================
echo.
echo [1] Verificando estructura de archivos...
echo.

if exist "templates\ecommerce\productos.html" (
    echo [OK] Template de productos encontrado
) else (
    echo [ERROR] Template de productos NO encontrado
)

if exist "templates\productos\form.html" (
    echo [OK] Template de formulario encontrado
) else (
    echo [ERROR] Template de formulario NO encontrado
)

if exist "productos\views.py" (
    echo [OK] Views de productos encontrado
) else (
    echo [ERROR] Views de productos NO encontrado
)

if exist "productos\forms.py" (
    echo [OK] Forms de productos encontrado
) else (
    echo [ERROR] Forms de productos NO encontrado
)

echo.
echo ============================================
echo   PRUEBAS MANUALES REQUERIDAS
echo ============================================
echo.
echo === PRUEBA 1: FILTROS CON DESHACER ===
echo.
echo 1. Abrir navegador en: http://localhost:8000/tienda/
echo 2. Buscar "laptop" en el campo de busqueda
echo 3. Verificar que aparece un chip azul con "Busqueda: laptop"
echo 4. Hacer click en la X del chip
echo 5. Verificar que el filtro se elimina con animacion
echo.
echo 6. Seleccionar una categoria
echo 7. Verificar que aparece un chip cyan con el nombre
echo 8. Hacer click en la X del chip
echo 9. Verificar que vuelve a "Todas las categorias"
echo.
echo 10. Cambiar ordenamiento a "Precio: Mayor a Menor"
echo 11. Verificar que aparece un chip verde
echo 12. Hacer click en la X del chip
echo 13. Verificar que vuelve a "Nombre A-Z"
echo.
echo 14. Aplicar multiples filtros (busqueda + categoria + orden)
echo 15. Hacer click en "Limpiar todo"
echo 16. Verificar que todos los filtros se eliminan
echo.
pause
echo.
echo === PRUEBA 2: REGISTRO DE PRODUCTOS ===
echo.
echo 1. Iniciar sesion como staff/admin
echo 2. Ir a: http://localhost:8000/productos/crear/
echo 3. Intentar guardar sin llenar campos
echo 4. Verificar que aparecen mensajes de error
echo 5. Los campos con error deben tener borde rojo
echo.
echo 6. Completar solo el campo "Nombre del producto"
echo 7. Intentar guardar
echo 8. Verificar que pide los demas campos obligatorios
echo.
echo 9. Completar todos los campos obligatorios:
echo    - Nombre del producto: "Laptop Dell Test"
echo    - Codigo SKU: "TEST-001"
echo    - Descripcion: "Producto de prueba"
echo    - Precio de compra: 1000
echo    - Precio de venta: 1500
echo    - Stock actual: 10
echo    - Stock minimo: 5
echo    - Stock maximo: 50
echo.
echo 10. Hacer click en "Crear Producto"
echo 11. Verificar que aparece "Guardando..." con spinner
echo 12. Verificar mensaje de exito
echo 13. Verificar redireccion a pagina de detalle
echo.
echo 14. Ir a la lista de productos
echo 15. Verificar que el producto "Laptop Dell Test" aparece
echo.
pause
echo.
echo ============================================
echo   PRUEBAS DE VALIDACION
echo ============================================
echo.
echo === PRUEBA 3: VALIDACION EN TIEMPO REAL ===
echo.
echo 1. Volver al formulario de crear producto
echo 2. Escribir algo en "Nombre del producto"
echo 3. Borrar todo el texto
echo 4. Hacer click fuera del campo
echo 5. Verificar que aparece borde rojo
echo.
echo 6. Volver a escribir texto
echo 7. Verificar que el borde rojo desaparece
echo.
echo 8. Ingresar precio negativo en "Precio de compra"
echo 9. Intentar guardar
echo 10. Verificar que no permite guardar
echo.
pause
echo.
echo ============================================
echo   PRUEBAS DE ANIMACIONES
echo ============================================
echo.
echo === PRUEBA 4: ANIMACIONES DE FILTROS ===
echo.
echo 1. Ir a: http://localhost:8000/tienda/
echo 2. Aplicar un filtro de busqueda
echo 3. Observar animacion de aparicion del chip (fade in + scale)
echo 4. Pasar el cursor sobre el boton X del chip
echo 5. Verificar que rota y hace zoom
echo 6. Hacer click en el boton X
echo 7. Observar animacion de desaparicion (fade out + scale)
echo.
echo 8. Aplicar 3 filtros diferentes
echo 9. Pasar cursor sobre boton "Limpiar todo"
echo 10. Verificar efecto hover
echo 11. Hacer click en "Limpiar todo"
echo 12. Verificar que todos desaparecen con animacion
echo.
pause
echo.
echo ============================================
echo   CHECKLIST FINAL
echo ============================================
echo.
echo Marcar con [X] las funcionalidades que funcionan:
echo.
echo FILTROS:
echo [ ] Chip de busqueda aparece/desaparece
echo [ ] Chip de categoria aparece/desaparece
echo [ ] Chip de ordenamiento aparece/desaparece
echo [ ] Boton X elimina filtro individual
echo [ ] Boton "Limpiar todo" funciona
echo [ ] Animaciones son suaves
echo [ ] Notificaciones aparecen
echo.
echo REGISTRO DE PRODUCTOS:
echo [ ] Validacion de campos obligatorios
echo [ ] Mensajes de error claros
echo [ ] Campos con error resaltados en rojo
echo [ ] Validacion en tiempo real funciona
echo [ ] Boton "Guardando..." aparece
echo [ ] Producto se guarda correctamente
echo [ ] Redireccion funciona
echo [ ] Mensaje de exito aparece
echo.
echo VALIDACIONES:
echo [ ] No permite precios negativos
echo [ ] No permite stocks negativos
echo [ ] No permite campos vacios
echo [ ] Validacion de SKU unico
echo.
echo ============================================
echo.
echo [!] Si todas las funcionalidades funcionan correctamente,
echo     las mejoras estan implementadas con exito!
echo.
echo ============================================
pause

