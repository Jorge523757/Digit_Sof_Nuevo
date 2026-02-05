# 🔥 SOLUCIÓN MANUAL - COPIA Y PEGA DIRECTAMENTE

## ⚠️ El sistema de edición automática no está funcionando correctamente

Por eso te voy a dar el código para que lo copies MANUALMENTE.

---

## 📝 PASO 1: Edita `templates/ordenes/editar.html` MANUALMENTE

### 1. Abre el archivo en tu editor:
```
templates/ordenes/editar.html
```

### 2. Busca esta sección (Línea ~175-200):
```html
        <!-- Sección: Costos -->
        <div class="form-section">
            <h4>
                <i class="fas fa-dollar-sign"></i>
                Costos del Servicio
            </h4>
            <div class="row">
                <div class="col-md-4 mb-3">
                    <label class="form-label">Costo de Diagnóstico</label>
                    <div class="input-group">
                        <span class="input-group-text">$</span>
                        {{ form.costo_diagnostico }}
                    </div>
                </div>
                <div class="col-md-4 mb-3">
                    <label class="form-label">Costo de Mano de Obra</label>
                    <div class="input-group">
                        <span class="input-group-text">$</span>
                        {{ form.costo_mano_obra }}
                    </div>
                </div>
                <div class="col-md-4 mb-3">
                    <div class="alert alert-info mb-0" style="margin-top: 32px;">
                        <strong>Costo Total:</strong> {{ orden.costo_total|peso_colombiano }}
                    </div>
                </div>
            </div>
        </div>
```

### 3. REEMPLÁZALA CON ESTE CÓDIGO:
```html
        <!-- Sección: Costos -->
        <div class="form-section">
            <h4>
                <i class="fas fa-dollar-sign"></i>
                Costos del Servicio
            </h4>
            <div class="row">
                <div class="col-md-4 mb-3">
                    <label class="form-label">Costo de Diagnóstico</label>
                    <div class="input-group">
                        <span class="input-group-text">$</span>
                        {{ form.costo_diagnostico }}
                    </div>
                </div>
                <div class="col-md-4 mb-3">
                    <label class="form-label">Costo de Mano de Obra</label>
                    <div class="input-group">
                        <span class="input-group-text">$</span>
                        {{ form.costo_mano_obra }}
                    </div>
                </div>
                <div class="col-md-4 mb-3">
                    <div class="alert alert-info mb-0" style="margin-top: 32px;">
                        <i class="fas fa-calculator me-2"></i>
                        <strong>Costo Total:</strong> 
                        <span id="costo-total-display" style="font-size: 1.6em; font-weight: bold; color: #1e3c72;">$0</span>
                    </div>
                </div>
            </div>
        </div>
```

**⚠️ LO ÚNICO QUE CAMBIA ES ESTA LÍNEA:**
```html
<!-- ANTES: -->
<strong>Costo Total:</strong> {{ orden.costo_total|peso_colombiano }}

<!-- DESPUÉS: -->
<i class="fas fa-calculator me-2"></i>
<strong>Costo Total:</strong> 
<span id="costo-total-display" style="font-size: 1.6em; font-weight: bold; color: #1e3c72;">$0</span>
```

---

## 📝 PASO 2: Agrega las Funciones JavaScript

### 1. Busca esta sección (Línea ~270):
```javascript
    // Formateo automático de campos de moneda (pesos colombianos)
    function formatearPesosColombianos(input) {
        // Obtener solo números
        let valor = input.value.replace(/\D/g, '');

        // Si está vacío, limpiar
        if (!valor) {
            input.value = '';
            return;
        }

        // Formatear con separador de miles (punto)
        input.value = parseInt(valor).toLocaleString('es-CO');
    }
```

### 2. REEMPLÁZALA CON ESTE CÓDIGO:
```javascript
    // ============= FUNCIONES DE CÁLCULO =============
    function limpiarFormato(valor) {
        return valor.replace(/[.\s]/g, '');
    }
    
    function calcularTotal() {
        let diagnostico = $('#id_costo_diagnostico').val() || '0';
        let manoObra = $('#id_costo_mano_obra').val() || '0';
        let valorDiagnostico = parseInt(limpiarFormato(diagnostico)) || 0;
        let valorManoObra = parseInt(limpiarFormato(manoObra)) || 0;
        let total = valorDiagnostico + valorManoObra;
        let totalFormateado = total.toLocaleString('es-CO');
        $('#costo-total-display').text('$' + totalFormateado);
        console.log('✅ TOTAL:', valorDiagnostico, '+', valorManoObra, '=', total);
    }
    
    function formatearPesosColombianos(input) {
        let valor = input.value.replace(/\D/g, '');
        if (!valor) {
            input.value = '';
            calcularTotal();
            return;
        }
        input.value = parseInt(valor).toLocaleString('es-CO');
        calcularTotal();
    }
    // ============= FIN FUNCIONES =============
```

### 3. Busca DESPUÉS de estas funciones (donde dice "// Aplicar formato mientras se escribe"):
```javascript
    // Aplicar formato mientras se escribe
    $('#id_costo_diagnostico, #id_costo_mano_obra').on('input', function() {
        formatearPesosColombianos(this);
    });
```

### 4. AGREGA DESPUÉS DE ESA LÍNEA:
```javascript
    // FORZAR cálculo al cargar
    setTimeout(function() {
        calcularTotal();
        console.log('✅ Sistema de cálculo cargado');
    }, 500);
```

### 5. Busca donde dice "// Al enviar el formulario":
```javascript
    // Al enviar el formulario, quitar el formato para enviar el número puro
    $('form').on('submit', function() {
```

### 6. CÁMBIALO A:
```javascript
    // Al enviar el formulario, quitar el formato
    $('#ordenForm').on('submit', function() {
```

---

## 📝 PASO 3: Guarda el Archivo

1. Presiona `Ctrl + S` para guardar
2. Verifica que se guardó correctamente

---

## 📝 PASO 4: Prueba en el Navegador

1. **Cierra el navegador completamente**
2. **Abre en modo incógnito:** `Ctrl + Shift + N`
3. **Ve a:** `http://localhost:8000/ordenes/42/editar/`
4. **Presiona F12** (DevTools)
5. **Recarga con:** `Ctrl + Shift + R`
6. **Ve a la pestaña "Console"**
7. **Deberías ver:** `✅ Sistema de cálculo cargado`
8. **Escribe valores** en los campos
9. **Deberías ver:** `✅ TOTAL: 50000 + 80000 = 130000`
10. **El total debe mostrar:** `$130.000` ✅

---

## 🎯 Resumen de Cambios

### En el HTML (1 cambio):
- Agregaste `id="costo-total-display"` al span del total

### En el JavaScript (3 cambios):
- Agregaste función `limpiarFormato()`
- Agregaste función `calcularTotal()`
- Modificaste `formatearPesosColombianos()` para llamar a `calcularTotal()`
- Agregaste `setTimeout(calcularTotal, 500)` para forzar cálculo al cargar

---

## ✅ Archivos de Referencia

Si tienes dudas, revisa estos archivos que creé:
- `SECCION_COSTOS_CORREGIDA.html` - HTML correcto
- `JAVASCRIPT_COMPLETO.js` - JavaScript completo

---

**IMPORTANTE: Debes hacer los cambios MANUALMENTE porque el sistema de edición automática no está guardando los cambios correctamente.**

**¿Ya hiciste los cambios? Dime qué ves en la consola (F12).** 🚀

