# 🏢 DIGIT SOFT - Sistema de Gestión Empresarial

Sistema completo de gestión para servicios técnicos, inventario, ventas y facturación.

## 📋 Tabla de Contenidos

- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Uso](#uso)
- [Módulos](#módulos)
- [Credenciales](#credenciales)
- [Estructura del Proyecto](#estructura-del-proyecto)

---

## ✨ Características

### Gestión de Clientes y Técnicos
- ✅ Registro completo de clientes
- ✅ Gestión de técnicos
- ✅ Reportes en PDF y Excel
- ✅ Búsqueda avanzada

### Órdenes de Servicio
- ✅ Gestión completa de órdenes
- ✅ Asignación de técnicos
- ✅ Seguimiento de estados
- ✅ Notificaciones por correo

### Inventario
- ✅ Gestión de equipos
- ✅ Control de productos
- ✅ Proveedores
- ✅ Garantías

### Ventas y Facturación
- ✅ Sistema de ventas
- ✅ Gestión de compras
- ✅ Facturación electrónica
- ✅ E-commerce integrado

### Seguridad
- ✅ Autenticación de usuarios
- ✅ Control de acceso por roles (Admin, Cliente, Técnico)
- ✅ Recuperación de contraseña por email
- ✅ Gestión de contraseñas (solo admin)
- ✅ Privacidad de datos por usuario

---

## 💻 Requisitos

- Python 3.9 o superior
- Django 6.0.2
- MySQL (opcional, usa SQLite por defecto)
- Windows / Linux / macOS

---

## 🚀 Instalación

### 1. Clonar el Repositorio

```bash
git clone https://github.com/tu-usuario/digit-soft.git
cd digit-soft
```

### 2. Crear Entorno Virtual

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar Base de Datos

**Opción 1: SQLite (Por defecto)**
```bash
python manage.py migrate
```

**Opción 2: MySQL**
```bash
# Editar config/settings.py - Sección DATABASES
python manage.py migrate
```

### 5. Crear Superusuario

**Opción 1: Script automático**
```bash
python crear_superusuario.py
```

**Opción 2: Manual**
```bash
python manage.py createsuperuser
```

**Opción 3: Windows (Doble click)**
```
CREAR_SUPERUSUARIO.bat
```

### 6. Iniciar Servidor

```bash
python manage.py runserver
```

### 7. Acceder al Sistema

```
http://127.0.0.1:8000/
```

---

## ⚙️ Configuración

### Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto (opcional):

```env
DEBUG=True
SECRET_KEY=tu-clave-secreta
DATABASE_NAME=digit_soft
DATABASE_USER=root
DATABASE_PASSWORD=tu_password
DATABASE_HOST=localhost
DATABASE_PORT=3306

# Email
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=tu_email@gmail.com
EMAIL_HOST_PASSWORD=tu_password_app
```

### Configurar Email (Gmail)

1. Ir a: https://myaccount.google.com/apppasswords
2. Crear "Contraseña de aplicación"
3. Ejecutar:
```bash
python CONFIGURAR_EMAIL_GMAIL.bat
```

O editar manualmente `config/settings.py`

---

## 🎯 Uso

### Credenciales por Defecto

**Superusuario:**
- Usuario: `admin`
- Contraseña: `admin123`
- Email: `admin@digitsoft.com`

**⚠️ IMPORTANTE:** Cambiar la contraseña después del primer login

### Accesos

**Sistema Principal:**
```
http://127.0.0.1:8000/usuarios/login/
```

**Panel Admin Django:**
```
http://127.0.0.1:8000/admin/
```

**Dashboard:**
```
http://127.0.0.1:8000/dashboard/
```

---

## 📦 Módulos

### Para Administradores

1. **Gestión de Usuarios**
   - Crear/Editar/Eliminar usuarios
   - Asignar roles
   - Gestionar permisos

2. **Gestión de Contraseñas**
   - Cambiar contraseñas de usuarios
   - Ver usuarios con/sin cuenta
   - Búsqueda y filtros

3. **Clientes**
   - Registro de clientes
   - Historial completo
   - Reportes

4. **Técnicos**
   - Gestión de técnicos
   - Asignación de órdenes
   - Disponibilidad

5. **Órdenes de Servicio**
   - Crear órdenes
   - Asignar técnicos
   - Seguimiento

6. **Equipos**
   - Registro de equipos
   - Historial de servicio
   - Garantías

7. **Productos**
   - Inventario
   - Stock
   - Precios

8. **Proveedores**
   - Gestión de proveedores
   - Compras
   - Historial

9. **Ventas**
   - Punto de venta
   - Facturación
   - Reportes

10. **Facturación**
    - Generación de facturas
    - Impresión
    - Exportación

11. **E-commerce**
    - Tienda online
    - Carrito de compras
    - Checkout

### Para Técnicos

1. **Órdenes Asignadas**
   - Ver órdenes propias
   - Actualizar estado
   - Registrar trabajo

2. **Clientes**
   - Ver clientes de sus órdenes
   - Información de contacto

3. **Equipos**
   - Ver equipos de sus órdenes
   - Historial

### Para Clientes

1. **Mis Equipos**
   - Ver equipos registrados
   - Reportar daños

2. **Mis Órdenes**
   - Ver estado de órdenes
   - Historial

3. **Mis Facturas**
   - Ver facturas
   - Descargar

4. **Mis Garantías**
   - Ver garantías activas
   - Fechas de vencimiento

---

## 🔐 Seguridad

### Roles y Permisos

**Administrador:**
- Acceso completo al sistema
- Gestión de usuarios y contraseñas
- Todos los módulos

**Técnico:**
- Órdenes asignadas
- Clientes de sus órdenes
- Equipos de sus órdenes

**Cliente:**
- Solo sus datos
- Sus equipos
- Sus órdenes
- Sus facturas
- Sus garantías

### Características de Seguridad

- ✅ Autenticación obligatoria
- ✅ Control de acceso por rol
- ✅ Filtros de privacidad en todas las vistas
- ✅ Protección CSRF
- ✅ Prevención XSS
- ✅ Sidebar dinámico según permisos
- ✅ Recuperación de contraseña segura

---

## 📁 Estructura del Proyecto

```
Digit_Sof_Nuevo/
├── config/                 # Configuración del proyecto
│   ├── settings.py        # Configuraciones generales
│   ├── urls.py            # URLs principales
│   └── wsgi.py            # WSGI para producción
├── core/                  # Módulo principal
│   └── decorators.py     # Decoradores de seguridad
├── usuarios/              # Gestión de usuarios
├── clientes/             # Gestión de clientes
├── tecnicos/             # Gestión de técnicos
├── ordenes/              # Órdenes de servicio
├── equipos/              # Gestión de equipos
├── productos/            # Inventario de productos
├── proveedores/          # Gestión de proveedores
├── ventas/               # Sistema de ventas
├── compras/              # Gestión de compras
├── facturacion/          # Facturación
├── garantias/            # Gestión de garantías
├── ecommerce/            # Tienda online
├── reportes_dano/        # Reportes de daños
├── capacitaciones/       # Módulo de capacitación
├── ayuda/                # Centro de ayuda
├── templates/            # Plantillas HTML
├── static/               # Archivos estáticos
├── media/                # Archivos subidos
├── manage.py             # Django manager
├── requirements.txt      # Dependencias Python
├── crear_superusuario.py # Script crear admin
├── CREAR_SUPERUSUARIO.bat # Ejecutable Windows
└── README.md             # Esta documentación
```

---

## 🛠️ Scripts Útiles

### Windows (.bat)

- `CREAR_SUPERUSUARIO.bat` - Crear administrador
- `CONFIGURAR_EMAIL_GMAIL.bat` - Configurar email
- `CREAR_BD_MYSQL.bat` - Crear base de datos MySQL

### Python (.py)

- `crear_superusuario.py` - Crear/actualizar admin
- `configurar_email_gmail.py` - Setup de email
- `verificar_seguridad.py` - Verificar protecciones

---

## 📊 Comandos Útiles

### Migraciones

```bash
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Ver migraciones
python manage.py showmigrations
```

### Base de Datos

```bash
# Shell de Django
python manage.py shell

# SQL de migración
python manage.py sqlmigrate app_name migration_name

# Limpiar base de datos
python manage.py flush
```

### Servidor

```bash
# Desarrollo
python manage.py runserver

# Puerto específico
python manage.py runserver 8080

# Acceso externo
python manage.py runserver 0.0.0.0:8000
```

### Archivos Estáticos

```bash
# Recolectar archivos estáticos
python manage.py collectstatic

# Limpiar archivos estáticos
python manage.py collectstatic --clear
```

---

## 🐛 Solución de Problemas

### Error: ModuleNotFoundError

```bash
pip install -r requirements.txt
```

### Error: Base de datos bloqueada

```bash
# Cerrar todas las conexiones
# Reiniciar el servidor
```

### Error: Puerto en uso

```bash
# Windows
netstat -ano | findstr :8000
taskkill /PID <numero_pid> /F

# Linux/Mac
lsof -ti:8000 | xargs kill -9
```

### Olvidé la contraseña del admin

```bash
python crear_superusuario.py
# Restablece a: admin123
```

### Email no se envía

1. Verificar configuración en `settings.py`
2. Verificar contraseña de aplicación
3. Revisar logs del servidor

---

## 📝 Documentación Adicional

En el proyecto encontrarás archivos `.md` con documentación específica:

- `SEGURIDAD_SISTEMA_COMPLETO.md` - Seguridad implementada
- `SUPERUSUARIO_CREADO.md` - Info del superusuario
- `PRIVACIDAD_COMPLETA_IMPLEMENTADA.md` - Privacidad de datos
- `MODULO_GESTION_CONTRASENAS_ADMIN.md` - Gestión de contraseñas

---

## 🤝 Contribuir

1. Fork el proyecto
2. Crea tu rama (`git checkout -b feature/nueva-caracteristica`)
3. Commit tus cambios (`git commit -am 'Agregar nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Crea un Pull Request

---

## 📄 Licencia

Este proyecto es privado y propietario.

---

## 👥 Autor

**DIGIT SOFT**  
Sistema de Gestión Empresarial  
© 2026 - Todos los derechos reservados

---

## 📞 Soporte

Para soporte, contactar a:
- Email: soporte@digitsoft.com
- Sistema: `/ayuda/` (Centro de Ayuda)

---

## ✅ Checklist de Instalación

- [ ] Python instalado
- [ ] Repositorio clonado
- [ ] Entorno virtual creado
- [ ] Dependencias instaladas
- [ ] Base de datos migrada
- [ ] Superusuario creado
- [ ] Email configurado (opcional)
- [ ] Servidor iniciado
- [ ] Login verificado
- [ ] Contraseña cambiada

---

## 🎉 ¡Listo para Usar!

El sistema está completamente configurado y listo para usar.

**Siguiente paso:** `python manage.py runserver`

---

**Última Actualización:** 11/02/2026  
**Versión:** 1.0.0  
**Estado:** ✅ Producción Ready

