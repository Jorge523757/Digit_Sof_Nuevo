# 🚀 GUÍA RÁPIDA DE USO - E-COMMERCE DIGIT SOFT

## ⚡ Inicio Rápido en 5 Minutos

---

## 🎯 Para el Cliente (Usuario Final)

### 1. Navegar y Comprar

```
1. Abrir navegador → http://127.0.0.1:8000/
2. Explorar productos en la landing page
3. Filtrar por categoría (Computadores, Periféricos, etc.)
4. Click en producto para ver detalles
5. Click en "Agregar al Carrito" 🛒
6. Abrir carrito (icono superior derecho)
7. Revisar productos y cantidades
8. Click en "Finalizar Compra"
9. Llenar formulario de checkout
10. Seleccionar método de pago
11. Click en "Confirmar Pedido"
12. ¡Listo! Recibirás tu número de orden
```

### 2. Gestionar Carrito

```javascript
// Desde el modal del carrito puedes:

✅ Aumentar cantidad     → Botón +
✅ Disminuir cantidad    → Botón -
✅ Eliminar producto     → Botón 🗑️ (con confirmación elegante)
✅ Vaciar carrito        → Botón "Vaciar Carrito"
✅ Ver total             → Se actualiza automáticamente
✅ Finalizar compra      → Botón "Finalizar Compra"
```

### 3. Crear Cuenta

```
1. Click en "Registro" en el menú
2. Completar formulario:
   - Nombre completo
   - Email
   - Usuario
   - Contraseña
   - Teléfono
   - Documento
3. Click en "Registrarse"
4. Login automático
5. ¡Ya puedes comprar!
```

---

## 👨‍💼 Para el Administrador

### 1. Acceder al Panel de Administración

```
1. Ir a: http://127.0.0.1:8000/admin/
2. Login con credenciales de superusuario
3. Acceso completo al sistema
```

### 2. Gestionar Productos

```
Panel Admin → Productos → Productos

Acciones disponibles:
✅ Agregar nuevo producto
✅ Editar producto existente
✅ Eliminar producto
✅ Ver stock actual
✅ Marcar como destacado
✅ Cambiar categoría
✅ Subir imagen
✅ Activar/desactivar en web
```

### 3. Gestionar Órdenes

```
Panel Admin → Main → Orders

Puedes ver:
📦 Número de orden
👤 Cliente
💰 Total
📅 Fecha
📊 Estado actual

Acciones:
✅ Cambiar estado (Confirmado → Enviado → Entregado)
✅ Ver detalles completos
✅ Generar factura
✅ Enviar notificación al cliente
✅ Cancelar orden
```

### 4. Monitorear Inventario

```
Dashboard → Inventario

Alertas automáticas:
⚠️ Productos con stock bajo
📉 Productos sin stock
📈 Productos más vendidos
💰 Valor total del inventario
```

### 5. Ver Reportes

```
Dashboard → Reportes

Disponibles:
📊 Ventas del día
📊 Ventas del mes
📊 Ventas por categoría
📊 Productos top
📊 Clientes frecuentes
📊 Métodos de pago usados
```

---

## 🔧 Para el Desarrollador

### 1. Estructura del Proyecto

```
main/              → E-commerce principal
productos/         → Gestión de productos
clientes/          → Gestión de clientes
ordenes/           → Órdenes de servicio técnico
dashboard/         → Panel de administración
usuarios/          → Autenticación
templates/         → HTML
static/            → CSS, JS, imágenes
media/             → Archivos subidos
```

### 2. Modelos Principales

```python
# Producto
productos.models.Producto
- Información completa del producto
- Control de inventario
- Precios y categorías

# Orden de Compra
main.models.Order
- Pedidos del e-commerce
- Estados de envío
- Métodos de pago

# Cliente
clientes.models.Cliente
- Datos del cliente
- Vinculado con User
- Historial de compras
```

### 3. URLs Importantes

