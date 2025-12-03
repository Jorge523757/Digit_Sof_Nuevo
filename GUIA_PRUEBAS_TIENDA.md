# 🧪 GUÍA DE PRUEBAS - TIENDA E-COMMERCE

## ✅ Verificación de Correcciones

### 1. Iniciar el Servidor
```bash
python manage.py runserver
```

Deberías ver:
```
Starting development server at http://127.0.0.1:8000/
```

---

## 🛒 PRUEBA 1: Agregar al Carrito

### Pasos:
1. Abre tu navegador en: `http://127.0.0.1:8000/tienda/`
2. Asegúrate de estar logueado (si no, haz login primero)
3. Busca cualquier producto con stock disponible
4. Haz clic en el botón **"Agregar"** (azul con icono de carrito)

### ✅ Resultado Esperado:
- El botón debe cambiar a verde con texto "¡Agregado!"
- Debe aparecer una notificación verde en la parte superior: **"✅ [Producto] agregado al carrito"**
- El contador del carrito (icono en el header) debe aumentar
- Después de 2 segundos, el botón vuelve a su estado normal

### ❌ Si No Funciona:
- Abre la consola del navegador (F12)
- Verifica si hay errores en rojo
- Comparte los errores que veas

---

## 📊 PRUEBA 2: Filtros de Ordenamiento

### Pasos:
1. En la tienda, busca el selector "Ordenar por" en el panel izquierdo
2. Prueba cada opción:
   - **Nombre A-Z**: Los productos deben ordenarse alfabéticamente
   - **Precio: Menor a Mayor**: Deben aparecer los más baratos primero
   - **Precio: Mayor a Menor**: Deben aparecer los más caros primero
   - **Más Nuevos**: Los productos recientes primero
   - **Mayor Stock**: Los que tienen más unidades primero

### ✅ Resultado Esperado:
- La página debe recargar automáticamente
- Los productos deben reordenarse según tu selección
- La URL debe cambiar (ej: `?orden=precio_desc`)

### ❌ Si No Funciona:
- Verifica que el selector tenga opciones
- Abre la consola y busca errores

---

## 🏷️ PRUEBA 3: Filtros por Categoría

### Pasos:
1. En el panel izquierdo, busca la sección "Categorías"
2. Haz clic en cualquier categoría (ej: "Laptops", "Computadora", etc.)

### ✅ Resultado Esperado:
- La página debe recargar
- Solo deben mostrarse productos de esa categoría
- El nombre de la categoría debe aparecer en negrita
- La URL debe cambiar (ej: `?categoria=1`)

### ❌ Si No Funciona:
- Verifica que existan productos en esa categoría
- Revisa la consola del navegador

---

## 🔍 PRUEBA 4: Búsqueda de Productos

### Pasos:
1. En el header superior, busca la barra de búsqueda
2. Escribe el nombre de un producto (ej: "Lenovo", "HP", "Monitor")
3. Presiona Enter o haz clic en el botón de búsqueda

### ✅ Resultado Esperado:
- Debe aparecer un mensaje azul: "Resultados para 'tu búsqueda': X productos encontrados"
- Solo deben mostrarse productos que coincidan con tu búsqueda
- Debe haber un botón "Ver todos" para volver al catálogo completo

---

## 🛍️ PRUEBA 5: Ver Carrito

### Pasos:
1. Agrega al menos 2-3 productos diferentes al carrito
2. Haz clic en el icono del carrito en el header (arriba a la derecha)

### ✅ Resultado Esperado:
- Debes ser redirigido a: `http://127.0.0.1:8000/tienda/carrito/`
- Deben aparecer todos los productos que agregaste
- Debe mostrar:
  - Nombre del producto
  - Precio unitario
  - Cantidad
  - Subtotal (precio × cantidad)
  - Total general

---

## 📈 PRUEBA 6: Contador del Carrito

