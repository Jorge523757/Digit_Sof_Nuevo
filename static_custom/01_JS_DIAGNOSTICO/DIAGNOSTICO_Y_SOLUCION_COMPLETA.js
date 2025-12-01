// ========================================
// DIAGNÓSTICO COMPLETO Y CORRECCIÓN AUTOMÁTICA
// Ejecutar en la consola del navegador (F12)
// ========================================

console.log('🔍 INICIANDO DIAGNÓSTICO COMPLETO...\n');

// 1. Ver todos los botones de agregar
console.log('📋 PASO 1: Verificando botones de agregar al carrito...');
const botones = document.querySelectorAll('.btn-add-cart, .btn-add-to-cart, .btn-add-exito');
console.log('   Botones encontrados:', botones.length);

if (botones.length > 0) {
    const primerBoton = botones[0];
    console.log('\n   Atributos del primer botón:');
    console.log('   - data-producto-id:', primerBoton.dataset.productoId);
    console.log('   - data-nombre:', primerBoton.dataset.nombre);
    console.log('   - data-precio:', primerBoton.dataset.precio);
    console.log('   - data-imagen:', primerBoton.dataset.imagen);
    console.log('   - data-stock:', primerBoton.dataset.stock);
    console.log('   - data-categoria:', primerBoton.dataset.categoria);

    if (!primerBoton.dataset.imagen || primerBoton.dataset.imagen === '') {
        console.warn('   ⚠️ El botón NO tiene data-imagen definido!');
        console.log('   ℹ️ Esto significa que el template HTML no está configurado correctamente');
    } else {
        console.log('   ✅ El botón TIENE data-imagen:', primerBoton.dataset.imagen);
    }
}

// 2. Ver el contenido actual del localStorage
console.log('\n📦 PASO 2: Verificando localStorage...');

const carritoRaw = localStorage.getItem('carrito');
const carritoV1Raw = localStorage.getItem('carrito_v1');

if (carritoRaw) {
    const carrito = JSON.parse(carritoRaw);
    console.log('   carrito (array):', carrito.length, 'items');
    carrito.forEach((item, i) => {
        console.log(`\n   Item ${i + 1}:`);
        console.log('   - ID:', item.id);
        console.log('   - Nombre:', item.nombre);
        console.log('   - Precio:', item.precio);
        console.log('   - Imagen:', item.imagen || '❌ NO DEFINIDA');
        console.log('   - Cantidad:', item.cantidad);
    });
} else {
    console.log('   ⚠️ No hay datos en localStorage.carrito');
}

if (carritoV1Raw) {
    const carritoV1 = JSON.parse(carritoV1Raw);
    console.log('\n   carrito_v1 (objeto):', Object.keys(carritoV1).length, 'items');
    Object.values(carritoV1).forEach((item, i) => {
        console.log(`\n   Item ${i + 1}:`);
        console.log('   - ID:', item.id);
        console.log('   - Nombre:', item.name || item.nombre);
        console.log('   - Precio:', item.price || item.precio);
        console.log('   - Imagen:', item.image || item.imagen || '❌ NO DEFINIDA');
        console.log('   - Cantidad:', item.qty || item.cantidad);
    });
} else {
    console.log('   ⚠️ No hay datos en localStorage.carrito_v1');
}

// 3. Buscar imágenes en la página
console.log('\n🖼️ PASO 3: Buscando imágenes de productos en la página...');
const imagenesProductos = document.querySelectorAll('.product-image-exito img, .product-card img');
console.log('   Imágenes de productos encontradas:', imagenesProductos.length);

if (imagenesProductos.length > 0) {
    const primeraImagen = imagenesProductos[0];
    console.log('   Primera imagen src:', primeraImagen.src);
    console.log('   ✅ Las imágenes SÍ existen en la página');
}

// 4. SOLUCIÓN AUTOMÁTICA
console.log('\n\n🔧 PASO 4: APLICANDO SOLUCIÓN AUTOMÁTICA...\n');

// Limpiar localStorage
console.log('   🧹 Limpiando localStorage...');
localStorage.removeItem('carrito');
localStorage.removeItem('carrito_v1');
console.log('   ✅ localStorage limpiado');

// Crear una función mejorada para agregar al carrito
console.log('\n   📝 Creando función mejorada de agregar al carrito...');

