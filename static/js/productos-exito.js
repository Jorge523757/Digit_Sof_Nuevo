// ========================================
// PRODUCTOS ESTILO E-COMMERCE - JavaScript
// Drawer, Filtros y Carrito
// ========================================

console.log('✅ productos-exito.js cargado');

// Inicializar cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', function() {
    console.log('🚀 Inicializando productos-exito.js');

    // Elementos del DOM
    const btnCarrito = document.getElementById('btnCarrito');
    const cartDrawer = document.getElementById('cartDrawer');
    const cartOverlay = document.getElementById('cartOverlay');
    const btnCloseDrawer = document.getElementById('btnCloseDrawer');
    const cartDrawerBody = document.getElementById('cartDrawerBody');
    const cartSubtotal = document.getElementById('cartSubtotal');
    const cartBadge = document.getElementById('cartBadge');
    const btnToggleFilters = document.getElementById('btnToggleFilters');
    const filtersSidebar = document.getElementById('filtersSidebar');
    const btnClearFilters = document.getElementById('btnClearFilters');
    const btnNotifications = document.getElementById('btnNotifications');
    const btnAccount = document.getElementById('btnAccount');
    
    // ========================================
    // BOTÓN DE NOTIFICACIONES
    // ========================================
    
    if (btnNotifications) {
        btnNotifications.addEventListener('click', function(e) {
            e.preventDefault();
            alert('🔔 Panel de Notificaciones\n\nAquí aparecerán tus notificaciones importantes.\n\n• Ofertas especiales\n• Estado de pedidos\n• Promociones exclusivas');
        });
    }
    
    // ========================================
    // BOTÓN MI CUENTA
    // ========================================
    
    if (btnAccount) {
        btnAccount.addEventListener('click', function(e) {
            e.preventDefault();
            // Redirigir al dashboard o mostrar menú
            const options = [
                '👤 Mi Perfil',
                '📦 Mis Pedidos',
                '❤️ Lista de Deseos',
                '⚙️ Configuración',
                '🚪 Cerrar Sesión'
            ].join('\n');
            alert('Mi Cuenta\n\n' + options + '\n\n(Próximamente disponible)');
        });
    }

    // ========================================
    // DRAWER DEL CARRITO
    // ========================================

    // Abrir drawer
    if (btnCarrito) {
        btnCarrito.addEventListener('click', function(e) {
            e.preventDefault();
            openCartDrawer();
        });
    }

    // Cerrar drawer
    if (btnCloseDrawer) {
        btnCloseDrawer.addEventListener('click', function() {
            closeCartDrawer();
        });
    }

    // Cerrar con overlay
    if (cartOverlay) {
        cartOverlay.addEventListener('click', function() {
            closeCartDrawer();
        });
    }

    function openCartDrawer() {
        if (cartDrawer && cartOverlay) {
            cartDrawer.classList.add('open');
            cartOverlay.classList.add('show');
            document.body.style.overflow = 'hidden';
            renderCartItems();
        }
    }

    function closeCartDrawer() {
        if (cartDrawer && cartOverlay) {
            cartDrawer.classList.remove('open');
            cartOverlay.classList.remove('show');
            document.body.style.overflow = 'auto';
        }
    }

    // Cerrar con ESC
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && cartDrawer && cartDrawer.classList.contains('open')) {
            closeCartDrawer();
        }
    });

    // ========================================
    // RENDERIZAR ITEMS DEL CARRITO
    // ========================================

    // Función auxiliar para normalizar URLs
    function normalizeImageUrl(url) {
        if (!url) return '';
        url = String(url).trim();
        if (url.startsWith('//')) return location.protocol + url;
        if (url.startsWith('/')) return location.origin + url;
        if (!url.startsWith('http')) return location.origin + '/' + url;
        return url;
    }

    function renderCartItems() {
        console.log('🎨 [RENDER] Renderizando carrito...');

        const carrito = JSON.parse(localStorage.getItem('carrito_v1') || '{}');
        const items = Object.values(carrito);

        console.log('🎨 [RENDER] Items encontrados:', items.length);

        if (!cartDrawerBody) {
            console.warn('⚠️ [RENDER] cartDrawerBody no encontrado');
            return;
        }

        if (items.length === 0) {
            cartDrawerBody.innerHTML = `
                <div style="text-align: center; padding: 40px 20px; color: #6b7280;">
                    <i class="fas fa-shopping-cart" style="font-size: 3rem; margin-bottom: 16px;"></i>
                    <p style="font-size: 1.1rem; font-weight: 600; margin-bottom: 8px;">Tu carrito está vacío</p>
                    <p style="font-size: 0.9rem;">¡Agrega productos increíbles!</p>
                </div>
            `;
            if (cartSubtotal) cartSubtotal.textContent = '$0';
            updateCartBadge();
            return;
        }

        let html = '';
        let subtotal = 0;

        items.forEach((item, index) => {
            const precio = parseFloat(item.price || item.precio || 0);
            const cantidad = parseInt(item.qty || item.cantidad || 1);
            const total = precio * cantidad;
            subtotal += total;

            // Obtener imagen con normalización
            let imagenSrc = item.image || item.imagen || item.img || '';
            imagenSrc = normalizeImageUrl(imagenSrc);

            const tieneImagen = imagenSrc && imagenSrc.trim() !== '';

            console.log(`🖼️ [RENDER] Item ${index + 1}:`, {
                id: item.id,
                nombre: (item.name || item.nombre || '').substring(0, 30),
                imagen: imagenSrc,
                tieneImagen: tieneImagen
            });

            html += `
                <div class="cart-item-drawer" data-id="${item.id}" style="display: flex; gap: 14px; padding: 18px; margin-bottom: 12px; border-radius: 12px; background: white; border: 1px solid #e5e7eb; transition: all 0.3s;">
                    ${tieneImagen ? `
                        <img src="${imagenSrc}" 
                             style="width: 85px; height: 85px; object-fit: contain; background: linear-gradient(135deg, #f9fafb 0%, #f3f4f6 100%); border-radius: 10px; padding: 10px; border: 1px solid #e5e7eb; flex-shrink: 0;"
                             alt="${item.name || item.nombre || ''}"
                             onerror="console.error('❌ Error cargando imagen:', this.src); this.style.display='none'; this.nextElementSibling.style.display='flex';">
                        <div style="display: none; width: 85px; height: 85px; background: linear-gradient(135deg, #f9fafb 0%, #f3f4f6 100%); border-radius: 10px; align-items: center; justify-content: center; border: 1px solid #e5e7eb; flex-shrink: 0;">
                            <i class="fas fa-image" style="font-size: 2rem; color: #d1d5db;"></i>
                        </div>
                    ` : `
                        <div style="width: 85px; height: 85px; background: linear-gradient(135deg, #f9fafb 0%, #f3f4f6 100%); border-radius: 10px; display: flex; align-items: center; justify-content: center; border: 1px solid #e5e7eb; flex-shrink: 0;">
                            <i class="fas fa-image" style="font-size: 2rem; color: #d1d5db;"></i>
                        </div>
                    `}
                    <div style="flex: 1; display: flex; flex-direction: column; gap: 6px;">
                        <div style="font-size: 0.92rem; font-weight: 600; color: #1f2937; line-height: 1.4;">
                            ${((item.name || item.nombre) || '').substring(0, 70)}${((item.name || item.nombre) || '').length > 70 ? '...' : ''}
                        </div>
                        <div style="color: #FF6B00; font-weight: 800; font-size: 1.15rem;">
                            $${precio.toLocaleString('es-CO', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}
                        </div>
                        <div style="display: flex; align-items: center; gap: 10px; margin-top: auto;">
                            <button class="qty-btn qty-decrease" data-id="${item.id}" style="background: linear-gradient(135deg, #ffffff 0%, #f9fafb 100%); border: 2px solid #e5e7eb; width: 32px; height: 32px; border-radius: 8px; cursor: pointer; display: flex; align-items: center; justify-content: center; transition: all 0.2s;">
                                <i class="fas fa-minus" style="color: #6b7280;"></i>
                            </button>
                            <span style="min-width: 35px; text-align: center; font-weight: 600; font-size: 1rem;">${cantidad}</span>
                            <button class="qty-btn qty-increase" data-id="${item.id}" style="background: linear-gradient(135deg, #ffffff 0%, #f9fafb 100%); border: 2px solid #e5e7eb; width: 32px; height: 32px; border-radius: 8px; cursor: pointer; display: flex; align-items: center; justify-content: center; transition: all 0.2s;">
                                <i class="fas fa-plus" style="color: #6b7280;"></i>
                            </button>
                            <button class="qty-btn qty-delete" data-id="${item.id}" style="margin-left: auto; background: linear-gradient(135deg, #ffffff 0%, #f9fafb 100%); border: 2px solid #e5e7eb; width: 32px; height: 32px; border-radius: 8px; cursor: pointer; display: flex; align-items: center; justify-content: center; color: #ef4444; transition: all 0.2s;">
                                <i class="fas fa-trash"></i>
                            </button>
                        </div>
                    </div>
                </div>
            `;
        });

        cartDrawerBody.innerHTML = html;

        if (cartSubtotal) {
            cartSubtotal.textContent = '$' + subtotal.toLocaleString('es-CO', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
        }

        console.log('✅ [RENDER] Carrito renderizado:', items.length, 'items, subtotal:', subtotal);

        // Agregar event listeners a los botones
        attachCartButtonEvents();
        updateCartBadge();
    }

    // ========================================
    // EVENTOS DE BOTONES DEL CARRITO
    // ========================================

    function attachCartButtonEvents() {
        // Botones de aumentar cantidad
        document.querySelectorAll('.qty-increase').forEach(btn => {
            btn.addEventListener('click', function() {
                const id = this.dataset.id;
                updateCartQuantity(id, 1);
            });
        });

        // Botones de disminuir cantidad
        document.querySelectorAll('.qty-decrease').forEach(btn => {
            btn.addEventListener('click', function() {
                const id = this.dataset.id;
                updateCartQuantity(id, -1);
            });
        });

        // Botones de eliminar
        document.querySelectorAll('.qty-delete').forEach(btn => {
            btn.addEventListener('click', function() {
                const id = this.dataset.id;

                // Obtener info del producto del carrito
                const carrito = JSON.parse(localStorage.getItem('carrito_v1') || '{}');
                const producto = carrito[id];

                if (producto) {
                    mostrarModalEliminar(id, producto);
                } else {
                    removeFromCart(id);
                }
            });
        });
    }

    function mostrarModalEliminar(productoId, producto) {
        const modal = document.getElementById('deleteModal');
        const productInfo = document.getElementById('deleteProductInfo');

        if (!modal || !productInfo) {
            console.warn('⚠️ Modal no encontrado, eliminando directamente');
            removeFromCart(productoId);
            return;
        }

        // Construir HTML del producto
        const imagen = producto.image || producto.imagen || '';
        const nombre = producto.name || producto.nombre || 'Producto';
        const precio = parseFloat(producto.price || producto.precio || 0);
        const cantidad = parseInt(producto.qty || producto.cantidad || 1);

        productInfo.innerHTML = `
            <div style="display: flex; gap: 15px; align-items: center;">
                ${imagen ? `
                    <img src="${imagen}" 
                         style="width: 80px; height: 80px; object-fit: contain; border-radius: 12px; border: 2px solid #e5e7eb; padding: 8px; background: #f9fafb;"
                         alt="${nombre}"
                         onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
                    <div style="display: none; width: 80px; height: 80px; background: #f3f4f6; border-radius: 12px; align-items: center; justify-content: center;">
                        <i class="fas fa-image" style="font-size: 2rem; color: #d1d5db;"></i>
                    </div>
                ` : `
                    <div style="width: 80px; height: 80px; background: #f3f4f6; border-radius: 12px; display: flex; align-items: center; justify-content: center;">
                        <i class="fas fa-image" style="font-size: 2rem; color: #d1d5db;"></i>
                    </div>
                `}
                <div style="flex: 1;">
                    <div style="font-weight: 600; color: #1f2937; font-size: 1.05rem; margin-bottom: 8px; line-height: 1.4;">
                        ${nombre}
                    </div>
                    <div style="display: flex; align-items: center; gap: 15px; flex-wrap: wrap;">
                        <div style="color: #FF6B00; font-weight: 700; font-size: 1.15rem;">
                            $${precio.toLocaleString('es-CO', { minimumFractionDigits: 2 })}
                        </div>
                        <div style="background: #f3f4f6; padding: 4px 12px; border-radius: 8px; font-size: 0.9rem; color: #6b7280;">
                            <i class="fas fa-box"></i> Cantidad: <strong>${cantidad}</strong>
                        </div>
                    </div>
                    <div style="margin-top: 8px; color: #ef4444; font-size: 0.9rem; font-weight: 600;">
                        <i class="fas fa-calculator"></i> Subtotal: $${(precio * cantidad).toLocaleString('es-CO', { minimumFractionDigits: 2 })}
                    </div>
                </div>
            </div>
        `;

        // Mostrar modal
        modal.classList.add('show');
        document.body.style.overflow = 'hidden';

        // Configurar botones
        const btnCancel = document.getElementById('btnCancelDelete');
        const btnConfirm = document.getElementById('btnConfirmDelete');

        // Limpiar eventos anteriores clonando los botones
        const newBtnCancel = btnCancel.cloneNode(true);
        const newBtnConfirm = btnConfirm.cloneNode(true);
        btnCancel.parentNode.replaceChild(newBtnCancel, btnCancel);
        btnConfirm.parentNode.replaceChild(newBtnConfirm, btnConfirm);

        // Agregar nuevos eventos
        newBtnCancel.addEventListener('click', () => {
            modal.classList.remove('show');
            document.body.style.overflow = 'auto';
        });

        newBtnConfirm.addEventListener('click', () => {
            console.log('✅ Producto eliminado:', productoId);
            removeFromCart(productoId);
            modal.classList.remove('show');
            document.body.style.overflow = 'auto';
        });

        // Cerrar al hacer clic fuera del modal
        const clickOutsideHandler = (e) => {
            if (e.target === modal) {
                modal.classList.remove('show');
                document.body.style.overflow = 'auto';
                modal.removeEventListener('click', clickOutsideHandler);
            }
        };
        modal.addEventListener('click', clickOutsideHandler);
    }

    function updateCartQuantity(id, change) {
        const carrito = JSON.parse(localStorage.getItem('carrito_v1') || '{}');

        if (carrito[id]) {
            const nuevaCantidad = parseInt(carrito[id].qty || carrito[id].cantidad || 1) + change;

            if (nuevaCantidad <= 0) {
                delete carrito[id];
            } else {
                carrito[id].qty = nuevaCantidad;
                carrito[id].cantidad = nuevaCantidad;
            }

            localStorage.setItem('carrito_v1', JSON.stringify(carrito));
            renderCartItems();
            updateCartBadge();
        }
    }

    function removeFromCart(id) {
        const carrito = JSON.parse(localStorage.getItem('carrito_v1') || '{}');
        delete carrito[id];
        localStorage.setItem('carrito_v1', JSON.stringify(carrito));
        renderCartItems();
        updateCartBadge();
    }

    // ========================================
    // ACTUALIZAR BADGE DEL CARRITO
    // ========================================

    function updateCartBadge() {
        const carrito = JSON.parse(localStorage.getItem('carrito_v1') || '{}');
        const items = Object.values(carrito);
        const total = items.reduce((sum, item) => sum + parseInt(item.qty || item.cantidad || 1), 0);

        if (cartBadge) {
            cartBadge.textContent = total;
            cartBadge.style.display = total > 0 ? 'flex' : 'none';
        }
    }

    // Actualizar badge al cargar
    updateCartBadge();

    // ========================================
    // FILTROS LATERALES (MÓVIL)
    // ========================================

    if (btnToggleFilters && filtersSidebar) {
        btnToggleFilters.addEventListener('click', function() {
            filtersSidebar.classList.toggle('open');
            if (cartOverlay) {
                cartOverlay.classList.add('show');
            }
        });
    }

    // Cerrar filtros con overlay
    if (cartOverlay) {
        cartOverlay.addEventListener('click', function() {
            if (filtersSidebar && filtersSidebar.classList.contains('open')) {
                filtersSidebar.classList.remove('open');
                cartOverlay.classList.remove('show');
            }
        });
    }

    // ========================================
    // LIMPIAR FILTROS
    // ========================================

    if (btnClearFilters) {
        btnClearFilters.addEventListener('click', function(e) {
            e.preventDefault();

            // Desmarcar todos los checkboxes y radios
            document.querySelectorAll('.filter-option input[type="checkbox"]').forEach(input => {
                input.checked = false;
            });

            document.querySelectorAll('.filter-option input[type="radio"]').forEach(input => {
                input.checked = false;
            });

            // Recargar sin parámetros de filtro
            window.location.href = window.location.pathname;
        });
    }

    // ========================================
    // ORDENAMIENTO
    // ========================================

    const sortSelect = document.getElementById('sortSelect');
    if (sortSelect) {
        sortSelect.addEventListener('change', function() {
            const url = new URL(window.location.href);
            url.searchParams.set('orden', this.value);
            window.location.href = url.toString();
        });

        // Restaurar valor seleccionado
        const urlParams = new URLSearchParams(window.location.search);
        const orden = urlParams.get('orden');
        if (orden) {
            sortSelect.value = orden;
        }
    }

    // ========================================
    // VISTA GRID/LIST
    // ========================================

    const viewBtns = document.querySelectorAll('.view-btn');
    const productsGrid = document.getElementById('productsGrid');

    viewBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const view = this.dataset.view;

            // Actualizar botones activos
            viewBtns.forEach(b => b.classList.remove('active'));
            this.classList.add('active');

            // Cambiar clase del grid
            if (productsGrid) {
                if (view === 'list') {
                    productsGrid.style.gridTemplateColumns = '1fr';
                    productsGrid.querySelectorAll('.product-card-exito').forEach(card => {
                        card.style.flexDirection = 'row';
                        card.querySelector('.product-image-exito').style.width = '200px';
                        card.querySelector('.product-image-exito').style.height = '200px';
                    });
                } else {
                    productsGrid.style.gridTemplateColumns = 'repeat(auto-fill, minmax(260px, 1fr))';
                    productsGrid.querySelectorAll('.product-card-exito').forEach(card => {
                        card.style.flexDirection = 'column';
                        card.querySelector('.product-image-exito').style.width = '100%';
                        card.querySelector('.product-image-exito').style.height = '220px';
                    });
                }
            }
        });
    });

    // ========================================
    // COLAPSAR/EXPANDIR FILTROS
    // ========================================

    document.querySelectorAll('.filter-title').forEach(title => {
        title.addEventListener('click', function() {
            const target = this.dataset.target;
            const content = document.querySelector(target);

            if (content) {
                content.classList.toggle('show');

                // Rotar icono
                const icon = this.querySelector('i');
                if (icon) {
                    if (content.classList.contains('show')) {
                        this.setAttribute('aria-expanded', 'true');
                    } else {
                        this.setAttribute('aria-expanded', 'false');
                    }
                }
            }
        });
    });

    // ========================================
    // APLICAR FILTROS AUTOMÁTICAMENTE
    // ========================================

    document.querySelectorAll('.filter-option input').forEach(input => {
        input.addEventListener('change', function() {
            applyFilters();
        });
    });

    function applyFilters() {
        const url = new URL(window.location.href);

        // Categorías
        const categorias = [];
        document.querySelectorAll('.filter-option input[name="category"]:checked').forEach(input => {
            categorias.push(input.value);
        });

        if (categorias.length > 0) {
            url.searchParams.set('categorias', categorias.join(','));
        } else {
            url.searchParams.delete('categorias');
        }

        // Marcas
        const marcas = [];
        document.querySelectorAll('.filter-option input[name="brand"]:checked').forEach(input => {
            marcas.push(input.value);
        });

        if (marcas.length > 0) {
            url.searchParams.set('marcas', marcas.join(','));
        } else {
            url.searchParams.delete('marcas');
        }

        // Precio
        const precio = document.querySelector('.filter-option input[name="price"]:checked');
        if (precio) {
            url.searchParams.set('precio', precio.value);
        } else {
            url.searchParams.delete('precio');
        }

        // Colores
        const colores = [];
        document.querySelectorAll('.filter-option input[name="color"]:checked').forEach(input => {
            colores.push(input.value);
        });

        if (colores.length > 0) {
            url.searchParams.set('colores', colores.join(','));
        } else {
            url.searchParams.delete('colores');
        }

        // Aplicar filtros (solo si cambió algo)
        if (url.toString() !== window.location.href) {
            window.location.href = url.toString();
        }
    }

    console.log('✅ productos-exito.js inicializado correctamente');

    // ========================================
    // EXPORTAR FUNCIONES GLOBALES
    // ========================================
    window.renderCartItems = renderCartItems;
    window.updateCartBadge = updateCartBadge;
    window.attachCartButtonEvents = attachCartButtonEvents;
    window.mostrarModalEliminar = mostrarModalEliminar;

    console.log('✅ Funciones del carrito exportadas globalmente');
});