### Pasos:
1. Con el carrito vacío, el contador no debe verse (o debe mostrar 0)
2. Agrega 1 producto → el contador debe mostrar **1**
3. Agrega otro producto → el contador debe mostrar **2**
4. Agrega el mismo producto 2 veces más → el contador debe aumentar

### ✅ Resultado Esperado:
- El contador del carrito (badge rojo) debe actualizarse automáticamente
- El número debe reflejar la cantidad total de items

---

## ⚠️ PRUEBA 7: Validación de Stock

### Pasos:
1. Busca un producto con poco stock (ej: "Solo quedan 5")
2. Agrégalo varias veces hasta alcanzar el límite

### ✅ Resultado Esperado:
- Cuando llegues al stock máximo, debe aparecer una notificación amarilla:
  **"⚠️ Ya tienes el máximo disponible de [Producto] en tu carrito"**
- No debe permitir agregar más unidades de las disponibles

---

## 🚨 PROBLEMAS COMUNES Y SOLUCIONES

### Problema 1: "Error 404 - No encontrado"
**Solución**: 
- Verifica que la URL sea correcta: `http://127.0.0.1:8000/tienda/`
- Asegúrate de que el servidor esté corriendo

### Problema 2: "Error 500 - Server Error"
**Solución**:
- Revisa la terminal donde corre Django
- Busca el error en rojo (traceback)
- Comparte el error completo

### Problema 3: "CSRF token missing"
**Solución**:
- Limpia las cookies del navegador
- Recarga la página con Ctrl + Shift + R
- Asegúrate de estar usando el template correcto

### Problema 4: El botón "Agregar" no responde
**Solución**:
1. Abre la consola del navegador (F12)
2. Ve a la pestaña "Console"
3. Busca errores en rojo
4. Verifica que veas estos mensajes:
   ```
   🚀 Productos.html cargado
   ✅ DOM cargado - Inicializando...
   ```

### Problema 5: Los filtros no funcionan
**Solución**:
- Verifica que el selector tenga el ID correcto: `id="ordenar"`
- Abre la consola y busca errores de JavaScript
- Asegúrate de que la función `changeOrder()` esté definida

---

## 📱 PRUEBAS EN CONSOLA DEL NAVEGADOR

Abre la consola (F12) y ejecuta estos comandos para verificar:

```javascript
// Verificar que las funciones existen
console.log(typeof addToCart);        // Debe mostrar: "function"
console.log(typeof changeOrder);      // Debe mostrar: "function"
console.log(typeof getCookie);        // Debe mostrar: "function"

// Verificar CSRF token
console.log(getCookie('csrftoken'));  // Debe mostrar un token largo

// Simular agregar al carrito (cambia 1 por un ID real)
addToCart(1);
```

---

## 📋 CHECKLIST FINAL

Marca cada prueba que funcione correctamente:

- [ ] ✅ Agregar productos al carrito funciona
- [ ] ✅ Ordenamiento "Precio: Mayor a Menor" funciona
- [ ] ✅ Ordenamiento "Precio: Menor a Mayor" funciona
- [ ] ✅ Filtros por categoría funcionan
- [ ] ✅ Búsqueda de productos funciona
- [ ] ✅ Contador del carrito se actualiza
- [ ] ✅ Ver carrito muestra los productos correctamente
- [ ] ✅ Validación de stock funciona
- [ ] ✅ Notificaciones aparecen correctamente
- [ ] ✅ Botones cambian de estado al agregar

---

## 📸 Capturas de Pantalla Recomendadas

Si algo no funciona, toma capturas de:

1. **Pantalla completa de la tienda**
2. **Consola del navegador (F12 → Console)**
3. **Terminal donde corre Django**
4. **Error específico que veas**

---

## 🆘 SOPORTE

Si después de estas pruebas algo sigue sin funcionar:

1. Indica qué prueba específica falla
2. Comparte los mensajes de error de la consola
3. Comparte los logs del servidor Django
4. Indica qué navegador estás usando

---

**Fecha de Creación**: 2025-12-01  
**Versión**: 1.0  
**Estado**: Listo para Probar ✅

