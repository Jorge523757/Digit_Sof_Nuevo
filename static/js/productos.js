/**
 * DIGT SOFT - JavaScript del Módulo de Productos
 */

document.addEventListener('DOMContentLoaded', function() {

    // Búsqueda en tiempo real
    const busquedaInput = document.getElementById('busqueda-producto');
    if (busquedaInput) {
        let timeout = null;
        busquedaInput.addEventListener('input', function() {
            clearTimeout(timeout);
            timeout = setTimeout(function() {
                // El formulario se enviará automáticamente
                // o se puede hacer con AJAX para mejor experiencia
            }, 500);
        });
    }

    // Validación de formulario de producto
    const formProducto = document.getElementById('form-producto');
    if (formProducto) {
        formProducto.addEventListener('submit', function(e) {
            let valid = true;
            const precioCompra = parseFloat(document.querySelector('[name="precio_compra"]').value);
            const precioVenta = parseFloat(document.querySelector('[name="precio_venta"]').value);
            const precioMayorista = parseFloat(document.querySelector('[name="precio_mayorista"]').value);
            const stockMinimo = parseInt(document.querySelector('[name="stock_minimo"]').value);
            const stockMaximo = parseInt(document.querySelector('[name="stock_maximo"]').value);

            // Validar precios
            if (precioVenta <= precioCompra) {
                alert('⚠️ El precio de venta debe ser mayor al precio de compra.');
                valid = false;
            }

            if (precioMayorista && precioMayorista < precioCompra) {
                alert('⚠️ El precio mayorista no puede ser menor al precio de compra.');
                valid = false;
            }

            // Validar stock
            if (stockMinimo > stockMaximo) {
                alert('⚠️ El stock mínimo no puede ser mayor al stock máximo.');
                valid = false;
            }

            if (!valid) {
                e.preventDefault();
            }
        });
    }

    // Cálculo automático de margen de utilidad
    const precioCompraInput = document.querySelector('[name="precio_compra"]');
    const precioVentaInput = document.querySelector('[name="precio_venta"]');

    if (precioCompraInput && precioVentaInput) {
        function calcularMargen() {
            const compra = parseFloat(precioCompraInput.value) || 0;
            const venta = parseFloat(precioVentaInput.value) || 0;

            if (compra > 0 && venta > 0) {
                const margen = ((venta - compra) / compra * 100).toFixed(1);
                console.log(`Margen de utilidad: ${margen}%`);
            }
        }

        precioCompraInput.addEventListener('input', calcularMargen);
        precioVentaInput.addEventListener('input', calcularMargen);
    }

    // Confirmación antes de eliminar
    const botonesEliminar = document.querySelectorAll('[href*="eliminar"]');
    botonesEliminar.forEach(function(boton) {
        if (!boton.closest('form')) { // Solo para enlaces, no para formularios
            boton.addEventListener('click', function(e) {
                if (!confirm('¿Está seguro que desea eliminar este producto?')) {
                    e.preventDefault();
                }
            });
        }
    });

    // Alerta de bajo stock
    const productosCards = document.querySelectorAll('.producto-card');
    productosCards.forEach(function(card) {
        const badge = card.querySelector('.badge.bg-danger');
        if (badge && badge.textContent.includes('Bajo Stock')) {
            card.style.borderLeft = '4px solid #dc3545';
        }
    });

    // Preview de imagen
    const imagenInput = document.querySelector('[name="imagen"]');
    if (imagenInput) {
        imagenInput.addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(event) {
                    console.log('Imagen seleccionada:', file.name);
                    // Aquí se podría mostrar un preview
                };
                reader.readAsDataURL(file);
            }
        });
    }

    // Animación de cards al cargar
    const cards = document.querySelectorAll('.producto-card, .stat-card');
    cards.forEach(function(card, index) {
        setTimeout(function() {
            card.style.opacity = '0';
            card.style.transform = 'translateY(20px)';

            setTimeout(function() {
                card.style.transition = 'all 0.5s ease';
                card.style.opacity = '1';
                card.style.transform = 'translateY(0)';
            }, 50);
        }, index * 50);
    });

    console.log('✅ Módulo de Productos cargado correctamente');
});

