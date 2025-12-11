# 🏢 DIGITSOFT - Sistema de Gestión Empresarial

Sistema web desarrollado con Django para la gestión integral de empresas de servicios técnicos.

## 📊 Estado del Proyecto

- **Versión:** 1.0.0
- **Última actualización:** Noviembre 2025
- **Estado:** En desarrollo activo
- **Framework:** Django 5.2.8
- **Python:** 3.13

---

## ✅ Módulos Completados

### 🧑‍💼 Módulo de Clientes (100%)
- ✅ Registrar cliente
- ✅ Buscar y filtrar clientes
- ✅ Modificar datos del cliente
- ✅ Eliminar cliente
- ✅ Tema claro/oscuro
- ✅ Diseño responsive

### 🛠️ Módulo de Técnicos (100%)
- ✅ Registrar técnico (RF1)
- ✅ Asignar técnico (RF2)
- ✅ Cambiar técnico (RF3)
- ✅ Buscar técnico (RF4)
- ✅ Eliminar técnico (RF5)
- ✅ Tema claro/oscuro
- ✅ Diseño responsive
- ✅ Validaciones completas
- ✅ 10 técnicos de prueba

### 👥 Módulo de Usuarios (100%)
- ✅ Perfiles de usuario extendidos
- ✅ Gestión de acceso
- ✅ Tipos de usuario (Admin, Cliente, Técnico, Proveedor)
- ✅ Control de bloqueo

---

## 🚀 Inicio Rápido

### 1. Activar Entorno Virtual
```bash
cd C:\Users\jorge\PycharmProjects\PythonProject1\DIGTSoft
.venv\Scripts\activate
```

### 2. Instalar Dependencias
```bash
pip install django pillow
```

### 3. Aplicar Migraciones
```bash
python manage.py migrate
```

### 4. Crear Superusuario (Opcional)
```bash
python manage.py createsuperuser
```

### 5. Crear Datos de Prueba
```bash
# Crear clientes de prueba (10 clientes)
python scripts/crear_clientes_prueba.py

# Crear técnicos de prueba (10 técnicos)
python scripts/crear_tecnicos_prueba.py

# O crear superusuario manualmente
python scripts/crear_superusuario.py
```

### 6. Iniciar Servidor
```bash
python manage.py runserver
```

### 7. Acceder al Sistema
```
Página principal: http://127.0.0.1:8000/
Panel Admin:      http://127.0.0.1:8000/admin/
Clientes:         http://127.0.0.1:8000/clientes/
Técnicos:         http://127.0.0.1:8000/tecnicos/
Dashboard:        http://127.0.0.1:8000/dashboard/
```

---

## 📁 Estructura del Proyecto

