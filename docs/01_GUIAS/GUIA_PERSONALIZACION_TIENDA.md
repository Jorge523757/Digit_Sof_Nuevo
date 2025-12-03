# 🎨 GUÍA DE PERSONALIZACIÓN - TIENDA E-COMMERCE

## 📝 CÓMO PERSONALIZAR TU TIENDA

---

## 1️⃣ CAMBIAR COLORES

### Archivo: `static/css/productos-exito.css`

**Colores principales (líneas 8-20)**:
```css
:root {
    /* Cambia estos valores según tu preferencia */
    --primary-color: #2c3e50;        /* Azul oscuro principal */
    --secondary-color: #3498db;      /* Azul claro */
    --accent-color: #e74c3c;         /* Rojo para alertas */
    --success-color: #27ae60;        /* Verde para éxito */
    --warning-color: #f39c12;        /* Naranja para alertas */
    
    --digit-blue: #3498db;           /* Azul de botones */
    --digit-dark-blue: #2c3e50;      /* Azul oscuro header */
    --digit-light-blue: #5dade2;     /* Azul claro hover */
}
```

**Ejemplo - Cambiar a verde corporativo**:
```css
:root {
    --primary-color: #27ae60;
    --secondary-color: #2ecc71;
    --digit-blue: #27ae60;
    --digit-dark-blue: #1e8449;
    --digit-light-blue: #58d68d;
}
```

---

## 2️⃣ MODIFICAR LOGO Y NOMBRE

### Archivo: `templates/ecommerce/productos_estilo_exito.html`

**Logo (línea 70)**:
```html
<a href="{% url 'core:landing' %}" class="logo">
    <i class="fas fa-laptop-code"></i>  <!-- Cambia el icono -->
    <strong>Digit</strong> Soft          <!-- Cambia el texto -->
</a>
```

