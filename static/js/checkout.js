// Checkout JavaScript para DigitSoft
document.addEventListener('DOMContentLoaded', function() {
    // Cargar items del carrito
    cargarItemsCheckout();

    // Toggle facturación
    const requiereFactura = document.getElementById('requiere_factura');
    const facturacionFields = document.getElementById('facturacion_fields');

    if (requiereFactura) {
        requiereFactura.addEventListener('change', function() {
            if (this.checked) {
                facturacionFields.style.display = 'block';
                // Hacer campos requeridos
                document.getElementById('razon_social').required = true;
                document.getElementById('ruc').required = true;
                document.getElementById('direccion_factura').required = true;
            } else {
                facturacionFields.style.display = 'none';
                // Quitar requeridos
                document.getElementById('razon_social').required = false;
                document.getElementById('ruc').required = false;
                document.getElementById('direccion_factura').required = false;
            }
        });
    }

    // Botón finalizar compra
    const btnFinalizar = document.getElementById('btnFinalizarCompra');
    if (btnFinalizar) {
        btnFinalizar.addEventListener('click', procesarCompra);
    }
});

function cargarItemsCheckout() {
    const carritoJSON = localStorage.getItem('carrito');
    if (!carritoJSON) {
        window.location.href = '/';
        return;
    }

    const items = JSON.parse(carritoJSON);
    if (items.length === 0) {
        window.location.href = '/';
        return;
    }

    // Renderizar items
    const container = document.getElementById('orden-items');
    container.innerHTML = items.map(item => `
        <div class="orden-item">
            <div class="item-info">
                <span class="item-cantidad">${item.cantidad}x</span>
                <span class="item-nombre">${item.nombre}</span>
            </div>
            <span class="item-precio">$${(item.precio * item.cantidad).toFixed(2)}</span>
        </div>
    `).join('');

    // Calcular totales
    const subtotal = items.reduce((sum, item) => sum + (item.precio * item.cantidad), 0);
    const iva = subtotal * 0.12;
    const total = subtotal + iva;

    document.getElementById('subtotal').textContent = `$${subtotal.toFixed(2)}`;
    document.getElementById('iva').textContent = `$${iva.toFixed(2)}`;
    document.getElementById('total').textContent = `$${total.toFixed(2)}`;
}

async function procesarCompra() {
    // Validar formulario
    const form = document.getElementById('checkoutForm');
    if (!form.checkValidity()) {
        form.reportValidity();
        return;
    }

    // Obtener datos del formulario
    const nombre = document.getElementById('nombre').value.trim();
    const apellido = document.getElementById('apellido').value.trim();
    const cedula = document.getElementById('cedula').value.trim();
    const telefono = document.getElementById('telefono').value.trim();
    const email = document.getElementById('email').value.trim();
    const direccion = document.getElementById('direccion').value.trim();
    const notas = document.getElementById('notas').value.trim();

    // Datos de facturación
    const requiereFactura = document.getElementById('requiere_factura').checked;
    let datosFacturacion = {};

    if (requiereFactura) {
        const razonSocial = document.getElementById('razon_social').value.trim();
        const ruc = document.getElementById('ruc').value.trim();
        const direccionFactura = document.getElementById('direccion_factura').value.trim();

        if (!razonSocial || !ruc || !direccionFactura) {
            alert('Por favor complete todos los campos de facturación');
            return;
        }

        datosFacturacion = {
            razon_social: razonSocial,
            ruc: ruc,
            direccion_factura: direccionFactura
        };
    }

    // Método de pago
    const tipoPago = document.querySelector('input[name="tipo_pago"]:checked').value;

    // Obtener items del carrito
    const carritoJSON = localStorage.getItem('carrito');
    const items = JSON.parse(carritoJSON);

    // Preparar datos para enviar
    const datos = {
        items: items,
        cliente: {
            nombre: nombre,
            apellido: apellido,
            cedula: cedula,
            telefono: telefono,
            email: email,
            direccion: direccion,
            notas: notas,
            requiere_factura: requiereFactura,
            ...datosFacturacion
        },
        tipo_pago: tipoPago
    };

    // Mostrar loading
    showLoading(true);

    try {
        const response = await fetch('/checkout/procesar-orden/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify(datos)
        });

        const result = await response.json();

        showLoading(false);

        if (result.success) {
            // Limpiar carrito
            localStorage.removeItem('carrito');

            // Mostrar modal de éxito
            mostrarConfirmacion(result);
        } else {
            alert('Error: ' + result.error);
        }

    } catch (error) {
        showLoading(false);
        alert('Error al procesar la compra: ' + error.message);
    }
}

function mostrarConfirmacion(result) {
    const modal = document.getElementById('confirmacionModal');
    const numeroOrden = document.getElementById('numeroOrden');
    const mensaje = document.getElementById('mensajeConfirmacion');
    const btnVerFactura = document.getElementById('btnVerFactura');

    numeroOrden.textContent = '#' + result.orden_id;
    mensaje.textContent = result.mensaje || 'Su pedido ha sido procesado exitosamente.';

    if (result.factura_id) {
        btnVerFactura.style.display = 'inline-block';
        btnVerFactura.href = `/checkout/factura/${result.orden_id}/`;
    }

    modal.style.display = 'flex';

    // Cerrar modal al hacer clic fuera
    modal.addEventListener('click', function(e) {
        if (e.target === modal) {
            window.location.href = '/';
        }
    });
}

function showLoading(show) {
    const overlay = document.getElementById('loadingOverlay');
    overlay.style.display = show ? 'flex' : 'none';
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Validación de cédula/RUC ecuatoriano (opcional)
document.getElementById('cedula')?.addEventListener('blur', function() {
    const cedula = this.value.trim();
    if (cedula.length === 10) {
        // Validar cédula
        if (!validarCedula(cedula)) {
            this.setCustomValidity('Cédula inválida');
        } else {
            this.setCustomValidity('');
        }
    } else if (cedula.length === 13) {
        // Es RUC
        this.setCustomValidity('');
    }
});

function validarCedula(cedula) {
    if (cedula.length !== 10) return false;

    const digitos = cedula.split('').map(Number);
    const provincia = parseInt(cedula.substr(0, 2));

    if (provincia < 1 || provincia > 24) return false;

    const coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2];
    let suma = 0;

    for (let i = 0; i < 9; i++) {
        let valor = digitos[i] * coeficientes[i];
        if (valor >= 10) valor -= 9;
        suma += valor;
    }

    const verificador = digitos[9];
    const resultado = suma % 10 === 0 ? 0 : 10 - (suma % 10);

    return resultado === verificador;
}

