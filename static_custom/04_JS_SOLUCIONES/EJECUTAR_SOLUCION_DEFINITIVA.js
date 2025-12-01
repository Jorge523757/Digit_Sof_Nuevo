// ============================================
// SOLUCIÓN DEFINITIVA - FORZAR IMÁGENES
// Ejecutar en consola (F12)
// ============================================

console.clear();
console.log('%c🔧 SOLUCIÓN DEFINITIVA PARA IMÁGENES', 'color: #4CAF50; font-size: 16px; font-weight: bold;');
console.log('');

// 1. LIMPIAR TODO
console.log('1️⃣ Limpiando localStorage...');
localStorage.removeItem('carrito');
localStorage.removeItem('carrito_v1');
console.log('   ✅ localStorage limpiado\n');

// 2. CREAR FUNCIÓN MEJORADA CON LOGS DETALLADOS
console.log('2️⃣ Creando función mejorada...');

window.agregarAlCarritoConImagen = function(boton) {
    console.log('\n' + '='.repeat(60));
    console.log('🛒 AGREGANDO PRODUCTO AL CARRITO');
    console.log('='.repeat(60));

    // Obtener datos del botón
    const productoId = boton.dataset.productoId;
    const nombre = boton.dataset.nombre;
    const precio = parseFloat(boton.dataset.precio);
    const stock = parseInt(boton.dataset.stock) || 999;
    const categoria = boton.dataset.categoria || 'General';
    let imagen = boton.dataset.imagen;

    console.log('📋 DATOS DEL BOTÓN:');
    console.log('   ID:', productoId);
    console.log('   Nombre:', nombre);
    console.log('   Precio:', precio);
    console.log('   data-imagen:', imagen || '⚠️ VACÍO');

    // BUSCAR IMAGEN EN MÚLTIPLES LUGARES
    if (!imagen || imagen === '' || imagen === 'undefined') {
        console.log('\n🔍 data-imagen vacío, buscando en el DOM...');

        // Buscar la tarjeta del producto
        const card = boton.closest('.product-card-exito') || boton.closest('.product-card');

        if (card) {
            console.log('   ✅ Tarjeta encontrada');

            // Buscar imagen dentro de la tarjeta
            const img = card.querySelector('.product-image-exito img') ||
                       card.querySelector('.product-image img') ||
                       card.querySelector('img');

            if (img && img.src) {
                imagen = img.src;
                console.log('   ✅ Imagen encontrada en DOM:', imagen);
            } else {
                console.log('   ❌ No se encontró <img> en la tarjeta');
            }
        } else {
            console.log('   ❌ No se encontró la tarjeta del producto');
        }
    } else {
        console.log('   ✅ Imagen desde data-imagen:', imagen);
    }

    console.log('\n🖼️ IMAGEN FINAL:', imagen || '❌ NO ENCONTRADA');

    // Si aún no hay imagen, usar placeholder
    if (!imagen || imagen === '') {
        console.log('   ⚠️ Usando placeholder genérico');
        imagen = '/static/images/no-image.png';
    }

    // Obtener carritos actuales
    let carrito = JSON.parse(localStorage.getItem('carrito') || '[]');
    let carritoV1 = JSON.parse(localStorage.getItem('carrito_v1') || '{}');

    console.log('\n📦 CARRITO ACTUAL:', carrito.length, 'items');

    // Buscar si ya existe
    const itemExistente = carrito.find(item => String(item.id) === String(productoId));

    if (itemExistente) {
        console.log('   ℹ️ Producto ya existe, incrementando cantidad');
        itemExistente.cantidad += 1;

        // Actualizar también la imagen por si no la tenía
        if (!itemExistente.imagen || itemExistente.imagen === '') {
            itemExistente.imagen = imagen;
            console.log('   🖼️ Imagen actualizada en item existente');
        }

        // Actualizar carritoV1
        if (carritoV1[productoId]) {
            carritoV1[productoId].cantidad += 1;
            carritoV1[productoId].qty += 1;
            if (!carritoV1[productoId].imagen || carritoV1[productoId].imagen === '') {
                carritoV1[productoId].imagen = imagen;
                carritoV1[productoId].image = imagen;
            }
        }

        console.log('   ✅ Cantidad:', itemExistente.cantidad);
    } else {
        console.log('   ✅ Agregando nuevo producto');

        // Crear objeto con TODAS las propiedades posibles
        const nuevoItem = {
            id: productoId,
            nombre: nombre,
            precio: precio,
            imagen: imagen,  // ← IMAGEN AQUÍ
            stock: stock,
            cantidad: 1,
            categoria: categoria
        };

        carrito.push(nuevoItem);
        console.log('   📦 Item agregado:', nuevoItem);

        // Agregar a carritoV1 con AMBAS propiedades (image e imagen)
        carritoV1[productoId] = {
            id: productoId,
            name: nombre,
            nombre: nombre,
            price: precio,
            precio: precio,
            image: imagen,    // ← IMAGEN AQUÍ
            imagen: imagen,   // ← Y AQUÍ TAMBIÉN
            stock: stock,
            qty: 1,
            cantidad: 1,
            categoria: categoria
        };

        console.log('   📦 Item en carritoV1:', carritoV1[productoId]);
    }

    // Guardar en localStorage
    console.log('\n💾 Guardando en localStorage...');
    localStorage.setItem('carrito', JSON.stringify(carrito));
    localStorage.setItem('carrito_v1', JSON.stringify(carritoV1));
    console.log('   ✅ Guardado exitosamente');

    // Verificar que se guardó correctamente
    const verificacion = JSON.parse(localStorage.getItem('carrito'));
    const ultimoItem = verificacion[verificacion.length - 1];
    console.log('\n✅ VERIFICACIÓN:');
    console.log('   Último item guardado:', ultimoItem);
    console.log('   Tiene imagen:', ultimoItem.imagen ? '✅ SÍ' : '❌ NO');
    console.log('   URL de imagen:', ultimoItem.imagen);

    // Actualizar UI
    console.log('\n🔄 Actualizando interfaz...');
    if (typeof renderCartItems === 'function') {
        renderCartItems();
        console.log('   ✅ Carrito renderizado');
    } else if (window.renderCartItems) {
        window.renderCartItems();
        console.log('   ✅ Carrito renderizado (window)');
    }

    if (typeof updateCartBadge === 'function') {
        updateCartBadge();
    } else if (window.updateCartBadge) {
        window.updateCartBadge();
    }

    // Abrir drawer
    const drawer = document.getElementById('cartDrawer');
    const overlay = document.getElementById('cartOverlay');
    if (drawer) {
        drawer.classList.add('open');
        console.log('   ✅ Drawer abierto');
    }
    if (overlay) {
        overlay.classList.add('show');
    }

    console.log('\n' + '='.repeat(60));
    console.log('✅ PRODUCTO AGREGADO EXITOSAMENTE');
    console.log('='.repeat(60) + '\n');

    return true;
};

