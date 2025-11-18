// ========== CARRITO DE COMPRAS ==========
class CarritoCompras {
    constructor() {
        this.items = this.cargarCarrito();
        this.actualizarBadge();
    }

    cargarCarrito() {
        try {
            const carritoJSON = localStorage.getItem('carrito');
            let items = carritoJSON ? JSON.parse(carritoJSON) : [];

            console.log('📦 Items cargados del localStorage:', items.length);

            // Eliminar duplicados basándose en el ID del producto
            const itemsUnicos = [];
            const idsVistos = new Set();

            for (const item of items) {
                // Validar que el item sea válido
                if (item && item.id && item.nombre && item.precio > 0) {
                    // Si no hemos visto este ID antes, agregarlo
                    if (!idsVistos.has(item.id)) {
                        idsVistos.add(item.id);
                        itemsUnicos.push(item);
                    } else {
                        console.warn('⚠️ Item duplicado eliminado:', item.nombre);
                    }
                }
            }

            // Si se encontraron duplicados, guardar la versión limpia
            if (itemsUnicos.length !== items.length) {
                console.log(`🧹 Limpiados ${items.length - itemsUnicos.length} items (duplicados o inválidos)`);
                localStorage.setItem('carrito', JSON.stringify(itemsUnicos));
            }

            console.log('✅ Items únicos en carrito:', itemsUnicos.length);
            return itemsUnicos;
        } catch (error) {
            console.error('❌ Error al cargar carrito:', error);
            // Si hay error al cargar, limpiar y empezar de nuevo
            localStorage.removeItem('carrito');
            return [];
        }
    }

    guardarCarrito() {
        try {
            localStorage.setItem('carrito', JSON.stringify(this.items));
            this.actualizarBadge();
        } catch (error) {
            if (error.name === 'QuotaExceededError' || error.code === 22) {
                console.warn('⚠️ LocalStorage lleno, limpiando datos antiguos...');
                // Limpiar otros datos del localStorage excepto el carrito
                const carritoActual = this.items;
                const keysToRemove = [];

                for (let i = 0; i < localStorage.length; i++) {
                    const key = localStorage.key(i);
                    if (key !== 'carrito') {
                        keysToRemove.push(key);
                    }
                }

                keysToRemove.forEach(key => localStorage.removeItem(key));

                // Intentar guardar nuevamente
                try {
                    localStorage.setItem('carrito', JSON.stringify(carritoActual));
                    this.actualizarBadge();
                    this.mostrarNotificacion('⚠️ Se limpió el almacenamiento para guardar el carrito', 'warning');
                } catch (e) {
                    console.error('❌ No se pudo guardar el carrito incluso después de limpiar:', e);
                    alert('El almacenamiento del navegador está lleno. Por favor, limpia los datos del sitio en la configuración del navegador.');
                }
            } else {
                console.error('❌ Error al guardar carrito:', error);
            }
        }
    }

    agregar(producto, cantidad = 1) {
        console.log('🛒 Método agregar llamado con:', producto);

        // Validación de datos del producto
        if (!producto) {
            console.error('❌ Producto es null o undefined');
            throw new Error('Producto inválido');
        }

        if (!producto.id) {
            console.error('❌ Producto sin ID:', producto);
            throw new Error('Producto sin identificador');
        }

        if (!producto.nombre) {
            console.error('❌ Producto sin nombre:', producto);
            throw new Error('Producto sin nombre');
        }

        if (!producto.precio || producto.precio <= 0) {
            console.error('❌ Producto sin precio válido:', producto);
            throw new Error('Producto sin precio válido');
        }

        if (!producto.stock || producto.stock <= 0) {
            console.error('❌ Producto sin stock:', producto);
            this.mostrarNotificacion('⚠️ Producto sin stock disponible', 'warning');
            return;
        }

        // Buscar si el producto ya existe en el carrito
        const itemExistente = this.items.find(item => item.id === producto.id);

        if (itemExistente) {
            // Si existe, incrementar cantidad
            const nuevaCantidad = itemExistente.cantidad + cantidad;
            if (nuevaCantidad > producto.stock) {
                itemExistente.cantidad = producto.stock;
                this.mostrarNotificacion('⚠️ Stock máximo alcanzado', 'warning');
            } else {
                itemExistente.cantidad = nuevaCantidad;
                this.mostrarNotificacion(`✅ Cantidad actualizada: ${producto.nombre} (${itemExistente.cantidad})`, 'success');
            }
        } else {
            // Si no existe, agregarlo como nuevo item
            const nuevoItem = {
                id: producto.id,
                nombre: producto.nombre,
                precio: producto.precio,
                stock: producto.stock,
                cantidad: Math.min(cantidad, producto.stock),
                categoria: producto.categoria || 'General',
                imagen: producto.imagen || null,
                codigo: producto.codigo || '',
                marca: producto.marca || ''
            };

            this.items.push(nuevoItem);
            this.mostrarNotificacion(`✅ ${producto.nombre} agregado al carrito`, 'success');
        }

        // Guardar y actualizar UI
        this.guardarCarrito();
        console.log('✅ Producto agregado correctamente. Items en carrito:', this.items.length);
        console.log('📦 Carrito actual:', this.items);

        // Mostrar el carrito
        this.mostrarCarrito();
    }

