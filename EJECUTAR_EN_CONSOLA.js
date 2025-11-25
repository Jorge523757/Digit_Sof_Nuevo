/* ═══════════════════════════════════════════════════════════════
   SCRIPT DE LIMPIEZA INMEDIATA - EJECUTAR EN CONSOLA (F12)
   Copia TODO este código y pégalo en la consola del navegador
   ═══════════════════════════════════════════════════════════════ */

console.log('%c🔧 INICIANDO LIMPIEZA FORZADA DEL CARRITO', 'background: #667eea; color: white; padding: 10px; font-size: 16px; font-weight: bold;');
console.log('');

// Obtener carrito actual
let carritoJSON = localStorage.getItem('carrito');

if (!carritoJSON) {
    console.log('%c✅ El carrito está vacío', 'color: #10b981; font-size: 14px;');
} else {
    let items = JSON.parse(carritoJSON);
    console.log('%c📦 Items encontrados: ' + items.length, 'color: #3b82f6; font-size: 14px;');
    console.log('');

    // Mostrar items actuales
    console.log('%cItems actuales:', 'font-weight: bold; font-size: 12px;');
    items.forEach((item, index) => {
        const nombre = item.nombre || item.nombre_producto || 'Sin nombre';
        const id = item.id;
        const cantidad = item.cantidad || 1;
        const precio = item.precio || item.precio_venta || 0;
        console.log(`   ${index + 1}. ${nombre} (ID: ${id}) - Cantidad: ${cantidad} - Precio: $${precio}`);
    });
    console.log('');

    // Crear mapa de productos únicos
    const productosUnicos = new Map();
    let duplicadosEncontrados = 0;

    items.forEach(item => {
        const id = parseInt(item.id);
        const nombre = item.nombre || item.nombre_producto || 'Sin nombre';
        const precio = parseFloat(item.precio || item.precio_venta || 0);
        const cantidad = parseInt(item.cantidad || 1);
        const stock = parseInt(item.stock || item.stock_actual || 0);

        if (!productosUnicos.has(id)) {
            // Primera vez que vemos este producto
            productosUnicos.set(id, {
                id: id,
                nombre: nombre.trim(),
                precio: precio,
                cantidad: cantidad,
                stock: stock,
                categoria: item.categoria || 'General',
                imagen: item.imagen || null,
                codigo: item.codigo || item.codigo_sku || '',
                marca: item.marca || ''
            });
        } else {
            // Producto duplicado - sumar cantidades
            const existente = productosUnicos.get(id);
            const cantidadAnterior = existente.cantidad;
            existente.cantidad += cantidad;
            duplicadosEncontrados++;
            console.warn(`⚠️ DUPLICADO ENCONTRADO Y CONSOLIDADO:`);
            console.warn(`   Producto: ${nombre}`);
            console.warn(`   ID: ${id}`);
            console.warn(`   Cantidad anterior: ${cantidadAnterior}`);
            console.warn(`   Sumando: ${cantidad}`);
            console.warn(`   Nueva cantidad total: ${existente.cantidad}`);
            console.log('');
        }
    });

    // Convertir a array
    const itemsLimpios = Array.from(productosUnicos.values());

    // Mostrar resultados
    console.log('');
    console.log('%c═══════════════════════════════════════════', 'color: #667eea; font-weight: bold;');
    console.log('%c📊 RESULTADOS DE LA LIMPIEZA', 'color: #667eea; font-size: 14px; font-weight: bold;');
    console.log('%c═══════════════════════════════════════════', 'color: #667eea; font-weight: bold;');
    console.log('');
    console.log(`   Items originales: ${items.length}`);
    console.log(`   Items únicos: ${itemsLimpios.length}`);
    console.log(`   Duplicados eliminados: ${duplicadosEncontrados}`);
    console.log('');

    if (duplicadosEncontrados > 0) {
        console.log('%cProductos después de consolidar:', 'font-weight: bold; font-size: 12px;');
        itemsLimpios.forEach((item, index) => {
            console.log(`   ${index + 1}. ${item.nombre} - Cantidad: x${item.cantidad} - Subtotal: $${(item.precio * item.cantidad).toFixed(2)}`);
        });
        console.log('');
    }

    // Calcular total
    const total = itemsLimpios.reduce((sum, item) => sum + (item.precio * item.cantidad), 0);
    console.log(`   💰 Total: $${total.toFixed(2)}`);
    console.log('');

    // Guardar carrito limpio
    localStorage.setItem('carrito', JSON.stringify(itemsLimpios));
    console.log('%c✅ ¡LIMPIEZA COMPLETADA!', 'background: #10b981; color: white; padding: 8px; font-size: 14px; font-weight: bold;');
    console.log('');
    console.log('%c🔄 Recargando página en 2 segundos...', 'color: #3b82f6; font-size: 12px;');

    // Recargar página
    setTimeout(() => {
        location.reload();
    }, 2000);
}

