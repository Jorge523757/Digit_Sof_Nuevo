# 👥 MÓDULO DE USUARIOS - UBICACIÓN Y ACCESOS

## ✅ MÓDULO AGREGADO AL SIDEBAR

He agregado el módulo de usuarios al menú lateral del dashboard en la sección **"Administración"**.

---

## 📍 UBICACIÓN EN EL MENÚ

```
╔════════════════════════════════════════╗
║                                        ║
║  📂 DASHBOARD                          ║
║                                        ║
║  📦 Clientes & Servicios               ║
║    • Gestión de Clientes               ║
║    • Gestión de Técnicos               ║
║    • Órdenes de Servicio               ║
║    • Gestión de Equipos                ║
║    • Garantías                         ║
║                                        ║
║  📦 Inventario & Proveedores           ║
║    • Gestión de Productos              ║
║    • Proveedores                       ║
║                                        ║
║  📦 Ventas & Facturación               ║
║    • Gestión de Ventas                 ║
║    • Gestión de Compras                ║
║    • Facturación                       ║
║                                        ║
║  📦 E-commerce                         ║
║    • Tienda Online                     ║
║                                        ║
║  📦 ADMINISTRACIÓN ⭐ NUEVO            ║
║    • Gestión de Usuarios 👥           ║
║    • Gestión de Contraseñas 🔐        ║
║                                        ║
║  📦 Otros                              ║
║    • Capacitaciones                    ║
║                                        ║
╚════════════════════════════════════════╝
```

---

## 🔗 URLs DISPONIBLES

### 1. Gestión de Usuarios
```
URL: /usuarios/gestionar/
Ruta: usuarios:listar_usuarios
Acceso: Sidebar → Administración → Gestión de Usuarios
```

**Funcionalidades:**
- ✅ Ver lista de todos los usuarios
- ✅ Crear nuevos usuarios
- ✅ Editar usuarios existentes
- ✅ Eliminar usuarios
- ✅ Bloquear/Desbloquear usuarios
- ✅ Cambiar rol (staff/usuario normal)
- ✅ Ver detalles de usuarios

---

### 2. Gestión de Contraseñas
```
URL: /usuarios/admin/gestionar-contrasenas/
Ruta: usuarios:admin_gestionar_contrasenas
Acceso: Sidebar → Administración → Gestión de Contraseñas
```

**Funcionalidades:**
- ✅ Ver todos los usuarios por categoría
- ✅ Cambiar contraseñas manualmente
- ✅ Generar contraseñas temporales
- ✅ Enviar contraseñas por correo
- ✅ Búsqueda en tiempo real
- ✅ Gestionar: Usuarios, Clientes, Técnicos, Proveedores

---

### 3. Otras URLs del Módulo de Usuarios

#### Autenticación (Públicas)
```
/usuarios/login/                  → Iniciar sesión
/usuarios/logout/                 → Cerrar sesión
/usuarios/registro/               → Registro de clientes
```

#### Recuperación de Contraseña (Públicas)
```
/usuarios/solicitar-recuperacion/ → Solicitar recuperación
/usuarios/recuperar-contrasena/<token>/ → Establecer nueva contraseña
```

#### Perfil de Usuario (Login requerido)
```
/usuarios/perfil/                 → Ver/editar perfil
/usuarios/cambiar-contrasena/     → Cambiar propia contraseña
```

#### Gestión de Usuarios (Admin/Staff)
```
/usuarios/gestionar/              → Lista de usuarios
/usuarios/gestionar/crear/        → Crear usuario
/usuarios/gestionar/<id>/         → Ver detalle
/usuarios/gestionar/<id>/editar/  → Editar usuario
/usuarios/gestionar/<id>/eliminar/ → Eliminar usuario
/usuarios/gestionar/<id>/bloquear/ → Bloquear usuario
/usuarios/gestionar/<id>/desbloquear/ → Desbloquear
/usuarios/gestionar/<id>/toggle-staff/ → Cambiar rol
```

---

## 🚀 CÓMO ACCEDER

### Opción 1: Desde el Sidebar
```
1. Iniciar sesión como admin/staff
2. En el menú lateral, buscar:
   📦 ADMINISTRACIÓN
3. Click en:
   👥 Gestión de Usuarios
   o
   🔐 Gestión de Contraseñas
```

### Opción 2: URL Directa
```
http://127.0.0.1:8000/usuarios/gestionar/
http://127.0.0.1:8000/usuarios/admin/gestionar-contrasenas/
```

---

## 👥 GESTIÓN DE USUARIOS

### ¿Qué puedes hacer?

#### Ver Usuarios
```
Lista completa de usuarios registrados
Con información de:
- Nombre y apellidos
- Email
- Username
- Rol (Admin/Staff/Usuario)
- Estado (Activo/Bloqueado)
- Fecha de registro
```

#### Crear Usuario
```
Formulario para crear nuevo usuario:
- Username único
- Email
- Nombre y apellidos
- Contraseña
- Rol (staff/superusuario)
- Permisos
```

#### Editar Usuario
```
Modificar datos de usuario existente:
- Información personal
- Email y username
- Cambiar rol
- Activar/desactivar
```

#### Bloquear/Desbloquear
```
Control de acceso rápido:
- Bloquear: Usuario no puede iniciar sesión
- Desbloquear: Restaurar acceso
- Sin eliminar datos
```

#### Eliminar Usuario
```
Eliminar permanentemente:
- Requiere confirmación
- Elimina todos los datos
- Acción irreversible
```

---

## 🔐 GESTIÓN DE CONTRASEÑAS

### Panel Completo