    eliminar(productoId) {
        this.items = this.items.filter(item => item.id !== productoId);
        this.guardarCarrito();
        this.mostrarCarrito();
    }

    actualizar(productoId, cantidad) {
        const item = this.items.find(item => item.id === productoId);
        if (item) {
            item.cantidad = Math.max(1, Math.min(cantidad, item.stock));
            this.guardarCarrito();
            this.mostrarCarrito();
        }
    }

    vaciar() {
        this.items = [];
        this.guardarCarrito();
        this.mostrarCarrito();
    }

    getTotal() {
        return this.items.reduce((total, item) => total + (item.precio * item.cantidad), 0);
    }

    getCantidadTotal() {
        return this.items.reduce((total, item) => total + item.cantidad, 0);
    }

    actualizarBadge() {
        const badge = document.getElementById('cartBadge');
        const cantidad = this.getCantidadTotal();

        if (badge) {
            badge.textContent = cantidad;
            badge.style.display = cantidad > 0 ? 'flex' : 'none';
        }
    }

    mostrarNotificacion(mensaje, tipo = 'success') {
        const existing = document.querySelector('.cart-notification');
        if (existing) existing.remove();

        const notification = document.createElement('div');
        notification.className = `cart-notification cart-notification-${tipo}`;
        notification.innerHTML = mensaje;
        notification.style.cssText = `
            position: fixed;
            top: 100px;
            right: 20px;
            background: ${tipo === 'success' ? '#10b981' : '#f59e0b'};
            color: white;
            padding: 15px 25px;
            border-radius: 10px;
            font-size: 0.95rem;
            font-weight: 600;
            z-index: 10001;
            animation: slideInRight 0.3s ease;
            box-shadow: 0 5px 20px rgba(0,0,0,0.2);
        `;
        document.body.appendChild(notification);

        setTimeout(() => {
            notification.style.animation = 'slideOutRight 0.3s ease';
            setTimeout(() => notification.remove(), 300);
        }, 3000);
    }

    mostrarCarrito() {
        const modal = document.getElementById('carritoModal');
        if (!modal) {
            this.crearModalCarrito();
            return;
        }

        const itemsContainer = document.getElementById('carritoItems');
        const totalElement = document.getElementById('carritoTotal');
        const emptyMessage = document.getElementById('carritoEmpty');

        if (this.items.length === 0) {
            itemsContainer.innerHTML = '';
            emptyMessage.style.display = 'block';
            totalElement.innerHTML = '<strong>Total: $0.00</strong>';
        } else {
            emptyMessage.style.display = 'none';
            itemsContainer.innerHTML = this.items.map(item => `
                <div class="carrito-item" data-id="${item.id}">
                    <div class="carrito-item-info">
                        <h4>${item.nombre}</h4>
                        <p class="carrito-item-precio">$${item.precio.toFixed(2)}</p>
                    </div>
                    <div class="carrito-item-controls">
                        <button class="btn-cantidad btn-disminuir" data-producto-id="${item.id}" data-cantidad="${item.cantidad - 1}">
                            <i class="fas fa-minus"></i>
                        </button>
                        <span class="cantidad">${item.cantidad}</span>
                        <button class="btn-cantidad btn-aumentar" data-producto-id="${item.id}" data-cantidad="${item.cantidad + 1}">
                            <i class="fas fa-plus"></i>
                        </button>
                        <button class="btn-eliminar" data-producto-id="${item.id}">
                            <i class="fas fa-trash"></i>
                        </button>
                    </div>
                    <div class="carrito-item-subtotal">
                        Subtotal: <strong>$${(item.precio * item.cantidad).toFixed(2)}</strong>
                    </div>
                </div>
            `).join('');

            totalElement.innerHTML = `<strong>Total: $${this.getTotal().toFixed(2)}</strong>`;

            // Agregar event listeners después de crear el HTML
            this.agregarEventListenersCarrito();
        }

        modal.style.display = 'block';
        document.body.style.overflow = 'hidden';
    }

