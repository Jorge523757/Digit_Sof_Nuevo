// SCRIPT DE LIMPIEZA INMEDIATA - EJECUTAR EN CONSOLA
// Copia y pega esto en la consola del navegador (F12)

console.log('🔧 INICIANDO LIMPIEZA FORZADA...');

// Obtener carrito actual
let carritoActual = localStorage.getItem('carrito');

if (!carritoActual) {
    console.log('✅ Carrito ya está vacío');
} else {
    let items = JSON.parse(carritoActual);
    console.log('📦 Items encontrados:', items.length);

    // Mostrar cada item
    items.forEach((item, index) => {
        console.log(`${index + 1}. ${item.nombre || item.nombre_producto} - ID: ${item.id} - Cantidad: ${item.cantidad}`);
    });

    // Crear mapa de productos únicos
    const productosUnicos = new Map();

    items.forEach(item => {
        const id = parseInt(item.id);
        const nombre = item.nombre || item.nombre_producto;
        const precio = parseFloat(item.precio || item.precio_venta);
        const cantidad = parseInt(item.cantidad || 1);

        if (!productosUnicos.has(id)) {
            productosUnicos.set(id, {
                id: id,
                nombre: nombre,
                precio: precio,
                cantidad: cantidad,
                stock: parseInt(item.stock || item.stock_actual || 0),
                categoria: item.categoria || 'General',
                imagen: item.imagen || null,
                codigo: item.codigo || item.codigo_sku || '',
                marca: item.marca || ''
            });
        } else {
            // Sumar cantidades si ya existe
            const existente = productosUnicos.get(id);
            existente.cantidad += cantidad;
            console.warn(`⚠️ DUPLICADO CONSOLIDADO: ${nombre} (ID: ${id})`);
        }
    });

    // Convertir a array
    const itemsLimpios = Array.from(productosUnicos.values());

    console.log('');
    console.log('📊 RESULTADOS:');
    console.log('   Items originales:', items.length);
    console.log('   Items únicos:', itemsLimpios.length);
    console.log('   Duplicados eliminados:', items.length - itemsLimpios.length);
    console.log('');
    console.log('✅ Items limpios:');
    itemsLimpios.forEach((item, index) => {
        console.log(`   ${index + 1}. ${item.nombre} - Cantidad: ${item.cantidad} - Precio: $${item.precio}`);
    });

    // Guardar carrito limpio
    localStorage.setItem('carrito', JSON.stringify(itemsLimpios));

    console.log('');
    console.log('💾 Carrito guardado correctamente');
    console.log('🔄 Recargando página...');

    // Recargar después de 1 segundo
    setTimeout(() => {
        location.reload();
    }, 1000);
}

