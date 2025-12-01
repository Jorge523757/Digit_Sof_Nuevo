# 🧪 GUÍA RÁPIDA DE PRUEBAS - CARRITO

## ⚡ Inicio Rápido

### 1. Inicia el servidor
```bash
python manage.py runserver
```

### 2. Abre tu navegador
```
http://127.0.0.1:8000/tienda/carrito/
```

---

## ✅ PRUEBA 1: Eliminar Producto (30 segundos)

**Pasos:**
1. Busca cualquier producto en tu carrito
2. Haz clic en el botón rojo **"Eliminar"**
3. Aparecerá un modal elegante

**¿Qué debes ver?**
- ✅ Modal con fondo oscuro difuminado
- ✅ Icono de basura rojo
- ✅ Título: "¿Eliminar producto?"
- ✅ Dos botones: "Cancelar" y "Eliminar"

**Acción:**
4. Haz clic en **"Eliminar"**

**¿Qué debe pasar?**
- ✅ Modal desaparece
- ✅ Aparece notificación verde en esquina superior derecha
- ✅ Dice: "¡Producto eliminado!"
- ✅ La página se recarga automáticamente (1 segundo)
- ✅ El producto ya NO está en el carrito

**❌ Si no funciona:**
- Abre la consola del navegador (F12)
- Busca errores en rojo
- Verifica que veas: `🗑️ Solicitando eliminar producto:`

---

## ✅ PRUEBA 2: Vaciar Carrito (30 segundos)

**Requisito:** Debes tener al menos 2 productos en el carrito

**Pasos:**
1. Busca el botón amarillo **"Vaciar Carrito"** (abajo a la izquierda)
2. Haz clic en él
3. Aparecerá un modal de advertencia

**¿Qué debes ver?**
- ✅ Modal con fondo oscuro
- ✅ Icono de advertencia amarillo (⚠️)
- ✅ Título: "¿Vaciar todo el carrito?"
- ✅ Mensaje: "Se eliminarán todos los productos..."
- ✅ Dos botones: "Cancelar" y "Vaciar Carrito"

**Acción:**
4. Haz clic en **"Vaciar Carrito"**

**¿Qué debe pasar?**
- ✅ Modal desaparece
- ✅ Notificación verde aparece
- ✅ Dice: "¡Carrito vaciado!"
- ✅ La página se recarga (1 segundo)
- ✅ Muestra mensaje: "Tu carrito está vacío"
- ✅ Aparece icono grande de carrito vacío
- ✅ Botón "Ir a la Tienda"

**❌ Si no funciona:**
- Consola (F12) debe mostrar: `🧹 Solicitando vaciar carrito`
- Verifica que tengas productos en el carrito primero

---

## ✅ PRUEBA 3: Proceder al Pago (20 segundos)

**Requisito:** Debes tener al menos 1 producto en el carrito

**Pasos:**
1. Ve al carrito con productos
2. Busca el botón verde grande **"Proceder al Pago"** (lado derecho)
3. Haz clic en él

**¿Qué debe pasar INMEDIATAMENTE?**
- ✅ Notificación azul aparece en esquina
- ✅ Dice: "Redirigiendo..."
- ✅ Ícono de tarjeta de crédito

**¿Qué debe pasar DESPUÉS (1 segundo)?**
- ✅ Eres redirigido a: `/tienda/checkout/`
- ✅ Página de checkout se carga
- ✅ Ves tu resumen de pedido:
  - Lista de productos
  - Subtotal
  - IVA (19%)
  - Total
  - Opciones de pago

**❌ Si no funciona:**
- Consola debe mostrar: `💳 Redirigiendo a checkout`
- Verifica que estés logueado
- Verifica que los productos tengan stock

---

## ✅ PRUEBA 4: Actualizar Cantidad (20 segundos)

**Pasos:**
1. Busca los botones **-** y **+** junto a la cantidad
2. Haz clic en **+** para aumentar
3. O haz clic en **-** para disminuir

**¿Qué debe pasar?**
- ✅ Notificación azul: "Cantidad actualizada"
- ✅ Página se recarga (0.8 segundos)
- ✅ Nueva cantidad se muestra
- ✅ Subtotal se recalcula
- ✅ Total se actualiza

**Nota:** No puedes:
- ❌ Poner cantidad menor a 1
- ❌ Exceder el stock disponible

---

## 🎨 Visual de los Modales

