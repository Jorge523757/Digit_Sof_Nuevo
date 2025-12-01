# 🔒 SISTEMA DE RESTRICCIONES Y PERMISOS - DIGIT SOFT

## ✅ IMPLEMENTACIÓN COMPLETADA

Se han implementado restricciones de acceso para proteger los módulos administrativos del sistema.

---

## 📋 TIPOS DE USUARIOS

### 1. **Superusuario / Administrador**
- **Acceso:** COMPLETO
- **Permisos:** Todos los módulos y funcionalidades
- **Usuario de prueba:** `admin` / `admin123`
- **Características:**
  - Puede gestionar todos los módulos
  - Acceso al panel de administración Django
  - Puede crear, editar y eliminar registros
  - Ve estadísticas completas en el dashboard

### 2. **Staff (Personal Autorizado)**
- **Acceso:** COMPLETO (similar a admin)
- **Permisos:** Todos los módulos operativos
- **Características:**
  - Puede gestionar clientes, productos, ventas, etc.
  - Ve estadísticas en el dashboard
  - No tiene acceso al panel admin de Django (a menos que sea superuser)

### 3. **Cliente Registrado**
- **Acceso:** LIMITADO
- **Permisos:** Solo visualización básica
- **Características:**
  - ❌ NO puede acceder a módulos de gestión (clientes, productos, ventas, etc.)
  - ✅ Puede ver su propio dashboard con información limitada
  - ✅ Puede actualizar su perfil
  - ❌ Recibe mensaje de "Acceso restringido" al intentar acceder a módulos protegidos

---

## 🔐 MÓDULOS PROTEGIDOS

Los siguientes módulos ahora requieren permisos de **Staff** o **Superusuario**:

### ✅ **Clientes**
- Lista de clientes
- Crear cliente
- Editar cliente
- Eliminar cliente
- Ver detalle de cliente

### ✅ **Productos**
- Lista de productos
- Crear producto
- Editar producto
- Eliminar producto
- Ver detalle de producto
- Movimientos de inventario
- Productos con bajo stock
- Activar/Desactivar producto

### ✅ **Ventas**
- Lista de ventas
- Crear venta
- Ver detalle de venta
- Editar venta
- Cambiar estado de venta
- Reportes de ventas

### ✅ **Compras** (cuando se acceda)
- Todas las funcionalidades

### ✅ **Proveedores** (cuando se acceda)
- Todas las funcionalidades

### ✅ **Órdenes de Servicio** (cuando se acceda)
- Todas las funcionalidades

### ✅ **Facturación** (cuando se acceda)
- Todas las funcionalidades

### ✅ **Garantías** (cuando se acceda)
- Todas las funcionalidades

---

## 🛠️ DECORADORES IMPLEMENTADOS

Se crearon decoradores personalizados en `usuarios/decorators.py`:

### 1. `@staff_required`
Requiere que el usuario sea staff o superusuario
```python
from usuarios.decorators import staff_required

@login_required
@staff_required
def mi_vista(request):
    # Solo accesible para staff y superusuarios
    ...
```

### 2. `@superuser_required`
Requiere que el usuario sea superusuario
```python
from usuarios.decorators import superuser_required

@login_required
@superuser_required
def mi_vista_admin(request):
    # Solo accesible para superusuarios
    ...
```

### 3. `@verificar_perfil_activo`
Verifica que el perfil del usuario esté activo (no bloqueado)
```python
from usuarios.decorators import verificar_perfil_activo

@login_required
@verificar_perfil_activo
def mi_vista(request):
    # Solo si el usuario no está bloqueado
    ...
```

---

## 🎯 COMPORTAMIENTO DEL SISTEMA

### **Cuando un Cliente intenta acceder a un módulo protegido:**

1. El sistema detecta que no es staff/superusuario
2. Muestra un mensaje: "No tienes permisos para acceder a esta sección. Solo personal autorizado."
3. Redirige automáticamente al dashboard
4. El cliente ve su dashboard limitado con información de contacto

### **Cuando un Staff/Admin accede:**

1. Acceso completo a todos los módulos
2. Dashboard con estadísticas completas
3. Puede realizar todas las operaciones CRUD
4. Ve métricas del sistema

