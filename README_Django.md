# Digit Soft - Proyecto Django

## Descripción
Sitio web corporativo para Digit Soft, empresa especializada en soluciones informáticas. Desarrollado con Django 5.2.

## Características

### 🏠 **Funcionalidades Principales**
- **Página de inicio** con información corporativa
- **Sección de servicios** detallada
- **Formulario de contacto** funcional
- **Sistema de login** con diferentes roles (Cliente, Administrador, Técnico)
- **Menú lateral** con acceso a módulos de gestión
- **Diseño responsive** para móviles y tablets

### 🔧 **Módulos de Gestión**
1. Gestión de Clientes, Orden de Servicios y Facturación
2. Administrador
3. Gestión de Técnicos
4. Gestión de Proveedores
5. Gestión de Productos
6. Gestión de Garantías
7. Gestión de Compras
8. Gestión de Ventas
9. Servicio Técnico
10. Equipos

### 🛠 **Tecnologías Utilizadas**
- **Backend**: Django 5.2
- **Base de datos**: SQLite (desarrollo)
- **Frontend**: HTML5, CSS3, JavaScript
- **Iconos**: Font Awesome 6.0
- **Responsive**: CSS Grid y Flexbox

## Instalación

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar o descargar el proyecto**
   ```bash
   cd digit-soft-django
   ```

2. **Crear un entorno virtual**
   ```bash
   python -m venv .venv
   ```

3. **Activar el entorno virtual**
   
   En Windows:
   ```bash
   .venv\Scripts\activate
   ```
   
   En Linux/Mac:
   ```bash
   source .venv/bin/activate
   ```

4. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

5. **Aplicar migraciones**
   ```bash
   python manage.py migrate
   ```

6. **Crear un superusuario (opcional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Ejecutar el servidor de desarrollo**
   ```bash
   python manage.py runserver
   ```

8. **Acceder al sitio**
   Abrir navegador en: `http://127.0.0.1:8000`

## Estructura del Proyecto

```
digitsoft_project/
├── digitsoft_project/          # Configuración principal del proyecto
│   ├── __init__.py
│   ├── settings.py            # Configuraciones de Django
│   ├── urls.py                # URLs principales
│   └── wsgi.py                # WSGI para deployment
├── main/                      # Aplicación principal
│   ├── __init__.py
│   ├── views.py               # Vistas del sitio
│   ├── urls.py                # URLs de la aplicación
│   ├── models.py              # Modelos de base de datos
│   └── apps.py
├── templates/                 # Templates de Django
│   ├── base.html              # Template base
│   └── main/                  # Templates específicos
│       ├── home.html          # Página principal
│       └── includes/          # Componentes reutilizables
│           ├── header.html
│           ├── sidebar.html
│           └── footer.html
├── static/                    # Archivos estáticos
│   ├── css/                   # Hojas de estilo
│   ├── js/                    # JavaScript
│   └── imagenes/              # Imágenes
├── modulos/                   # Módulos de gestión (HTML estático)
├── manage.py                  # Script de gestión de Django
└── requirements.txt           # Dependencias del proyecto
```

## Configuración

### Settings Importantes

- **DEBUG**: `True` en desarrollo, `False` en producción
- **ALLOWED_HOSTS**: Configurar para producción
- **DATABASES**: SQLite por defecto, cambiar para producción
- **STATIC_ROOT**: Configurado para archivos estáticos
- **LANGUAGE_CODE**: `es-es` (Español)
- **TIME_ZONE**: `America/Bogota`

### Variables de Entorno (Recomendadas)

Para producción, crear un archivo `.env` con:
```
SECRET_KEY=tu-clave-secreta-aqui
DEBUG=False
ALLOWED_HOSTS=tudominio.com,www.tudominio.com
```

## API Endpoints

### Formularios AJAX

- **POST** `/api/contact/` - Procesar formulario de contacto
- **POST** `/api/login/` - Procesar formulario de login

Ambos endpoints esperan JSON y retornan:
```json
{
    "success": true/false,
    "message": "Mensaje descriptivo"
}
```

## Deployment

### Preparación para Producción

1. **Configurar variables de entorno**
2. **Cambiar DEBUG a False**
3. **Configurar ALLOWED_HOSTS**
4. **Usar base de datos robusta** (PostgreSQL, MySQL)
5. **Configurar servidor web** (Nginx + Gunicorn)
6. **Recopilar archivos estáticos**:
   ```bash
   python manage.py collectstatic
   ```

### Comandos Útiles

```bash
# Ejecutar servidor de desarrollo
python manage.py runserver

# Aplicar migraciones
python manage.py migrate

# Crear migraciones
python manage.py makemigrations

# Recopilar archivos estáticos
python manage.py collectstatic

# Crear superusuario
python manage.py createsuperuser

# Shell de Django
python manage.py shell
```

## Desarrollo

### Agregar Nuevas Funcionalidades

1. **Modelos**: Definir en `main/models.py`
2. **Vistas**: Agregar en `main/views.py`
3. **URLs**: Configurar en `main/urls.py`
4. **Templates**: Crear en `templates/main/`

### Estructura de Templates

- **base.html**: Template principal con header, sidebar, footer
- **home.html**: Extiende base.html, contiene el contenido principal
- **includes/**: Componentes reutilizables

## Contacto

**Digit Soft**  
Calle 15 # 14-26, Duitama - Boyacá  
📞 (+57) 3215434380, (+57) 3148004120, (+57) 3214696917  
📧 info@digitsoft.com.co  

---
*Desarrollado con Django - Soluciones Tecnológicas Integrales*