# 🚀 DIGIT SOFT - Sistema de Gestión

## 📋 Descripción

Sistema completo de gestión de servicios técnicos con módulos integrados para:
- Clientes
- Técnicos  
- Órdenes de servicio
- Reportes de daños
- Inventario
- Compras
- Reportes y análisis

---

## ⚡ INICIO RÁPIDO (CONFIGURACIÓN AUTOMÁTICA)

### Requisitos Previos

- Python 3.8 o superior
- pip instalado

### Pasos de Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/Jorge523757/Digit_Sof_Nuevo.git
   cd Digit_Sof_Nuevo
   git checkout jorge-dev
   ```

2. **Ejecutar configuración automática**

   **En Windows:**
   ```bash
   SETUP_AUTOMATICO.bat
   ```

   **En Linux/Mac:**
   ```bash
   python setup_proyecto.py
   ```

   Esto instalará automáticamente:
   - ✅ Todas las dependencias
   - ✅ Migraciones de base de datos
   - ✅ Superusuario (admin/admin123)
   - ✅ Vistas SQL
   - ✅ Archivos estáticos

3. **Iniciar el servidor**
   ```bash
   python manage.py runserver
   ```

4. **Acceder al sistema**
   ```
   http://127.0.0.1:8000
   ```

---

## 🔑 CREDENCIALES PREDETERMINADAS

**Superusuario:**
- Usuario: `admin`
- Contraseña: `admin123`
- Email: `admin@digitsoft.com`

---

## 🎯 CARACTERÍSTICAS PRINCIPALES

### Módulo de Órdenes de Servicio
- ✅ Gestión completa de órdenes
- ✅ Seguimiento de estados
- ✅ Asignación de técnicos
- ✅ Cálculo automático de costos
- ✅ Sistema de notificaciones
- ✅ **Reportes en Excel y PDF**
- ✅ **Vistas SQL personalizadas**
- ✅ **Dashboard ejecutivo**

### Sistema de Reportes
- ✅ Generación de reportes Excel profesionales
- ✅ Generación de reportes PDF
- ✅ Vista previa AJAX en tiempo real
- ✅ Filtros avanzados (fecha, estado, cliente, técnico)

### Vistas SQL Avanzadas (8 vistas)
- ✅ Vista completa de órdenes con datos relacionados
- ✅ Estadísticas por estado
- ✅ Rendimiento de técnicos
- ✅ Historial de clientes
- ✅ Órdenes críticas
- ✅ Análisis de equipos
- ✅ Dashboard ejecutivo
- ✅ Timeline de órdenes

### Otros Módulos
- ✅ Gestión de clientes
- ✅ Gestión de técnicos
- ✅ Reportes de daños
- ✅ Inventario
- ✅ Sistema de compras
- ✅ Autenticación con Google OAuth
- ✅ Sistema de permisos

---

## 📂 ESTRUCTURA DEL PROYECTO

```
Digit_Sof_Nuevo/
├── config/                 # Configuración Django
├── core/                   # Módulo principal
├── clientes/              # Gestión de clientes
├── tecnicos/              # Gestión de técnicos
├── ordenes/               # Órdenes de servicio
│   ├── reportes.py        # Generador de reportes
│   ├── views_reportes.py  # Vistas de reportes
│   └── views_vistas.py    # Vistas SQL
├── usuarios/              # Autenticación
├── inventario/            # Gestión de inventario
├── compras/               # Sistema de compras
├── reportes_dano/         # Reportes de daños
├── templates/             # Plantillas HTML
├── static/                # Archivos estáticos
├── media/                 # Archivos multimedia
├── requirements.txt       # Dependencias
├── setup_proyecto.py      # Configuración automática
├── SETUP_AUTOMATICO.bat   # Script Windows
└── README.md             # Este archivo
```

---

## 🛠️ INSTALACIÓN MANUAL (OPCIONAL)

Si prefieres configurar manualmente:

### 1. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 2. Aplicar migraciones
```bash
python manage.py migrate
```

### 3. Crear superusuario
```bash
python manage.py createsuperuser
```

### 4. Crear vistas SQL (opcional)
```bash
python gestionar_vistas_ordenes.py crear
```

### 5. Recolectar archivos estáticos
```bash
python manage.py collectstatic
```

### 6. Iniciar servidor
```bash
python manage.py runserver
```

---

## 📊 ACCESO A LAS FUNCIONALIDADES

### Reportes de Órdenes
```
http://127.0.0.1:8000/ordenes/reportes/
```

### Dashboard Ejecutivo
```
http://127.0.0.1:8000/ordenes/vistas/dashboard-ejecutivo/
```

### Órdenes Críticas
```
http://127.0.0.1:8000/ordenes/vistas/criticas/
```

### Panel de Administración
```
http://127.0.0.1:8000/admin/
```

---

## 🔧 COMANDOS ÚTILES

### Crear datos de prueba
```bash
python crear_datos_prueba.py
```

### Reparar registros duplicados
```bash
python reparar_registros_duplicados.py
```

### Verificar sistema
```bash
python manage.py check
```

### Crear migraciones
```bash
python manage.py makemigrations
```

---

## 📦 DEPENDENCIAS PRINCIPALES

- Django 6.0.2
- django-allauth (Google OAuth)
- Pillow (Imágenes)
- openpyxl (Reportes Excel)
- reportlab (Reportes PDF)
- django-crispy-forms (Formularios)

Ver `requirements.txt` para la lista completa.

---

## 🌐 NAVEGADORES SOPORTADOS

- ✅ Chrome (Recomendado)
- ✅ Firefox
- ✅ Edge
- ✅ Safari

---

## 📱 RESPONSIVE

El sistema es completamente responsive y funciona en:
- ✅ Desktop
- ✅ Tablet
- ✅ Móvil

---

## 🎨 CARACTERÍSTICAS DE DISEÑO

- Interfaz moderna y profesional
- Modo oscuro disponible
- Animaciones suaves
- Diseño responsive
- Accesibilidad mejorada

---

## 🔐 SEGURIDAD

- ✅ Autenticación de usuarios
- ✅ Sistema de permisos
- ✅ Protección CSRF
- ✅ Validación de formularios
- ✅ Hash de contraseñas

---

## 📝 NOTAS IMPORTANTES

1. **Base de datos:** El proyecto usa SQLite por defecto (db.sqlite3)
2. **Archivos estáticos:** Se sirven desde /static/
3. **Archivos media:** Se suben a /media/
4. **Debug:** Está activado en desarrollo (DEBUG=True)

---

## 🆘 SOLUCIÓN DE PROBLEMAS

### Error: "No module named 'X'"
```bash
pip install -r requirements.txt
```

### Error: "No such table"
```bash
python manage.py migrate
```

### Error: Puerto 8000 ocupado
```bash
python manage.py runserver 8080
```

### Restablecer base de datos
```bash
# Eliminar db.sqlite3
python manage.py migrate
python setup_proyecto.py
```

---

## 📧 CONTACTO

**Desarrollador:** Jorge Guarín  
**Proyecto:** DIGIT SOFT  
**Fecha:** Febrero 2026

---

## 📄 LICENCIA

Este proyecto es privado y de uso exclusivo para DIGIT SOFT.

---

## ✨ ACTUALIZACIONES RECIENTES

### Versión Actual (jorge-dev)

**Últimas características agregadas:**
- ✅ Sistema completo de reportes Excel/PDF
- ✅ 8 vistas SQL personalizadas con filtros
- ✅ Dashboard ejecutivo con métricas en tiempo real
- ✅ Vista de órdenes críticas
- ✅ API JSON para integraciones
- ✅ Corrección de errores de registro
- ✅ Google OAuth funcionando
- ✅ Configuración automática del proyecto

---

## 🎯 PRÓXIMOS PASOS DESPUÉS DE INSTALAR

1. ✅ Acceder al sistema con admin/admin123
2. ✅ Explorar el módulo de órdenes
3. ✅ Generar tu primer reporte
4. ✅ Revisar el dashboard ejecutivo
5. ✅ Personalizar según tus necesidades

---

**¡Gracias por usar DIGIT SOFT! 🚀**