```python
# Frontend
/                          → Landing page
/tienda/productos/         → Catálogo e-commerce
/tienda/carrito/           → Página del carrito
/checkout/checkout/        → Checkout
/checkout/success/<id>/    → Confirmación

# APIs
/productos/api/publicos/   → Listar productos
/productos/api/reaccion/   → Reacciones
/tienda/agregar-carrito/   → Agregar al carrito
/tienda/actualizar-carrito/→ Actualizar cantidad
/tienda/eliminar-carrito/  → Eliminar producto

# Admin
/admin/                    → Django admin
/dashboard/                → Dashboard custom
/tecnicos/                 → Panel técnicos
```

### 4. JavaScript Principal

```javascript
// static/js/productos-landing.js

// Clases principales:
- CarritoCompras          → Gestión del carrito
- ProductosManager        → Carga y renderiza productos

// Funciones globales:
- agregarAlCarrito(id)    → Agregar producto
- verDetalle(id)          → Ver detalles
- verCarrito()            → Ver carrito en consola
- vaciarCarrito()         → Vaciar desde consola
- limpiarLocalStorage()   → Limpiar storage
```

### 5. Comandos Útiles

```bash
# Iniciar servidor
python manage.py runserver

# Crear superusuario
python manage.py createsuperuser

# Migraciones
python manage.py makemigrations
python manage.py migrate

# Crear datos de prueba
python agregar_productos_prueba.py

# Colectar archivos estáticos
python manage.py collectstatic
```

---

## 📊 FLUJO VISUAL DEL SISTEMA

```
┌─────────────────────────────────────────────────────────────┐
│                    USUARIO FINAL                            │
└────────────┬────────────────────────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────────────────────────┐
│  LANDING PAGE (/)                                           │
│  • Grid de productos                                        │
│  • Filtros por categoría                                    │
│  • Sistema de búsqueda                                      │
│  • Botón "Agregar al Carrito"                              │
└────────────┬────────────────────────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────────────────────────┐
│  CARRITO (Modal)                                            │
│  • LocalStorage                                             │
│  • Lista de productos                                       │
│  • Controles de cantidad                                    │
│  • Total calculado                                          │
│  • Botón "Finalizar Compra"                                │
└────────────┬────────────────────────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────────────────────────┐
│  CHECKOUT (/checkout/checkout/)                             │
│  • Formulario de datos personales                          │
│  • Dirección de envío                                       │
│  • Método de pago                                           │
│  • Resumen del pedido                                       │
│  • Validación de stock                                      │
└────────────┬────────────────────────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────────────────────────┐
│  BACKEND - PROCESAR ORDEN                                   │
│  1. Crear Order                                             │
│  2. Crear OrderItems                                        │
│  3. Actualizar inventario ⚡                                │
│  4. Generar factura                                         │
│  5. Enviar email confirmación                               │
│  6. Limpiar carrito                                         │
└────────────┬────────────────────────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────────────────────────┐
│  CONFIRMACIÓN (/checkout/success/)                          │
│  • Número de orden: DS12345678                              │
│  • Resumen del pedido                                       │
│  • Información de envío                                     │
│  • Estado: Pendiente                                        │
│  • Descargar factura                                        │
└────────────┬────────────────────────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────────────────────────┐
│  ADMINISTRADOR                                              │
│  • Panel de órdenes                                         │
│  • Cambiar estado                                           │
│  • Generar factura                                          │
│  • Notificar cliente                                        │
│  • Ver reportes                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🎯 CASOS DE USO COMUNES

### Caso 1: Compra Exitosa

```
1. Usuario navega productos ✅
2. Agrega 3 productos al carrito ✅
3. Abre carrito, revisa productos ✅
4. Va a checkout ✅
5. Completa formulario ✅
6. Selecciona "Transferencia Bancaria" ✅
7. Confirma pedido ✅
8. Recibe número de orden: DS87654321 ✅
9. Recibe email con detalles ✅
10. Admin procesa orden ✅
11. Admin marca como "Enviado" ✅
12. Cliente recibe notificación ✅
13. Orden llega en 3 días ✅
14. Admin marca como "Entregado" ✅
```

### Caso 2: Producto Sin Stock

```
1. Usuario intenta agregar producto ❌
2. Sistema verifica stock = 0 ⚠️
3. Muestra notificación: "Sin stock disponible" 🔴
4. No se agrega al carrito ❌
5. Usuario puede registrarse para notificación 📧
```

### Caso 3: Modificar Carrito

```
1. Usuario tiene 2 productos en carrito ✅
2. Aumenta cantidad de producto 1: 2 → 3 ✅
3. Sistema verifica stock disponible ✅
4. Actualiza subtotal automáticamente ✅
5. Decide eliminar producto 2 ✅
6. Click en 🗑️ → Modal de confirmación aparece 🎨
7. Confirma eliminación ✅
8. Producto eliminado + Toast de éxito ✅
```

### Caso 4: Gestión de Orden (Admin)

```
1. Admin recibe notificación de nueva orden 📧
2. Abre panel de órdenes 📊
3. Ve orden DS12345678 con estado "Pendiente" 🟡
4. Click en orden → Ve detalles completos 📄
5. Verifica pago recibido ✅
6. Cambia estado a "Confirmado" 🟢
7. Prepara productos para envío 📦
8. Cambia estado a "Enviado" 🚚
9. Cliente recibe notificación automática 📧
10. Días después, marca como "Entregado" ✅
11. Sistema genera factura automática 📄
```

---

## 🔍 DEBUGGING Y CONSOLA

### Comandos de Consola del Navegador

```javascript
// Ver contenido actual del carrito
verCarrito()
// Output: Array con todos los productos, total, cantidad

