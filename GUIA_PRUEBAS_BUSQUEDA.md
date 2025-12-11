# 🧪 GUÍA DE PRUEBAS - BÚSQUEDA DINÁMICA Y FILTROS

## 🚀 Cómo Iniciar

1. **Ejecutar el servidor:**
   ```
   Doble clic en: INICIAR_TIENDA_MEJORADA.bat
   O desde terminal: python manage.py runserver
   ```

2. **Abrir en el navegador:**
   ```
   http://localhost:8000/tienda/
   ```

---

## ✅ PRUEBAS A REALIZAR

### 1️⃣ **BÚSQUEDA DINÁMICA EN TIEMPO REAL**

**Objetivo:** Verificar que la búsqueda funciona sin recargar la página

**Pasos:**
1. En la barra de búsqueda superior, escribe: `laptop`
2. **Espera 0.5 segundos** sin presionar Enter
3. ✅ Los resultados deben aparecer automáticamente
4. ✅ Verás un spinner de carga brevemente
5. ✅ El contador muestra "X productos encontrados"

**Prueba adicional:**
- Borra el texto → Los productos se restauran
- Escribe `hp` → Filtra solo productos HP
- Escribe `core i5` → Busca en especificaciones

---

### 2️⃣ **FILTROS POR CATEGORÍA (SIN RECARGAR)**

**Objetivo:** Verificar que los filtros de categoría funcionan dinámicamente

**Pasos:**
1. En el sidebar izquierdo, haz clic en cualquier categoría (ej: "Laptops")
2. ✅ La página NO debe recargar
3. ✅ Los productos se filtran instantáneamente
4. ✅ La categoría seleccionada aparece en negrita y azul
5. Haz clic en "Todas las categorías"
6. ✅ Los productos se restauran

**Prueba combinada:**
- Selecciona categoría "Laptops"
- En el buscador escribe `hp`
- ✅ Debe mostrar solo laptops HP

---

### 3️⃣ **ORDENAMIENTO DINÁMICO**

**Objetivo:** Verificar que el ordenamiento funciona sin recargar

**Pasos:**
1. En el sidebar, busca el select de "Ordenar por"
2. Selecciona "Precio: Menor a Mayor"
3. ✅ Los productos se reordenan instantáneamente
4. ✅ NO hay recarga de página
5. Prueba cada opción:
   - Nombre A-Z
   - Precio: Menor a Mayor
   - Precio: Mayor a Menor
   - Más Nuevos
   - Mayor Stock

**Prueba combinada:**
- Busca `laptop`
- Selecciona categoría "Laptops"
- Ordena por "Precio: Mayor a Menor"
- ✅ Debe mostrar laptops ordenados por precio descendente

---

### 4️⃣ **INDICADORES VISUALES**

**Objetivo:** Verificar feedback visual

**Pasos:**
1. Escribe algo en el buscador
2. ✅ Verás un spinner con texto "Buscando productos..."
3. Si no hay resultados:
   - ✅ Aparece mensaje "No se encontraron productos"
   - ✅ Botón "Ver todos los productos"
4. Con resultados:
   - ✅ Contador: "12 productos encontrados"
   - ✅ Estadísticas actualizadas en sidebar

---

### 5️⃣ **API ENDPOINT (PRUEBA TÉCNICA)**

**Objetivo:** Verificar que la API funciona correctamente

**Método 1 - Navegador:**
Abre estas URLs directamente:
```
http://localhost:8000/tienda/api/buscar/
http://localhost:8000/tienda/api/buscar/?q=laptop
http://localhost:8000/tienda/api/buscar/?categoria=1
http://localhost:8000/tienda/api/buscar/?q=hp&orden=precio_asc
```

**Método 2 - Consola del Navegador:**
1. Presiona F12 → Pestaña Console
2. Pega este código:
```javascript
fetch('/tienda/api/buscar/?q=laptop')
  .then(r => r.json())
  .then(data => console.log(data));
```
3. ✅ Debes ver el JSON con productos

**Respuesta esperada:**
```json
{
  "success": true,
  "productos": [...],
  "total": 12
}
```

---

### 6️⃣ **TARJETAS DE PRODUCTO MEJORADAS**

**Objetivo:** Verificar que las tarjetas se generan correctamente

**Verifica que cada producto muestra:**
- ✅ Imagen del producto (o icono si no tiene)
- ✅ Marca en gris
- ✅ Nombre del producto
- ✅ Descripción corta
- ✅ Precio en formato colombiano (ej: $2.500.000)
- ✅ Badge de "OFERTA" si tiene precio mayorista
- ✅ Indicador de stock con color:
  - 🟢 Verde: Más de 10 unidades
  - 🟡 Amarillo: 5-10 unidades
  - 🔴 Rojo: Menos de 5 unidades
