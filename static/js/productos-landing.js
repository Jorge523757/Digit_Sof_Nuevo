// ========== CARRITO DE COMPRAS ==========
class CarritoCompras {
    constructor() {
        this.items = [];

        // Cargar y limpiar carrito
        this.cargarYLimpiarCarrito();

        // Crear modales de notificación
        this.crearModalesNotificacion();

        // Actualizar badge
        this.actualizarBadge();

        console.log('✅ CarritoCompras inicializado con', this.items.length, 'items');
    }

    cargarYLimpiarCarrito() {
        try {
            const carritoJSON = localStorage.getItem('carrito');

            if (!carritoJSON) {
                this.items = [];
                console.log('📦 Carrito vacío');
                return;
            }

            let items = JSON.parse(carritoJSON);
            console.log('📦 Items en localStorage:', items.length);

            // Limpiar duplicados usando Map
            const productosUnicos = new Map();

            items.forEach(item => {
                if (!item || !item.id) {
                    console.warn('⚠️ Item inválido ignorado:', item);
                    return;
                }

                const id = parseInt(item.id);

                if (isNaN(id)) {
                    console.warn('⚠️ ID inválido ignorado:', item.id);
                    return;
                }

                if (!productosUnicos.has(id)) {
                    // Primer item con este ID
                    productosUnicos.set(id, {
                        id: id,
                        nombre: (item.nombre || item.nombre_producto || 'Producto').trim(),
                        precio: parseFloat(item.precio || item.precio_venta || 0),
                        cantidad: parseInt(item.cantidad || 1),
                        stock: parseInt(item.stock || item.stock_actual || 0),
                        categoria: item.categoria || 'General',
                        imagen: item.imagen || null,
                        codigo: item.codigo || item.codigo_sku || '',
                        marca: item.marca || ''
                    });
                } else {
                    // Ya existe - sumar cantidad
                    const existente = productosUnicos.get(id);
                    existente.cantidad += parseInt(item.cantidad || 1);
                    console.warn('⚠️ Duplicado consolidado:', existente.nombre);
                }
            });

            this.items = Array.from(productosUnicos.values());

            if (items.length !== this.items.length) {
                console.log(`🧹 Duplicados eliminados: ${items.length} → ${this.items.length}`);
                this.guardarCarrito();
            }

            console.log('✅ Carrito cargado con', this.items.length, 'item(s) único(s)');

        } catch (error) {
            console.error('❌ Error al cargar carrito:', error);
            this.items = [];
            localStorage.removeItem('carrito');
        }
    }