// Vaciar el carrito manualmente
vaciarCarrito()
// Muestra notificación y limpia el carrito

// Limpiar todo el localStorage
limpiarLocalStorage()
// Modal de confirmación → Limpia → Recarga página

// Ver todos los productos cargados
productosManager.productos
// Array con todos los productos del catálogo

// Recargar productos
productosManager.cargarProductos('all')
// O por categoría: productosManager.cargarProductos('computadores')

// Ver instancia del carrito
carrito
// Object con todos los métodos y propiedades

// Agregar producto manualmente (para testing)
agregarAlCarrito(1)  // Agrega producto con ID 1
```

### Logs Útiles

```javascript
// El sistema hace log de todo:

console.log('🛒 Carrito cargado')
console.log('📦 Items cargados del localStorage:', cantidad)
console.log('✅ Producto agregado correctamente')
console.log('🗑️ Eliminando producto:', id)
console.log('🔢 Actualizando cantidad:', datos)
console.log('📡 Respuesta del servidor:', response)
```

---

## ⚠️ SOLUCIÓN DE PROBLEMAS

### Problema: Carrito no guarda productos

**Solución:**
```javascript
// Verificar localStorage
localStorage.getItem('carrito')

// Si está lleno, limpiar
limpiarLocalStorage()

// Recargar página
location.reload()
```

### Problema: Productos no se cargan

**Solución:**
```bash
# Verificar servidor Django
python manage.py runserver

# Verificar en navegador
Network Tab → /productos/api/publicos/

# Si hay error 500, verificar logs del servidor
```

### Problema: No puedo finalizar compra

**Solución:**
```
1. Verificar que estás logueado
2. Verificar que el carrito tiene productos
3. Verificar que los productos tienen stock
4. Revisar consola del navegador para errores
5. Verificar formulario de checkout completado
```

### Problema: Stock no se actualiza

**Solución:**
```python
# En Django shell
python manage.py shell

from productos.models import Producto

# Ver stock actual
p = Producto.objects.get(id=1)
print(p.stock_actual)

