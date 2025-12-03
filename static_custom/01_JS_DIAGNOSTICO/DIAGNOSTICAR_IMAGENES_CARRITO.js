// ========================================
// SCRIPT PARA DIAGNOSTICAR Y CORREGIR IMÁGENES EN EL CARRITO
// ========================================

console.log('🔍 INICIANDO DIAGNÓSTICO DEL CARRITO...\n');

// 1. Revisar carrito_v1 (usado por productos-exito.js)
console.log('📦 Revisando carrito_v1...');
const carritoV1Raw = localStorage.getItem('carrito_v1');
if (carritoV1Raw) {
    const carritoV1 = JSON.parse(carritoV1Raw);
    console.log('✅ carrito_v1 encontrado:', Object.keys(carritoV1).length, 'items');
    Object.values(carritoV1).forEach((item, index) => {
        console.log(`\n  Item ${index + 1}:`);
        console.log('    ID:', item.id);
        console.log('    Nombre:', item.name || item.nombre);
        console.log('    Precio:', item.price || item.precio);
        console.log('    Imagen:', item.image || item.imagen || 'NO DEFINIDA');
        console.log('    Propiedades:', Object.keys(item));
    });
} else {
    console.log('⚠️ carrito_v1 no encontrado');
}

// 2. Revisar carrito (usado por productos-landing.js)
console.log('\n📦 Revisando carrito...');
const carritoRaw = localStorage.getItem('carrito');
if (carritoRaw) {
    const carrito = JSON.parse(carritoRaw);
    console.log('✅ carrito encontrado:', carrito.length, 'items');
    carrito.forEach((item, index) => {
        console.log(`\n  Item ${index + 1}:`);
        console.log('    ID:', item.id);
        console.log('    Nombre:', item.nombre);
        console.log('    Precio:', item.precio);
        console.log('    Imagen:', item.imagen || 'NO DEFINIDA');
        console.log('    Propiedades:', Object.keys(item));
    });
} else {
    console.log('⚠️ carrito no encontrado');
}

// 3. SOLUCIÓN: Sincronizar carritos
console.log('\n\n🔧 SINCRONIZANDO CARRITOS...\n');

if (carritoRaw && carritoV1Raw) {
    const carrito = JSON.parse(carritoRaw);
    const carritoV1 = JSON.parse(carritoV1Raw);

    // Convertir carrito (array) a carritoV1 (objeto con estructura correcta)
    const carritoV1Nuevo = {};

    carrito.forEach(item => {
        carritoV1Nuevo[item.id] = {
            id: item.id,
            name: item.nombre,
            nombre: item.nombre,
            price: item.precio,
            precio: item.precio,
            qty: item.cantidad,
            cantidad: item.cantidad,
            image: item.imagen,
            imagen: item.imagen,
            stock: item.stock,
            categoria: item.categoria || 'General',
            codigo: item.codigo || '',
            marca: item.marca || ''
        };
    });

    // Guardar carrito_v1 actualizado
    localStorage.setItem('carrito_v1', JSON.stringify(carritoV1Nuevo));

    console.log('✅ SINCRONIZACIÓN COMPLETADA!');
    console.log('📊 Items sincronizados:', Object.keys(carritoV1Nuevo).length);
    console.log('\n✨ Recarga la página para ver los cambios');

} else if (carritoRaw) {
    // Solo existe carrito, crear carritoV1
    const carrito = JSON.parse(carritoRaw);
    const carritoV1Nuevo = {};

    carrito.forEach(item => {
        carritoV1Nuevo[item.id] = {
            id: item.id,
            name: item.nombre,
            nombre: item.nombre,
            price: item.precio,
            precio: item.precio,
            qty: item.cantidad,
            cantidad: item.cantidad,
            image: item.imagen,
            imagen: item.imagen,
            stock: item.stock,
            categoria: item.categoria || 'General',
            codigo: item.codigo || '',
            marca: item.marca || ''
        };
    });

    localStorage.setItem('carrito_v1', JSON.stringify(carritoV1Nuevo));
    console.log('✅ carrito_v1 CREADO desde carrito!');
    console.log('✨ Recarga la página para ver los cambios');

} else if (carritoV1Raw) {
    // Solo existe carritoV1, crear carrito
    const carritoV1 = JSON.parse(carritoV1Raw);
    const carritoNuevo = [];

    Object.values(carritoV1).forEach(item => {
        carritoNuevo.push({
            id: item.id,
            nombre: item.name || item.nombre,
            precio: item.price || item.precio,
            cantidad: item.qty || item.cantidad,
            imagen: item.image || item.imagen,
            stock: item.stock,
            categoria: item.categoria || 'General',
            codigo: item.codigo || '',
            marca: item.marca || ''
        });
    });

    localStorage.setItem('carrito', JSON.stringify(carritoNuevo));
    console.log('✅ carrito CREADO desde carrito_v1!');
    console.log('✨ Recarga la página para ver los cambios');
} else {
    console.log('⚠️ No hay carritos para sincronizar');
}

console.log('\n\n🎯 DIAGNÓSTICO COMPLETADO!');
console.log('📋 INSTRUCCIONES:');
console.log('   1. Recarga la página (F5)');
console.log('   2. Abre el carrito');
console.log('   3. Las imágenes deberían aparecer ahora');
console.log('\n💡 Si el problema persiste, agrega productos nuevos al carrito');

