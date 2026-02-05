// ========================================
// SCRIPT DE EMERGENCIA - COPIAR Y PEGAR EN LA CONSOLA
// ========================================

// Paso 1: Verificar que existen los elementos
console.log('🔍 VERIFICANDO ELEMENTOS...');
const inputDiagnostico = document.getElementById('id_costo_diagnostico');
const inputManoObra = document.getElementById('id_costo_mano_obra');
const displayTotal = document.getElementById('costo-total-display');

console.log('Campo Diagnóstico:', inputDiagnostico ? '✅ ENCONTRADO' : '❌ NO EXISTE');
console.log('Campo Mano Obra:', inputManoObra ? '✅ ENCONTRADO' : '❌ NO EXISTE');
console.log('Display Total:', displayTotal ? '✅ ENCONTRADO' : '❌ NO EXISTE');

if (!inputDiagnostico || !inputManoObra || !displayTotal) {
    console.error('❌ FALTAN ELEMENTOS NECESARIOS');
} else {
    console.log('✅ TODOS LOS ELEMENTOS EXISTEN');

    // Paso 2: Definir funciones
    function limpiarFormato(valor) {
        if (!valor) return '';
        return valor.toString().replace(/[.\s]/g, '');
    }

    function calcularTotal() {
        const diagnostico = inputDiagnostico.value || '0';
        const manoObra = inputManoObra.value || '0';
        const valorDiagnostico = parseInt(limpiarFormato(diagnostico)) || 0;
        const valorManoObra = parseInt(limpiarFormato(manoObra)) || 0;
        const total = valorDiagnostico + valorManoObra;
        const totalFormateado = total.toLocaleString('es-CO');

        displayTotal.textContent = '$' + totalFormateado;
        console.log('💰 TOTAL:', valorDiagnostico, '+', valorManoObra, '=', total);
        return total;
    }

    function formatearYCalcular(input) {
        let valor = input.value.replace(/\D/g, '');
        if (!valor) {
            input.value = '';
        } else {
            input.value = parseInt(valor).toLocaleString('es-CO');
        }
        calcularTotal();
    }

    // Paso 3: Agregar eventos
    inputDiagnostico.removeEventListener('input', formatearYCalcular);
    inputManoObra.removeEventListener('input', formatearYCalcular);

    inputDiagnostico.addEventListener('input', function() {
        formatearYCalcular(this);
    });

    inputManoObra.addEventListener('input', function() {
        formatearYCalcular(this);
    });

    // Paso 4: Calcular ahora mismo
    const totalActual = calcularTotal();

    console.log('✅ SISTEMA ACTIVADO - Total actual: $' + totalActual.toLocaleString('es-CO'));
    console.log('📝 Ahora escribe en los campos y el total se actualizará automáticamente');
}

