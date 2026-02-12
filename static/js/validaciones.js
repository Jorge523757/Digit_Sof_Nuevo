/**
 * Sistema de Validación en Tiempo Real - DIGIT SOFT
 * Validaciones profesionales con feedback instantáneo
 */

document.addEventListener('DOMContentLoaded', function() {

    // Configuración de validaciones
    const validaciones = {
        email: {
            regex: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
            mensaje: '📧 Ingrese un email válido (ejemplo: usuario@empresa.com)'
        },
        telefono: {
            regex: /^[0-9]{7,10}$/,
            mensaje: '📱 El teléfono debe tener entre 7 y 10 dígitos'
        },
        celular: {
            regex: /^3[0-9]{9}$/,
            mensaje: '📱 El celular debe empezar con 3 y tener 10 dígitos'
        },
        cedula: {
            regex: /^[0-9]{6,10}$/,
            mensaje: '🪪 La cédula debe tener entre 6 y 10 dígitos'
        },
        nit: {
            regex: /^[0-9]{8,10}$/,
            mensaje: '🏢 El NIT debe tener entre 8 y 10 dígitos'
        },
        precio: {
            regex: /^[0-9]+(\.[0-9]{1,2})?$/,
            mensaje: '💰 Ingrese un precio válido (ejemplo: 1000 o 1000.50)'
        },
        nombre: {
            regex: /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]{2,}$/,
            mensaje: '👤 El nombre solo puede contener letras (mínimo 2 caracteres)'
        },
        url: {
            regex: /^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$/,
            mensaje: '🔗 Ingrese una URL válida'
        }
    };

    // Aplicar validación a campos específicos
    aplicarValidaciones();

    // Validación de formularios al enviar
    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', function(e) {
            if (!validarFormulario(this)) {
                e.preventDefault();
                mostrarMensajeError('⚠️ Por favor corrija los errores antes de continuar');

                // Scroll al primer error
                const primerError = this.querySelector('.is-invalid');
                if (primerError) {
                    primerError.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    primerError.focus();
                }
            }
        });
    });

    // Función para aplicar validaciones
    function aplicarValidaciones() {
        // Email
        document.querySelectorAll('input[type="email"], input[name*="email"]').forEach(input => {
            validarCampo(input, 'email');
        });

        // Teléfono
        document.querySelectorAll('input[name*="telefono"], input[name*="phone"]').forEach(input => {
            validarCampo(input, 'telefono');
        });

        // Celular
        document.querySelectorAll('input[name*="celular"], input[name*="movil"]').forEach(input => {
            validarCampo(input, 'celular');
        });

        // Cédula
        document.querySelectorAll('input[name*="cedula"], input[name*="documento"]').forEach(input => {
            validarCampo(input, 'cedula');
        });

        // NIT
        document.querySelectorAll('input[name*="nit"]').forEach(input => {
            validarCampo(input, 'nit');
        });

        // Precio
        document.querySelectorAll('input[name*="precio"], input[name*="valor"], input[name*="total"]').forEach(input => {
            validarCampo(input, 'precio');
        });

        // Nombre
        document.querySelectorAll('input[name*="nombre"], input[name*="name"]').forEach(input => {
            if (input.type !== 'email') {
                validarCampo(input, 'nombre');
            }
        });

        // URL
        document.querySelectorAll('input[type="url"], input[name*="url"]').forEach(input => {
            validarCampo(input, 'url');
        });

        // Campos requeridos
        document.querySelectorAll('input[required], select[required], textarea[required]').forEach(input => {
            validarRequerido(input);
        });

        // Validación de contraseñas
        validarContraseñas();

        // Validación de fechas
        validarFechas();
    }

    // Validar campo específico
    function validarCampo(input, tipo) {
        const validacion = validaciones[tipo];

        input.addEventListener('blur', function() {
            if (this.value.trim() === '') {
                if (this.hasAttribute('required')) {
                    marcarInvalido(this, '⚠️ Este campo es obligatorio');
                } else {
                    limpiarValidacion(this);
                }
                return;
            }

            if (!validacion.regex.test(this.value.trim())) {
                marcarInvalido(this, validacion.mensaje);
            } else {
                marcarValido(this);
            }
        });

        input.addEventListener('input', function() {
            if (this.classList.contains('is-invalid')) {
                if (validacion.regex.test(this.value.trim())) {
                    marcarValido(this);
                }
            }
        });
    }

    // Validar campo requerido
    function validarRequerido(input) {
        input.addEventListener('blur', function() {
            if (this.value.trim() === '') {
                marcarInvalido(this, '⚠️ Este campo es obligatorio');
            } else {
                if (!this.classList.contains('is-invalid')) {
                    limpiarValidacion(this);
                }
            }
        });
    }

    // Validar contraseñas
    function validarContraseñas() {
        const passwordInputs = document.querySelectorAll('input[type="password"]');

        passwordInputs.forEach(input => {
            if (input.name.includes('password1') || input.name.includes('nueva_contraseña')) {
                input.addEventListener('input', function() {
                    validarFortalezaContraseña(this);
                });
            }

            // Confirmar contraseña
            if (input.name.includes('password2') || input.name.includes('confirmar')) {
                const password1 = document.querySelector('input[name*="password1"], input[name*="nueva_contraseña"]');
                if (password1) {
                    input.addEventListener('input', function() {
                        if (this.value !== password1.value) {
                            marcarInvalido(this, '🔐 Las contraseñas no coinciden');
                        } else {
                            marcarValido(this, '✓ Las contraseñas coinciden');
                        }
                    });
                }
            }
        });
    }

    // Validar fortaleza de contraseña
    function validarFortalezaContraseña(input) {
        const password = input.value;
        const requisitos = {
            longitud: password.length >= 8,
            mayuscula: /[A-Z]/.test(password),
            minuscula: /[a-z]/.test(password),
            numero: /[0-9]/.test(password),
            especial: /[!@#$%^&*(),.?":{}|<>]/.test(password)
        };

        const cumplidos = Object.values(requisitos).filter(Boolean).length;
        let mensaje = '';
        let clase = '';

        if (cumplidos < 3) {
            mensaje = '🔐 Contraseña débil';
            clase = 'is-invalid';
        } else if (cumplidos < 5) {
            mensaje = '🔐 Contraseña media - Agregue más caracteres';
            clase = 'is-invalid';
        } else {
            mensaje = '✓ Contraseña fuerte';
            clase = 'is-valid';
        }

        input.classList.remove('is-valid', 'is-invalid');
        input.classList.add(clase);

        mostrarFeedback(input, mensaje, clase === 'is-valid');
    }

    // Validar fechas
    function validarFechas() {
        const fechaInputs = document.querySelectorAll('input[type="date"]');

        fechaInputs.forEach(input => {
            input.addEventListener('change', function() {
                const fecha = new Date(this.value);
                const hoy = new Date();
                hoy.setHours(0, 0, 0, 0);

                // Validar que no sea fecha futura (si es fecha de nacimiento o similar)
                if (this.name.includes('nacimiento') || this.name.includes('fecha_inicio')) {
                    if (fecha > hoy) {
                        marcarInvalido(this, '📅 La fecha no puede ser en el futuro');
                    } else {
                        marcarValido(this);
                    }
                }
            });
        });
    }

    // Marcar campo como inválido
    function marcarInvalido(input, mensaje) {
        input.classList.remove('is-valid');
        input.classList.add('is-invalid');
        mostrarFeedback(input, mensaje, false);
    }

    // Marcar campo como válido
    function marcarValido(input, mensaje = null) {
        input.classList.remove('is-invalid');
        input.classList.add('is-valid');
        if (mensaje) {
            mostrarFeedback(input, mensaje, true);
        } else {
            const feedback = input.parentElement.querySelector('.invalid-feedback, .valid-feedback');
            if (feedback) {
                feedback.remove();
            }
        }
    }

    // Limpiar validación
    function limpiarValidacion(input) {
        input.classList.remove('is-valid', 'is-invalid');
        const feedback = input.parentElement.querySelector('.invalid-feedback, .valid-feedback');
        if (feedback) {
            feedback.remove();
        }
    }

    // Mostrar feedback
    function mostrarFeedback(input, mensaje, esValido) {
        // Eliminar feedback anterior
        const feedbackAnterior = input.parentElement.querySelector('.invalid-feedback, .valid-feedback');
        if (feedbackAnterior) {
            feedbackAnterior.remove();
        }

        // Crear nuevo feedback
        const feedback = document.createElement('div');
        feedback.className = esValido ? 'valid-feedback' : 'invalid-feedback';
        feedback.textContent = mensaje;
        feedback.style.display = 'block';

        input.parentElement.appendChild(feedback);
    }

    // Validar formulario completo
    function validarFormulario(form) {
        let valido = true;
        const inputs = form.querySelectorAll('input, select, textarea');

        inputs.forEach(input => {
            if (input.hasAttribute('required') && input.value.trim() === '') {
                marcarInvalido(input, '⚠️ Este campo es obligatorio');
                valido = false;
            }

            if (input.classList.contains('is-invalid')) {
                valido = false;
            }
        });

        return valido;
    }

    // Mostrar mensaje de error general
    function mostrarMensajeError(mensaje) {
        // Buscar o crear contenedor de mensajes
        let contenedor = document.querySelector('.messages-container');
        if (!contenedor) {
            contenedor = document.createElement('div');
            contenedor.className = 'messages-container';
            contenedor.style.position = 'fixed';
            contenedor.style.top = '20px';
            contenedor.style.right = '20px';
            contenedor.style.zIndex = '9999';
            document.body.appendChild(contenedor);
        }

        // Crear alerta
        const alerta = document.createElement('div');
        alerta.className = 'alert alert-danger alert-dismissible fade show';
        alerta.style.minWidth = '300px';
        alerta.innerHTML = `
            ${mensaje}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        `;

        contenedor.appendChild(alerta);

        // Auto-cerrar después de 5 segundos
        setTimeout(() => {
            alerta.remove();
        }, 5000);
    }

    // Formatear números automáticamente
    document.querySelectorAll('input[name*="precio"], input[name*="valor"]').forEach(input => {
        input.addEventListener('blur', function() {
            if (this.value && !isNaN(this.value)) {
                this.value = parseFloat(this.value).toFixed(2);
            }
        });
    });

    // Solo números en campos numéricos
    document.querySelectorAll('input[type="number"], input[name*="telefono"], input[name*="cedula"], input[name*="nit"]').forEach(input => {
        input.addEventListener('keypress', function(e) {
            if (!/[0-9]/.test(e.key) && e.key !== 'Backspace' && e.key !== 'Delete' && e.key !== 'Tab') {
                e.preventDefault();
            }
        });
    });

    // Contador de caracteres
    document.querySelectorAll('textarea[maxlength]').forEach(textarea => {
        const maxLength = textarea.getAttribute('maxlength');
        const contador = document.createElement('small');
        contador.className = 'form-text text-muted';
        contador.textContent = `0 / ${maxLength} caracteres`;
        textarea.parentElement.appendChild(contador);

        textarea.addEventListener('input', function() {
            contador.textContent = `${this.value.length} / ${maxLength} caracteres`;
            if (this.value.length >= maxLength * 0.9) {
                contador.style.color = '#ff4757';
            } else {
                contador.style.color = '#6c757d';
            }
        });
    });
});

