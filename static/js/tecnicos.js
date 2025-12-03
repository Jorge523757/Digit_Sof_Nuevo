/**
 * DIGT SOFT - JavaScript del Módulo de Técnicos
 * Funcionalidades interactivas y validaciones
 */

document.addEventListener('DOMContentLoaded', function() {

    // ==========================================
    // Auto-cerrar alertas después de 5 segundos
    // ==========================================
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.opacity = '0';
            alert.style.transform = 'translateY(-20px)';
            setTimeout(() => alert.remove(), 300);
        }, 5000);
    });

    // ==========================================
    // Botón de cerrar alertas
    // ==========================================
    const closeButtons = document.querySelectorAll('.btn-close');
    closeButtons.forEach(button => {
        button.addEventListener('click', function() {
            const alert = this.closest('.alert');
            alert.style.opacity = '0';
            alert.style.transform = 'translateY(-20px)';
            setTimeout(() => alert.remove(), 300);
        });
    });

    // ==========================================
    // Validación en tiempo real del formulario
    // ==========================================
    const form = document.querySelector('.tecnico-form');
    if (form) {
        // Validar nombres (solo letras y espacios)
        const nombresInput = form.querySelector('#id_nombres');
        if (nombresInput) {
            nombresInput.addEventListener('input', function() {
                const value = this.value;
                const regex = /^[a-záéíóúñA-ZÁÉÍÓÚÑ\s]*$/;
                if (!regex.test(value)) {
                    this.value = value.replace(/[^a-záéíóúñA-ZÁÉÍÓÚÑ\s]/g, '');
                }
            });
        }

        // Validar apellidos (solo letras y espacios)
        const apellidosInput = form.querySelector('#id_apellidos');
        if (apellidosInput) {
            apellidosInput.addEventListener('input', function() {
                const value = this.value;
                const regex = /^[a-záéíóúñA-ZÁÉÍÓÚÑ\s]*$/;
                if (!regex.test(value)) {
                    this.value = value.replace(/[^a-záéíóúñA-ZÁÉÍÓÚÑ\s]/g, '');
                }
            });
        }

        // Validar número de documento (solo números)
        const documentoInput = form.querySelector('#id_numero_documento');
        if (documentoInput) {
            documentoInput.addEventListener('input', function() {
                this.value = this.value.replace(/[^0-9]/g, '');
            });
        }

        // Validar teléfono (solo números y algunos símbolos)
        const telefonoInput = form.querySelector('#id_telefono');
        if (telefonoInput) {
            telefonoInput.addEventListener('input', function() {
                this.value = this.value.replace(/[^0-9+\-() ]/g, '');
            });
        }

        // Validación antes de enviar
        form.addEventListener('submit', function(e) {
            let isValid = true;
            const errors = [];

            // Validar campos requeridos
            const requiredFields = form.querySelectorAll('[required]');
            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    field.style.borderColor = 'var(--tecnicos-danger)';
                    errors.push(`El campo ${field.previousElementSibling.textContent} es requerido`);
                } else {
                    field.style.borderColor = 'var(--tecnicos-border)';
                }
            });

            // Validar email
            const emailInput = form.querySelector('#id_correo');
            if (emailInput && emailInput.value) {
                const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                if (!emailRegex.test(emailInput.value)) {
                    isValid = false;
                    emailInput.style.borderColor = 'var(--tecnicos-danger)';
                    errors.push('El correo electrónico no es válido');
                }
            }

            if (!isValid) {
                e.preventDefault();
                showNotification('Por favor complete todos los campos correctamente', 'error');
            }
        });
    }

    // ==========================================
    // Búsqueda en tiempo real
    // ==========================================
    const searchInput = document.querySelector('#busqueda');
    if (searchInput) {
        let searchTimeout;
        searchInput.addEventListener('input', function() {
            clearTimeout(searchTimeout);
            searchTimeout = setTimeout(() => {
                const form = this.closest('form');
                if (form) {
                    form.submit();
                }
            }, 500);
        });
    }

    // ==========================================
    // Filtro de estado con actualización automática
    // ==========================================
    const estadoSelect = document.querySelector('#estado');
    if (estadoSelect) {
        estadoSelect.addEventListener('change', function() {
            const form = this.closest('form');
            if (form) {
                form.submit();
            }
        });
    }

    // ==========================================
    // Confirmación de eliminación
    // ==========================================
    const deleteForm = document.querySelector('.delete-form');
    if (deleteForm) {
        deleteForm.addEventListener('submit', function(e) {
            e.preventDefault();

            if (confirm('¿Está completamente seguro de que desea eliminar este técnico? Esta acción no se puede deshacer.')) {
                this.submit();
            }
        });
    }

    // ==========================================
    // Animación de entrada para las tarjetas
    // ==========================================
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Observar elementos animables
    const animatableElements = document.querySelectorAll('.stat-card, .table-container, .form-container');
    animatableElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
        observer.observe(el);
    });

    // ==========================================
    // Tooltips para botones de acción
    // ==========================================
    const actionButtons = document.querySelectorAll('.btn-action');
    actionButtons.forEach(button => {
        button.addEventListener('mouseenter', function() {
            const title = this.getAttribute('title');
            if (title) {
                const tooltip = document.createElement('div');
                tooltip.className = 'custom-tooltip';
                tooltip.textContent = title;
                tooltip.style.cssText = `
                    position: absolute;
                    background: var(--tecnicos-text);
                    color: white;
                    padding: 0.3rem 0.6rem;
                    border-radius: 4px;
                    font-size: 0.8rem;
                    z-index: 1000;
                    pointer-events: none;
                    white-space: nowrap;
                `;
                document.body.appendChild(tooltip);

                const rect = this.getBoundingClientRect();
                tooltip.style.top = (rect.top - tooltip.offsetHeight - 5) + 'px';
                tooltip.style.left = (rect.left + rect.width / 2 - tooltip.offsetWidth / 2) + 'px';

                this._tooltip = tooltip;
            }
        });

        button.addEventListener('mouseleave', function() {
            if (this._tooltip) {
                this._tooltip.remove();
                delete this._tooltip;
            }
        });
    });

    // ==========================================
    // Contador de caracteres para campos de texto
    // ==========================================
    const textInputs = document.querySelectorAll('input[type="text"], textarea');
    textInputs.forEach(input => {
        const maxLength = input.getAttribute('maxlength');
        if (maxLength) {
            const counter = document.createElement('small');
            counter.style.cssText = `
                display: block;
                text-align: right;
                color: var(--tecnicos-text-muted);
                font-size: 0.8rem;
                margin-top: 0.3rem;
            `;

            const updateCounter = () => {
                const remaining = maxLength - input.value.length;
                counter.textContent = `${input.value.length}/${maxLength} caracteres`;
                if (remaining < 10) {
                    counter.style.color = 'var(--tecnicos-danger)';
                } else {
                    counter.style.color = 'var(--tecnicos-text-muted)';
                }
            };

            input.parentNode.appendChild(counter);
            input.addEventListener('input', updateCounter);
            updateCounter();
        }
    });

    // ==========================================
    // Función para mostrar notificaciones
    // ==========================================
    function showNotification(message, type = 'success') {
        const notification = document.createElement('div');
        notification.className = `alert alert-${type}`;
        notification.innerHTML = `
            <i class="fas fa-${type === 'success' ? 'check-circle' : 'exclamation-triangle'}"></i>
            ${message}
            <button type="button" class="btn-close">×</button>
        `;

        const container = document.querySelector('.tecnicos-container');
        if (container) {
            container.insertBefore(notification, container.firstChild);

            // Auto cerrar después de 5 segundos
            setTimeout(() => {
                notification.style.opacity = '0';
                notification.style.transform = 'translateY(-20px)';
                setTimeout(() => notification.remove(), 300);
            }, 5000);

            // Botón de cerrar
            notification.querySelector('.btn-close').addEventListener('click', function() {
                notification.style.opacity = '0';
                notification.style.transform = 'translateY(-20px)';
                setTimeout(() => notification.remove(), 300);
            });
        }
    }

    // ==========================================
    // Efecto de ripple en botones
    // ==========================================
    const buttons = document.querySelectorAll('.btn, .btn-action');
    buttons.forEach(button => {
        button.addEventListener('click', function(e) {
            const ripple = document.createElement('span');
            ripple.style.cssText = `
                position: absolute;
                border-radius: 50%;
                background: rgba(255, 255, 255, 0.6);
                width: 100px;
                height: 100px;
                margin-top: -50px;
                margin-left: -50px;
                animation: ripple 0.6s;
                pointer-events: none;
            `;

            const rect = this.getBoundingClientRect();
            ripple.style.left = (e.clientX - rect.left) + 'px';
            ripple.style.top = (e.clientY - rect.top) + 'px';

            this.style.position = 'relative';
            this.style.overflow = 'hidden';
            this.appendChild(ripple);

            setTimeout(() => ripple.remove(), 600);
        });
    });

    // ==========================================
    // Agregar animación de ripple al CSS
    // ==========================================
    if (!document.querySelector('#ripple-animation')) {
        const style = document.createElement('style');
        style.id = 'ripple-animation';
        style.textContent = `
            @keyframes ripple {
                from {
                    opacity: 1;
                    transform: scale(0);
                }
                to {
                    opacity: 0;
                    transform: scale(2);
                }
            }
        `;
        document.head.appendChild(style);
    }

    // ==========================================
    // Formato automático de teléfono
    // ==========================================
    const phoneInputs = document.querySelectorAll('#id_telefono');
    phoneInputs.forEach(input => {
        input.addEventListener('blur', function() {
            let value = this.value.replace(/\D/g, '');
            if (value.length === 10) {
                this.value = value.replace(/(\d{3})(\d{3})(\d{4})/, '($1) $2-$3');
            }
        });
    });

    // ==========================================
    // Convertir primera letra en mayúscula
    // ==========================================
    const capitalizeInputs = document.querySelectorAll('#id_nombres, #id_apellidos, #id_profesion');
    capitalizeInputs.forEach(input => {
        input.addEventListener('blur', function() {
            this.value = this.value.toLowerCase().replace(/\b\w/g, char => char.toUpperCase());
        });
    });

    console.log('✅ Módulo de Técnicos inicializado correctamente');
});