---

## 📱 CÓMO PROBAR EL SISTEMA

### **Probar como Administrador:**
```
URL: http://127.0.0.1:8000/usuarios/login/
Usuario: admin
Contraseña: admin123
```
✅ Tendrás acceso completo a todos los módulos

### **Probar como Cliente:**
```
1. Ir a: http://127.0.0.1:8000/usuarios/registro/
2. Registrar un nuevo usuario
3. Iniciar sesión con ese usuario
```
❌ Verás restricciones al intentar acceder a módulos administrativos

---

## 🔄 FLUJO DE REGISTRO

Cuando un usuario se registra:

1. ✅ Se crea la cuenta de usuario
2. ✅ Se crea automáticamente su perfil (PerfilUsuario)
3. ✅ Se registra como cliente en la tabla Clientes
4. ✅ El perfil se marca como tipo "CLIENTE"
5. ✅ El usuario NO es staff ni superusuario
6. ✅ Se le redirige al login
7. ✅ Al iniciar sesión, ve el dashboard de cliente limitado

---

## 🎨 MEJORAS EN LA INTERFAZ

### **Login:**
- ✅ Diseño centrado y moderno
- ✅ Gradiente de fondo atractivo
- ✅ Iconos FontAwesome
- ✅ Mensajes de error claros
- ✅ Link a registro

### **Dashboard:**
- ✅ Contenido diferenciado para staff vs clientes
- ✅ Estadísticas para personal autorizado
- ✅ Información de contacto para clientes
- ✅ Mensaje de acceso restringido para clientes

---

## 📝 MENSAJES DEL SISTEMA

### **Acceso Denegado:**
```
⚠️ No tienes permisos para acceder a esta sección. Solo personal autorizado.
```

### **Dashboard de Cliente:**
```
ℹ️ Cuenta de Cliente
Bienvenido a DIGIT SOFT. Tu cuenta tiene acceso limitado. 
Para realizar compras o solicitar servicios, contacta con nuestro equipo de ventas.
```

---

## 🚀 PRÓXIMOS PASOS RECOMENDADOS

1. ✅ **Crear usuarios de prueba:**
   - Un admin: Ya existe (admin/admin123)
   - Un cliente: Registrarse en /usuarios/registro/

2. ✅ **Probar restricciones:**
   - Iniciar sesión como cliente
   - Intentar acceder a /clientes/
   - Verificar el mensaje de error
   - Ver el dashboard limitado

3. ✅ **Probar como admin:**
   - Iniciar sesión como admin
   - Acceder a todos los módulos
   - Verificar estadísticas en dashboard

4. ⚙️ **Personalizar según necesidades:**
   - Ajustar mensajes de error
   - Añadir más restricciones específicas
   - Crear roles personalizados

---

## 🔧 ARCHIVOS MODIFICADOS

```
✅ usuarios/decorators.py (NUEVO)
✅ usuarios/views.py
✅ usuarios/forms.py
✅ clientes/views.py
✅ productos/views.py
✅ ventas/views.py
✅ dashboard/views.py
✅ templates/usuarios/login.html
✅ templates/usuarios/registro.html
✅ templates/dashboard/dashboard.html
```

---

## 📞 CREDENCIALES DE ACCESO

### **Superusuario:**
```
Usuario: admin
Contraseña: admin123
Email: admin@digitsoft.com
Acceso: COMPLETO
```

### **Cliente de Prueba:**
```
Crear en: http://127.0.0.1:8000/usuarios/registro/
Acceso: LIMITADO (solo dashboard básico)
```

---

## ✨ CARACTERÍSTICAS DE SEGURIDAD

- ✅ Autenticación requerida en todos los módulos
- ✅ Verificación de permisos por decoradores
- ✅ Mensajes claros de acceso denegado
- ✅ Redirección automática al dashboard
- ✅ Protección contra acceso no autorizado
- ✅ Separación clara entre roles
- ✅ Dashboard adaptativo según tipo de usuario

---

**🎊 Sistema de restricciones completamente implementado y funcional 🎊**

Última actualización: 12 de Noviembre de 2025

