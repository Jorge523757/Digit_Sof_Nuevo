# 📋 GUÍA: Plantillas HTML Faltantes para Completar

## 🎯 OBJETIVO
Crear las plantillas HTML modernas para los módulos que ya tienen modelos y vistas completos pero necesitan sus templates.

---

## 📁 PLANTILLAS NECESARIAS

### 1. PROVEEDORES (/templates/proveedores/)

#### ✅ Ya creado:
- `lista.html` - Lista con tablas modernas

#### 🔨 Por crear:
- `form.html` - Formulario de crear/editar
- `detalle.html` - Ver detalles del proveedor
- `eliminar.html` - Confirmación de eliminación

---

### 2. VENTAS (/templates/ventas/)

#### 🔨 Por crear:
- `lista.html` - Lista de ventas con filtros
- `form.html` - Formulario de crear venta (con formset de productos)
- `detalle.html` - Ver detalles de la venta
- `reportes.html` - Reportes y estadísticas

---

### 3. ÓRDENES DE SERVICIO (/templates/ordenes/)

#### 🔨 Por crear:
- `lista.html` - Lista de órdenes con filtros
- `form.html` - Formulario de crear/editar orden
- `detalle.html` - Ver detalles de la orden
- `repuestos.html` - Agregar repuestos
- `tablero.html` - Vista Kanban de órdenes

---

## 🎨 ESTRUCTURA BASE DE UNA PLANTILLA

Todas las plantillas deben seguir esta estructura:

```html
{% extends 'base_dashboard.html' %}
{% load static %}

{% block title %}Título - DIGIT SOFT{% endblock %}

{% block extra_css %}
<link rel="stylesheet" href="{% static 'css/clientes-enhanced.css' %}">
<style>
    /* Estilos adicionales específicos */
</style>
{% endblock %}

{% block content %}
<div class="container-fluid clientes-container animate-fade-in">
    <!-- Encabezado del Módulo -->
    <div class="module-header animate-slide-in">
        <div class="d-flex justify-content-between align-items-center">
            <div>
                <h2><i class="fas fa-icon"></i> Título del Módulo</h2>
                <p>Descripción breve</p>
            </div>
            <a href="{% url 'app:accion' %}" class="btn btn-light btn-enhanced">
                <i class="fas fa-plus"></i> Acción Principal
            </a>
        </div>
    </div>

    <!-- Contenido principal aquí -->
    
</div>
{% endblock %}

{% block extra_js %}
<script>
    // JavaScript específico
</script>
{% endblock %}
```

---

## 📝 EJEMPLO: form.html para Proveedores

```html
{% extends 'base_dashboard.html' %}
{% load static %}
{% load widget_tweaks %}

{% block title %}{{ titulo }} - DIGIT SOFT{% endblock %}

{% block extra_css %}
<link rel="stylesheet" href="{% static 'css/clientes-enhanced.css' %}">
{% endblock %}

{% block content %}
<div class="container-fluid clientes-container animate-fade-in">
    <div class="module-header animate-slide-in">
        <div>
            <h2><i class="fas fa-truck"></i> {{ titulo }}</h2>
            <p>Complete el formulario con los datos del proveedor</p>
        </div>
    </div>

    <div class="row animate-slide-in">
        <div class="col-lg-8 mx-auto">
            <div class="card card-enhanced">
                <div class="card-header card-header-enhanced">
                    <i class="fas fa-edit"></i> Información del Proveedor
                </div>
                <div class="card-body">
                    <form method="post" enctype="multipart/form-data">
                        {% csrf_token %}
                        
                        <div class="row">
                            <div class="col-md-8 mb-3">
                                <label class="form-label">{{ form.nombre_empresa.label }}</label>
                                {{ form.nombre_empresa }}
                                {% if form.nombre_empresa.errors %}
                                    <div class="text-danger">{{ form.nombre_empresa.errors }}</div>
                                {% endif %}
                            </div>
                            <div class="col-md-4 mb-3">
                                <label class="form-label">{{ form.nit.label }}</label>
                                {{ form.nit }}
                                {% if form.nit.errors %}
                                    <div class="text-danger">{{ form.nit.errors }}</div>
                                {% endif %}
                            </div>
                        </div>

                        <!-- Más campos aquí siguiendo el mismo patrón -->

                        <div class="mt-4">
                            <button type="submit" class="btn btn-primary-enhanced btn-enhanced">
                                <i class="fas fa-save"></i> {{ accion }}
                            </button>
                            <a href="{% url 'proveedores:lista' %}" class="btn btn-secondary-enhanced btn-enhanced">
                                <i class="fas fa-times"></i> Cancelar
                            </a>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

---

## 📝 EJEMPLO: detalle.html

```html
{% extends 'base_dashboard.html' %}
{% load static %}

{% block title %}Detalle Proveedor - DIGIT SOFT{% endblock %}