    agregarEventListenersCarrito() {
        // Botones de disminuir cantidad
        document.querySelectorAll('.btn-disminuir').forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.stopPropagation();
                const productoId = parseInt(btn.dataset.productoId);
                const cantidad = parseInt(btn.dataset.cantidad);
                this.actualizar(productoId, cantidad);
            });
        });

        // Botones de aumentar cantidad
        document.querySelectorAll('.btn-aumentar').forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.stopPropagation();
                const productoId = parseInt(btn.dataset.productoId);
                const cantidad = parseInt(btn.dataset.cantidad);
                this.actualizar(productoId, cantidad);
            });
        });

        // Botones de eliminar
        document.querySelectorAll('.btn-eliminar').forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.stopPropagation();
                const productoId = parseInt(btn.dataset.productoId);
                this.eliminar(productoId);
            });
        });
    }
    cerrarCarrito() {
        const modal = document.getElementById('carritoModal');
        if (modal) {
            modal.style.display = 'none';
            document.body.style.overflow = 'auto';
        }
    }

    crearModalCarrito() {
        const modal = document.createElement('div');
        modal.id = 'carritoModal';
        modal.className = 'carrito-modal';

        modal.innerHTML = `
            <div class="carrito-modal-content">
                <div class="carrito-header">
                    <h2><i class="fas fa-shopping-cart"></i> Mi Carrito</h2>
                    <button class="close-carrito" id="btnCerrarCarrito">
                        <i class="fas fa-times"></i>
                    </button>
                </div>
                <div id="carritoEmpty" class="carrito-empty" style="display: none;">
                    <i class="fas fa-shopping-cart" style="font-size: 4rem; color: #ccc; margin-bottom: 1rem;"></i>
                    <p>Tu carrito está vacío</p>
                    <button id="btnSeguirComprando" class="btn btn-primary">
                        Seguir Comprando
                    </button>
                </div>
                <div class="carrito-items" id="carritoItems"></div>
                <div class="carrito-footer">
                    <div class="carrito-total" id="carritoTotal">
                        <strong>Total: $0.00</strong>
                    </div>
                    <div class="carrito-actions">
                        <button id="btnVaciarCarrito" class="btn btn-secondary">
                            <i class="fas fa-trash"></i> Vaciar Carrito
                        </button>
                        <button id="btnFinalizarCompra" class="btn btn-primary">
                            <i class="fas fa-check"></i> Finalizar Compra
                        </button>
                    </div>
                </div>
            </div>
        `;

        document.body.appendChild(modal);

        // Event listeners para botones del modal
        document.getElementById('btnCerrarCarrito').addEventListener('click', () => {
            this.cerrarCarrito();
        });

        document.getElementById('btnSeguirComprando').addEventListener('click', () => {
            this.cerrarCarrito();
        });

        document.getElementById('btnVaciarCarrito').addEventListener('click', () => {
            if (confirm('¿Estás seguro de que quieres vaciar el carrito?')) {
                this.vaciar();
            }
        });

        document.getElementById('btnFinalizarCompra').addEventListener('click', () => {
            this.finalizarCompra();
        });

        // Cerrar al hacer clic fuera
        modal.addEventListener('click', (e) => {
            if (e.target === modal) {
                this.cerrarCarrito();
            }
        });

        this.mostrarCarrito();
    }

    finalizarCompra() {
        if (this.items.length === 0) {
            this.mostrarNotificacion('⚠️ El carrito está vacío', 'warning');
            return;
        }

        // Redirigir al checkout
        window.location.href = '/checkout/checkout/';
    }

    generarMensajeWhatsApp() {
        let mensaje = '🛒 *Solicitud de Cotización*\n\n';
        mensaje += '*Productos:*\n';

        this.items.forEach((item, index) => {
            mensaje += `${index + 1}. ${item.nombre}\n`;
            mensaje += `   Cantidad: ${item.cantidad}\n`;
            mensaje += `   Precio Unit.: $${item.precio.toFixed(2)}\n`;
            mensaje += `   Subtotal: $${(item.precio * item.cantidad).toFixed(2)}\n\n`;
        });

        mensaje += `*Total: $${this.getTotal().toFixed(2)}*\n\n`;
        mensaje += '¿Podrían confirmar disponibilidad y tiempos de entrega?';

        return mensaje;
    }
}