window.agregarAlCarritoMejorado = function(boton) {
    console.log('\n🛒 [MEJORADO] Agregando producto al carrito...');

    // Obtener datos del botón
    const productoId = boton.dataset.productoId;
    const nombre = boton.dataset.nombre;
    const precio = parseFloat(boton.dataset.precio);
    const stock = parseInt(boton.dataset.stock);
    const categoria = boton.dataset.categoria;
    let imagen = boton.dataset.imagen;

    // Si no hay imagen en data-imagen, buscar la imagen del producto
    if (!imagen || imagen === '') {
        console.log('   ⚠️ No hay data-imagen, buscando en el DOM...');
        const card = boton.closest('.product-card-exito, .product-card');
        if (card) {
            const img = card.querySelector('img');
            if (img) {
                imagen = img.src;
                console.log('   ✅ Imagen encontrada en el DOM:', imagen);
            }
        }
    } else {
        console.log('   ✅ Imagen desde data-imagen:', imagen);
    }

    console.log('\n   📦 Datos del producto:');
    console.log('   - ID:', productoId);
    console.log('   - Nombre:', nombre);
    console.log('   - Precio:', precio);
    console.log('   - Imagen:', imagen);
    console.log('   - Stock:', stock);

    // Obtener o crear carrito
    let carrito = JSON.parse(localStorage.getItem('carrito') || '[]');
    let carritoV1 = JSON.parse(localStorage.getItem('carrito_v1') || '{}');

    // Buscar si ya existe
    const itemExistente = carrito.find(item => item.id == productoId);

    if (itemExistente) {
        console.log('   ℹ️ Producto ya existe, incrementando cantidad');
        itemExistente.cantidad += 1;

        // Actualizar también en carritoV1
        if (carritoV1[productoId]) {
            carritoV1[productoId].cantidad += 1;
            carritoV1[productoId].qty += 1;
        }
    } else {
        console.log('   ✅ Agregando nuevo producto');

        // Agregar a carrito
        carrito.push({
            id: productoId,
            nombre: nombre,
            precio: precio,
            imagen: imagen,
            stock: stock,
            cantidad: 1,
            categoria: categoria || 'General'
        });

        // Agregar a carritoV1
        carritoV1[productoId] = {
            id: productoId,
            name: nombre,
            nombre: nombre,
            price: precio,
            precio: precio,
            image: imagen,
            imagen: imagen,
            stock: stock,
            qty: 1,
            cantidad: 1,
            categoria: categoria || 'General'
        };
    }

    // Guardar
    localStorage.setItem('carrito', JSON.stringify(carrito));
    localStorage.setItem('carrito_v1', JSON.stringify(carritoV1));

    console.log('   ✅ Producto agregado al carrito!');
    console.log('   📊 Total items:', carrito.length);

    // Actualizar badge y abrir drawer si existe
    if (typeof updateCartBadge === 'function') {
        updateCartBadge();
    }
    if (typeof renderCartItems === 'function') {
        renderCartItems();
    }
    if (typeof openCartDrawer === 'function') {
        openCartDrawer();
    }

    // Mostrar notificación
    alert('✅ ' + nombre + ' agregado al carrito');

    return true;
};

console.log('   ✅ Función mejorada creada: agregarAlCarritoMejorado()');

// 5. Reconfigurar botones
console.log('\n   🔗 Reconfigurando botones...');

let botonesConfigurados = 0;
botones.forEach(boton => {
    // Remover listeners anteriores clonando el botón
    const nuevoBoton = boton.cloneNode(true);
    boton.parentNode.replaceChild(nuevoBoton, boton);

    // Agregar nuevo listener
    nuevoBoton.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        agregarAlCarritoMejorado(this);
    });

    botonesConfigurados++;
});

console.log('   ✅ Botones reconfigurados:', botonesConfigurados);

// 6. Instrucciones finales
console.log('\n\n' + '='.repeat(60));
console.log('✨ DIAGNÓSTICO Y CORRECCIÓN COMPLETADOS');
console.log('='.repeat(60));
console.log('\n📋 INSTRUCCIONES:');
console.log('   1. Haz clic en "Agregar" de cualquier producto');
console.log('   2. Se abrirá una alerta de confirmación');
console.log('   3. Abre el carrito');
console.log('   4. Las imágenes deberían aparecer');
console.log('\n💡 Si aún no aparecen:');
console.log('   - El problema está en el template HTML');
console.log('   - Los botones no tienen data-imagen definido');
console.log('   - Pero la función mejorada busca la imagen en el DOM');
console.log('\n🔍 Para verificar después de agregar:');
console.log('   const c = JSON.parse(localStorage.getItem("carrito"));');
console.log('   c.forEach(i => console.log(i.nombre, "→", i.imagen));');
console.log('\n' + '='.repeat(60) + '\n');

