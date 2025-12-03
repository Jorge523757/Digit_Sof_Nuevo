/**
 * DIGT SOFT - JavaScript del Módulo de Garantías
 */

document.addEventListener('DOMContentLoaded', function() {

    // Búsqueda en tiempo real
    const busquedaInput = document.getElementById('busqueda-garantia');
    if (busquedaInput) {
        let timeout = null;
        busquedaInput.addEventListener('input', function() {
            clearTimeout(timeout);
            timeout = setTimeout(function() {
                // El formulario se enviará automáticamente
            }, 500);
        });
    }

    // Validación de formulario de garantía
    const formGarantia = document.getElementById('form-garantia');
    if (formGarantia) {
        formGarantia.addEventListener('submit', function(e) {
            let valid = true;

            const fechaCompra = new Date(document.querySelector('[name="fecha_compra"]').value);
            const fechaInicio = new Date(document.querySelector('[name="fecha_inicio"]').value);
            const fechaVencimiento = new Date(document.querySelector('[name="fecha_vencimiento"]').value);

            // Validar que la fecha de inicio no sea anterior a la de compra
            if (fechaInicio < fechaCompra) {
                alert('⚠️ La fecha de inicio no puede ser anterior a la fecha de compra.');
                valid = false;
            }

            // Validar que la fecha de vencimiento sea posterior a la de inicio
            if (fechaVencimiento <= fechaInicio) {
                alert('⚠️ La fecha de vencimiento debe ser posterior a la fecha de inicio.');
                valid = false;
            }

            // Validar cédula (solo números)
            const cedula = document.querySelector('[name="cedula"]').value;
            if (cedula && !/^\d+$/.test(cedula)) {
                alert('⚠️ La cédula debe contener solo números.');
                valid = false;
            }

            // Validar email
            const email = document.querySelector('[name="correo_electronico"]').value;
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (email && !emailRegex.test(email)) {
                alert('⚠️ El correo electrónico no es válido.');
                valid = false;
            }

            if (!valid) {
                e.preventDefault();
            }
        });
    }

    // Cálculo automático de fecha de vencimiento
    const fechaInicioInput = document.querySelector('[name="fecha_inicio"]');
    const mesesGarantiaInput = document.querySelector('[name="meses_garantia"]');
    const fechaVencimientoInput = document.querySelector('[name="fecha_vencimiento"]');

    if (fechaInicioInput && mesesGarantiaInput && fechaVencimientoInput) {
        function calcularVencimiento() {
            const fechaInicio = new Date(fechaInicioInput.value);
            const meses = parseInt(mesesGarantiaInput.value) || 12;

            if (fechaInicio && meses > 0) {
                const fechaVencimiento = new Date(fechaInicio);
                fechaVencimiento.setMonth(fechaVencimiento.getMonth() + meses);

                // Formatear fecha para input type="date" (YYYY-MM-DD)
                const year = fechaVencimiento.getFullYear();
                const month = String(fechaVencimiento.getMonth() + 1).padStart(2, '0');
                const day = String(fechaVencimiento.getDate()).padStart(2, '0');

                fechaVencimientoInput.value = `${year}-${month}-${day}`;
            }
        }

        fechaInicioInput.addEventListener('change', calcularVencimiento);
        mesesGarantiaInput.addEventListener('change', calcularVencimiento);
    }

    // Autocompletar producto
    const productoSelect = document.querySelector('[name="producto"]');
    const nombreProductoInput = document.querySelector('[name="nombre_producto"]');

    if (productoSelect && nombreProductoInput) {
        productoSelect.addEventListener('change', function() {
            const selectedOption = this.options[this.selectedIndex];
            if (selectedOption && selectedOption.value) {
                nombreProductoInput.value = selectedOption.text;
            }
        });
    }

    // Confirmación antes de eliminar
    const botonesEliminar = document.querySelectorAll('[href*="eliminar"]');
    botonesEliminar.forEach(function(boton) {
        if (!boton.closest('form')) {
            boton.addEventListener('click', function(e) {
                if (!confirm('¿Está seguro que desea eliminar esta garantía?')) {
                    e.preventDefault();
                }
            });
        }
    });

    // Resaltar garantías próximas a vencer
    const filas = document.querySelectorAll('tbody tr');
    filas.forEach(function(fila) {
        const diasRestantes = fila.querySelector('td:nth-child(8)');
        if (diasRestantes) {
            const texto = diasRestantes.textContent;
            if (texto.includes('días')) {
                const dias = parseInt(texto);
                if (dias > 0 && dias <= 30) {
                    fila.style.background = 'rgba(255, 193, 7, 0.1)';
                    fila.style.borderLeft = '4px solid #ffc107';
                }
            } else if (texto.includes('Vencida')) {
                fila.style.background = 'rgba(220, 53, 69, 0.1)';
                fila.style.borderLeft = '4px solid #dc3545';
            }
        }
    });

    // Mostrar/ocultar sección de reclamación
    const estadoSelect = document.querySelector('[name="estado"]');
    if (estadoSelect) {
        estadoSelect.addEventListener('change', function() {
            const reclamacionCard = document.querySelector('.card-header.bg-danger');
            if (reclamacionCard && reclamacionCard.parentElement) {
                if (this.value === 'EN_REVISION' || this.value === 'RECHAZADA') {
                    reclamacionCard.parentElement.style.display = 'block';
                }
            }
        });
    }

    // Animación de progress bar
    const progressBars = document.querySelectorAll('.progress-bar');
    progressBars.forEach(function(bar) {
        const width = bar.style.width;
        bar.style.width = '0%';
        setTimeout(function() {
            bar.style.width = width;
        }, 500);
    });

    // Tooltip para badges de estado
    const badges = document.querySelectorAll('.badge');
    badges.forEach(function(badge) {
        badge.setAttribute('title', badge.textContent);
    });

    console.log('✅ Módulo de Garantías cargado correctamente');
});