// ========== CARGA DE PRODUCTOS ==========
class ProductosManager {
    constructor() {
        this.productos = [];
        this.filtroActual = 'all';
        this.cargarProductos();
    }

    async cargarProductos(categoria = 'all') {
        console.log('📦 Cargando productos, categoría:', categoria);

        try {
            const url = `/productos/api/publicos/?categoria=${categoria}`;
            console.log('🌐 URL de petición:', url);

            const response = await fetch(url);
            console.log('📡 Respuesta recibida:', response.status);

            const data = await response.json();
            console.log('📊 Datos recibidos:', data);

            if (data.success) {
                this.productos = data.productos;
                this.filtroActual = categoria;
                console.log('✅ Productos cargados:', this.productos.length);
                this.renderizarProductos();
            } else {
                console.error('❌ Error en la respuesta:', data);
                this.mostrarError();
            }
        } catch (error) {
            console.error('❌ Error en la petición:', error);
            this.mostrarError();
        }
    }

    renderizarProductos() {
        const grid = document.querySelector('.products-grid');
        if (!grid) return;

        if (this.productos.length === 0) {
            grid.innerHTML = `
                <div class="no-productos">
                    <i class="fas fa-box-open" style="font-size: 4rem; color: #ccc; margin-bottom: 1rem;"></i>
                    <p>No hay productos disponibles en esta categoría</p>
                </div>
            `;
            return;
        }

        grid.innerHTML = this.productos.map(producto => `
            <div class="product-card ${producto.destacado ? 'destacado' : ''}" data-filter="${producto.categoria.toLowerCase()}" data-producto-id="${producto.id}">
                ${producto.destacado ? '<div class="badge-destacado">⭐ Destacado</div>' : ''}
                
                <!-- Reacciones -->
                <div class="product-reactions">
                    <button class="reaction-btn reaction-like" data-producto-id="${producto.id}" data-tipo="like" title="Me gusta">
                        <i class="fas fa-thumbs-up"></i>
                        <span class="reaction-count" id="like-${producto.id}">0</span>
                    </button>
                    <button class="reaction-btn reaction-dislike" data-producto-id="${producto.id}" data-tipo="dislike" title="No me gusta">
                        <i class="fas fa-thumbs-down"></i>
                        <span class="reaction-count" id="dislike-${producto.id}">0</span>
                    </button>
                </div>
                
                <div class="product-image producto-ver-detalle" data-producto-id="${producto.id}">
                    ${producto.imagen ?
                        `<img src="${producto.imagen}" alt="${producto.nombre}">` :
                        `<div class="no-image"><i class="fas fa-image"></i></div>`
                    }
                </div>
                <div class="product-info">
                    <span class="product-category">${producto.categoria}</span>
                    <h3 class="product-name producto-ver-detalle" data-producto-id="${producto.id}">${producto.nombre}</h3>
                    <p class="product-specs">
                        ${producto.procesador ? `<span><i class="fas fa-microchip"></i> ${producto.procesador}</span>` : ''}
                        ${producto.memoria_ram ? `<span><i class="fas fa-memory"></i> ${producto.memoria_ram}</span>` : ''}
                        ${producto.memoria_rom ? `<span><i class="fas fa-hdd"></i> ${producto.memoria_rom}</span>` : ''}
                    </p>
                    <div class="product-footer">
                        <div class="product-price">
                            <span class="price">$${producto.precio.toFixed(2)}</span>
                            <span class="stock"><i class="fas fa-box"></i> ${producto.stock} disponibles</span>
                        </div>
                        <div class="product-actions">
                            <button class="btn-ver-detalle" data-producto-id="${producto.id}" title="Ver detalles">
                                <i class="fas fa-info-circle"></i>
                            </button>
                            <button class="btn-add-cart" data-producto-id="${producto.id}" title="Agregar al carrito">
                                <i class="fas fa-cart-plus"></i>
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        `).join('');

        // Cargar contadores de reacciones para cada producto
        this.productos.forEach(producto => {
            this.cargarReacciones(producto.id);
        });

        // Agregar event listeners a todos los botones
        this.agregarEventListenersProductos();
    }