    guardarCarrito() {
        try {
            // Guardar en formato antiguo (para compatibilidad)
            localStorage.setItem('carrito', JSON.stringify(this.items));

            // Guardar TAMBIÉN en carrito_v1 con estructura para renderizado
            const carritoV1 = {};
            this.items.forEach(item => {
                carritoV1[item.id] = {
                    id: item.id,
                    name: item.nombre,
                    nombre: item.nombre,
                    price: item.precio,
                    precio: item.precio,
                    qty: item.cantidad,
                    cantidad: item.cantidad,
                    image: item.imagen || '',
                    imagen: item.imagen || '',
                    stock: item.stock,
                    categoria: item.categoria,
                    codigo: item.codigo,
                    marca: item.marca
                };
            });
            localStorage.setItem('carrito_v1', JSON.stringify(carritoV1));
            console.log('💾 Carrito guardado en localStorage (carrito y carrito_v1)');

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
        console.log('🛒 [CarritoCompras.agregar] Método llamado');
        console.log('  📦 Producto:', producto.nombre, '(ID:', producto.id, ')');
        console.log('  🔢 Cantidad a agregar:', cantidad);
        console.log('  📊 Estado actual del carrito:', this.items.length, 'items');

        // PASO 1: Validaciones básicas
        if (!producto || !producto.id || !producto.nombre) {
            console.error('❌ Producto inválido:', producto);
            this.mostrarNotificacion('❌ Error: Producto inválido', 'error');
            return;
        }

        if (!producto.precio || parseFloat(producto.precio) <= 0) {
            console.error('❌ Precio inválido:', producto.precio);
            this.mostrarNotificacion('❌ Error: Precio inválido', 'error');
            return;
        }

        if (!producto.stock || parseInt(producto.stock) <= 0) {
            console.error('❌ Sin stock:', producto.nombre);
            this.mostrarNotificacion('⚠️ Producto sin stock disponible', 'warning');
            return;
        }

        // PASO 2: Normalizar y validar ID
        let productoId = producto.id;

        // Validar que el ID existe y no está vacío
        if (!productoId || productoId === '' || productoId === 'undefined' || productoId === 'null') {
            console.error('❌ ID inválido:', producto.id);
            this.mostrarNotificacion('❌ Error: ID de producto inválido', 'error');
            return;
        }

        // Normalizar: Si es un número puro string (ej: "123"), convertir a número
        // Si es un ID con formato especial (ej: "prod-123-abc"), mantener como string
        if (typeof productoId === 'string' && /^\d+$/.test(productoId)) {
            productoId = parseInt(productoId);
        }

        console.log('  🔑 ID normalizado:', productoId, '(tipo:', typeof productoId, ')');

        // PASO 3: FORZAR limpieza de duplicados ANTES de agregar
        console.log('  🧹 Limpiando duplicados antes de agregar...');
        const itemsAntes = this.items.length;
        this.limpiarDuplicadosInmediato();
        const itemsDespues = this.items.length;
        if (itemsAntes !== itemsDespues) {
            console.warn(`  ⚠️ Se eliminaron ${itemsAntes - itemsDespues} duplicados`);
        }

        // PASO 4: Buscar si ya existe (comparación flexible para strings y números)
        const itemExistente = this.items.find(item => {
            // Comparar de forma flexible: convertir ambos a string para comparación
            return String(item.id) === String(productoId);
        });

        if (itemExistente) {
            // PRODUCTO YA EXISTE - Solo incrementar cantidad
            console.log('  ℹ️ Producto YA EXISTE en el carrito');
            const cantidadActual = parseInt(itemExistente.cantidad);
            const nuevaCantidad = cantidadActual + parseInt(cantidad);
            const stockDisponible = parseInt(producto.stock);

            console.log('    📊 Cantidad actual:', cantidadActual);
            console.log('    📊 Nueva cantidad:', nuevaCantidad);
            console.log('    📦 Stock disponible:', stockDisponible);

            if (nuevaCantidad > stockDisponible) {
                itemExistente.cantidad = stockDisponible;
                this.mostrarNotificacion(`⚠️ Stock máximo alcanzado: ${producto.nombre} (${stockDisponible} unidades)`, 'warning');
                console.log(`⚠️ Stock máximo: ${producto.nombre} limitado a ${stockDisponible}`);
            } else {
                itemExistente.cantidad = nuevaCantidad;
                this.mostrarNotificacion(`✅ Cantidad actualizada: ${producto.nombre} (x${nuevaCantidad})`, 'success');
                console.log(`✅ Incrementado: ${producto.nombre} de ${cantidadActual} a ${nuevaCantidad}`);
            }

            console.log('  ✅ NO se agregó item duplicado, solo se actualizó cantidad');
        } else {
            // PRODUCTO NUEVO - Agregarlo
            console.log('  ℹ️ Producto NUEVO, agregando al carrito...');
            const nuevoItem = {
                id: productoId,
                nombre: producto.nombre.trim(),
                precio: parseFloat(producto.precio),
                stock: parseInt(producto.stock),
                cantidad: Math.min(parseInt(cantidad), parseInt(producto.stock)),
                categoria: producto.categoria || 'General',
                imagen: producto.imagen || null,
                codigo: producto.codigo || producto.codigo_sku || '',
                marca: producto.marca || ''
            };

            this.items.push(nuevoItem);
            this.mostrarNotificacion(`✅ ${producto.nombre} agregado al carrito`, 'success');
            console.log('✅ Producto NUEVO agregado:', nuevoItem);
        }

        // PASO 5: VERIFICAR que no haya duplicados después de agregar
        const idsUnicos = new Set(this.items.map(i => parseInt(i.id)));
        console.log('  🔍 Verificación final: IDs únicos =', idsUnicos.size, ', Items totales =', this.items.length);

        if (idsUnicos.size !== this.items.length) {
            console.error('⚠️ ¡DUPLICADOS DETECTADOS DESPUÉS DE AGREGAR! Limpiando...');
            console.error('  IDs únicos:', Array.from(idsUnicos));
            console.error('  Items:', this.items.map(i => ({ id: i.id, nombre: i.nombre })));
            this.limpiarDuplicadosInmediato();
        }

        // PASO 6: Guardar y actualizar UI
        this.guardarCarrito();
        console.log(`✅ [CarritoCompras.agregar] Completado. Carrito tiene ${this.items.length} producto(s) único(s)`);
        console.log('📦 Items finales:', this.items.map(i => `${i.nombre} (ID:${i.id}, x${i.cantidad})`));

        // PASO 7: Mostrar el carrito
        this.mostrarCarrito();
    }

    eliminar(productoId) {
        console.log('🗑️ Eliminando producto:', productoId);
        console.log('📦 Items antes:', this.items.length);

        // Convertir a string para comparación
        const idString = String(productoId);
        this.items = this.items.filter(item => String(item.id) !== idString);

        console.log('📦 Items después:', this.items.length);
        this.guardarCarrito();
        this.mostrarNotificacion('🗑️ Producto eliminado del carrito', 'success');
        this.mostrarCarrito();
    }

    actualizar(productoId, cantidad) {
        console.log('🔢 Actualizando cantidad:', { productoId, cantidad });

        // Convertir a string para comparación
        const idString = String(productoId);
        const item = this.items.find(item => String(item.id) === idString);

        if (item) {
            const nuevaCantidad = Math.max(1, Math.min(cantidad, item.stock));
            console.log('✅ Nueva cantidad:', nuevaCantidad);

            item.cantidad = nuevaCantidad;
            this.guardarCarrito();
            this.mostrarCarrito();
        } else {
            console.error('❌ Item no encontrado:', productoId);
        }
    }

    vaciar() {
        console.log('🧹 Vaciando carrito...');
        this.items = [];
        this.guardarCarrito();
        this.mostrarNotificacion('🧹 Carrito vaciado correctamente', 'success');
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
        // Remover notificaciones anteriores
        const existing = document.querySelectorAll('.cart-notification');
        existing.forEach(notif => notif.remove());

        const notification = document.createElement('div');
        notification.className = `cart-notification cart-notification-${tipo}`;

        // Determinar color e icono según tipo
        let bgColor, icon;
        if (tipo === 'success') {
            bgColor = '#10b981';
            icon = '<i class="fas fa-check-circle" style="font-size: 1.5rem;"></i>';
        } else if (tipo === 'warning') {
            bgColor = '#ffc107';
            icon = '<i class="fas fa-exclamation-triangle" style="font-size: 1.5rem;"></i>';
        } else {
            bgColor = '#ef4444';
            icon = '<i class="fas fa-exclamation-circle" style="font-size: 1.5rem;"></i>';
        }

        notification.innerHTML = `
            <div style="display: flex; align-items: center; gap: 12px;">
                ${icon}
                <div style="flex: 1;">${mensaje}</div>
            </div>
        `;

        notification.style.cssText = `
            position: fixed;
            top: 80px;
            left: 50%;
            transform: translateX(-50%);
            background: white;
            color: #333;
            padding: 16px 24px;
            border-radius: 12px;
            font-size: 0.95rem;
            font-weight: 600;
            z-index: 10001;
            min-width: 350px;
            max-width: 550px;
            box-shadow: 0 8px 30px rgba(0,0,0,0.25);
            border-left: 5px solid ${bgColor};
            animation: slideDown 0.4s ease-out;
        `;

        // Agregar animación CSS
        if (!document.getElementById('cart-notification-styles')) {
            const style = document.createElement('style');
            style.id = 'cart-notification-styles';
            style.textContent = `
                @keyframes slideDown {
                    from {
                        transform: translateX(-50%) translateY(-100px);
                        opacity: 0;
                    }
                    to {
                        transform: translateX(-50%) translateY(0);
                        opacity: 1;
                    }
                }
                @keyframes slideUp {
                    from {
                        transform: translateX(-50%) translateY(0);
                        opacity: 1;
                    }
                    to {
                        transform: translateX(-50%) translateY(-100px);
                        opacity: 0;
                    }
                }
                .cart-notification i {
                    color: ${bgColor};
                }
            `;
            document.head.appendChild(style);
        }

        document.body.appendChild(notification);

        setTimeout(() => {
            notification.style.animation = 'slideUp 0.4s ease-out forwards';
            setTimeout(() => notification.remove(), 400);
        }, 4000);
    }

    mostrarCarrito() {
        // FORZAR limpieza antes de mostrar
        this.limpiarDuplicadosInmediato();

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

            // Crear items usando los datos limpios
            itemsContainer.innerHTML = this.items.map(item => `
                <div class="carrito-item" data-id="${item.id}">
                    <div class="carrito-item-info">
                        <h4>${item.nombre}</h4>
                        <p class="carrito-item-precio">$${parseFloat(item.precio).toFixed(2)}</p>
                        <p class="carrito-item-subtotal">Subtotal: $${(parseFloat(item.precio) * parseInt(item.cantidad)).toFixed(2)}</p>
                    </div>
                    <div class="carrito-item-controls">
                        <button class="btn-cantidad btn-disminuir" data-producto-id="${item.id}">
                            <i class="fas fa-minus"></i>
                        </button>
                        <span class="cantidad">${item.cantidad}</span>
                        <button class="btn-cantidad btn-aumentar" data-producto-id="${item.id}">
                            <i class="fas fa-plus"></i>
                        </button>
                        <button class="btn-eliminar" data-producto-id="${item.id}">
                            <i class="fas fa-trash"></i>
                        </button>
                    </div>
                </div>
            `).join('');

            // Calcular total correctamente
            const total = this.items.reduce((sum, item) => {
                return sum + (parseFloat(item.precio) * parseInt(item.cantidad));
            }, 0);

            totalElement.innerHTML = `<strong>Total: $${total.toFixed(2)}</strong>`;

            console.log('📊 Carrito mostrado:', {
                items: this.items.length,
                total: total.toFixed(2),
                productos: this.items.map(i => `${i.nombre} (x${i.cantidad})`)
            });

            // Agregar event listeners después de crear el HTML
            this.agregarEventListenersCarrito();
        }

        modal.style.display = 'block';
    }

