// Menu móvil
document.addEventListener('DOMContentLoaded', function() {
    const mobileMenu = document.getElementById('mobileMenu');
    const navMenu = document.getElementById('navMenu');
    
    if (mobileMenu && navMenu) {
        mobileMenu.addEventListener('click', function () {
            navMenu.classList.toggle('show');
        });
    }

    // Modal de inicio de sesión
    const modal = document.getElementById('loginModal');
    const btn = document.getElementById('ingresoBtn');
    const span = document.getElementsByClassName('close')[0];

    // Abrir modal al hacer clic en Ingreso
    if (btn && modal) {
        btn.onclick = function (e) {
            e.preventDefault();
            modal.style.display = 'block';
        }
    }

    // Cerrar modal al hacer clic en la X
    if (span && modal) {
        span.onclick = function () {
            modal.style.display = 'none';
        }
    }

    // Cerrar modal al hacer clic fuera del contenido
    window.onclick = function (event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    }
    
    // ================================
    // DROPDOWN DE PRODUCTOS (Versión Simplificada)
    // ================================
    
    const dropdown = document.querySelector('.dropdown');
    const dropbtn = dropdown ? dropdown.querySelector('.dropbtn') : null;
    
    if (dropdown && dropbtn) {
        console.log('Inicializando dropdown de productos...');
        
        // Manejar clic en el botón principal
        dropbtn.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            
            console.log('Clic en dropdown button');
            
            // Toggle del dropdown
            if (dropdown.classList.contains('active')) {
                dropdown.classList.remove('active');
                console.log('Dropdown cerrado');
            } else {
                // Cerrar otros dropdowns
                document.querySelectorAll('.dropdown.active').forEach(other => {
                    if (other !== dropdown) {
                        other.classList.remove('active');
                    }
                });
                
                dropdown.classList.add('active');
                console.log('Dropdown abierto');
            }
        });
        
        // Cerrar al hacer clic fuera
        document.addEventListener('click', function(e) {
            if (!dropdown.contains(e.target)) {
                dropdown.classList.remove('active');
            }
        });
        
        // Prevenir que el dropdown se cierre al hacer clic dentro
        const dropdownContent = dropdown.querySelector('.dropdown-content');
        if (dropdownContent) {
            dropdownContent.addEventListener('click', function(e) {
                e.stopPropagation();
            });
        }
        
        console.log('Dropdown inicializado correctamente');
    } else {
        console.log('Elementos del dropdown no encontrados');
    }

    // Manejar el envío del formulario de inicio de sesión
    const loginForm = document.getElementById('login-form');
    if (loginForm) {
        loginForm.addEventListener('submit', function (event) {
            event.preventDefault();

            const user = document.getElementById('username').value;
            const pass = document.getElementById('password').value;
            const role = document.querySelector('input[name="role"]:checked').value;

            if (!user.includes("@") || !user.includes(".")) {
                alert('Por favor, ingrese un correo electrónico válido.');
                return;
            }

            if (pass.length < 8) {
                alert('La contraseña debe tener al menos 8 caracteres.');
                return;
            }

            let roleMessage;
            switch (role) {
                case 'admin':
                    roleMessage = 'Administrador';
                    break;
                case 'technician':
                    roleMessage = 'Técnico';
                    break;
                default:
                    roleMessage = 'Cliente';
            }

            // Aquí normalmente enviarías los datos al servidor para autenticación
            console.log('Inicio de sesión:', { user, pass, role });

            // Mostrar mensaje de éxito
            alert(`Bienvenido ${user} (${roleMessage})`);

            // Cerrar el modal y limpiar el formulario
            modal.style.display = 'none';
            this.reset();

            // Aquí podrías redirigir al usuario según su rol
            // window.location.href = 'dashboard.html';
        });
    }

    // Selección de roles
    const roleOptions = document.querySelectorAll('.role-option');
    roleOptions.forEach(option => {
        option.addEventListener('click', function () {
            roleOptions.forEach(opt => opt.classList.remove('selected'));
            this.classList.add('selected');
        });
    });

    // Seleccionar cliente por defecto
    const clientOption = document.getElementById('client-option');
    if (clientOption) {
        clientOption.classList.add('selected');
    }

    // =============================================
    // FUNCIONALIDADES DE AUTENTICACIÓN
    // =============================================

    // Manejo del dropdown de usuario autenticado
    const userMenuToggle = document.getElementById('userMenuToggle');
    const userMenu = document.querySelector('.user-menu');
    const userDropdown = document.getElementById('userDropdown');

    if (userMenuToggle && userMenu) {
        // Toggle del menú desplegable
        userMenuToggle.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            
            // Cerrar otros menús abiertos si los hay
            document.querySelectorAll('.user-menu.active').forEach(menu => {
                if (menu !== userMenu) {
                    menu.classList.remove('active');
                }
            });
            
            userMenu.classList.toggle('active');
            
            // Agregar clase para animación
            if (userMenu.classList.contains('active')) {
                userDropdown?.classList.add('opening');
                setTimeout(() => {
                    userDropdown?.classList.remove('opening');
                }, 300);
            }
        });

        // Cerrar dropdown al hacer clic fuera
        document.addEventListener('click', function(e) {
            if (!userMenu.contains(e.target)) {
                userMenu.classList.remove('active');
            }
        });

        // Prevenir que el dropdown se cierre al hacer clic en él
        if (userDropdown) {
            userDropdown.addEventListener('click', function(e) {
                e.stopPropagation();
            });
            
            // Mejorar la interacción con los enlaces del dropdown
            const dropdownLinks = userDropdown.querySelectorAll('a');
            dropdownLinks.forEach(link => {
                link.addEventListener('click', function(e) {
                    // Si es el botón de carrito, no cerrar el menú
                    if (this.getAttribute('onclick')?.includes('DigitSoftCart')) {
                        e.stopPropagation();
                        return;
                    }
                    
                    // Para otros enlaces, cerrar el menú después de un pequeño delay
                    setTimeout(() => {
                        userMenu.classList.remove('active');
                    }, 150);
                });
            });
        }

        // Cerrar con la tecla Escape
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape' && userMenu.classList.contains('active')) {
                userMenu.classList.remove('active');
                userMenuToggle.focus();
            }
        });

        // Mejorar accesibilidad
        userMenuToggle.setAttribute('aria-haspopup', 'true');
        userMenuToggle.setAttribute('aria-expanded', 'false');
        
        // Actualizar aria-expanded cuando se abre/cierra
        const observer = new MutationObserver(function(mutations) {
            mutations.forEach(function(mutation) {
                if (mutation.type === 'attributes' && mutation.attributeName === 'class') {
                    const isActive = userMenu.classList.contains('active');
                    userMenuToggle.setAttribute('aria-expanded', isActive.toString());
                }
            });
        });
        
        observer.observe(userMenu, { attributes: true });
    }

    // Función para actualizar el contador del carrito en el header
    function updateCartCounter() {
        const cartCount = document.getElementById('cart-count');
        if (cartCount && window.DigitSoftCart) {
            const itemCount = DigitSoftCart.getItemCount();
            if (itemCount > 0) {
                cartCount.textContent = itemCount;
                cartCount.style.display = 'flex';
            } else {
                cartCount.style.display = 'none';
            }
        }
    }

    // Actualizar el contador del carrito cuando se carga la página
    if (typeof DigitSoftCart !== 'undefined') {
        updateCartCounter();
        
        // Actualizar cuando se modifique el carrito
        document.addEventListener('cartUpdated', updateCartCounter);
    }

    // Mostrar mensajes de estado en el header
    function showHeaderMessage(message, type = 'info', duration = 5000) {
        // Remover mensaje existente si hay uno
        const existingMessage = document.querySelector('.header-message');
        if (existingMessage) {
            existingMessage.remove();
        }

        // Crear nuevo mensaje
        const messageDiv = document.createElement('div');
        messageDiv.className = `header-message ${type}`;
        messageDiv.textContent = message;

        // Insertar antes del header
        const header = document.querySelector('header');
        if (header) {
            document.body.insertBefore(messageDiv, header);

            // Remover después del tiempo especificado
            setTimeout(() => {
                if (messageDiv && messageDiv.parentNode) {
                    messageDiv.style.animation = 'slideUp 0.3s ease';
                    setTimeout(() => {
                        messageDiv.remove();
                    }, 300);
                }
            }, duration);
        }
    }

    // Contador del carrito
    function updateCartCount(count = 0) {
        let cartCountElement = document.querySelector('.cart-count');
        const cartLink = document.querySelector('a[href*="carrito"]');

        if (count > 0) {
            if (!cartCountElement && cartLink) {
                // Crear contador si no existe
                cartCountElement = document.createElement('span');
                cartCountElement.className = 'cart-count';
                cartLink.style.position = 'relative';
                cartLink.appendChild(cartCountElement);
            }
            
            if (cartCountElement) {
                cartCountElement.textContent = count;
                cartCountElement.style.display = 'flex';
            }
        } else {
            if (cartCountElement) {
                cartCountElement.style.display = 'none';
            }
        }
    }

    // Función para logout con confirmación
    const logoutLinks = document.querySelectorAll('a[href*="logout"]');
    logoutLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            if (confirm('¿Estás seguro de que deseas cerrar sesión?')) {
                // Crear y enviar formulario POST para logout
                const form = document.createElement('form');
                form.method = 'POST';
                form.action = this.href;
                
                // Agregar CSRF token
                const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]');
                if (csrfToken) {
                    const csrfInput = document.createElement('input');
                    csrfInput.type = 'hidden';
                    csrfInput.name = 'csrfmiddlewaretoken';
                    csrfInput.value = csrfToken.value;
                    form.appendChild(csrfInput);
                }
                
                document.body.appendChild(form);
                form.submit();
            }
        });
    });

    // Función de inicialización del carrito (si existe)
    if (typeof DigitSoftCart !== 'undefined') {
        const cart = new DigitSoftCart();
        updateCartCount(cart.getTotalItems());

        // Escuchar cambios en el carrito
        document.addEventListener('cartUpdated', function(e) {
            updateCartCount(e.detail.totalItems);
        });
    }

    // Exponer funciones globales
    window.showHeaderMessage = showHeaderMessage;
    window.updateCartCount = updateCartCount;
});

// CSS adicional para animación slideUp
const style = document.createElement('style');
style.textContent = `
    @keyframes slideUp {
        0% {
            transform: translateY(0);
            opacity: 1;
        }
        100% {
            transform: translateY(-100%);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);