    agregarEventListenersProductos() {
        // Botones de reacciones
        document.querySelectorAll('.reaction-like, .reaction-dislike').forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.stopPropagation();
                const productoId = parseInt(btn.dataset.productoId);
                const tipo = btn.dataset.tipo;
                reaccionarProducto(e, productoId, tipo);
            });
        });

        // Elementos clickeables para ver detalle
        document.querySelectorAll('.producto-ver-detalle, .btn-ver-detalle').forEach(element => {
            element.addEventListener('click', (e) => {
                e.stopPropagation();
                const productoId = parseInt(element.dataset.productoId);
                verDetalle(productoId);
            });
        });

        // Botones de agregar al carrito
        document.querySelectorAll('.btn-add-cart').forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.stopPropagation();
                const productoId = parseInt(btn.dataset.productoId);
                agregarAlCarrito(productoId);
            });
        });
    }

    mostrarError() {
        const grid = document.querySelector('.products-grid');
        if (grid) {
            grid.innerHTML = `
                <div class="error-productos">
                    <i class="fas fa-exclamation-triangle" style="font-size: 4rem; color: #ef4444; margin-bottom: 1rem;"></i>
                    <p>Error al cargar los productos</p>
                    <button onclick="productosManager.cargarProductos()" class="btn btn-primary">
                        <i class="fas fa-redo"></i> Reintentar
                    </button>
                </div>
            `;
        }
    }

    obtenerProductoPorId(id) {
        console.log('🔍 Buscando producto ID:', id);
        console.log('📦 Productos disponibles:', this.productos.length);
        const producto = this.productos.find(p => p.id === id);
        if (producto) {
            console.log('✅ Producto encontrado:', producto);
        } else {
            console.error('❌ Producto no encontrado con ID:', id);
            console.log('IDs disponibles:', this.productos.map(p => p.id));
        }
        return producto;
    }

    async cargarReacciones(productoId) {
        try {
            const response = await fetch(`/productos/api/reaccion/?producto_id=${productoId}`);
            const data = await response.json();

            if (data.success) {
                const likeElement = document.getElementById(`like-${productoId}`);
                const dislikeElement = document.getElementById(`dislike-${productoId}`);

                if (likeElement) likeElement.textContent = data.contadores.likes || 0;
                if (dislikeElement) dislikeElement.textContent = data.contadores.dislikes || 0;
            }
        } catch (error) {
            console.error('Error cargando reacciones:', error);
        }
    }
}

// ========== INICIALIZACIÓN ==========
let carrito;
let productosManager;

// Función para limpiar localStorage si está muy lleno
function limpiarLocalStorageAntiguos() {
    try {
        console.log('🧹 Verificando espacio en localStorage...');

        // Calcular tamaño aproximado del localStorage
        let totalSize = 0;
        for (let key in localStorage) {
            if (localStorage.hasOwnProperty(key)) {
                totalSize += localStorage[key].length + key.length;
            }
        }

        console.log(`📊 Tamaño actual del localStorage: ${(totalSize / 1024).toFixed(2)} KB`);

        // Si está cerca del límite (> 4MB), limpiar datos no esenciales
        if (totalSize > 4 * 1024 * 1024) {
            console.warn('⚠️ LocalStorage cerca del límite, limpiando...');

            // Guardar solo datos esenciales
            const carritoData = localStorage.getItem('carrito');

            // Limpiar todo
            localStorage.clear();

            // Restaurar datos esenciales
            if (carritoData) {
                localStorage.setItem('carrito', carritoData);
            }

            console.log('✅ LocalStorage limpiado exitosamente');
        }
    } catch (error) {
        console.error('Error al verificar localStorage:', error);
    }
}

document.addEventListener('DOMContentLoaded', function() {
    // Limpiar localStorage si es necesario
    limpiarLocalStorageAntiguos();

    // Inicializar carrito
    carrito = new CarritoCompras();

    // Inicializar gestor de productos
    productosManager = new ProductosManager();

    // Configurar filtros de categoría
    const filterButtons = document.querySelectorAll('.filter-btn');
    filterButtons.forEach(btn => {
        btn.addEventListener('click', function() {
            filterButtons.forEach(b => b.classList.remove('active'));
            this.classList.add('active');

            const filter = this.getAttribute('data-filter');
            productosManager.cargarProductos(filter);
        });
    });

    // Botón del carrito en el header
    const cartBtn = document.getElementById('cartBtn');
    if (cartBtn) {
        cartBtn.addEventListener('click', (e) => {
            e.preventDefault();
            carrito.mostrarCarrito();
        });
    }
});

