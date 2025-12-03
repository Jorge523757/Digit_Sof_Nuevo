// 🛒 SISTEMA DE CARRITO COMPLETO - DIGIT SOFT
// Versión: 2.0 - Optimizada y funcional

class DigitSoftCart {
    constructor() {
        this.storageKey = 'digitSoftCart';
        this.notificationKey = 'restockNotifications';
        this.cart = this.loadCart();
        this.init();
    }

    init() {
        console.log('🛒 Iniciando sistema de carrito Digit Soft...');
        this.updateCartCounter();
        this.createFloatingCartButton();
        this.addEventListeners();
        console.log('✅ Sistema de carrito inicializado correctamente');
    }

    // Cargar carrito desde localStorage
    loadCart() {
        try {
            const cartData = localStorage.getItem(this.storageKey);
            if (cartData) {
                return JSON.parse(cartData);
            }
        } catch (error) {
            console.error('Error cargando carrito:', error);
        }
        
        return {
            items: [],
            discount: 0,
            discountCode: '',
            created: new Date().toISOString()
        };
    }

    // Guardar carrito en localStorage
    saveCart() {
        try {
            localStorage.setItem(this.storageKey, JSON.stringify(this.cart));
            console.log('💾 Carrito guardado:', this.cart);
        } catch (error) {
            console.error('Error guardando carrito:', error);
            this.showErrorToast('❌ Error al guardar el carrito');
        }
    }

    // Datos de productos disponibles
    getProductsData() {
        return {
            1: { 
                name: 'Laptop HP Pavilion', 
                price: 850000, 
                image: '/static/productos/imagenes/laptop-hp.svg',
                category: 'Computadores',
                description: 'Laptop HP Pavilion de alto rendimiento para trabajo y gaming',
                stock: 15
            },
            2: { 
                name: 'Mouse Logitech MX Master', 
                price: 45000, 
                image: '/static/productos/imagenes/mouse-logitech.svg',
                category: 'Periféricos',
                description: 'Mouse inalámbrico ergonómico con precisión profesional',
                stock: 25
            },
            3: { 
                name: 'Teclado Mecánico RGB', 
                price: 120000, 
                image: '/static/productos/imagenes/teclado-mecanico.svg',
                category: 'Periféricos',
                description: 'Teclado mecánico con retroiluminación RGB personalizable',
                stock: 18
            },
            4: { 
                name: 'Monitor 24" Full HD', 
                price: 320000, 
                image: '/static/productos/imagenes/monitor-24.svg',
                category: 'Monitores',
                description: 'Monitor profesional de 24 pulgadas con resolución Full HD',
                stock: 12
            },
            5: { 
                name: 'Impresora Epson EcoTank', 
                price: 180000, 
                image: '/static/productos/imagenes/impresora-epson.svg',
                category: 'Impresoras',
                description: 'Impresora multifuncional con sistema de tanque de tinta',
                stock: 8
            }
        };
    }

    // Agregar producto al carrito
    addToCart(productId, quantity = 1) {
        const products = this.getProductsData();
        const product = products[productId];
        
        if (!product) {
            this.showErrorToast('❌ Producto no encontrado');
            return false;
        }

        // Verificar stock disponible
        const availableStock = this.getAvailableStock(productId);
        const existingItem = this.cart.items.find(item => item.id == productId);
        const currentQuantityInCart = existingItem ? existingItem.quantity : 0;
        const newTotalQuantity = currentQuantityInCart + quantity;

        if (newTotalQuantity > availableStock) {
            this.showErrorToast(`❌ Stock insuficiente. Disponible: ${availableStock}, En carrito: ${currentQuantityInCart}`);
            return false;
        }

        if (existingItem) {
            existingItem.quantity = newTotalQuantity;
            this.showSuccessToast(`✅ Cantidad actualizada: ${product.name} (${newTotalQuantity} unidades)`);
        } else {
            this.cart.items.push({
                id: productId,
                name: product.name,
                price: product.price,
                image: product.image,
                quantity: quantity,
                category: product.category,
                description: product.description
            });
            this.showCartSuccessToast(product.name, quantity);
        }

        this.saveCart();
        this.updateCartCounter();
        this.updateProductButtons();
        return true;
    }