#### Vista Organizada
```
4 pestañas:
├── 👥 Usuarios del Sistema
├── 👔 Clientes
├── 🔧 Técnicos
└── 🚛 Proveedores
```

#### Estadísticas
```
Contadores en tiempo real:
• Total de usuarios
• Total de clientes
• Total de técnicos
• Total de proveedores
```

#### Búsqueda
```
Buscar por:
- Nombre
- Email
- Username
- En tiempo real
- Sin recargar página
```

#### Acciones por Usuario
```
1. Cambiar Contraseña
   → Manual o auto-generada
   → Opción enviar por email
   
2. Generar Temporal
   → 12 caracteres aleatorios
   → Envío automático por email
```

---

## 🎯 CASOS DE USO

### Caso 1: Crear Nuevo Usuario Administrador
```
1. Sidebar → Administración → Gestión de Usuarios
2. Click "Crear Usuario"
3. Llenar formulario:
   - Username: nuevo_admin
   - Email: admin@empresa.com
   - Contraseña: [segura]
   - ☑️ Es staff
4. Guardar
5. ¡Usuario creado!
```

### Caso 2: Cliente Olvidó su Contraseña
```
Opción A - Admin cambia:
1. Sidebar → Gestión de Contraseñas
2. Pestaña "Clientes"
3. Buscar cliente
4. "Cambiar Contraseña"
5. ☑️ Enviar por correo
6. Cliente recibe email

Opción B - Cliente auto-recupera:
1. Cliente va al login
2. "¿Olvidaste tu contraseña?"
3. Ingresa email
4. Recibe enlace
5. Establece nueva contraseña
```

### Caso 3: Bloquear Usuario Temporal
```
1. Gestión de Usuarios
2. Buscar usuario
3. Click "Bloquear"
4. Usuario no puede iniciar sesión
5. Cuando sea necesario: "Desbloquear"
```

### Caso 4: Promover Usuario a Staff
```
1. Gestión de Usuarios
2. Ver detalles del usuario
3. Click "Toggle Staff"
4. Usuario ahora es staff
5. Puede acceder al dashboard
```

---

## 🛡️ PERMISOS REQUERIDOS

### Gestión de Usuarios
```
Requiere: is_staff = True
o
Requiere: is_superuser = True
```

### Gestión de Contraseñas
```
Requiere: is_staff = True
o
Requiere: is_superuser = True
```

### Recuperación Pública
```
No requiere login
Cualquier usuario puede solicitar
```

---

## 📊 INFORMACIÓN MOSTRADA

### En Lista de Usuarios
```
┌──────────────────────────────────────┐
│ ID: 1                                │
│ 👤 Jorge Administrador               │
│ 📧 jorge@admin.com                   │
│ 🔑 Username: admin                   │
│ 🏷️ ROL: Superusuario               │
│ ✅ Estado: Activo                    │
│ 📅 Registro: 01/12/2025              │
│                                      │
│ [Ver] [Editar] [Eliminar]           │
│ [Bloquear] [Cambiar Rol]            │
└──────────────────────────────────────┘
```

### En Panel de Contraseñas
```
┌──────────────────────────────────────┐
│ 👤 Jorge Administrador               │
│ 📧 jorge@admin.com                   │
│ 🏷️ Usuario del Sistema              │
│                                      │
│ [Cambiar Contraseña]                 │
│ [Generar Temporal]                   │
└──────────────────────────────────────┘
```

---

## 🎨 DISEÑO

### Gestión de Usuarios
- Diseño azul corporativo
- Cards informativos
- Tablas responsivas
- Botones de acción claros
- Confirmaciones antes de eliminar

### Gestión de Contraseñas
- Diseño rojo (acción crítica)
- Pestañas por categoría
- Búsqueda destacada
- Modal para cambiar contraseña
- Generación automática visible

---

## ✅ VENTAJAS DEL MÓDULO

### Centralizado
```
Todo en un solo lugar:
• Ver usuarios
• Crear usuarios
• Gestionar contraseñas
• Controlar accesos
```

### Seguro
```
• Solo staff puede acceder
• Confirmaciones importantes
• Logs de acciones
• Tokens seguros
```

### Eficiente
```
• Búsqueda rápida
• Acciones en 2 clicks
• Generación automática
• Envío de emails
```

### Completo
```
• Gestión total de usuarios
• Recuperación automática
• Panel de administración
• Reportes de acceso
```

---

## 🎉 RESUMEN

```
╔═══════════════════════════════════════════╗
║                                           ║
║  👥 MÓDULO DE USUARIOS                   ║
║     AGREGADO AL SIDEBAR                  ║
║                                           ║
║  📍 Ubicación:                            ║
║     Dashboard → Administración            ║
║                                           ║
║  🔗 2 Enlaces:                            ║
║     • Gestión de Usuarios                 ║
║     • Gestión de Contraseñas              ║
║                                           ║
║  ✅ Funcionalidades:                      ║
║     • Crear/Editar/Eliminar               ║
║     • Bloquear/Desbloquear                ║
║     • Cambiar contraseñas                 ║
║     • Generar temporales                  ║
║     • Envío de emails                     ║
║     • Búsqueda inteligente                ║
║                                           ║
║  🎯 Acceso:                               ║
║     Solo Admin/Staff                      ║
║                                           ║
║  ¡LISTO PARA USAR! 🎊                    ║
║                                           ║
╚═══════════════════════════════════════════╝
```

---

**Ubicación**: Sidebar → Administración  
**Enlaces**: 2 (Usuarios + Contraseñas)  
**Estado**: ✅ AGREGADO Y FUNCIONAL  
**Acceso**: /usuarios/gestionar/  
**Permisos**: Solo Staff/Admin