// Función global para agregar al carrito
function agregarAlCarrito(productoId) {
    console.log('🛒 Intentando agregar producto ID:', productoId);

    if (!productosManager) {
        console.error('❌ ProductosManager no está inicializado');
        alert('Error: El sistema de productos no está listo. Por favor, recarga la página.');
        return;
    }

    if (!carrito) {
        console.error('❌ Carrito no está inicializado');
        alert('Error: El carrito no está listo. Por favor, recarga la página.');
        return;
    }

    const producto = productosManager.obtenerProductoPorId(productoId);

    if (!producto) {
        console.error('❌ Producto no encontrado:', productoId);
        alert('Error: Producto no encontrado.');
        return;
    }

    console.log('📦 Producto encontrado:', producto);

    try {
        carrito.agregar(producto);
        console.log('✅ Producto agregado exitosamente');
    } catch (error) {
        console.error('❌ Error al agregar producto:', error);

        // Si es error de cuota, sugerir limpieza
        if (error.name === 'QuotaExceededError' || error.message.includes('quota')) {
            alert('El almacenamiento del navegador está lleno.\n\nPara solucionarlo, ejecuta este comando en la consola:\nlimpiarLocalStorage()\n\nO limpia los datos del sitio manualmente.');
        } else {
            alert('Error al agregar el producto al carrito: ' + error.message);
        }
    }
}

// Función global para limpiar localStorage (accesible desde consola)
function limpiarLocalStorage() {
    if (confirm('¿Estás seguro de que quieres limpiar el almacenamiento del navegador?\n\nEsto vaciará el carrito y otros datos guardados.')) {
        localStorage.clear();
        console.log('✅ LocalStorage limpiado exitosamente');
        alert('Almacenamiento limpiado. Recargando página...');
        location.reload();
    }
}

// Función global para vaciar solo el carrito (accesible desde consola)
function vaciarCarrito() {
    if (carrito) {
        carrito.vaciar();
        console.log('✅ Carrito vaciado exitosamente');
        alert('Carrito vaciado correctamente.');
    } else {
        console.error('❌ Carrito no está inicializado');
    }
}

// Función global para ver detalles del producto (accesible desde consola)
function verCarrito() {
    if (carrito) {
        console.log('📦 Items en el carrito:', carrito.items);
        console.log('🔢 Cantidad total:', carrito.getCantidadTotal());
        console.log('💰 Total:', '$' + carrito.getTotal().toFixed(2));
        return carrito.items;
    } else {
        console.error('❌ Carrito no está inicializado');
        return null;
    }
}

// Función para ver detalles de un producto
function verDetalle(productoId) {
    window.location.href = `/productos/detalle/${productoId}/`;
}

// Función para reaccionar a un producto
async function reaccionarProducto(event, productoId, tipo) {
    event.stopPropagation();

    try {
        const response = await fetch('/productos/api/reaccion/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                producto_id: productoId,
                tipo: tipo
            })
        });

        const data = await response.json();

        if (data.success) {
            // Actualizar contadores
            const likeElement = document.getElementById(`like-${productoId}`);
            const dislikeElement = document.getElementById(`dislike-${productoId}`);

            if (likeElement) likeElement.textContent = data.contadores.likes;
            if (dislikeElement) dislikeElement.textContent = data.contadores.dislikes;

            // Animación visual
            const card = document.querySelector(`[data-producto-id="${productoId}"]`);
            if (card) {
                card.style.transform = 'scale(1.02)';
                setTimeout(() => {
                    card.style.transform = 'scale(1)';
                }, 200);
            }
        }
    } catch (error) {
        console.error('Error al reaccionar:', error);
    }
}

// Cerrar carrito con ESC
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && carrito) {
        carrito.cerrarCarrito();
    }
});

// Animaciones CSS necesarias
const style = document.createElement('style');
style.textContent = `
@keyframes slideInRight {
    from { transform: translateX(400px); opacity: 0; }
    to { transform: translateX(0); opacity: 1; }
}

@keyframes slideOutRight {
    from { transform: translateX(0); opacity: 1; }
    to { transform: translateX(400px); opacity: 0; }
}
`;
document.head.appendChild(style);