{% block content %}
<div class="container-fluid clientes-container animate-fade-in">
    <div class="module-header animate-slide-in">
        <div class="d-flex justify-content-between align-items-center">
            <div>
                <h2><i class="fas fa-truck"></i> Detalle del Proveedor</h2>
                <p>{{ proveedor.nombre_empresa }}</p>
            </div>
            <div>
                <a href="{% url 'proveedores:editar' proveedor.pk %}" class="btn btn-warning btn-enhanced">
                    <i class="fas fa-edit"></i> Editar
                </a>
                <a href="{% url 'proveedores:lista' %}" class="btn btn-secondary btn-enhanced">
                    <i class="fas fa-arrow-left"></i> Volver
                </a>
            </div>
        </div>
    </div>

    <div class="row animate-slide-in">
        <div class="col-lg-8">
            <div class="card card-enhanced">
                <div class="card-header card-header-enhanced">
                    <i class="fas fa-info-circle"></i> Información General
                </div>
                <div class="card-body">
                    <div class="row">
                        <div class="col-md-6 mb-3">
                            <strong>Empresa:</strong><br>
                            {{ proveedor.nombre_empresa }}
                        </div>
                        <div class="col-md-6 mb-3">
                            <strong>NIT:</strong><br>
                            {{ proveedor.nit }}
                        </div>
                        <!-- Más campos... -->
                    </div>
                </div>
            </div>
        </div>

        <div class="col-lg-4">
            <div class="card card-enhanced">
                <div class="card-header card-header-enhanced">
                    <i class="fas fa-star"></i> Calificación
                </div>
                <div class="card-body text-center">
                    <div class="calificacion-stars" style="font-size: 2rem;">
                        {% for i in "12345" %}
                            {% if forloop.counter <= proveedor.calificacion %}
                                <i class="fas fa-star"></i>
                            {% else %}
                                <i class="far fa-star"></i>
                            {% endif %}
                        {% endfor %}
                    </div>
                    <p class="mt-2">{{ proveedor.get_calificacion_display }}</p>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

---

## 🎨 CLASES CSS DISPONIBLES

### Contenedores:
- `.clientes-container` - Contenedor principal
- `.module-header` - Encabezado del módulo
- `.card-enhanced` - Cards mejorados
- `.card-header-enhanced` - Encabezados de cards

### Botones:
- `.btn-enhanced` - Botón con efectos
- `.btn-primary-enhanced` - Botón primario
- `.btn-secondary-enhanced` - Botón secundario
- `.btn-success-enhanced` - Botón éxito
- `.btn-danger-enhanced` - Botón peligro
- `.btn-warning-enhanced` - Botón advertencia
- `.btn-info-enhanced` - Botón información

### Animaciones:
- `.animate-fade-in` - Desvanecimiento
- `.animate-slide-in` - Deslizamiento

### Badges:
- `.badge-enhanced` - Badge mejorado
- `.badge-success-enhanced` - Verde
- `.badge-danger-enhanced` - Rojo
- `.badge-warning-enhanced` - Amarillo
- `.badge-info-enhanced` - Azul

---

## 🚀 PASOS PARA IMPLEMENTAR

1. **Crear directorios si no existen:**
   ```cmd
   mkdir templates\ventas
   mkdir templates\ordenes
   ```

2. **Copiar estructura base** desde `templates/clientes/` o `templates/proveedores/`

3. **Adaptar contenido** según el modelo:
   - Cambiar nombres de campos
   - Ajustar íconos
   - Modificar URLs

4. **Probar en navegador:**
   - Verificar formularios
   - Probar crear/editar/eliminar
   - Validar búsquedas y filtros

---

## 📚 REFERENCIAS

### Plantillas Existentes (para copiar estructura):
- `templates/clientes/` - ✅ Completo y funcional
- `templates/productos/` - ✅ Completo con imágenes
- `templates/tecnicos/` - ✅ Completo y funcional
- `templates/garantias/` - ✅ Completo
- `templates/proveedores/lista.html` - ✅ Ejemplo reciente

### Estilos:
- `static/css/clientes-enhanced.css` - Estilos principales
- Bootstrap 5 - Framework CSS
- Font Awesome 6 - Iconos

---

## ✅ CHECKLIST POR MÓDULO

### Proveedores:
- [x] models.py
- [x] views.py  
- [x] forms.py
- [x] urls.py
- [x] admin.py
- [x] lista.html
- [ ] form.html
- [ ] detalle.html
- [ ] eliminar.html

### Ventas:
- [x] models.py
- [x] views.py
- [x] forms.py
- [x] urls.py
- [x] admin.py
- [ ] lista.html
- [ ] form.html
- [ ] detalle.html
- [ ] reportes.html

### Órdenes:
- [x] models.py
- [x] views.py
- [x] forms.py
- [x] urls.py
- [x] admin.py
- [ ] lista.html
- [ ] form.html
- [ ] detalle.html
- [ ] repuestos.html
- [ ] tablero.html

---

## 🎯 PRIORIDAD

1. **ALTA:** `form.html` y `lista.html` - Necesarios para CRUD básico
2. **MEDIA:** `detalle.html` - Importante para visualización
3. **BAJA:** `eliminar.html`, `reportes.html`, `tablero.html` - Features adicionales

---

¡Con esta guía puedes completar todas las plantillas siguiendo el mismo estilo moderno y consistente del sistema!