    // Obtener stock disponible (simulado)
    getAvailableStock(productId) {
        const products = this.getProductsData();
        return products[productId]?.stock || 0;
    }

    // Remover producto del carrito
    removeFromCart(productId) {
        const itemIndex = this.cart.items.findIndex(item => item.id == productId);
        if (itemIndex > -1) {
            const removedItem = this.cart.items.splice(itemIndex, 1)[0];
            this.saveCart();
            this.updateCartCounter();
            this.showSuccessToast(`🗑️ ${removedItem.name} eliminado del carrito`);
            return true;
        }
        return false;
    }

    // Actualizar cantidad de producto
    updateQuantity(productId, newQuantity) {
        const item = this.cart.items.find(item => item.id == productId);
        if (!item) return false;

        if (newQuantity <= 0) {
            return this.removeFromCart(productId);
        }

        const availableStock = this.getAvailableStock(productId);
        if (newQuantity > availableStock) {
            this.showErrorToast(`❌ Stock máximo: ${availableStock}`);
            return false;
        }

        item.quantity = newQuantity;
        this.saveCart();
        this.updateCartCounter();
        return true;
    }

    // Limpiar carrito
    clearCart() {
        this.cart.items = [];
        this.cart.discount = 0;
        this.cart.discountCode = '';
        this.saveCart();
        this.updateCartCounter();
        this.showSuccessToast('🧹 Carrito vaciado');
    }

    // Aplicar descuento
    applyDiscount(code, percentage) {
        this.cart.discountCode = code;
        this.cart.discount = percentage;
        this.saveCart();
        this.showSuccessToast(`🎉 Descuento aplicado: ${percentage}% (Código: ${code})`);
    }

    // Calcular totales
    calculateTotals() {
        const subtotal = this.cart.items.reduce((sum, item) => sum + (item.price * item.quantity), 0);
        const discountAmount = subtotal * (this.cart.discount / 100);
        const subtotalWithDiscount = subtotal - discountAmount;
        const tax = subtotalWithDiscount * 0.19; // IVA 19%
        const total = subtotalWithDiscount + tax;

        return {
            subtotal,
            discount: this.cart.discount,
            discountAmount,
            subtotalWithDiscount,
            tax,
            total,
            itemCount: this.cart.items.reduce((sum, item) => sum + item.quantity, 0)
        };
    }

    // Actualizar contador del carrito
    updateCartCounter() {
        const totals = this.calculateTotals();
        const counters = document.querySelectorAll('.cart-counter, #cartItemsCount, .cart-badge');
        
        counters.forEach(counter => {
            if (counter) {
                counter.textContent = totals.itemCount;
                counter.style.display = totals.itemCount > 0 ? 'flex' : 'none';
            }
        });

        // Actualizar botón flotante
        this.updateFloatingCartButton(totals.itemCount);
    }

    // Crear botón flotante del carrito
    createFloatingCartButton() {
        let existingButton = document.getElementById('floatingCartButton');
        if (existingButton) {
            existingButton.remove();
        }

        const button = document.createElement('div');
        button.id = 'floatingCartButton';
        button.className = 'floating-cart-button';
        button.innerHTML = `
            <a href="/carrito/" style="color: white; text-decoration: none; display: flex; align-items: center; justify-content: center; width: 100%; height: 100%; position: relative;">
                <i class="fas fa-shopping-cart"></i>
                <span class="cart-badge" id="floatingCartBadge">0</span>
            </a>
        `;

        // Estilos del botón flotante
        button.style.cssText = `
            position: fixed;
            bottom: 80px;
            right: 20px;
            width: 60px;
            height: 60px;
            background: linear-gradient(135deg, #007bff, #0056b3);
            border-radius: 50%;
            box-shadow: 0 4px 15px rgba(0, 123, 255, 0.3);
            z-index: 9999;
            cursor: pointer;
            transition: all 0.3s ease;
            display: none;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
        `;

        document.body.appendChild(button);

        // Efectos hover
        button.addEventListener('mouseenter', () => {
            button.style.transform = 'scale(1.1)';
            button.style.boxShadow = '0 6px 20px rgba(0, 123, 255, 0.4)';
        });

        button.addEventListener('mouseleave', () => {
            button.style.transform = 'scale(1)';
            button.style.boxShadow = '0 4px 15px rgba(0, 123, 255, 0.3)';
        });
    }