- ✅ Botón "Agregar" (si hay stock y está autenticado)
- ✅ Botón "Ver detalles" (ícono de ojo)

---

### 7️⃣ **BÚSQUEDA CON ENTER**

**Objetivo:** Verificar que funciona con tecla Enter

**Pasos:**
1. Escribe en el buscador: `laptop`
2. Presiona Enter
3. ✅ Debe buscar inmediatamente (sin esperar 0.5s)

---

### 8️⃣ **RESPONSIVE (MÓVIL)**

**Objetivo:** Verificar que funciona en móvil

**Pasos:**
1. Presiona F12 → Toggle device toolbar (Ctrl+Shift+M)
2. Selecciona un dispositivo móvil
3. ✅ El layout se adapta
4. ✅ La búsqueda sigue funcionando
5. ✅ Los filtros están accesibles

---

### 9️⃣ **PERFORMANCE Y CARGA**

**Objetivo:** Verificar tiempos de respuesta

**Pasos:**
1. Abre F12 → Pestaña Network
2. Escribe algo en el buscador
3. Busca la petición a `/tienda/api/buscar/`
4. ✅ Tiempo de respuesta < 500ms
5. ✅ Status: 200 OK
6. ✅ Response Type: application/json

---

### 🔟 **AGREGAR AL CARRITO DESDE BÚSQUEDA**

**Objetivo:** Verificar que el botón de agregar funciona

**Pasos:**
1. Realiza una búsqueda
2. Haz clic en "Agregar" de algún producto
3. ✅ Debe aparecer notificación de éxito
4. ✅ Contador del carrito se actualiza
5. ✅ Botón cambia a "¡Agregado!" brevemente

---

## 🐛 POSIBLES PROBLEMAS Y SOLUCIONES

### ❌ **La búsqueda no funciona**
**Solución:**
1. Abre la consola del navegador (F12)
2. Busca errores en rojo
3. Verifica que la URL de la API sea correcta:
   - Debe ser: `/tienda/api/buscar/`
   - NO: `/productos/api/buscar/`

### ❌ **Los filtros recargan la página**
**Solución:**
1. Verifica que el JavaScript esté cargado
2. Revisa que los event listeners estén activos
3. Limpia caché del navegador (Ctrl+Shift+R)

### ❌ **Error 404 en API**
**Solución:**
1. Verifica que `ecommerce_urls.py` tenga:
   ```python
   path('api/buscar/', productos_views.buscar_productos_api, ...)
   ```
2. Reinicia el servidor

### ❌ **Las imágenes no aparecen**
**Solución:**
1. Verifica que los productos tengan imágenes en el admin
2. Revisa que MEDIA_URL esté configurado correctamente

---

## 📊 CHECKLIST COMPLETO

Marca cada funcionalidad probada:

- [ ] Búsqueda dinámica funciona
- [ ] Búsqueda con delay (0.5s)
- [ ] Búsqueda con Enter
- [ ] Filtro por categorías sin recargar
- [ ] Ordenamiento sin recargar
- [ ] Combinación búsqueda + filtros
- [ ] Indicadores de carga
- [ ] Contador de resultados actualizado
- [ ] Mensaje cuando no hay resultados
- [ ] API endpoint funciona
- [ ] Tarjetas de producto correctas
- [ ] Formato de precios colombiano
- [ ] Indicadores de stock con colores
- [ ] Botón agregar al carrito funciona
- [ ] Responsive en móvil
- [ ] Performance < 500ms
- [ ] Sin errores en consola

---

## 🎯 RESULTADO ESPERADO

Si todas las pruebas pasan, deberías tener:

✅ **Búsqueda instantánea** mientras escribes
✅ **Filtros que funcionan** sin recargar la página
✅ **Experiencia fluida** similar a Amazon o MercadoLibre
✅ **Sin errores** en consola del navegador
✅ **Responsive** en todos los dispositivos
✅ **Rápido** (< 500ms por búsqueda)

---

## 📞 SOPORTE

Si encuentras algún problema:
1. Revisa la consola del navegador (F12)
2. Revisa los logs del servidor
3. Verifica que todas las dependencias estén instaladas
4. Lee el archivo: `BUSQUEDA_DINAMICA_MEJORADA.md`

---

**Fecha:** 4 de Diciembre de 2025
**Versión:** 1.0 - Búsqueda Dinámica Completa

