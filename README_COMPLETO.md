# 🖥️ DIGITSOFT - Sistema de Gestión Empresarial

![Django](https://img.shields.io/badge/Django-5.2.8-green.svg)
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

Sistema integral de gestión empresarial desarrollado con Django, especializado en la administración de productos, garantías, clientes, técnicos y servicios.

## 🌟 Características Principales

### 📦 **Gestión de Productos e Inventario**
- ✅ CRUD completo de productos
- ✅ Control de stock en tiempo real
- ✅ Alertas de bajo stock
- ✅ Categorización de productos
- ✅ Registro de movimientos de inventario
- ✅ Búsqueda y filtros avanzados
- ✅ Gestión de precios (compra/venta)

### 🛡️ **Sistema de Garantías**
- ✅ Registro y seguimiento de garantías
- ✅ Estados: Registrada, En Proceso, Solucionada, Rechazada
- ✅ Historial de seguimiento
- ✅ Vinculación con productos y clientes
- ✅ Observaciones y notas

### 👥 **Gestión de Clientes**
- ✅ Base de datos completa de clientes
- ✅ Información de contacto
- ✅ Historial de compras
- ✅ Historial de garantías

### 🔧 **Gestión de Técnicos**
- ✅ Registro de técnicos
- ✅ Perfiles profesionales
- ✅ Asignación de garantías
- ✅ Especialidades y certificaciones

### 📊 **Dashboard Intuitivo**
- ✅ Estadísticas en tiempo real
- ✅ Gráficos y reportes
- ✅ Resumen de actividades
- ✅ Alertas importantes

### 🎨 **Interfaz Moderna**
- ✅ Diseño responsive (mobile-first)
- ✅ Tema claro/oscuro
- ✅ Iconos Font Awesome
- ✅ Bootstrap 5
- ✅ Animaciones suaves

## 🚀 Instalación

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git

### Pasos de Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/Jorge523757/Digit_Sof_Nuevo.git
cd Digit_Sof_Nuevo
```

2. **Crear entorno virtual**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Configurar base de datos**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Crear superusuario**
```bash
python manage.py createsuperuser
```

6. **Recolectar archivos estáticos**
```bash
python manage.py collectstatic --noinput
```

7. **Iniciar servidor de desarrollo**
```bash
python manage.py runserver
```

8. **Acceder a la aplicación**
```
http://127.0.0.1:8000/
```

## 📁 Estructura del Proyecto

```
DIGTSoft/
├── capacitaciones/     # Módulo de capacitaciones
├── clientes/          # Gestión de clientes
├── compras/           # Módulo de compras
├── config/            # Configuración Django
├── core/              # Funcionalidades core
├── dashboard/         # Dashboard principal
├── equipos/           # Gestión de equipos
├── facturacion/       # Sistema de facturación
├── garantias/         # Sistema de garantías ⭐
├── ordenes/           # Órdenes de servicio
├── productos/         # Gestión de productos e inventario ⭐
├── proveedores/       # Gestión de proveedores
├── scripts/           # Scripts útiles
├── static/            # Archivos estáticos (CSS, JS, imágenes)
├── staticfiles/       # Archivos estáticos recolectados
├── tecnicos/          # Gestión de técnicos
├── templates/         # Plantillas HTML
├── usuarios/          # Sistema de usuarios
├── ventas/            # Módulo de ventas
├── manage.py          # Script de gestión Django
└── requirements.txt   # Dependencias del proyecto
```

## 🛠️ Tecnologías Utilizadas

- **Backend:** Django 5.2.8
- **Base de Datos:** SQLite (desarrollo), PostgreSQL (producción)
- **Frontend:** HTML5, CSS3, JavaScript
- **Framework CSS:** Bootstrap 5
- **Iconos:** Font Awesome 6
- **Control de Versiones:** Git

## 📝 Módulos Principales

### Productos
- Gestión completa de inventario
- Control de stock automático
- Movimientos de entrada/salida
- Categorización

### Garantías
- Registro de solicitudes
- Seguimiento de estado
- Asignación a técnicos
- Historial completo

### Clientes
- Base de datos centralizada
- Historial de transacciones
- Información de contacto

### Técnicos
- Perfiles profesionales
- Asignación de tareas
- Seguimiento de desempeño

## 🔒 Seguridad

- Autenticación de usuarios
- Control de acceso por roles
- Protección CSRF
- Validación de formularios
- Sanitización de datos

## 📈 Próximas Características

- [ ] Sistema de reportes PDF
- [ ] Exportación a Excel
- [ ] Notificaciones por email
- [ ] API REST
- [ ] Aplicación móvil
- [ ] Integración con pasarelas de pago
- [ ] Chat en tiempo real
- [ ] Sistema de backup automático

## 🤝 Contribuir

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/NuevaCaracteristica`)
3. Commit tus cambios (`git commit -m 'Agregar nueva característica'`)
4. Push a la rama (`git push origin feature/NuevaCaracteristica`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👨‍💻 Autor

**Jorge**
- GitHub: [@Jorge523757](https://github.com/Jorge523757)

## 📞 Soporte

Si tienes alguna pregunta o problema, por favor abre un issue en GitHub.

## 🙏 Agradecimientos

- Django Software Foundation
- Bootstrap Team
- Font Awesome
- Comunidad de código abierto

---

⭐ Si este proyecto te fue útil, por favor dale una estrella en GitHub!

**Desarrollado con ❤️ usando Django**

