# 🚨 SOLUCIÓN DE EMERGENCIA - EJECUTAR EN LA CONSOLA

## ❌ Problema Actual

El Costo Total muestra **$0** a pesar de escribir:
- Diagnóstico: 20000
- Mano Obra: 30000
- **Debería mostrar:** $50.000

Esto significa que el JavaScript NO se está ejecutando.

---

## ✅ SOLUCIÓN INMEDIATA (2 minutos)

### PASO 1: Abre DevTools
Presiona **F12** en la página de editar orden

### PASO 2: Ve a la pestaña "Console"
Clic en **"Console"** o **"Consola"**

### PASO 3: Copia TODO este código:

```javascript
// SCRIPT DE EMERGENCIA
const inputDiagnostico = document.getElementById('id_costo_diagnostico');
const inputManoObra = document.getElementById('id_costo_mano_obra');
const displayTotal = document.getElementById('costo-total-display');

console.log('Diagnóstico:', inputDiagnostico ? '✅' : '❌');
console.log('Mano Obra:', inputManoObra ? '✅' : '❌');
console.log('Total:', displayTotal ? '✅' : '❌');

if (inputDiagnostico && inputManoObra && displayTotal) {
    function limpiarFormato(valor) {
        return valor ? valor.toString().replace(/[.\s]/g, '') : '';
    }

    function calcularTotal() {
        const d = inputDiagnostico.value || '0';
        const m = inputManoObra.value || '0';
        const vd = parseInt(limpiarFormato(d)) || 0;
        const vm = parseInt(limpiarFormato(m)) || 0;
        const total = vd + vm;
        displayTotal.textContent = '$' + total.toLocaleString('es-CO');
        console.log('💰 TOTAL:', vd, '+', vm, '=', total);
        return total;
    }

    function formatear(input) {
        let v = input.value.replace(/\D/g, '');
        input.value = v ? parseInt(v).toLocaleString('es-CO') : '';
        calcularTotal();
    }

    inputDiagnostico.addEventListener('input', function() { formatear(this); });
    inputManoObra.addEventListener('input', function() { formatear(this); });
    
    calcularTotal();
    console.log('✅ SISTEMA ACTIVADO');
} else {
    console.error('❌ FALTAN ELEMENTOS');
}
```

### PASO 4: Pega el código en la consola
**Click derecho → Paste** o **Ctrl + V**

### PASO 5: Presiona Enter

**DEBERÍAS VER:**
```
Diagnóstico: ✅
Mano Obra: ✅
Total: ✅
💰 TOTAL: 20000 + 30000 = 50000
✅ SISTEMA ACTIVADO
```

**Y el Costo Total DEBE cambiar a:** `$50.000` ✅

### PASO 6: Prueba escribir nuevos valores
Cambia cualquier campo y el total se actualizará automáticamente.

---

## 🔍 Si NO Funciona

Si ves:
```
❌ FALTAN ELEMENTOS
```

Significa que el HTML **NO tiene el ID correcto**. En ese caso:

1. Copia el contenido de `SECCION_COSTOS_CORREGIDA.html`
2. Abre `templates/ordenes/editar.html` manualmente
3. Reemplaza la sección de Costos
4. Guarda con `Ctrl + S`
5. Recarga la página con `Ctrl + Shift + R`
6. Ejecuta el script de nuevo

---

## 💡 Explicación

Este script:
1. ✅ Verifica que existen los elementos necesarios
2. ✅ Define las funciones de cálculo
3. ✅ Agrega los event listeners
4. ✅ Calcula el total inmediatamente
5. ✅ NO depende de jQuery (JavaScript puro)

---

## 📝 Resultado Esperado

Después de ejecutar el script:
- Escribes en **Diagnóstico:** 20000
- Escribes en **Mano Obra:** 30000
- **Costo Total muestra:** $50.000 ✅
- En la consola ves: `💰 TOTAL: 20000 + 30000 = 50000`

---

**EJECUTA EL SCRIPT AHORA Y DIME QUÉ VES EN LA CONSOLA.** 🚀

