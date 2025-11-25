/**
 * DIGIT SOFT - E-commerce JavaScript
 * Funciones para el carrito de compras
 */

console.log('🛒 Carrito JS cargado');

// ========================================
// FUNCIONES DE UTILIDAD
// ========================================

/**
 * Obtener cookie CSRF
 */
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

/**
 * Mostrar notificación
 */
function showNotification(message, type = 'success') {
    // Remover notificaciones anteriores
    const existingNotifications = document.querySelectorAll('.custom-notification');
    existingNotifications.forEach(notif => notif.remove());

    // Configuración según tipo
    let icon, bgColor;
    if (type === 'success') {
        icon = 'fa-check-circle';
        bgColor = '#28a745';
    } else if (type === 'warning') {
        icon = 'fa-exclamation-triangle';
        bgColor = '#ffc107';
    } else {
        icon = 'fa-exclamation-circle';
        bgColor = '#dc3545';
    }

    // Crear notificación
    const notification = document.createElement('div');
    notification.className = 'custom-notification';
    notification.style.cssText = `
        position: fixed;
        top: 70px;
        left: 50%;
        transform: translateX(-50%);
        z-index: 10000;
        min-width: 350px;
        max-width: 550px;
        background: white;
        border-left: 5px solid ${bgColor};
        border-radius: 10px;
        box-shadow: 0 5px 25px rgba(0,0,0,0.25);
        animation: slideDown 0.4s ease-out;
    `;

    notification.innerHTML = `
        <div style="display: flex; align-items: start; padding: 1rem;">
            <i class="fas ${icon}" style="color: ${bgColor}; font-size: 2rem; margin-right: 1rem; margin-top: 2px; flex-shrink: 0;"></i>
            <div style="flex-grow: 1; color: #333; font-size: 0.95rem; line-height: 1.6;">
                ${message}
            </div>
            <button onclick="this.parentElement.parentElement.remove()" style="background: none; border: none; font-size: 1.5rem; color: #999; cursor: pointer; padding: 0; margin-left: 1rem; flex-shrink: 0;">&times;</button>
        </div>
    `;

    // Agregar estilos de animación si no existen
    if (!document.getElementById('notification-styles')) {
        const style = document.createElement('style');
        style.id = 'notification-styles';
        style.textContent = `
            @keyframes slideDown {
                from { transform: translateX(-50%) translateY(-100px); opacity: 0; }
                to { transform: translateX(-50%) translateY(0); opacity: 1; }
            }
            @keyframes slideUp {
                from { transform: translateX(-50%) translateY(0); opacity: 1; }
                to { transform: translateX(-50%) translateY(-100px); opacity: 0; }
            }
        `;
        document.head.appendChild(style);
    }

    document.body.appendChild(notification);

    // Auto eliminar después de 6 segundos
    setTimeout(() => {
        if (notification.parentElement) {
            notification.style.animation = 'slideUp 0.4s ease-out forwards';
            setTimeout(() => notification.remove(), 400);
        }
    }, 6000);
}

// ========================================
// FUNCIONES DEL CARRITO
// ========================================

/**
 * Actualizar contador del carrito
 */
function updateCartCounter() {
    const carrito = JSON.parse(localStorage.getItem('carrito') || '{}');
    const totalItems = Object.values(carrito).reduce((sum, item) => sum + (item.cantidad || 0), 0);

    console.log('📊 Total items en carrito:', totalItems);

    // Actualizar contador del header
    const headerCounter = document.getElementById('cart-counter-header');
    if (headerCounter) {
        if (totalItems > 0) {
            headerCounter.textContent = totalItems;
            headerCounter.style.display = 'inline-block';
        } else {
            headerCounter.style.display = 'none';
        }
    }

    // Actualizar otros contadores
    const badges = document.querySelectorAll('#carrito-count, .cart-badge');
    badges.forEach(badge => {
        badge.textContent = totalItems;
    });
}

/**
 * Agregar producto al carrito
 */
async function addToCart(productoId) {
    console.log('=== AGREGAR AL CARRITO ===');
    console.log('Producto ID:', productoId);

    const button = event.target.closest('button');
    if (!button) {
        console.error('❌ No se encontró el botón');
        return;
    }

    const originalText = button.innerHTML;

    // Mostrar loading
    button.innerHTML = '<i class="fas fa-spinner fa-spin me-1"></i>Agregando...';
    button.disabled = true;

    const url = '/tienda/carrito/agregar/';
    const csrfToken = getCookie('csrftoken');

    console.log('📍 URL:', url);
    console.log('🔑 CSRF Token:', csrfToken ? 'Presente ✅' : 'FALTA ❌');

    if (!csrfToken) {
        showNotification('❌ Error de seguridad. Por favor recarga la página.', 'error');
        button.innerHTML = originalText;
        button.disabled = false;
        return;
    }

    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify({
                producto_id: productoId,
                cantidad: 1
            })
        });

        console.log('📥 Response status:', response.status);

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        console.log('📦 Response data:', data);

        if (data.success) {
            // Sincronizar con localStorage
            const carrito = JSON.parse(localStorage.getItem('carrito') || '{}');
            const card = button.closest('.card');
            const productoNombre = card.querySelector('.card-title a')?.textContent?.trim() || 'Producto';
            const precioText = card.querySelector('.price-sale')?.textContent?.replace(/[$,]/g, '') || '0';
            const precio = parseFloat(precioText);

            carrito[productoId] = {
                cantidad: (carrito[productoId]?.cantidad || 0) + 1,
                nombre: productoNombre,
                precio: precio
            };

            localStorage.setItem('carrito', JSON.stringify(carrito));
            console.log('💾 Carrito actualizado en localStorage:', carrito);

            // Actualizar contador
            updateCartCounter();

            // Mostrar éxito en el botón
            button.innerHTML = '<i class="fas fa-check me-1"></i>¡Agregado!';
            button.classList.remove('btn-add-cart');
            button.classList.add('btn-success');

            // Volver al estado original después de 2 segundos
            setTimeout(() => {
                button.innerHTML = originalText;
                button.classList.remove('btn-success');
                button.classList.add('btn-add-cart');
                button.disabled = false;
            }, 2000);

            // Mostrar notificación
            showNotification(data.message || '✅ Producto agregado al carrito', 'success');

        } else {
            console.error('❌ Error del servidor:', data.error);
            button.innerHTML = originalText;
            button.disabled = false;

            // Mostrar error
            if (data.max_reached) {
                showNotification(data.error || 'Stock máximo alcanzado', 'warning');
            } else {
                showNotification(data.error || 'Error al agregar al carrito', 'error');
            }

            // Redirigir si es necesario
            if (data.redirect) {
                setTimeout(() => {
                    window.location.href = data.redirect;
                }, 2000);
            }
        }
    } catch (error) {
        console.error('❌ Error catch:', error);
        button.innerHTML = originalText;
        button.disabled = false;
        showNotification('❌ Error al agregar al carrito: ' + error.message, 'error');
    }
}

// ========================================
// INICIALIZACIÓN
// ========================================

document.addEventListener('DOMContentLoaded', function() {
    console.log('✅ DOM cargado - Inicializando carrito');

    // Cargar contador inicial
    updateCartCounter();

    // Escuchar cambios en localStorage desde otras pestañas
    window.addEventListener('storage', function(e) {
        if (e.key === 'carrito') {
            console.log('🔄 Carrito actualizado desde otra pestaña');
            updateCartCounter();
        }
    });

    // Actualizar contador cada 5 segundos
    setInterval(updateCartCounter, 5000);

    console.log('🚀 Carrito inicializado correctamente');
});