    agregarEventListenersCarrito() {
        console.log('🔧 Configurando event listeners del carrito...');

        // Botones de disminuir cantidad
        const btnsDisminuir = document.querySelectorAll('.btn-disminuir');
        console.log('Botones disminuir encontrados:', btnsDisminuir.length);

        btnsDisminuir.forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();

                const productoId = btn.dataset.productoId;
                const cantidadActual = parseInt(btn.parentElement.querySelector('.cantidad').textContent);
                const nuevaCantidad = Math.max(1, cantidadActual - 1);
                
                console.log('Disminuir:', productoId, 'de', cantidadActual, 'a', nuevaCantidad);
                this.actualizar(productoId, nuevaCantidad);
            });
        });

        // Botones de aumentar cantidad
        const btnsAumentar = document.querySelectorAll('.btn-aumentar');
        console.log('Botones aumentar encontrados:', btnsAumentar.length);

        btnsAumentar.forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();

                const productoId = btn.dataset.productoId;
                const cantidadActual = parseInt(btn.parentElement.querySelector('.cantidad').textContent);
                const nuevaCantidad = cantidadActual + 1;
                
                console.log('Aumentar:', productoId, 'de', cantidadActual, 'a', nuevaCantidad);
                this.actualizar(productoId, nuevaCantidad);
            });
        });

        // Botones de eliminar
        const btnsEliminar = document.querySelectorAll('.btn-eliminar');
        console.log('Botones eliminar encontrados:', btnsEliminar.length);

        btnsEliminar.forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();

                const productoId = btn.dataset.productoId;
                
                if (confirm('¿Estás seguro de eliminar este producto del carrito?')) {
                    console.log('Eliminar:', productoId);
                    this.eliminar(productoId);
                }
            });
        });

        console.log('✅ Event listeners configurados');
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
            this.showConfirmModal(
                '¿Vaciar todo el carrito?',
                'Se eliminarán todos los productos de tu carrito. Esta acción no se puede deshacer.',
                'warning',
                'Vaciar Carrito',
                () => {
                    this.vaciar();
                    this.showToast('¡Carrito vaciado!', 'Todos los productos han sido eliminados.', 'success');
                }
            );
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

    limpiarDuplicadosInmediato() {
        const idsUnicos = new Set();
        const itemsLimpios = [];

        this.items.forEach(item => {
            const id = parseInt(item.id);
            if (!idsUnicos.has(id)) {
                idsUnicos.add(id);
                itemsLimpios.push({
                    ...item,
                    id: id,
                    cantidad: parseInt(item.cantidad),
                    precio: parseFloat(item.precio),
                    stock: parseInt(item.stock)
                });
            } else {
                console.warn('⚠️ Duplicado ignorado:', item.nombre);
            }
        });

        if (this.items.length !== itemsLimpios.length) {
            console.log(`🧹 Duplicados eliminados: ${this.items.length} → ${itemsLimpios.length}`);
            this.items = itemsLimpios;
            this.guardarCarrito();
        }
    }

    crearModalesNotificacion() {
        // Crear contenedor para modales si no existe
        if (!document.getElementById('modal-container')) {
            const container = document.createElement('div');
            container.id = 'modal-container';
            document.body.appendChild(container);
        }

        // Crear estilos para los modales
        if (!document.getElementById('modal-notification-styles')) {
            const style = document.createElement('style');
            style.id = 'modal-notification-styles';
            style.textContent = `
                .modal-overlay {
                    position: fixed;
                    top: 0;
                    left: 0;
                    right: 0;
                    bottom: 0;
                    background: rgba(0, 0, 0, 0.5);
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    z-index: 10000;
                    animation: fadeIn 0.3s ease;
                }
                
                .modal-content-custom {
                    background: white;
                    border-radius: 12px;
                    padding: 2rem;
                    max-width: 400px;
                    width: 90%;
                    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
                    animation: scaleIn 0.3s ease;
                }
                
                .modal-header-custom {
                    display: flex;
                    align-items: center;
                    gap: 1rem;
                    margin-bottom: 1rem;
                }
                
                .modal-icon {
                    font-size: 2.5rem;
                }
                
                .modal-icon.success { color: #10b981; }
                .modal-icon.warning { color: #ffc107; }
                .modal-icon.error { color: #ef4444; }
                .modal-icon.info { color: #3b82f6; }
                
                .modal-title-custom {
                    font-size: 1.5rem;
                    font-weight: 600;
                    color: #333;
                }
                
                .modal-body-custom {
                    color: #666;
                    margin-bottom: 1.5rem;
                    line-height: 1.6;
                }
                
                .modal-actions {
                    display: flex;
                    gap: 0.75rem;
                    justify-content: flex-end;
                }
                
                .modal-btn {
                    padding: 0.5rem 1.5rem;
                    border: none;
                    border-radius: 6px;
                    font-weight: 600;
                    cursor: pointer;
                    transition: all 0.2s;
                }
                
                .modal-btn-primary {
                    background: #667eea;
                    color: white;
                }
                
                .modal-btn-primary:hover {
                    background: #5568d3;
                }
                
                .modal-btn-secondary {
                    background: #e5e7eb;
                    color: #666;
                }
                
                .modal-btn-secondary:hover {
                    background: #d1d5db;
                }
                
                .toast-notification {
                    position: fixed;
                    top: 20px;
                    right: 20px;
                    background: white;
                    border-radius: 8px;
                    padding: 1rem 1.5rem;
                    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
                    z-index: 10001;
                    min-width: 300px;
                    animation: slideInRight 0.3s ease;
                }
                
                .toast-header-custom {
                    display: flex;
                    align-items: center;
                    gap: 0.75rem;
                    margin-bottom: 0.5rem;
                }
                
                .toast-icon {
                    font-size: 1.5rem;
                }
                
                .toast-title {
                    font-weight: 600;
                    color: #333;
                }
                
                .toast-body {
                    color: #666;
                    font-size: 0.9rem;
                }
                
                @keyframes fadeIn {
                    from { opacity: 0; }
                    to { opacity: 1; }
                }
                
                @keyframes scaleIn {
                    from { transform: scale(0.9); opacity: 0; }
                    to { transform: scale(1); opacity: 1; }
                }
            `;
            document.head.appendChild(style);
        }

        console.log('✅ Modales de notificación creados');
    }

    showConfirmModal(titulo, mensaje, tipo = 'info', textoConfirmar = 'Confirmar', callback = null) {
        const modal = document.createElement('div');
        modal.className = 'modal-overlay';

        const iconos = {
            success: 'fa-check-circle',
            warning: 'fa-exclamation-triangle',
            error: 'fa-times-circle',
            info: 'fa-info-circle'
        };

        modal.innerHTML = `
            <div class="modal-content-custom">
                <div class="modal-header-custom">
                    <i class="fas ${iconos[tipo]} modal-icon ${tipo}"></i>
                    <h3 class="modal-title-custom">${titulo}</h3>
                </div>
                <div class="modal-body-custom">
                    ${mensaje}
                </div>
                <div class="modal-actions">
                    <button class="modal-btn modal-btn-secondary" id="btn-cancel">Cancelar</button>
                    <button class="modal-btn modal-btn-primary" id="btn-confirm">${textoConfirmar}</button>
                </div>
            </div>
        `;

        document.body.appendChild(modal);

        const btnCancel = modal.querySelector('#btn-cancel');
        const btnConfirm = modal.querySelector('#btn-confirm');

        btnCancel.addEventListener('click', () => {
            modal.remove();
        });

        btnConfirm.addEventListener('click', () => {
            if (callback) callback();
            modal.remove();
        });

        modal.addEventListener('click', (e) => {
            if (e.target === modal) {
                modal.remove();
            }
        });
    }

    showToast(titulo, mensaje, tipo = 'success') {
        const toast = document.createElement('div');
        toast.className = 'toast-notification';

        const iconos = {
            success: 'fa-check-circle',
            warning: 'fa-exclamation-triangle',
            error: 'fa-times-circle',
            info: 'fa-info-circle'
        };

        toast.innerHTML = `
            <div class="toast-header-custom">
                <i class="fas ${iconos[tipo]} toast-icon ${tipo}"></i>
                <span class="toast-title">${titulo}</span>
            </div>
            <div class="toast-body">${mensaje}</div>
        `;

        document.body.appendChild(toast);

        setTimeout(() => {
            toast.style.animation = 'slideOutRight 0.3s ease forwards';
            setTimeout(() => toast.remove(), 300);
        }, 3000);
    }

    // Método para generar mensaje de WhatsApp (disponible para uso futuro)
    // generarMensajeWhatsApp() {
    //     let mensaje = '🛒 *Solicitud de Cotización*\n\n';
    //     mensaje += '*Productos:*\n';
    //
    //     this.items.forEach((item, index) => {
    //         mensaje += `${index + 1}. ${item.nombre}\n`;
    //         mensaje += `   Cantidad: ${item.cantidad}\n`;
    //         mensaje += `   Precio Unit.: $${item.precio.toFixed(2)}\n`;
    //         mensaje += `   Subtotal: $${(item.precio * item.cantidad).toFixed(2)}\n\n`;
    //     });
    //
    //     mensaje += `*Total: $${this.getTotal().toFixed(2)}*\n\n`;
    //     mensaje += '¿Podrían confirmar disponibilidad y tiempos de entrega?';
    //
    //     return mensaje;
    // }
}

