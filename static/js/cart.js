// Sistema de Carrito Digit Soft - Versión Corregida
console.log('Cargando DigitSoftCart...');

// Variables globales
let cartInstance = null;
let cartItems = [];
let cartVisible = false;

// Funciones principales del carrito
const DigitSoftCart = {
    // Inicializar carrito
    init: function() {
        console.log('Inicializando carrito...');
        
        // Cargar items del localStorage
        this.loadCartItems();
        
        // Crear el contenedor del carrito
        this.createCartContainer();
        
        // Actualizar contador
        this.updateCounter();
        
        // Configurar eventos
        this.bindEvents();
        
        console.log('Carrito inicializado correctamente');
    },

    // Cargar items del localStorage
    loadCartItems: function() {
        try {
            const saved = localStorage.getItem('digitsoft_cart');
            cartItems = saved ? JSON.parse(saved) : [];
            console.log('Items cargados:', cartItems.length);
        } catch (error) {
            console.error('Error cargando items:', error);
            cartItems = [];
        }
    },

    // Guardar items en localStorage
    saveCartItems: function() {
        try {
            localStorage.setItem('digitsoft_cart', JSON.stringify(cartItems));
        } catch (error) {
            console.error('Error guardando items:', error);
        }
    },

    // Crear contenedor del carrito
    createCartContainer: function() {
        // Verificar si ya existe
        if (document.getElementById('cart-container')) {
            console.log('Contenedor del carrito ya existe');
            return;
        }

        console.log('Creando contenedor del carrito...');

        // Crear el HTML del carrito
        const cartHTML = `
            <div id="cart-container" class="cart-container">
                <div class="cart-overlay" id="cart-overlay"></div>
                <div class="cart-sidebar" id="cart-sidebar">
                    <div class="cart-header">
                        <h3><i class="fas fa-shopping-cart"></i> Mi Carrito</h3>
                        <button class="cart-close" id="cart-close">
                            <i class="fas fa-times"></i>
                        </button>
                    </div>
                    <div class="cart-body" id="cart-body">
                        <div class="empty-cart">
                            <i class="fas fa-shopping-cart" style="font-size: 3rem; opacity: 0.5; margin-bottom: 1rem;"></i>
                            <h4>Tu carrito está vacío</h4>
                            <p>Explora nuestros productos y agrega algunos a tu carrito</p>
                        </div>
                    </div>
                    <div class="cart-footer">
                        <div class="cart-total">
                            <strong>Total: $<span id="cart-total">0.00</span></strong>
                        </div>
                        <button class="btn-checkout" onclick="DigitSoftCart.checkout()">
                            <i class="fas fa-credit-card"></i> Proceder al Pago
                        </button>
                        <button class="btn-clear-cart" onclick="DigitSoftCart.clearCart()">
                            <i class="fas fa-trash"></i> Vaciar Carrito
                        </button>
                    </div>
                </div>
            </div>
        `;

        // Agregar al body
        document.body.insertAdjacentHTML('beforeend', cartHTML);

        // Agregar estilos CSS
        this.addCartStyles();
    },

    // Agregar estilos CSS
    addCartStyles: function() {
        if (document.getElementById('cart-styles')) {
            return;
        }

        const styles = document.createElement('style');
        styles.id = 'cart-styles';
        styles.textContent = `
            .cart-container {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                z-index: 9999;
                pointer-events: none;
                transition: all 0.3s ease;
            }
            
            .cart-container.active {
                pointer-events: all;
            }
            
            .cart-overlay {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(0, 0, 0, 0.5);
                opacity: 0;
                transition: opacity 0.3s ease;
            }
            
            .cart-container.active .cart-overlay {
                opacity: 1;
            }
            
            .cart-sidebar {
                position: absolute;
                top: 0;
                right: -400px;
                width: 400px;
                height: 100%;
                background: white;
                box-shadow: -5px 0 15px rgba(0, 0, 0, 0.1);
                transition: right 0.3s ease;
                display: flex;
                flex-direction: column;
            }
            
            .cart-container.active .cart-sidebar {
                right: 0;
            }
            
            .cart-header {
                padding: 1.5rem;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            
            .cart-close {
                background: none;
                border: none;
                color: white;
                font-size: 1.2rem;
                cursor: pointer;
                padding: 0.5rem;
                border-radius: 50%;
                transition: background-color 0.3s ease;
            }
            
            .cart-close:hover {
                background-color: rgba(255, 255, 255, 0.2);
            }
            
            .cart-body {
                flex: 1;
                padding: 1rem;
                overflow-y: auto;
            }
            
            .cart-footer {
                padding: 1.5rem;
                background: #f8f9fa;
                border-top: 1px solid #eee;
            }
            
            .cart-total {
                text-align: center;
                margin-bottom: 1rem;
                font-size: 1.2rem;
                color: #333;
            }
            
            .btn-checkout, .btn-clear-cart {
                width: 100%;
                padding: 1rem;
                margin-bottom: 0.5rem;
                border: none;
                border-radius: 8px;
                font-weight: 600;
                cursor: pointer;
                transition: all 0.3s ease;
            }
            
            .btn-checkout {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
            }
            
            .btn-checkout:hover {
                transform: translateY(-2px);
                box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
            }
            
            .btn-clear-cart {
                background: #f8f9fa;
                color: #666;
                border: 2px solid #e9ecef;
            }
            
            .btn-clear-cart:hover {
                background: #e9ecef;
                color: #333;
            }
            
            .empty-cart {
                text-align: center;
                padding: 3rem 1rem;
                color: #666;
            }
            
            @media (max-width: 768px) {
                .cart-sidebar {
                    width: 100%;
                    right: -100%;
                }
            }
        `;
        
        document.head.appendChild(styles);
    },

    // Configurar eventos
    bindEvents: function() {
        // Cerrar carrito al hacer click en overlay o botón cerrar
        document.addEventListener('click', function(e) {
            if (e.target.id === 'cart-overlay' || e.target.id === 'cart-close' || e.target.closest('#cart-close')) {
                DigitSoftCart.hideCart();
            }
        });
    },

    // Mostrar/ocultar carrito
    toggleCart: function() {
        console.log('Toggle carrito');
        if (cartVisible) {
            this.hideCart();
        } else {
            this.showCart();
        }
    },

    // Mostrar carrito
    showCart: function() {
        console.log('Mostrando carrito');
        const container = document.getElementById('cart-container');
        if (container) {
            container.classList.add('active');
            cartVisible = true;
            document.body.style.overflow = 'hidden';
        }
    },

    // Ocultar carrito
    hideCart: function() {
        console.log('Ocultando carrito');
        const container = document.getElementById('cart-container');
        if (container) {
            container.classList.remove('active');
            cartVisible = false;
            document.body.style.overflow = '';
        }
    },

    // Agregar producto
    addItem: function(product) {
        console.log('Agregando producto:', product);
        
        const existingItem = cartItems.find(item => item.id === product.id);
        
        if (existingItem) {
            existingItem.quantity += 1;
        } else {
            cartItems.push({
                id: product.id,
                name: product.name,
                price: product.price,
                image: product.image || '/static/imagenes/producto-default.jpg',
                quantity: 1
            });
        }
        
        this.saveCartItems();
        this.updateCounter();
        this.renderCart();
        this.showNotification(product.name + ' agregado al carrito');
    },

    // Vaciar carrito
    clearCart: function() {
        console.log('Vaciando carrito');
        cartItems = [];
        this.saveCartItems();
        this.updateCounter();
        this.renderCart();
        this.showNotification('Carrito vaciado');
    },

    // Proceder al pago
    checkout: function() {
        if (cartItems.length === 0) {
            alert('Tu carrito está vacío');
            return;
        }
        
        const total = this.getTotal();
        alert('Procediendo al pago por un total de $' + total + '. Esta funcionalidad se implementará próximamente.');
    },

    // Calcular total
    getTotal: function() {
        return cartItems.reduce(function(total, item) {
            return total + (item.price * item.quantity);
        }, 0).toFixed(2);
    },

    // Actualizar contador
    updateCounter: function() {
        const counter = document.getElementById('cart-count');
        const totalItems = cartItems.reduce(function(total, item) {
            return total + item.quantity;
        }, 0);
        
        if (counter) {
            if (totalItems > 0) {
                counter.textContent = totalItems;
                counter.style.display = 'inline';
            } else {
                counter.style.display = 'none';
            }
        }
    },

    // Renderizar carrito
    renderCart: function() {
        const cartBody = document.getElementById('cart-body');
        const cartTotal = document.getElementById('cart-total');
        
        if (cartBody) {
            if (cartItems.length === 0) {
                cartBody.innerHTML = `
                    <div class="empty-cart">
                        <i class="fas fa-shopping-cart" style="font-size: 3rem; opacity: 0.5; margin-bottom: 1rem;"></i>
                        <h4>Tu carrito está vacío</h4>
                        <p>Explora nuestros productos y agrega algunos a tu carrito</p>
                    </div>
                `;
            } else {
                cartBody.innerHTML = cartItems.map(function(item) {
                    return `
                        <div class="cart-item" style="display: flex; align-items: center; padding: 1rem; border-bottom: 1px solid #eee;">
                            <img src="${item.image}" alt="${item.name}" style="width: 60px; height: 60px; object-fit: cover; border-radius: 8px;">
                            <div style="flex: 1; margin-left: 1rem;">
                                <div style="font-weight: 600; color: #333; margin-bottom: 0.5rem;">${item.name}</div>
                                <div style="color: #667eea; font-weight: 500;">$${item.price}</div>
                            </div>
                            <div style="display: flex; align-items: center; gap: 0.5rem;">
                                <span>Cantidad: ${item.quantity}</span>
                                <button onclick="DigitSoftCart.removeItem('${item.id}')" style="background: #e74c3c; color: white; border: none; padding: 0.25rem 0.5rem; border-radius: 4px; cursor: pointer;">
                                    <i class="fas fa-trash"></i>
                                </button>
                            </div>
                        </div>
                    `;
                }).join('');
            }
        }
        
        if (cartTotal) {
            cartTotal.textContent = this.getTotal();
        }
    },

    // Eliminar producto
    removeItem: function(productId) {
        console.log('Eliminando producto:', productId);
        cartItems = cartItems.filter(function(item) {
            return item.id !== productId;
        });
        this.saveCartItems();
        this.updateCounter();
        this.renderCart();
        this.showNotification('Producto eliminado del carrito');
    },

    // Mostrar notificación
    showNotification: function(message) {
        console.log('Notificación:', message);
        
        // Crear notificación temporal
        const notification = document.createElement('div');
        notification.className = 'cart-notification';
        notification.textContent = message;
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: #667eea;
            color: white;
            padding: 1rem 1.5rem;
            border-radius: 8px;
            z-index: 10000;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
            transform: translateX(100%);
            transition: transform 0.3s ease;
        `;
        
        document.body.appendChild(notification);
        
        // Mostrar notificación
        setTimeout(function() {
            notification.style.transform = 'translateX(0)';
        }, 100);
        
        // Ocultar notificación
        setTimeout(function() {
            notification.style.transform = 'translateX(100%)';
            setTimeout(function() {
                if (document.body.contains(notification)) {
                    document.body.removeChild(notification);
                }
            }, 300);
        }, 3000);
    }
};

// Inicializar cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM listo, inicializando carrito...');
    DigitSoftCart.init();
    
    // Hacer disponible globalmente
    window.DigitSoftCart = DigitSoftCart;
    cartInstance = DigitSoftCart;
    
    console.log('DigitSoftCart disponible globalmente');
});

// Hacer disponible inmediatamente también
window.DigitSoftCart = DigitSoftCart;

console.log('Archivo cart.js cargado completamente');