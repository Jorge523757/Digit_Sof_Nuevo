/**
 * Script de Prueba Rápida del Sistema de Carrito
 * Ejecuta esto en la consola del navegador (F12) para probar todas las funcionalidades
 */

console.log('🧪 === INICIANDO PRUEBAS DEL SISTEMA DE CARRITO ===');

// Test 1: Verificar que el carrito está inicializado
console.log('\n📋 Test 1: Verificar inicialización del carrito');
if (typeof carrito !== 'undefined') {
    console.log('✅ PASS: Carrito inicializado');
    console.log('  - Items:', carrito.items.length);
    console.log('  - Total:', '$' + carrito.getTotal().toFixed(2));
} else {
    console.log('❌ FAIL: Carrito no está inicializado');
}

// Test 2: Verificar que ProductosManager está inicializado
console.log('\n📋 Test 2: Verificar ProductosManager');
if (typeof productosManager !== 'undefined') {
    console.log('✅ PASS: ProductosManager inicializado');
    console.log('  - Productos cargados:', productosManager.productos.length);
} else {
    console.log('❌ FAIL: ProductosManager no está inicializado');
}

// Test 3: Verificar métodos del carrito
console.log('\n📋 Test 3: Verificar métodos del carrito');
const metodos = [
    'agregar',
    'eliminar',
    'actualizar',
    'vaciar',
    'mostrarCarrito',
    'cerrarCarrito',
    'limpiarDuplicadosInmediato',
    'crearModalesNotificacion',
    'showConfirmModal',
    'showToast'
];

metodos.forEach(metodo => {
    if (typeof carrito[metodo] === 'function') {
        console.log(`✅ PASS: carrito.${metodo}() existe`);
    } else {
        console.log(`❌ FAIL: carrito.${metodo}() no encontrado`);
    }
});

// Test 4: Verificar elementos del DOM
console.log('\n📋 Test 4: Verificar elementos del DOM');
const elementos = {
    'cartBtn': 'Botón del carrito',
    'cartBadge': 'Badge del contador',
    'cart-counter-header': 'Contador del header'
};

Object.entries(elementos).forEach(([id, descripcion]) => {
    const elemento = document.getElementById(id);
    if (elemento) {
        console.log(`✅ PASS: ${descripcion} encontrado (#${id})`);
    } else {
        console.log(`⚠️ WARN: ${descripcion} no encontrado (#${id})`);
    }
});

// Test 5: Verificar botones de agregar al carrito
console.log('\n📋 Test 5: Verificar botones de productos');
const botonesAgregar = document.querySelectorAll('.btn-add-cart, .btn-add-to-cart');
console.log(`  - Botones "Agregar al carrito" encontrados: ${botonesAgregar.length}`);
if (botonesAgregar.length > 0) {
    console.log('✅ PASS: Botones de productos encontrados');
    const primerBoton = botonesAgregar[0];
    console.log('  - Primer botón tiene data-producto-id:', primerBoton.dataset.productoId ? 'Sí ✅' : 'No ❌');
} else {
    console.log('⚠️ WARN: No se encontraron botones de agregar al carrito');
}

// Test 6: Verificar localStorage
console.log('\n📋 Test 6: Verificar localStorage');
try {
    const carritoData = localStorage.getItem('carrito');
    if (carritoData) {
        const items = JSON.parse(carritoData);
        console.log('✅ PASS: localStorage funcionando');
        console.log('  - Items guardados:', Array.isArray(items) ? items.length : 'formato antiguo');
    } else {
        console.log('✅ PASS: localStorage vacío (normal si no has agregado productos)');
    }
} catch (error) {
    console.log('❌ FAIL: Error al acceder a localStorage:', error.message);
}

// Test 7: Probar notificación
console.log('\n📋 Test 7: Probar sistema de notificaciones');
try {
    if (typeof carrito !== 'undefined' && carrito.showToast) {
        carrito.showToast('🧪 Test', 'Notificación de prueba funcionando', 'success');
        console.log('✅ PASS: Sistema de notificaciones funcional');
        console.log('  - Deberías ver una notificación en la esquina superior derecha');
    } else {
        console.log('❌ FAIL: Método showToast no disponible');
    }
} catch (error) {
    console.log('❌ FAIL: Error al mostrar notificación:', error.message);
}

// Test 8: Funciones globales
console.log('\n📋 Test 8: Verificar funciones globales');
const funcionesGlobales = [
    'agregarAlCarrito',
    'limpiarDuplicados',
    'vaciarCarrito',
    'verCarrito',
    'limpiarLocalStorage'
];

funcionesGlobales.forEach(funcion => {
    if (typeof window[funcion] === 'function') {
        console.log(`✅ PASS: ${funcion}() disponible globalmente`);
    } else {
        console.log(`❌ FAIL: ${funcion}() no encontrada`);
    }
});

// Resumen final
console.log('\n🎉 === PRUEBAS COMPLETADAS ===');
console.log('\n📊 Comandos útiles disponibles:');
console.log('  - verCarrito()           → Ver contenido del carrito');
console.log('  - limpiarDuplicados()    → Eliminar productos duplicados');
console.log('  - vaciarCarrito()        → Vaciar todo el carrito');
console.log('  - limpiarLocalStorage()  → Limpiar almacenamiento completo');
console.log('  - carrito.mostrarCarrito() → Abrir modal del carrito');
console.log('\n✅ Sistema listo para usar!');

