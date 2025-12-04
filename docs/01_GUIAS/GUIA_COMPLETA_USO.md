# 🎯 GUÍA COMPLETA - SISTEMA 100% FUNCIONAL

## ✅ ESTADO ACTUAL

**Todos los módulos están configurados y funcionando correctamente.**

El problema de "no aparece nada" se debe a que **NO HAY DATOS REGISTRADOS**.

---

## 🚀 SOLUCIÓN: AGREGAR DATOS DESDE EL ADMIN

### Paso 1: Inicia el Sistema
```cmd
Doble click en: INICIAR_ACTUALIZADO.bat
```

### Paso 2: Accede al Admin
```
URL: http://127.0.0.1:8000/admin/
Usuario: admin
Contraseña: admin123
```

---

## 📋 ORDEN RECOMENDADO PARA AGREGAR DATOS

### 1. ✅ CLIENTES (Ya existen 5)
- Admin → Clientes
- Ya hay datos de prueba
- Si necesitas más: Click "Agregar cliente"

### 2. ✅ TÉCNICOS (Ya existen 2-3)
- Admin → Técnicos
- Ya hay datos de prueba
- Si necesitas más: Click "Agregar técnico"

### 3. ⚠️ PRODUCTOS (DEBES AGREGAR)
**IMPORTANTE: Sin productos NO puedes crear ventas**

**Cómo agregar un producto:**
1. Admin → Productos → Agregar producto
2. **Campos obligatorios:**
   - ✅ Nombre producto: `Laptop HP Pavilion 15`
   - ✅ Código SKU: `LAP-HP-001` (debe ser único)
   - ✅ Precio venta: `1800000`
   - ✅ Precio compra: `1500000`
   - ✅ Stock actual: `10`
   - ✅ Stock mínimo: `2`
3. **Campos opcionales:**
   - Categoría (puedes crear primero en CategoríasProducto)
   - Descripción
   - Marca
   - Modelo
4. Click **"Guardar"**

**Agrega al menos 3 productos antes de continuar**

### 4. PROVEEDORES (Opcional pero recomendado)
1. Admin → Proveedores → Agregar proveedor
2. **Campos principales:**
   - Nombre empresa: `Tecnología Global S.A.`
   - NIT: `900123456-7`
   - Nombre contacto: `Roberto García`
   - Email: `ventas@tecnologiaglobal.com`
   - Teléfono: `6013334455`
3. Guardar

### 5. ⭐ VENTAS (Ahora sí puedes agregar)
**REQUISITO: Debes tener Clientes y Productos**

**Paso a paso:**
1. Admin → Ventas → Agregar venta
2. **Información Básica:**
   - Cliente: Selecciona uno (Juan Pérez, María Rodríguez, etc.)
   - Canal venta: `TIENDA`
   - Vendedor: Tu nombre o "Vendedor Demo"
3. **Estado y Pago:**
   - Estado: `COMPLETADA`
   - Método pago: `EFECTIVO`
   - Pagado: ✓ (marcar)
4. **NO toques estos campos** (se llenan solos):
   - Número de venta (se genera: VEN-000001)
   - Fecha de venta (automática)
   - Subtotal (se calcula)
   - Total (se calcula)
5. **IMPORTANTE - Agregar Productos:**
   - Scroll hasta abajo: "Detalles de venta"
   - Click "Agregar otro Detalle de venta"
   - Producto: Selecciona uno
   - Cantidad: `1`
   - Precio unitario: `1800000` (el precio del producto)
   - Con garantía: ✓
6. Click **"Guardar"**

### 6. ⭐ FACTURAS
**REQUISITO: Debes tener Clientes (y opcionalmente Ventas)**

1. Admin → Facturas → Agregar factura
2. **Información Básica:**
   - Cliente: Selecciona uno
   - Venta relacionada: (opcional) Si ya creaste una venta
   - Tipo factura: `VENTA`
3. **Estado y Fechas:**
   - Estado: `EMITIDA`
   - Fecha vencimiento: (OPCIONAL - puede estar en blanco)
4. **Montos:**
   - Subtotal: `1800000`
   - IVA: `342000` (19% del subtotal)
   - Total: `2142000`
5. **NO toques:**
   - Número de factura (se genera: FAC-000001)
   - Fecha de emisión (automática)
6. Click **"Guardar"**

### 7. ÓRDENES DE SERVICIO
1. Admin → Órdenes de servicio → Agregar orden
2. **Campos principales:**
   - Cliente: Selecciona uno
   - Técnico asignado: Selecciona uno
   - Tipo equipo: `Laptop`
   - Marca: `HP`
   - Modelo: `Pavilion 15`
   - Falla reportada: `No enciende`
   - Estado: `RECIBIDA`
   - Prioridad: `ALTA`
3. Guardar

### 8. COMPRAS
1. Admin → Compras → Agregar compra
2. **Campos:**
   - Proveedor: Selecciona uno (debes crear primero)
   - Estado: `COMPLETADA`
   - Método pago: `TRANSFERENCIA`
3. **Detalles:**
   - Agrega productos con cantidades y precios
