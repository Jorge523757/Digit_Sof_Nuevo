# 📋 Instrucciones de Desarrollo - DIGIT SOFT

## ✅ Estado del Proyecto
- ✅ Proyecto subido a GitHub: https://github.com/Jorge523757/Digit_Sof_Nuevo
- ✅ Módulos de Productos y Garantías funcionando correctamente
- ✅ Error de 'dashboard' corregido
- ✅ Código profesional y documentado

## 🛠️ Problemas Resueltos

### 1. Error NoReverseMatch: 'dashboard' not found
**Problema:** Las plantillas de productos y garantías intentaban usar `{% url 'dashboard:index' %}` que no existía.

**Solución:** Se cambió a `{% url 'core:home' %}` en:
- `templates/productos/lista.html`
- `templates/garantias/lista.html`

### 2. Configuración de Git y GitHub
**Acciones realizadas:**
```bash
git init
git config user.name "Jorge"
git config user.email "jorge@digitsoft.com"
git branch -M main
git add .
git commit -m "Primer commit"
git remote add origin https://github.com/Jorge523757/Digit_Sof_Nuevo.git
git pull origin main --allow-unrelated-histories
git push -u origin main
```

## 🚀 Cómo Ejecutar el Proyecto

### Desde el Repositorio Clonado
```bash
# Clonar el repositorio
git clone https://github.com/Jorge523757/Digit_Sof_Nuevo.git
cd Digit_Sof_Nuevo

# Crear entorno virtual
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Instalar dependencias
pip install -r requirements.txt

# Migrar base de datos
python manage.py makemigrations
python manage.py migrate

# Crear superusuario (opcional)
python manage.py createsuperuser

# Ejecutar servidor
python manage.py runserver
```

### Acceder a la Aplicación
- **Home:** http://127.0.0.1:8000/
- **Productos:** http://127.0.0.1:8000/productos/
- **Garantías:** http://127.0.0.1:8000/garantias/
- **Clientes:** http://127.0.0.1:8000/clientes/
- **Técnicos:** http://127.0.0.1:8000/tecnicos/
- **Admin:** http://127.0.0.1:8000/admin/

## 📦 Módulos Principales

### Productos (E-commerce e Inventario)
**Archivos principales:**
- `productos/models.py` - Modelos de Producto, Categoría, MovimientoInventario
- `productos/views.py` - CRUD completo con búsqueda y filtros
- `productos/forms.py` - Formularios con validaciones
- `templates/productos/` - Plantillas HTML profesionales
- `static/css/productos.css` - Estilos modernos con tema claro/oscuro

**Características:**
- ✅ Gestión completa de inventario
- ✅ Control de stock automático
- ✅ Alertas de bajo stock
- ✅ Búsqueda y filtros avanzados
- ✅ Imágenes de productos
- ✅ Categorización
- ✅ Movimientos de entrada/salida

### Garantías
**Archivos principales:**
- `garantias/models.py` - Modelos de Garantía y SeguimientoGarantia
- `garantias/views.py` - Sistema de seguimiento completo
- `garantias/forms.py` - Formularios con validaciones
- `templates/garantias/` - Plantillas HTML profesionales
- `static/css/garantias.css` - Estilos modernos

**Características:**
- ✅ Registro de garantías
- ✅ Estados: Registrada, En Proceso, Solucionada, Rechazada
- ✅ Historial de seguimiento
- ✅ Asignación a técnicos
- ✅ Vinculación con productos y clientes

## 🎨 Características de Diseño

### Diseño Responsive
- ✅ Mobile-first approach
- ✅ Bootstrap 5
- ✅ Funciona en todos los dispositivos

### Tema Claro/Oscuro
- ✅ Variables CSS personalizadas
- ✅ Transiciones suaves
- ✅ Preferencia guardada

### Iconos y Animaciones
- ✅ Font Awesome 6
- ✅ Transiciones CSS
- ✅ Hover effects

## 🔧 Personalización

### Cambiar Colores del Tema
Editar variables en `static/css/productos.css` o `static/css/garantias.css`:
```css
:root {
    --card-bg: #ffffff;
    --text-primary: #2c3e50;
    --border-color: #dee2e6;
    /* ... más variables ... */
}
```

### Agregar Nuevo Módulo
1. Crear app: `python manage.py startapp nombre_modulo`
2. Agregar a `INSTALLED_APPS` en `config/settings.py`
3. Crear modelos en `models.py`
4. Crear vistas en `views.py`
5. Crear URLs en `urls.py`
6. Agregar al `config/urls.py`
7. Crear plantillas en `templates/nombre_modulo/`
8. Crear CSS en `static/css/nombre_modulo.css`

## 📊 Datos de Prueba

### Crear Datos de Prueba
```bash
# Ejecutar scripts de prueba
python manage.py shell < scripts/crear_productos_prueba.py
python manage.py shell < scripts/crear_clientes_prueba.py
python manage.py shell < scripts/crear_tecnicos_prueba.py
python manage.py shell < scripts/crear_garantias_prueba.py
```

## 🐛 Debug y Solución de Problemas

### Ver logs en tiempo real
- Los errores se muestran en la consola donde corre `runserver`
- Revisar `DEBUG = True` en `config/settings.py` (solo desarrollo)

### Errores comunes

**Error: No module named 'XXX'**
```bash
pip install -r requirements.txt
```

**Error: No such table**
```bash
python manage.py makemigrations
python manage.py migrate
```

**Error: Static files not found**
```bash
python manage.py collectstatic
```

## 📝 Buenas Prácticas

### Git
- Commits descriptivos
- Branching para features
- Pull requests para cambios importantes

### Python/Django
- Seguir PEP 8
- Documentar funciones complejas
- Usar type hints cuando sea posible
- Validar datos en forms y models

### Frontend
- CSS organizado por módulo
- JavaScript modular
- Accesibilidad (aria-labels, alt text)

## 🔐 Seguridad

### Antes de Producción
- [ ] Cambiar `SECRET_KEY` en `settings.py`
- [ ] Configurar `DEBUG = False`
- [ ] Configurar `ALLOWED_HOSTS`
- [ ] Usar base de datos PostgreSQL
- [ ] Configurar HTTPS
- [ ] Configurar variables de entorno
- [ ] Revisar permisos de archivos
- [ ] Configurar backups automáticos

## 📞 Contacto

**Desarrollador:** Jorge  
**GitHub:** [@Jorge523757](https://github.com/Jorge523757)  
**Repositorio:** https://github.com/Jorge523757/Digit_Sof_Nuevo

## 🎯 Próximos Pasos

1. [ ] Implementar sistema de reportes PDF
2. [ ] Agregar exportación a Excel
3. [ ] Implementar notificaciones por email
4. [ ] Crear API REST
5. [ ] Agregar gráficos de estadísticas
6. [ ] Implementar sistema de roles y permisos
7. [ ] Agregar tests unitarios
8. [ ] Optimizar queries de base de datos
9. [ ] Implementar caché
10. [ ] Documentar API con Swagger

---

**Última actualización:** 2025-11-10  
**Versión:** 1.0.0  
**Estado:** ✅ Producción Ready