```
DIGTSoft/
├── config/                     # Configuración principal
│   ├── settings.py            # Configuración del proyecto
│   ├── urls.py                # URLs principales
│   ├── wsgi.py                # WSGI para producción
│   └── asgi.py                # ASGI para aplicaciones asíncronas
│
├── static/                     # Archivos estáticos
│   ├── css/
│   │   ├── landing.css        # Estilos página principal
│   │   ├── dashboard.css      # Estilos dashboard
│   │   ├── clientes-enhanced.css  # Estilos módulo clientes
│   │   ├── tecnicos.css       # Estilos módulo técnicos
│   │   ├── theme-switcher.css # Tema claro/oscuro
│   │   └── accessibility.css  # Accesibilidad
│   ├── js/
│   │   ├── landing.js         # JavaScript página principal
│   │   ├── tecnicos.js        # JavaScript técnicos
│   │   ├── theme-switcher.js  # Cambio de tema
│   │   └── accessibility.js   # Funciones de accesibilidad
│   └── images/                # Imágenes del sitio
│
├── templates/                  # Plantillas HTML
│   ├── base.html              # Template base
│   ├── base_dashboard.html    # Base del dashboard
│   ├── core/                  # Templates core
│   ├── clientes/              # Templates clientes
│   ├── tecnicos/              # Templates técnicos
│   ├── dashboard/             # Templates dashboard
│   └── usuarios/              # Templates usuarios
│
├── clientes/                   # App de Clientes ✅
│   ├── models.py              # Modelo Cliente
│   ├── views.py               # Vistas CRUD
│   ├── forms.py               # Formularios
│   ├── urls.py                # URLs del módulo
│   ├── admin.py               # Admin personalizado
│   └── migrations/            # Migraciones de BD
│
├── tecnicos/                   # App de Técnicos ✅
│   ├── models.py              # Modelo Tecnico
│   ├── views.py               # Vistas CRUD
│   ├── forms.py               # Formularios
│   ├── urls.py                # URLs del módulo
│   ├── admin.py               # Admin personalizado
│   └── migrations/            # Migraciones de BD
│
├── usuarios/                   # App de Usuarios ✅
│   ├── models.py              # Modelo PerfilUsuario
│   ├── views.py               # Vistas
│   ├── forms.py               # Formularios
│   ├── urls.py                # URLs del módulo
│   ├── admin.py               # Admin personalizado
│   └── migrations/            # Migraciones de BD
│
├── core/                       # App principal ✅
│   ├── views.py               # Vistas generales
│   └── urls.py                # URLs generales
│
├── dashboard/                  # Dashboard ✅
│   ├── views.py               # Vistas del dashboard
│   └── urls.py                # URLs del dashboard
│
├── ordenes/                    # Órdenes de servicio 🚧
├── productos/                  # Productos 🚧
├── proveedores/                # Proveedores 🚧
├── ventas/                     # Ventas 🚧
├── compras/                    # Compras 🚧
├── equipos/                    # Equipos 🚧
├── facturacion/                # Facturación 🚧
├── garantias/                  # Garantías 🚧
├── capacitaciones/             # Capacitaciones 🚧
│
├── scripts/                    # Scripts de utilidad
│   ├── crear_clientes_prueba.py    # Crear clientes de prueba
│   ├── crear_tecnicos_prueba.py    # Crear técnicos de prueba
│   ├── crear_superusuario.py       # Crear superusuario
│   └── check_users.py              # Verificar usuarios
│
├── media/                      # Archivos subidos
├── staticfiles/                # Archivos estáticos compilados
├── db.sqlite3                  # Base de datos SQLite
├── manage.py                   # Comando de Django
└── README.md                   # Esta documentación
```

---

## 🎨 Características Principales

### ✨ Diseño Moderno
- Interfaz limpia y profesional
- Gradientes y animaciones suaves
- Iconos de Font Awesome
- Cards con sombras y efectos hover

### 🌓 Tema Claro/Oscuro
- Cambio instantáneo entre temas
- Transiciones suaves (0.3s)
- Persistencia de preferencia
- Todos los módulos adaptados

### 📱 100% Responsive
- **Desktop** (> 768px): Vista completa
- **Tablet** (768px): Vista adaptada
- **Mobile** (< 768px): Cards apilados

### ✅ Validaciones Completas
- Validación en frontend (JavaScript)
- Validación en backend (Django)
- Mensajes de error claros
- Prevención de datos duplicados

### 🔍 Búsqueda Avanzada
- Búsqueda en tiempo real
- Filtros por múltiples campos
- Paginación (10 registros por página)
- Resultados instantáneos

### 🎯 Animaciones e Interactividad
- Entrada suave de elementos
- Hover effects en botones
- Ripple effect en clicks
- Tooltips informativos
- Alertas auto-cerradas

---

## 💾 Base de Datos

### Modelos Principales

#### Cliente
```python
- nombres, apellidos
- numero_documento (único)
- telefono, correo
- direccion
- observaciones
- activo
- fecha_registro, fecha_actualizacion
```

#### Técnico
```python
- nombres, apellidos
- numero_documento (único)
- telefono, correo (único)
- profesion
- activo
- fecha_registro, fecha_actualizacion
```