**Iconos disponibles**: [Font Awesome Icons](https://fontawesome.com/icons)

Ejemplos:
```html
<i class="fas fa-store"></i>         <!-- Tienda -->
<i class="fas fa-shopping-bag"></i>  <!-- Bolsa -->
<i class="fas fa-gem"></i>           <!-- Gema -->
<i class="fas fa-rocket"></i>        <!-- Cohete -->
```

---

## 3️⃣ AGREGAR/QUITAR FILTROS

### Archivo: `templates/ecommerce/productos_estilo_exito.html`

**Agregar nuevo filtro de talla (después línea 157)**:
```html
<!-- Tallas -->
<div class="filter-section">
    <button class="filter-title" data-toggle="collapse" data-target="#sizeCollapse">
        Talla
        <i class="fas fa-chevron-down"></i>
    </button>
    <div class="filter-content collapse show" id="sizeCollapse">
        <label class="filter-option">
            <input type="checkbox" name="size" value="s">
            <span>S</span>
        </label>
        <label class="filter-option">
            <input type="checkbox" name="size" value="m">
            <span>M</span>
        </label>
        <label class="filter-option">
            <input type="checkbox" name="size" value="l">
            <span>L</span>
        </label>
        <label class="filter-option">
            <input type="checkbox" name="size" value="xl">
            <span>XL</span>
        </label>
    </div>
</div>
```

---

## 4️⃣ CAMBIAR NÚMERO DE COLUMNAS EN GRID

### Archivo: `static/css/productos-exito.css`

**Grid de productos (línea 396)**:
```css
.products-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));  /* 260px = ancho mínimo */
    gap: 20px;
}
```

**Opciones**:
```css
/* 3 columnas fijas */
grid-template-columns: repeat(3, 1fr);

/* 5 columnas adaptables */
grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));

/* 2 columnas en móvil, 4 en desktop */
@media (min-width: 768px) {
    grid-template-columns: repeat(4, 1fr);
}
```

---

## 5️⃣ PERSONALIZAR MENSAJES

### Archivo: `static/js/productos-exito.js`

**Mensajes del carrito (líneas 74, 136-140)**:
```javascript
// Cambiar mensaje de producto agregado
this.mostrarNotificacion(`✅ ${producto.nombre} agregado al carrito`, 'success');

// Cambiar a:
this.mostrarNotificacion(`🎉 ¡Genial! ${producto.nombre} está en tu carrito`, 'success');
```

**Mensaje de carrito vacío (línea 121)**:
```html
cartDrawerBody.innerHTML = `
    <div style="text-align: center; padding: 40px 20px; color: #6b7280;">
        <i class="fas fa-shopping-cart" style="font-size: 3rem; margin-bottom: 16px;"></i>
        <p>Tu carrito está vacío</p>
        <p>¡Agrega productos increíbles!</p>  <!-- Nuevo -->
    </div>
`;
```

---

## 6️⃣ MODIFICAR NAVEGACIÓN SECUNDARIA

### Archivo: `templates/ecommerce/productos_estilo_exito.html` (línea 82)

```html
<ul class="nav-items">
    <li><a href="{% url 'core:landing' %}">Inicio</a></li>
    <li><a href="#" class="active">Productos</a></li>
    <li><a href="#">Ofertas</a></li>
    <li><a href="#">Envío gratis</a></li>
    <!-- Agregar más links -->
    <li><a href="#">Contacto</a></li>
    <li><a href="#">Nosotros</a></li>
</ul>
```

---

## 7️⃣ CAMBIAR TAMAÑO DEL DRAWER

### Archivo: `static/css/productos-exito.css` (línea 773)

```css
.cart-drawer {
    position: fixed;
    top: 0;
    right: -450px;         /* Cambiar este valor */
    width: 420px;          /* Y este también */
    height: 100%;
    /* ...resto del código... */
}
```

**Ejemplos**:
```css
/* Drawer más angosto */
right: -350px;
width: 320px;

/* Drawer más ancho */
right: -550px;
width: 520px;

/* Drawer de mitad de pantalla */
right: -50%;
width: 50%;
```

---

## 8️⃣ AGREGAR IMÁGENES DE PLACEHOLDER

### Archivo: `templates/ecommerce/productos_estilo_exito.html` (línea 304)

```html
{% if producto.imagen %}
<img src="{{ producto.imagen.url }}" alt="{{ producto.nombre_producto }}">
{% else %}
<div class="no-image">
    <i class="fas fa-laptop-code"></i>
    <!-- Cambiar a imagen placeholder -->
    <!-- <img src="{% static 'images/no-product.png' %}" alt="Sin imagen"> -->
</div>
{% endif %}
```

---

## 9️⃣ MODIFICAR ANIMACIONES

### Archivo: `static/css/productos-exito.css`

**Velocidad de transiciones (buscar `transition`)**:
```css
/* Cambiar de 0.3s a 0.5s para animaciones más lentas */
.product-card-exito {
    transition: all 0.3s;  /* Cambiar a 0.5s */
}

/* O más rápidas */
.btn-add-exito {
    transition: all 0.2s;  /* Cambiar a 0.1s */
}
```

**Animación del drawer (línea 773)**:
```css
.cart-drawer {
    transition: right 0.3s ease;  /* Cambiar velocidad o efecto */
}

/* Opciones de efecto: */
/* ease, ease-in, ease-out, ease-in-out, linear */
```

---

## 🔟 AGREGAR MÁS OPCIONES DE ORDENAMIENTO

### Archivo: `templates/ecommerce/productos_estilo_exito.html` (línea 253)

```html
<select class="form-select form-select-sm" id="sortSelect">
    <option value="relevance">Relevancia</option>
    <option value="price_asc">Precio: Menor a Mayor</option>
    <option value="price_desc">Precio: Mayor a Menor</option>
    <option value="newest">Más Nuevos</option>
    <!-- Agregar nuevas opciones -->
    <option value="popular">Más Populares</option>
    <option value="rating">Mejor Valorados</option>
    <option value="name">Nombre A-Z</option>
</select>
```

### Actualizar backend: `ecommerce_views.py` (línea 369)

```python
orden_map = {
    'relevance': '-destacado',
    'price_asc': 'precio_venta',
    'price_desc': '-precio_venta',
    'newest': '-fecha_registro',
    # Agregar nuevos
    'popular': '-veces_vendido',
    'rating': '-calificacion',
    'name': 'nombre_producto',
}
```

---

## 1️⃣1️⃣ PERSONALIZAR BADGES

### Archivo: `templates/ecommerce/productos_estilo_exito.html` (línea 267)

```html
<!-- Badge de destacado -->
{% if producto.destacado %}
<div class="product-badge badge-featured">
    <i class="fas fa-star"></i> Destacado  <!-- Cambiar texto e icono -->
</div>
{% endif %}

<!-- Badge de descuento -->
{% if producto.precio_mayorista %}
<div class="product-badge badge-discount">
    -{{ producto.descuento|default:"20" }}%  <!-- Cambiar formato -->
</div>
{% endif %}

<!-- Agregar más badges -->
{% if producto.nuevo %}
<div class="product-badge badge-new">
    <i class="fas fa-sparkles"></i> Nuevo
</div>
{% endif %}
```

### Estilos para nuevos badges: `static/css/productos-exito.css`

```css
.badge-new {
    background: var(--success-color);
    color: white;
    top: 44px;  /* Posicionar debajo del otro badge */
}

.badge-hot {
    background: var(--digit-red);
    color: white;
}
```

---

## 1️⃣2️⃣ CAMBIAR FORMATO DE PRECIOS

### Archivo: `static/js/productos-exito.js` (línea 110, 137)

```javascript
// Formato actual: $1.329.900
precio.toLocaleString('es-CO')

// Cambiar a:
precio.toLocaleString('es-CO', {
    style: 'currency',
    currency: 'COP',
    minimumFractionDigits: 0
})
// Resultado: COP 1.329.900

// O sin decimales simples:
'$' + precio.toFixed(0).replace(/\B(?=(\d{3})+(?!\d))/g, '.')
// Resultado: $1.329.900
```

---

## 📱 RESPONSIVE PERSONALIZADO

### Archivo: `static/css/productos-exito.css` (línea 918)

```css
/* Ajustar breakpoints */
@media (max-width: 992px) {
    /* Tablets */
}

@media (max-width: 768px) {
    /* Móviles */
}

/* Agregar breakpoint personalizado */
@media (max-width: 1200px) {
    .products-grid {
        grid-template-columns: repeat(3, 1fr);
    }
}
```

---

## 🎯 TIPS DE OPTIMIZACIÓN

1. **Imágenes**: Comprime las imágenes de productos (máx 500KB)
2. **Lazy Loading**: Agrega `loading="lazy"` a las imágenes
3. **Caché**: Habilita caché de archivos estáticos
4. **CDN**: Usa CDN para Bootstrap y Font Awesome
5. **Minificar**: Minifica CSS y JS en producción

---

## 🆘 SOLUCIÓN DE PROBLEMAS

### El CSS no se aplica
```bash
python manage.py collectstatic --clear
```

### Los filtros no funcionan
1. Verifica que `productos-exito.js` esté cargando
2. Abre la consola del navegador (F12)
3. Busca errores en rojo

### El carrito no guarda productos
1. Verifica que localStorage esté habilitado
2. Revisa que el usuario esté autenticado
3. Comprueba la clave `carrito_v1` en DevTools → Application → Local Storage

---

## 📚 RECURSOS ADICIONALES

- **Bootstrap Docs**: https://getbootstrap.com/docs/5.3/
- **Font Awesome**: https://fontawesome.com/search
- **CSS Grid Guide**: https://css-tricks.com/snippets/css/complete-guide-grid/
- **Django Templates**: https://docs.djangoproject.com/en/4.2/topics/templates/

---

**¡Personaliza tu tienda y hazla única! 🎨✨**