# Actualizar manualmente si necesario
p.stock_actual = 10
p.save()
```

---

## 📱 RESPONSIVE DESIGN

El sistema funciona perfectamente en:

- ✅ **Desktop** (1920px+) → Grid 4 columnas
- ✅ **Laptop** (1366px - 1920px) → Grid 3 columnas  
- ✅ **Tablet** (768px - 1366px) → Grid 2 columnas
- ✅ **Mobile** (320px - 768px) → Grid 1 columna

El modal del carrito y el checkout son 100% responsive.

---

## 🎨 PERSONALIZACIÓN

### Cambiar Colores

```css
/* static/css/landing.css */

:root {
    --color-primary: #667eea;    /* Púrpura */
    --color-secondary: #764ba2;   /* Púrpura oscuro */
    --color-success: #10b981;     /* Verde */
    --color-danger: #ef4444;      /* Rojo */
    --color-warning: #ffc107;     /* Amarillo */
}
```

### Cambiar Textos

```html
<!-- templates/main/landing.html -->

<!-- Título principal -->
<h1>¡Bienvenido a Digit Soft!</h1>

<!-- Botón de carrito -->
<button>Agregar al Carrito</button>

<!-- Modal del carrito -->
<h2>Mi Carrito de Compras</h2>
```

### Agregar Nueva Categoría

```python
# Django shell
python manage.py shell

from productos.models import CategoriaProducto

CategoriaProducto.objects.create(
    nombre='Accesorios',
    descripcion='Accesorios para computadoras',
    activo=True
)
```

---

## 📧 NOTIFICACIONES

### Emails Automáticos

El sistema envía emails en:

1. **Registro de cliente**
   - Bienvenida
   - Confirmación de cuenta

2. **Nueva orden**
   - Resumen del pedido
   - Número de orden
   - Instrucciones de pago

3. **Confirmación de pago**
   - Pago recibido
   - Tiempo estimado de envío

4. **Orden enviada**
   - Código de tracking
   - Fecha estimada de entrega

5. **Orden entregada**
   - Confirmación de entrega
   - Solicitud de review

6. **Stock bajo** (Admin)
   - Alerta de reposición

---

## 🔐 SEGURIDAD

### Protecciones Implementadas

✅ **CSRF Token** en todos los formularios  
✅ **Autenticación requerida** para checkout  
✅ **Validación de stock** múltiple capa  
✅ **Transacciones atómicas** en DB  
✅ **Sanitización de inputs**  
✅ **Protección contra SQL Injection**  
✅ **XSS Prevention** con escapejs  
✅ **Rate limiting** en APIs  
✅ **Passwords hasheados** con Django  

---

## 🚀 DEPLOYMENT

### Preparar para Producción

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Configurar variables de entorno
# Crear archivo .env con:
DEBUG=False
SECRET_KEY=tu-clave-secreta-super-segura
DATABASE_URL=postgres://...
ALLOWED_HOSTS=tudominio.com

# 3. Migraciones
python manage.py migrate

# 4. Colectar estáticos
python manage.py collectstatic

# 5. Crear superusuario
python manage.py createsuperuser

# 6. Usar servidor WSGI (Gunicorn)
gunicorn config.wsgi:application --bind 0.0.0.0:8000

# 7. Configurar Nginx como reverse proxy
# 8. Configurar SSL con Let's Encrypt
```

---

## 📞 SOPORTE

### ¿Necesitas Ayuda?

**Documentación completa:**  
Ver: `ARQUITECTURA_ECOMMERCE_COMPLETA.md`

**Issues comunes:**  
Ver: `TROUBLESHOOTING.md`

**Contacto:**  
- Email: soporte@digitsoft.com
- WhatsApp: +57 300 123 4567
- GitHub Issues

---

## 🎉 ¡LISTO PARA USAR!

El sistema está **100% funcional** y listo para:

✅ Recibir pedidos reales  
✅ Procesar pagos  
✅ Gestionar inventario  
✅ Administrar clientes  
✅ Generar reportes  
✅ Escalar según necesidades  

**¡Empieza a vender ahora!** 🚀

---

**Actualizado:** 24 de Noviembre, 2025  
**Versión:** 2.0  
**© Digit Soft - Todos los derechos reservados**