### Modal de Eliminar (Rojo)
```
┌──────────────────────────────────┐
│          🗑️                      │
│   ¿Eliminar producto?            │
│                                  │
│  Este producto será eliminado    │
│  de tu carrito de compras.       │
│                                  │
│   [Cancelar]    [Eliminar]      │
└──────────────────────────────────┘
```

### Modal de Vaciar (Amarillo)
```
┌──────────────────────────────────┐
│          ⚠️                      │
│   ¿Vaciar todo el carrito?       │
│                                  │
│  Se eliminarán TODOS los         │
│  productos. No se puede deshacer │
│                                  │
│   [Cancelar]  [Vaciar Carrito]  │
└──────────────────────────────────┘
```

### Toast de Éxito (Verde)
```
┌─────────────────────────────┐
│  ✅  ¡Producto eliminado!   │
│     El producto ha sido     │
│     eliminado de tu carrito │  [X]
└─────────────────────────────┘
```

---

## 🔍 Mensajes en Consola (F12)

### Al Cargar la Página
```
✅ DOM cargado, inicializando carrito
💾 Carrito sincronizado: 5 productos
🎉 Sistema de carrito listo
```

### Al Eliminar
```
🗑️ Solicitando eliminar producto: 1
✅ Confirmado, enviando petición...
📡 Respuesta recibida: 200
📦 Datos: {success: true, message: "✅ Producto eliminado"}
✅ LocalStorage actualizado
```

### Al Vaciar
```
🧹 Solicitando vaciar carrito
✅ Confirmado, enviando petición...
📡 Respuesta recibida: 200
📦 Datos: {success: true, message: "✅ Carrito vaciado"}
✅ LocalStorage limpiado
```

---

## ⚡ Atajos de Teclado

Cuando un modal está abierto:
- **ESC** → Cierra el modal (hacer clic fuera también funciona)
- **ENTER** → Confirma la acción

---

## 📱 Prueba en Diferentes Tamaños

### Desktop (> 1200px)
- ✅ Modales centrados
- ✅ Toasts en esquina superior derecha
- ✅ 2 columnas (productos | resumen)

### Tablet (768px - 1200px)
- ✅ Modales más pequeños
- ✅ Toasts se adaptan
- ✅ 2 columnas responsive

### Móvil (< 768px)
- ✅ Modales ocupan más ancho
- ✅ Toasts en centro superior
- ✅ 1 columna (productos arriba, resumen abajo)

---

## 🎯 Checklist Rápido

Marca las pruebas completadas:

- [ ] ✅ Eliminar producto funciona
- [ ] ✅ Modal aparece correctamente
- [ ] ✅ Toast verde se muestra
- [ ] ✅ Producto se elimina del carrito
- [ ] ✅ Vaciar carrito funciona
- [ ] ✅ Modal warning aparece
- [ ] ✅ Carrito queda vacío
- [ ] ✅ Proceder al pago funciona
- [ ] ✅ Redirección a checkout OK
- [ ] ✅ Actualizar cantidad funciona
- [ ] ✅ Totales se recalculan bien

---

## 🆘 Problemas Comunes

### Modal no aparece
**Causa:** JavaScript no cargó  
**Solución:** 
1. Recarga la página (Ctrl + Shift + R)
2. Limpia caché del navegador
3. Verifica consola por errores

### Toast no se ve
**Causa:** Puede estar fuera de pantalla  
**Solución:**
1. Verifica scroll de la página
2. Prueba en modo ventana completa
3. Busca en esquina superior derecha

### "Error de conexión"
**Causa:** Servidor no está corriendo  
**Solución:**
```bash
python manage.py runserver
```

### "CSRF token missing"
**Causa:** Token de seguridad expirado  
**Solución:**
1. Recarga la página
2. Limpia cookies
3. Vuelve a intentar

---

## 📸 Capturas Recomendadas

Si algo no funciona, toma capturas de:

1. **El modal** (si aparece distorsionado)
2. **La consola** (F12 → Console) con errores
3. **El carrito completo** antes de la acción
4. **La terminal** donde corre Django

---

## ⏱️ Tiempo Total de Pruebas

- ✅ Prueba 1 (Eliminar): **30 segundos**
- ✅ Prueba 2 (Vaciar): **30 segundos**
- ✅ Prueba 3 (Pago): **20 segundos**
- ✅ Prueba 4 (Cantidad): **20 segundos**

**Total: ~2 minutos** ⚡

---

**¡Comienza las pruebas y verifica que todo funcione!** 🚀

Cualquier problema, revisa:
- `CORRECCIONES_CARRITO.md` (documentación técnica completa)
- Consola del navegador (F12)
- Terminal de Django (errores del servidor)