// ========== CARGA DE PRODUCTOS ==========
class ProductosManager {
    constructor() {
        this.productos = [];
        this.filtroActual = 'all';
        this.paginaActual = 1;
        this.productosPorPagina = 12; // Mostrar 12 productos por página
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
                this.paginaActual = 1; // Resetear a página 1 al cambiar filtro
                console.log('✅ Productos cargados:', this.productos.length);
                this.renderizarProductos();
                this.renderizarPaginacion();
            } else {
                console.error('❌ Error en la respuesta:', data);
                this.mostrarError();
            }
        } catch (error) {
            console.error('❌ Error en la petición:', error);
            this.mostrarError();
        }
    }

    obtenerProductosPagina() {
        const inicio = (this.paginaActual - 1) * this.productosPorPagina;
        const fin = inicio + this.productosPorPagina;
        return this.productos.slice(inicio, fin);
    }

    getTotalPaginas() {
        return Math.ceil(this.productos.length / this.productosPorPagina);
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

        // Obtener solo los productos de la página actual
        const productosPagina = this.obtenerProductosPagina();

        grid.innerHTML = productosPagina.map(producto => `
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
        productosPagina.forEach(producto => {
            this.cargarReacciones(producto.id);
        });

        // Agregar event listeners a todos los botones
        this.agregarEventListenersProductos();
    }

    renderizarPaginacion() {
        const totalPaginas = this.getTotalPaginas();

        // Buscar o crear contenedor de paginación
        let paginacionContainer = document.querySelector('.pagination-container');

        if (!paginacionContainer) {
            // Crear contenedor si no existe
            const grid = document.querySelector('.products-grid');
            if (grid && grid.parentElement) {
                paginacionContainer = document.createElement('div');
                paginacionContainer.className = 'pagination-container';
                grid.parentElement.appendChild(paginacionContainer);
            } else {
                return;
            }
        }

        if (totalPaginas <= 1) {
            paginacionContainer.innerHTML = '';
            return;
        }

        let paginacionHTML = '<div class="pagination">';

        // Botón anterior
        paginacionHTML += `
            <button class="pagination-btn ${this.paginaActual === 1 ? 'disabled' : ''}" 
                    data-pagina="${this.paginaActual - 1}"
                    ${this.paginaActual === 1 ? 'disabled' : ''}>
                <i class="fas fa-chevron-left"></i> Anterior
            </button>
        `;

        // Números de página
        for (let i = 1; i <= totalPaginas; i++) {
            if (
                i === 1 ||
                i === totalPaginas ||
                (i >= this.paginaActual - 2 && i <= this.paginaActual + 2)
            ) {
                paginacionHTML += `
                    <button class="pagination-btn ${i === this.paginaActual ? 'active' : ''}" 
                            data-pagina="${i}">
                        ${i}
                    </button>
                `;
            } else if (
                i === this.paginaActual - 3 ||
                i === this.paginaActual + 3
            ) {
                paginacionHTML += '<span class="pagination-dots">...</span>';
            }
        }

        // Botón siguiente
        paginacionHTML += `
            <button class="pagination-btn ${this.paginaActual === totalPaginas ? 'disabled' : ''}" 
                    data-pagina="${this.paginaActual + 1}"
                    ${this.paginaActual === totalPaginas ? 'disabled' : ''}>
                Siguiente <i class="fas fa-chevron-right"></i>
            </button>
        `;

        paginacionHTML += '</div>';

        // Info de página
        const inicio = (this.paginaActual - 1) * this.productosPorPagina + 1;
        const fin = Math.min(this.paginaActual * this.productosPorPagina, this.productos.length);

        paginacionHTML += `
            <div class="pagination-info">
                Mostrando ${inicio} - ${fin} de ${this.productos.length} productos
            </div>
        `;

        paginacionContainer.innerHTML = paginacionHTML;

        // Agregar event listeners a los botones
        paginacionContainer.querySelectorAll('.pagination-btn:not(.disabled)').forEach(btn => {
            btn.addEventListener('click', () => {
                const pagina = parseInt(btn.dataset.pagina);
                this.cambiarPagina(pagina);
            });
        });
    }

    cambiarPagina(pagina) {
        const totalPaginas = this.getTotalPaginas();

        if (pagina < 1 || pagina > totalPaginas) return;

        this.paginaActual = pagina;
        this.renderizarProductos();
        this.renderizarPaginacion();

        // Scroll suave hacia arriba
        const grid = document.querySelector('.products-grid');
        if (grid) {
            grid.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }

        console.log(`📄 Página ${pagina} de ${totalPaginas}`);
    }

    agregarEventListenersProductos() {
        // Botones de reacciones
        document.querySelectorAll('.reaction-like, .reaction-dislike').forEach(btn => {
            // Remover listener anterior si existe
            const newBtn = btn.cloneNode(true);
            btn.parentNode.replaceChild(newBtn, btn);

            newBtn.addEventListener('click', (e) => {
                e.stopPropagation();
                e.preventDefault();
                const productoId = parseInt(newBtn.dataset.productoId);
                const tipo = newBtn.dataset.tipo;
                reaccionarProducto(e, productoId, tipo);
            }, { once: false });
        });

        // Elementos clickeables para ver detalle
        document.querySelectorAll('.producto-ver-detalle, .btn-ver-detalle').forEach(element => {
            // Remover listener anterior si existe
            const newElement = element.cloneNode(true);
            element.parentNode.replaceChild(newElement, element);

            newElement.addEventListener('click', (e) => {
                e.stopPropagation();
                e.preventDefault();
                const productoId = parseInt(newElement.dataset.productoId);
                verDetalle(productoId);
            }, { once: false });
        });

        // Botones de agregar al carrito - CRÍTICO: Evitar duplicados
        document.querySelectorAll('.btn-add-cart, .btn-add-to-cart').forEach(btn => {
            // Verificar si ya tiene el flag de listener
            if (btn.dataset.listenerAdded === 'true') {
                console.log('⚠️ Listener ya existe para botón, saltando...');
                return;
            }

            // Marcar que se agregó el listener
            btn.dataset.listenerAdded = 'true';

            btn.addEventListener('click', (e) => {
                e.stopPropagation();
                e.preventDefault();

                // Verificar si el botón está deshabilitado
                if (btn.disabled) {
                    console.log('⚠️ Botón deshabilitado, ignorando clic');
                    return;
                }

                // Deshabilitar temporalmente para evitar doble clic
                btn.disabled = true;
                const originalHTML = btn.innerHTML;
                btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Agregando...';

                const productoId = parseInt(btn.dataset.productoId);
                console.log('🛒 Botón clickeado, agregando producto:', productoId);

                // Llamar a la función con timeout para re-habilitar el botón
                agregarAlCarrito(productoId);

                // Re-habilitar después de 2 segundos
                setTimeout(() => {
                    btn.disabled = false;
                    btn.innerHTML = originalHTML;
                }, 2000);
            }, { once: false });
        });

        console.log('✅ Event listeners configurados para',
                   document.querySelectorAll('.btn-add-cart, .btn-add-to-cart').length,
                   'botones');
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

// Variable para controlar el debounce de agregar al carrito
let agregarAlCarritoTimeout = null;
let ultimoProductoAgregado = null;
let ultimoTimestamp = 0;

// Función global para agregar al carrito
function agregarAlCarrito(productoId) {
    const ahora = Date.now();
    console.log('🛒 [agregarAlCarrito] Llamada recibida para producto ID:', productoId);

    // Protección contra múltiples clics rápidos (menos de 500ms)
    if (ultimoProductoAgregado === productoId && (ahora - ultimoTimestamp) < 500) {
        console.warn('⚠️ [PROTECCIÓN] Clic duplicado detectado! Ignorando... (tiempo desde último: ' + (ahora - ultimoTimestamp) + 'ms)');
        return;
    }

    // Actualizar timestamp y producto
    ultimoTimestamp = ahora;
    ultimoProductoAgregado = productoId;

    console.log('✅ [agregarAlCarrito] Procesando solicitud...');

    // Resetear después de 1 segundo
    if (agregarAlCarritoTimeout) {
        clearTimeout(agregarAlCarritoTimeout);
    }
    agregarAlCarritoTimeout = setTimeout(() => {
        ultimoProductoAgregado = null;
        ultimoTimestamp = 0;
        agregarAlCarritoTimeout = null;
        console.log('🔄 [agregarAlCarrito] Protección reseteada');
    }, 1000);

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

    console.log('📦 [agregarAlCarrito] Producto encontrado:', producto.nombre);
    console.log('📊 [agregarAlCarrito] Carrito ANTES:', carrito.items.length, 'items');

    try {
        carrito.agregar(producto);
        console.log('✅ [agregarAlCarrito] Producto agregado exitosamente');
        console.log('📊 [agregarAlCarrito] Carrito DESPUÉS:', carrito.items.length, 'items');
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
    // Usar el modal del carrito si existe
    if (window.carrito && window.carrito.showConfirmModal) {
        window.carrito.showConfirmModal(
            '⚠️ Limpiar almacenamiento',
            'Esto vaciará el carrito y otros datos guardados. ¿Estás seguro?',
            'warning',
            'Limpiar Todo',
            () => {
                localStorage.clear();
                console.log('✅ LocalStorage limpiado exitosamente');
                window.carrito.showToast('¡Limpieza completa!', 'Almacenamiento limpiado. Recargando página...', 'success');
                setTimeout(() => location.reload(), 1500);
            }
        );
    } else {
        // Fallback si no está disponible el sistema de notificaciones
        if (confirm('¿Estás seguro de que quieres limpiar el almacenamiento del navegador?\n\nEsto vaciará el carrito y otros datos guardados.')) {
            localStorage.clear();
            console.log('✅ LocalStorage limpiado exitosamente');
            alert('Almacenamiento limpiado. Recargando página...');
            location.reload();
        }
    }
}

// Función global para vaciar solo el carrito (accesible desde consola)
function vaciarCarrito() {
    if (carrito) {
        carrito.vaciar();
        console.log('✅ Carrito vaciado exitosamente');
        if (carrito.showToast) {
            carrito.showToast('¡Carrito vaciado!', 'El carrito ha sido vaciado correctamente.', 'success');
        }
    } else {
        console.error('❌ Carrito no está inicializado');
    }
}

// Función global para limpiar duplicados del carrito (accesible desde consola)
function limpiarDuplicados() {
    console.log('🧹 Limpiando duplicados del carrito...');

    if (!carrito) {
        console.error('❌ Carrito no está inicializado');
        return;
    }

    const itemsOriginales = carrito.items.length;
    console.log('📦 Items antes de limpiar:', itemsOriginales);

    // Crear un mapa de productos únicos
    const productosUnicos = new Map();

    carrito.items.forEach(item => {
        const id = parseInt(item.id);
        if (!productosUnicos.has(id)) {
            // Primera vez que vemos este producto
            productosUnicos.set(id, {
                ...item,
                id: id,
                precio: parseFloat(item.precio),
                cantidad: parseInt(item.cantidad),
                stock: parseInt(item.stock)
            });
        } else {
            // Ya existe, sumar la cantidad
            const existente = productosUnicos.get(id);
            existente.cantidad += parseInt(item.cantidad);
            console.log(`⚠️ Duplicado encontrado y consolidado: ${item.nombre} (ID: ${id})`);
        }
    });

    // Actualizar el carrito con los items únicos
    carrito.items = Array.from(productosUnicos.values());
    carrito.guardarCarrito();

    const itemsLimpiados = carrito.items.length;
    const eliminados = itemsOriginales - itemsLimpiados;

    if (eliminados > 0) {
        console.log(`✅ Limpieza completada: ${eliminados} duplicado(s) eliminado(s)`);
        console.log(`📦 Items después de limpiar: ${itemsLimpiados}`);
        if (carrito.showToast) {
            carrito.showToast(
                '✅ Duplicados eliminados',
                `Se eliminaron ${eliminados} producto(s) duplicado(s)`,
                'success'
            );
        }
        carrito.mostrarCarrito();
    } else {
        console.log('✅ No se encontraron duplicados');
        if (carrito.showToast) {
            carrito.showToast('✅ Carrito limpio', 'No se encontraron productos duplicados', 'info');
        }
    }

    console.log('📊 Carrito actual:', carrito.items);
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

