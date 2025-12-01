// ===============================================
// SCRIPT PARA LIMPIAR Y PROBAR EL CARRITO
// ===============================================
// Copia y pega este código en la consola del navegador (F12)

console.log('%c🧹 LIMPIEZA Y PRUEBA DEL CARRITO', 'font-size: 20px; font-weight: bold; color: #FF6B00; background: #000; padding: 10px;');
console.log('=========================================\n');

// 1. LIMPIAR CARRITO
console.log('%c1️⃣ Limpiando carrito anterior...', 'font-size: 14px; font-weight: bold; color: #dc2626');
localStorage.removeItem('carrito_v1');
localStorage.removeItem('cart');
localStorage.removeItem('carrito');
console.log('   ✅ Carrito limpiado\n');

// 2. VERIFICAR PRODUCTOS EN LA PÁGINA
console.log('%c2️⃣ Verificando productos...', 'font-size: 14px; font-weight: bold; color: #1e40af');
const productos = document.querySelectorAll('.product-card-exito');
console.log(`   ✅ ${productos.length} productos encontrados\n`);

// 3. VERIFICAR BOTONES Y SUS IMÁGENES
console.log('%c3️⃣ Verificando data-imagen en botones...', 'font-size: 14px; font-weight: bold; color: #1e40af');
const botones = document.querySelectorAll('.btn-add-exito, .btn-add-to-cart');
let conImagen = 0;
let sinImagen = 0;

botones.forEach((btn, index) => {
    const imagen = btn.getAttribute('data-imagen') || btn.dataset.imagen || '';
    const productoId = btn.dataset.productoId || btn.dataset.id;
    const nombre = btn.dataset.nombre || btn.dataset.name || '';

    if (imagen && imagen.trim() !== '') {
        conImagen++;
        if (index < 3) {  // Mostrar solo los primeros 3
            console.log(`   ✅ Botón ${index + 1} (ID: ${productoId}):`, {
                nombre: nombre.substring(0, 30) + '...',
                imagen: imagen
            });
        }
    } else {
        sinImagen++;
        console.log(`   ❌ Botón ${index + 1} (ID: ${productoId}): SIN IMAGEN`);
    }
});

console.log(`\n   Resumen: ${conImagen} con imagen, ${sinImagen} sin imagen\n`);

// 4. SIMULAR AGREGAR UN PRODUCTO
console.log('%c4️⃣ Simulando agregar producto...', 'font-size: 14px; font-weight: bold; color: #16a34a');

if (botones.length > 0) {
    const primerBoton = botones[0];
    const card = primerBoton.closest('.product-card-exito');
    const img = card ? card.querySelector('.product-image-exito img') : null;

    console.log('   Primer botón seleccionado:');
    console.log('   - ID:', primerBoton.dataset.productoId || primerBoton.dataset.id);
    console.log('   - Nombre:', primerBoton.dataset.nombre || primerBoton.dataset.name);
    console.log('   - Precio:', primerBoton.dataset.precio || primerBoton.dataset.price);
    console.log('   - data-imagen:', primerBoton.getAttribute('data-imagen'));
    console.log('   - dataset.imagen:', primerBoton.dataset.imagen);

    if (img) {
        console.log('   - Imagen en tarjeta:', img.src);
    }

    console.log('\n   💡 Ahora haz clic en el botón "Agregar" del primer producto\n');
} else {
    console.log('   ❌ No se encontraron botones\n');
}

// 5. INSTRUCCIONES
console.log('%c5️⃣ INSTRUCCIONES:', 'font-size: 14px; font-weight: bold; color: #7c3aed');
console.log('   1. Haz clic en cualquier botón "Agregar"');
console.log('   2. Observa los logs en la consola:');
console.log('      - 🛒 Agregando producto...');
console.log('      - ✅ Producto nuevo agregado al carrito');
console.log('   3. Abre el carrito (icono superior derecha)');
console.log('   4. Verifica que aparezca la IMAGEN del producto');
console.log('\n=========================================\n');

// 6. FUNCIÓN AUXILIAR PARA VER EL CARRITO
window.verCarrito = function() {
    const carrito = JSON.parse(localStorage.getItem('carrito_v1') || '{}');
    const items = Object.values(carrito);

    console.log('%c📦 CONTENIDO DEL CARRITO', 'font-size: 16px; font-weight: bold; color: #FF6B00');
    console.log('=========================================');

    if (items.length === 0) {
        console.log('⚠️ El carrito está vacío');
    } else {
        items.forEach((item, index) => {
            console.log(`\nItem ${index + 1}:`);
            console.log('  ID:', item.id);
            console.log('  Nombre:', item.nombre || item.name);
            console.log('  Precio:', item.precio || item.price);
            console.log('  Cantidad:', item.cantidad || item.qty);
            console.log('  Imagen:', item.imagen || item.image || '❌ NO TIENE');

            if (item.imagen || item.image) {
                console.log('  ✅ TIENE IMAGEN');
            } else {
                console.log('  ❌ NO TIENE IMAGEN - PROBLEMA!');
            }
        });
    }

    console.log('\n=========================================');
};

console.log('%c💡 COMANDOS DISPONIBLES:', 'font-size: 14px; font-weight: bold; color: #0891b2');
console.log('   verCarrito()     - Ver contenido del carrito');
console.log('   localStorage.removeItem("carrito_v1") - Limpiar carrito');
console.log('\n=========================================\n');

