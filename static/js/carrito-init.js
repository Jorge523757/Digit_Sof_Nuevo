// Inicializador del Carrito - DigitSoft
// Este script asegura que el carrito funcione correctamente

console.log('🔄 Cargando inicializador del carrito...');

// Función principal de inicialización
function inicializarCarrito() {
    console.log('🎯 Ejecutando inicializador del carrito...');

    // Esperar a que el objeto carrito esté disponible
    if (typeof carrito === 'undefined' || !carrito) {
        console.log('⏳ Esperando que el carrito esté disponible...');
        return false;
    }

    console.log('✅ Carrito disponible!');

    // Conectar botón del header
    const cartBtn = document.getElementById('cartBtn');
    const cartBadge = document.getElementById('cartBadge');

    if (cartBtn) {
        console.log('✅ Botón del carrito encontrado');

        // Remover eventos anteriores
        const nuevoBtn = cartBtn.cloneNode(true);
        cartBtn.parentNode.replaceChild(nuevoBtn, cartBtn);

        // Agregar evento
        nuevoBtn.addEventListener('click', function(e) {
            e.preventDefault();
            console.log('🛒 Click en botón del carrito');
            carrito.mostrarCarrito();
        });
    }

    // Función para actualizar badge
    function actualizarBadge() {
        if (cartBadge && carrito) {
            const cantidad = carrito.getCantidadTotal();
            cartBadge.textContent = cantidad;
            cartBadge.style.display = cantidad > 0 ? 'flex' : 'none';
        }
    }

    // Actualizar badge periódicamente
    setInterval(actualizarBadge, 500);
    actualizarBadge();

    // Conectar botones de productos
    conectarBotonesProductos();

    // Reconectar cada 2 segundos por si cargan más productos
    setInterval(conectarBotonesProductos, 2000);

    return true;
}

// Función para conectar botones de productos
function conectarBotonesProductos() {
    if (typeof carrito === 'undefined' || !carrito) {
        return;
    }

    // Buscar todos los botones de carrito
    const botones = document.querySelectorAll('button[class*="cart"], a[class*="cart"], [onclick*="carrito"]');

    botones.forEach((boton, index) => {
        // Verificar si ya tiene el evento
        if (boton.dataset.carritoConectado) {
            return;
        }

        // Marcar como conectado
        boton.dataset.carritoConectado = 'true';

        // Agregar evento
        boton.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();

            console.log(`🛒 Click en botón de producto`);

            // Obtener datos del producto
            const card = this.closest('[class*="card"]') || this.closest('[class*="product"]');

            if (!card) {
                console.warn('⚠️ No se encontró tarjeta de producto');
                return;
            }

            // Extraer información
            const nombre = card.querySelector('h3, h4, [class*="title"], [class*="nombre"]')?.textContent?.trim() || 'Producto';

            const precioElement = card.querySelector('[class*="price"], [class*="precio"]');
            let precio = 0;
            if (precioElement) {
                const precioTexto = precioElement.textContent.replace(/[^0-9.]/g, '');
                precio = parseFloat(precioTexto) || 0;
            }

            const stockElement = card.querySelector('[class*="stock"], [class*="disponible"]');
            let stock = 10;
            if (stockElement) {
                const stockTexto = stockElement.textContent.match(/\d+/);
                stock = stockTexto ? parseInt(stockTexto[0]) : 10;
            }

            const categoria = card.querySelector('[class*="category"], [class*="categoria"]')?.textContent?.trim() || 'General';

            if (precio === 0) {
                console.error('❌ No se pudo obtener el precio del producto');
                alert('Error: No se pudo obtener el precio del producto');
                return;
            }

            // Crear objeto producto
            const producto = {
                id: 'prod-' + Date.now() + '-' + Math.random().toString(36).substr(2, 9),
                nombre: nombre,
                precio: precio,
                stock: stock,
                categoria: categoria,
                cantidad: 1
            };

            console.log('📦 Producto a agregar:', producto);

            // Agregar al carrito
            try {
                carrito.agregar(producto);
                console.log('✅ Producto agregado exitosamente');
            } catch (error) {
                console.error('❌ Error al agregar producto:', error);
                alert('Error al agregar el producto al carrito');
            }
        });
    });

    if (botones.length > 0) {
        console.log(`✅ ${botones.length} botones de carrito conectados`);
    }
}

// Intentar inicializar cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', function() {
    console.log('📄 DOM listo');

    // Intentar inicializar cada 200ms hasta que funcione
    let intentos = 0;
    const maxIntentos = 25; // 5 segundos máximo

    const intervalo = setInterval(function() {
        intentos++;

        if (inicializarCarrito()) {
            console.log('✅ Carrito inicializado exitosamente');
            clearInterval(intervalo);
        } else if (intentos >= maxIntentos) {
            console.error('❌ No se pudo inicializar el carrito después de ' + (maxIntentos * 200) + 'ms');
            clearInterval(intervalo);
        } else {
            console.log(`⏳ Intento ${intentos}/${maxIntentos}...`);
        }
    }, 200);
});

// También intentar cuando la ventana termine de cargar
window.addEventListener('load', function() {
    console.log('🌐 Ventana cargada completamente');
    setTimeout(inicializarCarrito, 500);
});

console.log('✅ Inicializador del carrito cargado');

