// ============================================
// DEBUG FINAL - Copiar y pegar en consola
// ============================================

console.clear();
console.log('%c🔍 DEBUG FINAL - IMÁGENES CARRITO', 'color: #FF6B00; font-size: 20px; font-weight: bold;');
console.log('');

// 1. Ver estructura de los botones
console.log('1️⃣ BOTONES EN LA PÁGINA:');
const botones = document.querySelectorAll('.btn-add-exito, .btn-add-to-cart, .btn-add-cart');
console.log('   Total encontrados:', botones.length);

if (botones.length > 0) {
    const btn = botones[0];
    console.log('\n   Primer botón:');
    console.log('   - Clase:', btn.className);
    console.log('   - data-producto-id:', btn.dataset.productoId);
    console.log('   - data-nombre:', btn.dataset.nombre);
    console.log('   - data-imagen:', btn.dataset.imagen || '⚠️ VACÍO');

    // Buscar imagen en la tarjeta
    const card = btn.closest('.product-card-exito, .product-card');
    if (card) {
        console.log('\n   Tarjeta del producto encontrada');
        const imgs = card.querySelectorAll('img');
        console.log('   - Imágenes en tarjeta:', imgs.length);
        imgs.forEach((img, i) => {
            console.log(`   - Imagen ${i + 1}: ${img.src}`);
        });
    } else {
        console.log('   ⚠️ No se encontró la tarjeta del producto');
    }
} else {
    console.log('   ⚠️ NO SE ENCONTRARON BOTONES');
}

// 2. Ver contenido del localStorage
console.log('\n2️⃣ CONTENIDO DEL LOCALSTORAGE:');

const carritoRaw = localStorage.getItem('carrito');
const carritoV1Raw = localStorage.getItem('carrito_v1');

if (carritoRaw) {
    const carrito = JSON.parse(carritoRaw);
    console.log('   carrito:', carrito.length, 'items');
    carrito.forEach((item, i) => {
        console.log(`\n   Item ${i + 1}:`);
        console.log('   - Nombre:', item.nombre);
        console.log('   - Imagen:', item.imagen || '❌ NO TIENE');
        console.log('   - Keys:', Object.keys(item).join(', '));
    });
}

if (carritoV1Raw) {
    const carritoV1 = JSON.parse(carritoV1Raw);
    console.log('\n   carrito_v1:', Object.keys(carritoV1).length, 'items');
    Object.values(carritoV1).forEach((item, i) => {
        console.log(`\n   Item ${i + 1}:`);
        console.log('   - Nombre:', item.name || item.nombre);
        console.log('   - image:', item.image || '❌ NO TIENE');
        console.log('   - imagen:', item.imagen || '❌ NO TIENE');
        console.log('   - Keys:', Object.keys(item).join(', '));
    });
}

// 3. Ver el drawer HTML
console.log('\n3️⃣ DRAWER DEL CARRITO:');
const drawer = document.getElementById('cartDrawer');
const drawerBody = document.getElementById('cartDrawerBody');

if (drawer) {
    console.log('   Drawer encontrado: ✅');
    console.log('   Está abierto:', drawer.classList.contains('open') ? 'SÍ' : 'NO');
}

if (drawerBody) {
    console.log('   Drawer body encontrado: ✅');
    const items = drawerBody.querySelectorAll('.cart-item-drawer');
    console.log('   Items renderizados:', items.length);

    if (items.length > 0) {
        const item = items[0];
        console.log('\n   Primer item HTML:');
        const imgs = item.querySelectorAll('img');
        console.log('   - <img> tags:', imgs.length);
        imgs.forEach((img, i) => {
            console.log(`   - Imagen ${i + 1}:`);
            console.log('     src:', img.src);
            console.log('     style.display:', img.style.display);
            console.log('     offsetWidth:', img.offsetWidth);
            console.log('     offsetHeight:', img.offsetHeight);
        });

        const noImgIcons = item.querySelectorAll('.no-image-icon');
        console.log('   - Placeholder icons:', noImgIcons.length);
        noImgIcons.forEach((icon, i) => {
            console.log(`   - Icon ${i + 1}:`);
            console.log('     style.display:', icon.style.display);
        });
    }
}

// 4. PROBAR CARGAR IMAGEN MANUALMENTE
console.log('\n4️⃣ PRUEBA DE CARGA DE IMAGEN:');

if (carritoRaw) {
    const carrito = JSON.parse(carritoRaw);
    if (carrito.length > 0 && carrito[0].imagen) {
        const testImg = new Image();
        testImg.onload = function() {
            console.log('   ✅ LA IMAGEN SÍ SE PUEDE CARGAR:', carrito[0].imagen);
        };
        testImg.onerror = function() {
            console.log('   ❌ ERROR AL CARGAR IMAGEN:', carrito[0].imagen);
        };
        testImg.src = carrito[0].imagen;
    } else {
        console.log('   ⚠️ No hay imagen para probar');
    }
}

// 5. RESUMEN
console.log('\n' + '='.repeat(60));
console.log('📊 RESUMEN:');
console.log('='.repeat(60));

const resumen = {
    'Botones encontrados': botones.length > 0 ? '✅' : '❌',
    'Botones tienen data-imagen': botones.length > 0 && botones[0].dataset.imagen ? '✅' : '❌',
    'localStorage tiene datos': carritoRaw || carritoV1Raw ? '✅' : '❌',
    'Items tienen propiedad imagen': false,
    'Drawer existe': drawer ? '✅' : '❌',
    'Items renderizados en drawer': 0
};

if (carritoRaw) {
    const carrito = JSON.parse(carritoRaw);
    resumen['Items tienen propiedad imagen'] = carrito.some(i => i.imagen) ? '✅' : '❌';
}

if (drawerBody) {
    resumen['Items renderizados en drawer'] = drawerBody.querySelectorAll('.cart-item-drawer').length;
}

console.table(resumen);

console.log('\n💡 DIAGNÓSTICO:');

if (botones.length === 0) {
    console.log('   ❌ PROBLEMA: No se encontraron botones de agregar');
    console.log('   📝 SOLUCIÓN: Verifica que la página esté completamente cargada');
}

if (botones.length > 0 && !botones[0].dataset.imagen) {
    console.log('   ⚠️ PROBLEMA: Los botones NO tienen data-imagen');
    console.log('   📝 SOLUCIÓN: El template HTML no está pasando la URL de la imagen');
}

if (carritoRaw) {
    const carrito = JSON.parse(carritoRaw);
    if (carrito.length > 0 && !carrito[0].imagen) {
        console.log('   ❌ PROBLEMA: Los items en localStorage NO tienen imagen');
        console.log('   📝 SOLUCIÓN: Ejecuta el script de corrección para agregar imágenes');
    } else if (carrito.length > 0 && carrito[0].imagen) {
        console.log('   ✅ Los items SÍ tienen imagen en localStorage');
        console.log('   ⚠️ El problema está en la RENDERIZACIÓN del drawer');
        console.log('   📝 SOLUCIÓN: Verifica el código de renderCartItems()');
    }
}

console.log('\n' + '='.repeat(60));
console.log('');