    // Actualizar botón flotante
    updateFloatingCartButton(itemCount) {
        const button = document.getElementById('floatingCartButton');
        const badge = document.getElementById('floatingCartBadge');
        
        if (button && badge) {
            badge.textContent = itemCount;
            button.style.display = itemCount > 0 ? 'flex' : 'none';
        }
    }

    // Actualizar botones de productos
    updateProductButtons() {
        // Esta función se ejecutará en la página de productos para actualizar estados
        if (typeof window.updateProductButtonStates === 'function') {
            window.updateProductButtonStates();
        }
    }

    // Agregar event listeners
    addEventListeners() {
        // Escuchar eventos de storage para sincronizar entre pestañas
        window.addEventListener('storage', (e) => {
            if (e.key === this.storageKey) {
                this.cart = this.loadCart();
                this.updateCartCounter();
            }
        });
    }

    // Funciones de notificación
    showSuccessToast(message) {
        this.createToast(message, 'success');
    }

    showErrorToast(message) {
        this.createToast(message, 'error');
    }

    showInfoToast(message) {
        this.createToast(message, 'info');
    }

    showCartSuccessToast(productName, quantity) {
        const toast = document.createElement('div');
        toast.className = 'cart-success-toast';
        toast.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: linear-gradient(135deg, #28a745, #20c997);
            color: white;
            padding: 20px 25px;
            border-radius: 12px;
            z-index: 10000;
            font-weight: 600;
            box-shadow: 0 8px 25px rgba(40, 167, 69, 0.4);
            animation: slideInRight 0.4s ease;
            max-width: 350px;
            cursor: pointer;
            border: 2px solid rgba(255, 255, 255, 0.2);
        `;
        
        toast.innerHTML = `
            <div style="display: flex; align-items: center; gap: 12px;">
                <i class="fas fa-cart-plus" style="font-size: 1.5rem; color: #fff;"></i>
                <div>
                    <div style="font-size: 16px; margin-bottom: 4px;">✅ ${productName}</div>
                    <div style="font-size: 14px; opacity: 0.9;">${quantity} unidad${quantity > 1 ? 'es' : ''} agregada${quantity > 1 ? 's' : ''}</div>
                    <div style="font-size: 12px; margin-top: 5px; opacity: 0.8;">
                        🖱️ Haz clic para ver el carrito
                    </div>
                </div>
            </div>
        `;
        
        toast.onclick = () => {
            window.location.href = '/carrito/';
        };
        
        document.body.appendChild(toast);
        
        setTimeout(() => {
            toast.style.opacity = '0';
            toast.style.transform = 'translateX(100%)';
            setTimeout(() => toast.remove(), 300);
        }, 5000);
    }

    createToast(message, type) {
        const toast = document.createElement('div');
        const colors = {
            success: 'linear-gradient(135deg, #28a745, #20c997)',
            error: 'linear-gradient(135deg, #dc3545, #c82333)',
            info: 'linear-gradient(135deg, #17a2b8, #007bff)',
            warning: 'linear-gradient(135deg, #ffc107, #ff8f00)'
        };
        
        toast.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: ${colors[type] || colors.info};
            color: white;
            padding: 15px 25px;
            border-radius: 10px;
            z-index: 10000;
            font-weight: 600;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
            animation: slideInRight 0.3s ease;
            max-width: 300px;
        `;
        toast.innerHTML = message;
        document.body.appendChild(toast);
        
        setTimeout(() => {
            toast.style.opacity = '0';
            toast.style.transform = 'translateX(100%)';
            setTimeout(() => toast.remove(), 300);
        }, 4000);
    }

    // Códigos de descuento predefinidos
    getDiscountCodes() {
        return {
            'DIGIT10': { percentage: 10, description: 'Descuento del 10%' },
            'SOFT15': { percentage: 15, description: 'Descuento del 15%' },
            'PROMO20': { percentage: 20, description: 'Descuento del 20%' },
            'VIP25': { percentage: 25, description: 'Descuento VIP del 25%' },
            'NUEVO50': { percentage: 50, description: 'Descuento especial nuevos clientes' }
        };
    }

    // Validar código de descuento
    validateDiscountCode(code) {
        const codes = this.getDiscountCodes();
        return codes[code.toUpperCase()] || null;
    }

    // Función para notificación de restock
    notifyRestock(productId) {
        const products = this.getProductsData();
        const product = products[productId];
        
        if (!product) return false;

        let notifications = [];
        try {
            notifications = JSON.parse(localStorage.getItem(this.notificationKey) || '[]');
        } catch (error) {
            console.error('Error cargando notificaciones:', error);
        }
        
        if (!notifications.includes(productId)) {
            notifications.push(productId);
            localStorage.setItem(this.notificationKey, JSON.stringify(notifications));
            this.showSuccessToast(`🔔 Te notificaremos cuando ${product.name} esté disponible`);
            return true;
        } else {
            this.showInfoToast(`ℹ️ Ya estás suscrito a notificaciones de ${product.name}`);
            return false;
        }
    }

    // Obtener estadísticas del carrito
    getCartStats() {
        const totals = this.calculateTotals();
        return {
            totalItems: this.cart.items.length,
            totalQuantity: totals.itemCount,
            subtotal: totals.subtotal,
            total: totals.total,
            discount: totals.discount,
            isEmpty: this.cart.items.length === 0
        };
    }

    // Exportar carrito (para respaldo)
    exportCart() {
        const cartData = {
            ...this.cart,
            exported: new Date().toISOString(),
            version: '2.0'
        };
        
        const dataStr = JSON.stringify(cartData, null, 2);
        const dataUri = 'data:application/json;charset=utf-8,'+ encodeURIComponent(dataStr);
        
        const exportFileDefaultName = `carrito_digitsoft_${new Date().getFullYear()}_${(new Date().getMonth()+1).toString().padStart(2,'0')}_${new Date().getDate().toString().padStart(2,'0')}.json`;
        
        const linkElement = document.createElement('a');
        linkElement.setAttribute('href', dataUri);
        linkElement.setAttribute('download', exportFileDefaultName);
        linkElement.click();
        
        this.showSuccessToast('💾 Carrito exportado exitosamente');
    }
}

// CSS Animations
const cartAnimations = `
    @keyframes slideInRight {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    .cart-badge {
        position: absolute;
        top: -8px;
        right: -8px;
        background: #dc3545;
        color: white;
        border-radius: 50%;
        width: 24px;
        height: 24px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.8rem;
        font-weight: 600;
        border: 2px solid white;
    }
    
    .floating-cart-button {
        animation: bounce 2s infinite;
    }
    
    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% {
            transform: translateY(0);
        }
        40% {
            transform: translateY(-10px);
        }
        60% {
            transform: translateY(-5px);
        }
    }
`;

// Agregar estilos al documento
if (!document.getElementById('cartSystemStyles')) {
    const style = document.createElement('style');
    style.id = 'cartSystemStyles';
    style.textContent = cartAnimations;
    document.head.appendChild(style);
}

// Inicializar sistema de carrito globalmente
window.digitSoftCart = new DigitSoftCart();

// Funciones globales para compatibilidad con HTML existente
window.addProductToCart = function(productId) {
    const quantityInput = document.getElementById(`qty-${productId}`);
    const quantity = quantityInput ? parseInt(quantityInput.value) || 1 : 1;
    
    if (window.digitSoftCart.addToCart(productId, quantity)) {
        // Resetear cantidad si se agregó exitosamente
        if (quantityInput) {
            quantityInput.value = 1;
        }
    }
};

window.quickAddToCart = function(productId, quantity) {
    window.digitSoftCart.addToCart(productId, quantity);
};

window.notifyRestock = function(productId) {
    window.digitSoftCart.notifyRestock(productId);
};

// Log de inicialización
console.log('🚀 Sistema de carrito Digit Soft cargado completamente');
console.log('📦 Carrito actual:', window.digitSoftCart.cart);