4. Guardar

### 9. ⭐ EQUIPOS
1. Admin → Equipos → Agregar equipo
2. **Campos:**
   - Código equipo: `EQ-001` (único)
   - Nombre: `Laptop HP ProBook`
   - Tipo equipo: `LAPTOP`
   - Marca: `HP`
   - Modelo: `ProBook 450`
   - Fecha adquisición: (fecha de hoy)
   - Valor adquisición: `2500000`
   - Estado: `OPERATIVO`
   - Ubicación: `Oficina Principal`
3. Guardar

### 10. ⭐ CAPACITACIONES
1. Admin → Capacitaciones → Agregar capacitación
2. **Campos:**
   - Código: `CAP-001` (único)
   - Nombre: `Reparación de Laptops Modernas`
   - Tipo: `TECNICA`
   - Instructor: `Ing. Roberto Sánchez`
   - Descripción: `Curso avanzado de reparación`
   - Fecha inicio: (fecha futura, ej: 7 días desde hoy)
   - Fecha fin: (fecha inicio + 2 días)
   - Duración horas: `16`
   - Lugar: `Centro de Capacitación DIGIT SOFT`
   - Modalidad: `PRESENCIAL`
   - Estado: `PROGRAMADA`
   - Cupo máximo: `15`
   - Costo: `500000`
3. Guardar

---

## 🎨 CÓMO VER LOS DATOS EN EL FRONTEND

### Una vez que agregues datos en el admin:

**Ventas:**
```
http://127.0.0.1:8000/ventas/
```
Verás: Tabla con todas las ventas, estadísticas, botones de acción

**Facturas:**
```
http://127.0.0.1:8000/facturacion/
```
Verás: Lista de facturas con estados

**Capacitaciones:**
```
http://127.0.0.1:8000/capacitaciones/
```
Verás: Lista de capacitaciones con información completa

**Órdenes:**
```
http://127.0.0.1:8000/ordenes/
```
Verás: Tabla moderna con badges de estados y prioridades

**Otros módulos:**
- Clientes: `/clientes/`
- Técnicos: `/tecnicos/`
- Productos: `/productos/`
- Proveedores: `/proveedores/`
- Compras: `/compras/`
- Equipos: `/equipos/`
- Garantías: `/garantias/`

---

## ⚠️ ERRORES COMUNES Y SOLUCIONES

### "No aparece nada en Ventas"
**Causa:** No hay ventas registradas
**Solución:** Agrega ventas desde el admin siguiendo los pasos arriba

### "No hay botón de agregar"
**Causa:** Estás viendo el frontend, no el admin
**Solución:** Ve a http://127.0.0.1:8000/admin/ para agregar datos

### "Error al crear venta: Producto no puede ser nulo"
**Causa:** No agregaste productos en "Detalles de venta"
**Solución:** En el formulario de venta, scroll abajo y agrega al menos 1 producto

### "Error: No se puede crear producto sin SKU"
**Causa:** El campo Código SKU es obligatorio
**Solución:** Agrega un código único, ej: LAP-HP-001

### "No aparece la categoría"
**Causa:** No has creado categorías
**Solución:** Admin → Categorías producto → Agregar (opcional)

---

## 📊 FLUJO COMPLETO RECOMENDADO

### Para empezar a usar el sistema:

```
1. ✅ Inicia servidor: INICIAR_ACTUALIZADO.bat
2. ✅ Login en admin: admin / admin123
3. ✅ Verifica Clientes (ya existen 5)
4. ⭐ AGREGA PRODUCTOS (mínimo 3)
5. ⭐ AGREGA VENTAS (usando los productos)
6. ⭐ AGREGA FACTURAS (relacionadas a ventas)
7. ⭐ AGREGA CAPACITACIONES
8. ⭐ AGREGA EQUIPOS
9. ⭐ Ve al frontend y verifica que todo se muestra
```

---

## 🎯 CHECKLIST DE VERIFICACIÓN

```
☐ Servidor iniciado correctamente
☐ Login en admin funciona (admin/admin123)
☐ Clientes existen (mínimo 3)
☐ Técnicos existen (mínimo 2)
☐ Productos creados (mínimo 3) ⭐ IMPORTANTE
☐ Venta creada con productos
☐ Factura creada
☐ Capacitación creada
☐ Equipo creado
☐ Frontend muestra los datos (/ventas/, /facturacion/, etc.)
```

---

## 📞 RESUMEN RÁPIDO

**PROBLEMA:** "No aparece nada en ventas/facturación/capacitaciones"
**CAUSA:** No hay datos registrados en la base de datos
**SOLUCIÓN:** Agregar datos desde http://127.0.0.1:8000/admin/

**ORDEN:**
1. Productos (OBLIGATORIO)
2. Ventas (con productos)
3. Facturas
4. Capacitaciones
5. Equipos

**DESPUÉS:** Ve al frontend y verás todo funcionando

---

**¡El sistema está 100% funcional! Solo necesita datos.** 🎉

**Sigue esta guía paso a paso y tendrás el sistema completo funcionando.**