#### PerfilUsuario
```python
- user (OneToOne con User)
- tipo_usuario (Admin, Cliente, Técnico, Proveedor)
- telefono, direccion, documento
- foto
- activo, bloqueado
- cliente (FK a Cliente)
- fecha_registro, fecha_actualizacion
```

---

## 🔧 Comandos Útiles

### Gestión de Base de Datos
```bash
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Ver estado de migraciones
python manage.py showmigrations

# Acceder a shell de Django
python manage.py shell
```

### Gestión de Archivos Estáticos
```bash
# Recolectar archivos estáticos
python manage.py collectstatic

# Limpiar archivos estáticos
python manage.py collectstatic --clear --noinput
```

### Usuarios
```bash
# Crear superusuario
python manage.py createsuperuser

# Cambiar contraseña
python manage.py changepassword <username>
```

### Verificación
```bash
# Verificar proyecto
python manage.py check

# Ver información del sistema
python manage.py version
```

---

## 📊 Datos de Prueba

El sistema incluye scripts para crear datos de prueba ubicados en la carpeta `scripts/`:

### Clientes de Prueba (10)
```bash
python scripts/crear_clientes_prueba.py
```
- 8 clientes activos, 2 inactivos
- Datos realistas colombianos
- Diferentes tipos de clientes

### Técnicos de Prueba (10)
```bash
python scripts/crear_tecnicos_prueba.py
```
- 8 técnicos activos, 2 inactivos
- Diferentes profesiones técnicas
- Datos completos de contacto

### Crear Superusuario
```bash
python scripts/crear_superusuario.py
# O manualmente:
python manage.py createsuperuser
```

### Verificar Usuarios
```bash
python scripts/check_users.py
```

---

## 🎯 Módulos Disponibles

### ✅ Implementados
- **Clientes:** Gestión completa de clientes
- **Técnicos:** Gestión completa de técnicos
- **Usuarios:** Perfiles y control de acceso
- **Core:** Página principal y navegación
- **Dashboard:** Panel de control

### 🚧 En Desarrollo
- **Órdenes de Servicio:** Gestión de servicios
- **Productos:** Catálogo de productos
- **Proveedores:** Gestión de proveedores
- **Ventas:** Registro de ventas
- **Compras:** Registro de compras
- **Equipos:** Gestión de equipos
- **Facturación:** Generación de facturas
- **Garantías:** Control de garantías
- **Capacitaciones:** Registro de capacitaciones

---

## 🔐 Seguridad

### Implementado
- ✅ Protección CSRF en formularios
- ✅ Validación de datos en backend
- ✅ Sanitización de entradas
- ✅ Campos únicos en base de datos
- ✅ Confirmación de acciones destructivas

### Recomendaciones para Producción
- [ ] Cambiar SECRET_KEY
- [ ] DEBUG = False
- [ ] Configurar ALLOWED_HOSTS
- [ ] Usar base de datos PostgreSQL
- [ ] Configurar HTTPS
- [ ] Implementar autenticación de dos factores
- [ ] Configurar copias de seguridad

---

## 🎨 Temas y Estilos

### Paleta de Colores

#### Tema Claro
- Fondo: `#f8f9fa`
- Cards: `#ffffff`
- Texto: `#2c3e50`
- Bordes: `#dee2e6`

#### Tema Oscuro
- Fondo: `#1a1a2e`
- Cards: `#16213e`
- Texto: `#eaeaea`
- Bordes: `#2d3748`

#### Colores de Estado
- 🟣 Primario: `#667eea` - `#764ba2`
- 🟢 Activo/Éxito: `#2ecc71`
- 🔴 Inactivo/Peligro: `#e74c3c`
- 🟡 Advertencia: `#f39c12`
- 🔵 Información: `#3498db`

---

## 🧪 Testing

### Pruebas Recomendadas

#### Clientes
- [ ] Crear cliente con datos válidos
- [ ] Intentar crear con documento duplicado
- [ ] Buscar cliente por nombre
- [ ] Editar cliente existente
- [ ] Eliminar cliente
- [ ] Filtrar por estado

