// ========================================
// SCRIPT DE DIAGNÓSTICO DEL CARRITO
// ========================================
// Copia y pega este script en la consola del navegador (F12)

console.log('%c📋 DIAGNÓSTICO DEL CARRITO', 'font-size: 20px; font-weight: bold; color: #FF6B00');
console.log('==========================================\n');

// 1. Verificar localStorage
console.log('%c1️⃣ VERIFICANDO LOCALSTORAGE...', 'font-size: 14px; font-weight: bold; color: #1e40af');
const carrito = JSON.parse(localStorage.getItem('carrito_v1') || '{}');
const items = Object.values(carrito);
console.log(`   ✅ Items en carrito: ${items.length}`);

if (items.length > 0) {
    console.log('\n%c📦 ITEMS EN CARRITO:', 'font-weight: bold; color: #16a34a');
    items.forEach((item, index) => {
        console.log(`\n   Item ${index + 1}:`);
        console.log(`   - ID: ${item.id}`);
        console.log(`   - Nombre: ${item.nombre || item.name}`);
        console.log(`   - Precio: $${item.precio || item.price}`);
        console.log(`   - Cantidad: ${item.cantidad || item.qty}`);
        console.log(`   - Imagen: ${item.imagen || item.image || '❌ NO TIENE'}`);

        if (item.imagen || item.image) {
            console.log(`   - URL válida: ✅`);
        } else {
            console.log(`   - URL válida: ❌ FALTA IMAGEN`);
        }
    });
} else {
    console.log('   ⚠️ El carrito está vacío');
}

// 2. Verificar productos en la página
console.log('\n%c2️⃣ VERIFICANDO PRODUCTOS EN LA PÁGINA...', 'font-size: 14px; font-weight: bold; color: #1e40af');
const productos = document.querySelectorAll('.product-card-exito');
console.log(`   ✅ Productos encontrados: ${productos.length}`);

let productosConImagen = 0;
let productosSinImagen = 0;

productos.forEach(card => {
    const img = card.querySelector('.product-image-exito img');
    if (img && img.src) {
        productosConImagen++;
    } else {
        productosSinImagen++;
    }
});

console.log(`   ✅ Con imagen: ${productosConImagen}`);
console.log(`   ❌ Sin imagen: ${productosSinImagen}`);

// 3. Verificar botones
console.log('\n%c3️⃣ VERIFICANDO BOTONES DE AGREGAR...', 'font-size: 14px; font-weight: bold; color: #1e40af');
const botones = document.querySelectorAll('.btn-add-exito, .btn-add-to-cart');
console.log(`   ✅ Botones encontrados: ${botones.length}`);

let botonesConDataImagen = 0;
let botonesSinDataImagen = 0;

botones.forEach(btn => {
    if (btn.dataset.imagen && btn.dataset.imagen !== '') {
        botonesConDataImagen++;
    } else {
        botonesSinDataImagen++;
    }
});

console.log(`   ✅ Con data-imagen: ${botonesConDataImagen}`);
console.log(`   ⚠️ Sin data-imagen: ${botonesSinDataImagen}`);

// 4. Verificar funciones
console.log('\n%c4️⃣ VERIFICANDO FUNCIONES...', 'font-size: 14px; font-weight: bold; color: #1e40af');
console.log(`   renderCartItems: ${typeof window.renderCartItems === 'function' ? '✅' : '❌'}`);
console.log(`   updateCartBadge: ${typeof window.updateCartBadge === 'function' ? '✅' : '❌'}`);
console.log(`   attachCartButtonEvents: ${typeof window.attachCartButtonEvents === 'function' ? '✅' : '❌'}`);

// 5. Probar renderizado
console.log('\n%c5️⃣ PROBANDO RENDERIZADO...', 'font-size: 14px; font-weight: bold; color: #1e40af');
if (typeof window.renderCartItems === 'function') {
    window.renderCartItems();
    console.log('   ✅ Carrito renderizado correctamente');
} else {
    console.log('   ❌ Función renderCartItems no encontrada');
}

// 6. Verificar drawer
console.log('\n%c6️⃣ VERIFICANDO DRAWER DEL CARRITO...', 'font-size: 14px; font-weight: bold; color: #1e40af');
const drawer = document.getElementById('cartDrawer');
const drawerBody = document.getElementById('cartDrawerBody');
console.log(`   Drawer: ${drawer ? '✅' : '❌'}`);
console.log(`   Drawer Body: ${drawerBody ? '✅' : '❌'}`);

// 7. Resumen
console.log('\n%c📊 RESUMEN', 'font-size: 16px; font-weight: bold; color: #dc2626');
console.log('==========================================');

if (items.length === 0) {
    console.log('%c⚠️ El carrito está vacío. Agrega productos para probar.', 'color: #f59e0b');
} else {
    const itemsConImagen = items.filter(item => item.imagen || item.image);
    const itemsSinImagen = items.filter(item => !(item.imagen || item.image));

    if (itemsSinImagen.length === 0) {
        console.log('%c✅ TODO ESTÁ PERFECTO!', 'color: #16a34a; font-weight: bold; font-size: 14px');
        console.log('   Todos los items tienen imagen');
    } else {
        console.log('%c⚠️ PROBLEMAS DETECTADOS', 'color: #dc2626; font-weight: bold; font-size: 14px');
        console.log(`   ${itemsSinImagen.length} items sin imagen`);
        console.log('\n   Items problemáticos:');
        itemsSinImagen.forEach(item => {
            console.log(`   - ID ${item.id}: ${item.nombre || item.name}`);
        });

        console.log('\n%c🔧 SOLUCIÓN:', 'color: #1e40af; font-weight: bold');
        console.log('   1. Elimina el carrito: localStorage.removeItem("carrito_v1")');
        console.log('   2. Recarga la página');
        console.log('   3. Agrega los productos de nuevo');
    }
}

console.log('\n%c==========================================', 'color: #6b7280');

// Función de ayuda para limpiar carrito
console.log('\n%c💡 COMANDOS ÚTILES:', 'font-size: 14px; font-weight: bold; color: #7c3aed');
console.log('   Para limpiar el carrito:');
console.log('   > localStorage.removeItem("carrito_v1")');
console.log('\n   Para ver el carrito:');
console.log('   > JSON.parse(localStorage.getItem("carrito_v1"))');
console.log('\n   Para renderizar de nuevo:');
console.log('   > window.renderCartItems()');
console.log('\n==========================================\n');

