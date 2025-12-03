// ========================================
// SCRIPT RÁPIDO PARA LIMPIAR Y PROBAR CARRITO
// Ejecutar en la consola del navegador (F12)
// ========================================

console.log('🧹 LIMPIANDO CARRITO...\n');

// Limpiar ambos carritos
localStorage.removeItem('carrito');
localStorage.removeItem('carrito_v1');

console.log('✅ Carrito limpiado exitosamente!');
console.log('📋 INSTRUCCIONES:');
console.log('   1. Recarga la página (F5)');
console.log('   2. Agrega UN producto al carrito');
console.log('   3. Abre el carrito');
console.log('   4. Verifica que la imagen aparezca');
console.log('\n💡 IMPORTANTE: Los cambios están en el código JavaScript');
console.log('   Las imágenes ahora se capturan desde el atributo data-imagen');
console.log('\n🔍 Para ver logs detallados, abre la consola antes de agregar productos');