#### Técnicos
- [ ] Crear técnico con datos válidos
- [ ] Validar documento único
- [ ] Validar correo único
- [ ] Buscar técnico
- [ ] Editar técnico
- [ ] Eliminar técnico
- [ ] Cambiar tema claro/oscuro

#### Responsive
- [ ] Vista desktop (1920px)
- [ ] Vista tablet (768px)
- [ ] Vista mobile (375px)
- [ ] Rotación de pantalla

---

## 📚 Tecnologías Utilizadas

- **Backend:** Django 5.2.8
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **Base de Datos:** SQLite (desarrollo), PostgreSQL (recomendado para producción)
- **Iconos:** Font Awesome 6
- **Fuentes:** System fonts
- **Servidor:** Django Development Server (desarrollo)

---

## 🤝 Contribución

Este es un proyecto privado para DIGITSOFT. Para contribuir:

1. Crear una rama para tu feature
2. Realizar los cambios
3. Probar exhaustivamente
4. Documentar los cambios
5. Crear pull request

---

## 📝 Convenciones de Código

### Python
- Seguir PEP 8
- Docstrings en español
- Nombres de variables descriptivos
- Comentarios cuando sea necesario

### HTML/CSS
- Indentación de 4 espacios
- Clases en kebab-case
- IDs únicos y descriptivos
- CSS organizado por secciones

### JavaScript
- camelCase para variables y funciones
- Comentarios en español
- Código modular y reutilizable

---

## 🐛 Solución de Problemas

### Error: No module named 'django'
```bash
pip install django
```

### Error: No such table
```bash
python manage.py migrate
```

### Archivos estáticos no cargan
```bash
python manage.py collectstatic --noinput
```

### Puerto 8000 en uso
```bash
python manage.py runserver 8001
```

---

## 📞 Soporte

Para dudas o problemas:
1. Revisar esta documentación
2. Verificar logs de Django
3. Revisar consola del navegador (F12)
4. Verificar migraciones aplicadas

---

## 🗺️ Roadmap

### Versión 1.1 (Próxima)
- [ ] Módulo de Órdenes de Servicio
- [ ] Dashboard con estadísticas
- [ ] Reportes básicos
- [ ] Notificaciones por email

### Versión 1.2
- [ ] Módulo de Productos
- [ ] Módulo de Proveedores
- [ ] Módulo de Ventas
- [ ] Inventario

### Versión 1.3
- [ ] Facturación electrónica
- [ ] Módulo de Compras
- [ ] Control de garantías
- [ ] Reportes avanzados

### Versión 2.0
- [ ] API REST
- [ ] App móvil
- [ ] Multi-empresa
- [ ] Integración con ERP

---

## 📄 Licencia

Proyecto privado - Todos los derechos reservados
© 2025 DIGIT SOFT

---

## 👥 Créditos

- **Desarrollador:** Equipo DIGIT SOFT
- **Framework:** Django Software Foundation
- **Iconos:** Font Awesome
- **Inspiración:** Sistemas modernos de gestión empresarial

---

## 📈 Estadísticas del Proyecto

- **Líneas de código:** ~5,000+
- **Archivos Python:** 50+
- **Templates HTML:** 20+
- **Archivos CSS:** 10+
- **Archivos JavaScript:** 5+
- **Modelos de BD:** 3 (activos)
- **Vistas:** 30+
- **URLs:** 25+

---

## 🎯 Objetivos del Proyecto

1. ✅ Crear un sistema moderno y funcional
2. ✅ Implementar diseño responsive
3. ✅ Incluir tema claro/oscuro
4. ✅ Validaciones completas
5. 🚧 Completar todos los módulos
6. 🚧 Implementar reportes
7. 🚧 Desplegar en producción

---

**Última actualización:** 7 de Noviembre, 2025
**Versión:** 1.0.0
**Estado:** ✅ En desarrollo activo