console.log('   ✅ Función creada: agregarAlCarritoConImagen()\n');

// 3. RECONFIGURAR BOTONES
console.log('3️⃣ Reconfigurando botones...');

let botonesReconfigurados = 0;

// Todos los posibles selectores de botones
const selectores = [
    '.btn-add-exito',
    '.btn-add-to-cart',
    '.btn-add-cart',
    'button[class*="btn-add"]',
    'button[data-producto-id]'
];

selectores.forEach(selector => {
    const botones = document.querySelectorAll(selector);
    botones.forEach(boton => {
        // Remover listeners anteriores clonando
        const nuevoBoton = boton.cloneNode(true);
        if (boton.parentNode) {
            boton.parentNode.replaceChild(nuevoBoton, boton);
        }

        // Agregar nuevo listener
        nuevoBoton.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            agregarAlCarritoConImagen(this);
        });

        botonesReconfigurados++;
    });
});

console.log('   ✅ Botones reconfigurados:', botonesReconfigurados, '\n');

// 4. INSTRUCCIONES FINALES
console.log('═'.repeat(60));
console.log('%c✨ ¡CONFIGURACIÓN COMPLETADA!', 'color: #4CAF50; font-size: 14px; font-weight: bold;');
console.log('═'.repeat(60));
console.log('');
console.log('📋 AHORA:');
console.log('   1. Haz clic en "Agregar" de CUALQUIER producto');
console.log('   2. Observa los logs detallados aquí en la consola');
console.log('   3. El drawer se abrirá automáticamente');
console.log('   4. LA IMAGEN DEBERÍA APARECER 🎉');
console.log('');
console.log('🔍 DESPUÉS DE AGREGAR, ejecuta esto para verificar:');
console.log('   const c = JSON.parse(localStorage.carrito);');
console.log('   c.forEach(i => console.log("✓", i.nombre, "→", i.imagen));');
console.log('');
console.log('═'.repeat(60));
console.log('');

