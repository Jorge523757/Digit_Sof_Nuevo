document.addEventListener('DOMContentLoaded', function () {
    // ========== INITIALIZE AOS ANIMATIONS ==========
    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 1000,
            easing: 'ease-in-out',
            once: true,
            offset: 100
        });
    }

    // ========== BRIGHTNESS CONTROLS ==========
    let brightnessLevel = 4; // Nivel inicial (0-10)
    const overlay = document.getElementById('heroOverlay');
    const brightnessIndicator = document.getElementById('brightnessLevel');
    const btnDecrease = document.getElementById('brightnessDecrease');
    const btnIncrease = document.getElementById('brightnessIncrease');

    function updateBrightness() {
        // Actualizar clases del overlay
        overlay.className = 'hero-overlay brightness-' + brightnessLevel;

        // Actualizar indicador visual
        if (brightnessIndicator) {
            const percentage = (brightnessLevel / 10) * 100;
            brightnessIndicator.style.width = percentage + '%';
        }

        // Guardar preferencia
        localStorage.setItem('heroBrightness', brightnessLevel);
    }

    if (btnDecrease) {
        btnDecrease.addEventListener('click', function() {
            if (brightnessLevel > 0) {
                brightnessLevel--;
                updateBrightness();
                showBrightnessNotification('🌙 Fondo oscurecido');
            }
        });
    }

    if (btnIncrease) {
        btnIncrease.addEventListener('click', function() {
            if (brightnessLevel < 10) {
                brightnessLevel++;
                updateBrightness();
                showBrightnessNotification('☀️ Fondo aclarado');
            }
        });
    }

    // Cargar brillo guardado
    const savedBrightness = localStorage.getItem('heroBrightness');
    if (savedBrightness !== null) {
        brightnessLevel = parseInt(savedBrightness);
        updateBrightness();
    } else {
        updateBrightness();
    }

    function showBrightnessNotification(message) {
        const existing = document.querySelector('.brightness-notification');
        if (existing) existing.remove();

        const notification = document.createElement('div');
        notification.className = 'brightness-notification';
        notification.textContent = message;
        notification.style.cssText = `
            position: fixed;
            top: 100px;
            left: 210px;
            background: rgba(0, 0, 0, 0.8);
            color: white;
            padding: 10px 20px;
            border-radius: 20px;
            font-size: 0.9rem;
            font-weight: 600;
            z-index: 10001;
            animation: fadeIn 0.3s ease;
            backdrop-filter: blur(10px);
        `;
        document.body.appendChild(notification);

        setTimeout(() => {
            notification.style.animation = 'fadeOut 0.3s ease';
            setTimeout(() => notification.remove(), 300);
        }, 2000);
    }

    // ========== MENU TOGGLE ==========
    const menuToggle = document.querySelector('.menu-toggle');
    const nav = document.querySelector('nav ul');

    if (menuToggle) {
        menuToggle.addEventListener('click', function () {
            nav.classList.toggle('active');
            this.querySelector('i').classList.toggle('fa-times');
            this.querySelector('i').classList.toggle('fa-bars');
        });
    }

    // ========== SMOOTH SCROLLING ==========
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();

            if (this.getAttribute('href') === '#') return;

            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                window.scrollTo({
                    top: target.offsetTop - 80,
                    behavior: 'smooth'
                });

                // Close mobile menu if open
                if (nav && nav.classList.contains('active')) {
                    nav.classList.remove('active');
                    if (menuToggle) {
                        menuToggle.querySelector('i').classList.remove('fa-times');
                        menuToggle.querySelector('i').classList.add('fa-bars');
                    }
                }
            }
        });
    });

    // ========== HEADER SCROLL EFFECT ==========
    const header = document.querySelector('header');
    window.addEventListener('scroll', function () {
        if (window.scrollY > 100) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });

    // ========== SIDEBAR TOGGLE ==========
    const sidebar = document.querySelector('.sidebar');
    const sidebarOverlay = document.querySelector('.sidebar-overlay');
    const sidebarToggle = document.getElementById('menuToggle');
    const closeSidebar = document.querySelector('.close-sidebar');
    const body = document.body;

    console.log('Sidebar elements:', {
        sidebar: !!sidebar,
        overlay: !!sidebarOverlay,
        toggle: !!sidebarToggle,
        close: !!closeSidebar
    });

    // Abrir menú lateral
    if (sidebarToggle) {
        sidebarToggle.addEventListener('click', function (e) {
            e.preventDefault();
            console.log('Opening sidebar...');

            if (sidebar) sidebar.classList.add('open');
            if (sidebarOverlay) sidebarOverlay.classList.add('open');
            if (body) body.classList.add('menu-open');
        });
    } else {
        console.error('Sidebar toggle button not found!');
    }

    // Cerrar menú lateral
    if (closeSidebar) {
        closeSidebar.addEventListener('click', function () {
            console.log('Closing sidebar...');
            if (sidebar) sidebar.classList.remove('open');
            if (sidebarOverlay) sidebarOverlay.classList.remove('open');
            if (body) body.classList.remove('menu-open');
        });
    }

    // Cerrar al hacer clic fuera
    if (sidebarOverlay) {
        sidebarOverlay.addEventListener('click', function () {
            console.log('Closing sidebar via overlay...');
            if (sidebar) sidebar.classList.remove('open');
            sidebarOverlay.classList.remove('open');
            if (body) body.classList.remove('menu-open');
        });
    }

    // Cerrar con tecla ESC
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && sidebar && sidebar.classList.contains('open')) {
            console.log('Closing sidebar via ESC...');
            sidebar.classList.remove('open');
            if (sidebarOverlay) sidebarOverlay.classList.remove('open');
            if (body) body.classList.remove('menu-open');
        }
    });

    // ========== MODAL LOGIN ==========
    const modal = document.getElementById('loginModal');
    const btnIngreso = document.getElementById('ingresoBtn');
    const closeModal = document.querySelector('.close');

    console.log('╔════════════════════════════════╗');
    console.log('║   DIAGNÓSTICO MODAL LOGIN      ║');
    console.log('╠════════════════════════════════╣');
    console.log('║ Modal:       ', modal ? '✅ Encontrado' : '❌ NO encontrado');
    console.log('║ Btn Ingreso: ', btnIngreso ? '✅ Encontrado' : '❌ NO encontrado');
    console.log('║ Btn Cerrar:  ', closeModal ? '✅ Encontrado' : '❌ NO encontrado');
    console.log('╚════════════════════════════════╝');

    // Abrir modal
    if (btnIngreso) {
        console.log('✅ Agregando event listener al botón Ingreso');
        btnIngreso.addEventListener('click', function (e) {
            e.preventDefault();
            console.log('🚀 CLICK EN BOTÓN INGRESO - Abriendo modal...');
            if (modal) {
                modal.style.display = 'block';
                document.body.style.overflow = 'hidden'; // Evitar scroll
                console.log('✅ Modal mostrado exitosamente');
            } else {
                console.error('❌ ERROR: Modal no encontrado al hacer click!');
            }
        });
    } else {
        console.error('❌ ERROR CRÍTICO: Botón Ingreso (ingresoBtn) no encontrado!');
        console.log('🔍 Buscando el botón manualmente...');
        const allLinks = document.querySelectorAll('a');
        console.log('📋 Todos los enlaces encontrados:', allLinks.length);
        allLinks.forEach((link, index) => {
            if (link.textContent.includes('Ingreso')) {
                console.log(`   ${index}: ${link.textContent} - ID: ${link.id || 'SIN ID'}`);
            }
        });
    }

    // Cerrar modal
    if (closeModal) {
        closeModal.addEventListener('click', function () {
            console.log('Closing login modal...');
            if (modal) {
                modal.style.display = 'none';
                document.body.style.overflow = 'auto'; // Restaurar scroll
            }
        });
    }

    // Cerrar al hacer clic fuera
    window.addEventListener('click', function (event) {
        if (event.target === modal) {
            console.log('Closing modal via overlay...');
            modal.style.display = 'none';
            document.body.style.overflow = 'auto';
        }
    });

    // Cerrar con ESC
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && modal && modal.style.display === 'block') {
            console.log('Closing modal via ESC...');
            modal.style.display = 'none';
            document.body.style.overflow = 'auto';
        }
    });

    // ========== LOGIN FORM ==========
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

            console.log('Inicio de sesión:', { user, pass, role });
            alert(`Bienvenido ${user} (${roleMessage})`);

            modal.style.display = 'none';
            this.reset();
        });
    }

    // ========== ROLE SELECTOR ==========
    const roleOptions = document.querySelectorAll('.role-option');
    roleOptions.forEach(option => {
        option.addEventListener('click', function () {
            roleOptions.forEach(opt => opt.classList.remove('selected'));
            this.classList.add('selected');
            this.querySelector('input').checked = true;
        });
    });

    // Seleccionar cliente por defecto
    const clientOption = document.getElementById('client-option');
    if (clientOption) {
        clientOption.classList.add('selected');
    }

    // ========== PRODUCT DATA ==========
    const products = [
        {
            id: 1,
            title: 'Laptop HP EliteBook',
            price: 899.99,
            category: 'laptop',
            image: 'https://images.unsplash.com/photo-1593642632823-8f785ba67e45?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60'
        },
        {
            id: 2,
            title: 'Computadora Dell OptiPlex',
            price: 699.99,
            category: 'desktop',
            image: 'https://images.unsplash.com/photo-1551645120-d70bfe850c07?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60'
        },
        {
            id: 3,
            title: 'Teclado Mecánico RGB',
            price: 89.99,
            category: 'accesorio',
            image: 'https://images.unsplash.com/photo-1587829741301-dc798b83add3?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60'
        },
        {
            id: 4,
            title: 'Laptop Lenovo ThinkPad',
            price: 1099.99,
            category: 'laptop',
            image: 'https://images.unsplash.com/photo-1593642702821-c8da6771f0c6?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60'
        },
        {
            id: 5,
            title: 'Monitor 27" 4K',
            price: 349.99,
            category: 'accesorio',
            image: 'https://images.unsplash.com/photo-1546538915-a9e2c8d1dc41?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60'
        },
        {
            id: 6,
            title: 'Computadora All-in-One',
            price: 799.99,
            category: 'desktop',
            image: 'https://images.unsplash.com/photo-1586211082275-c412e00a1d3a?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60'
        },
        {
            id: 7,
            title: 'Mouse Inalámbrico',
            price: 29.99,
            category: 'accesorio',
            image: 'https://images.unsplash.com/photo-1527814050087-3793815479db?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60'
        },
        {
            id: 8,
            title: 'Laptop ASUS VivoBook',
            price: 749.99,
            category: 'laptop',
            image: 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60'
        }
    ];

    // ========== DISPLAY PRODUCTS ==========
    const productsGrid = document.querySelector('.products-grid');

    function displayProducts(productsToDisplay) {
        if (!productsGrid) return;

        productsGrid.innerHTML = '';

        if (productsToDisplay.length === 0) {
            productsGrid.innerHTML = '<p class="no-products">No hay productos disponibles en esta categoría.</p>';
            return;
        }

        productsToDisplay.forEach(product => {
            const productCard = document.createElement('div');
            productCard.className = 'product-card';
            productCard.innerHTML = `
                <div class="product-image">
                    <img src="${product.image}" alt="${product.title}">
                </div>
                <div class="product-info">
                    <span class="product-category">${getCategoryName(product.category)}</span>
                    <h3 class="product-title">${product.title}</h3>
                    <p class="product-price">$${product.price.toFixed(2)}</p>
                    <a href="#contacto" class="product-btn">Consultar</a>
                </div>
            `;
            productsGrid.appendChild(productCard);
        });
    }

    function getCategoryName(category) {
        switch (category) {
            case 'laptop': return 'Laptop';
            case 'desktop': return 'Computadora';
            case 'accesorio': return 'Accesorio';
            default: return category;
        }
    }

    // Display all products initially
    displayProducts(products);

    // ========== PRODUCT FILTER ==========
    const filterBtns = document.querySelectorAll('.filter-btn');
    filterBtns.forEach(btn => {
        btn.addEventListener('click', function () {
            filterBtns.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');

            const filter = this.dataset.filter;

            if (filter === 'all') {
                displayProducts(products);
            } else {
                const filteredProducts = products.filter(product => product.category === filter);
                displayProducts(filteredProducts);
            }
        });
    });

    // ========== COUNTER ANIMATION ==========
    const counters = document.querySelectorAll('.counter');
    const speed = 200;

    function animateCounters() {
        counters.forEach(counter => {
            const target = +counter.getAttribute('data-target');
            const count = +counter.innerText;
            const increment = target / speed;

            if (count < target) {
                counter.innerText = Math.ceil(count + increment);
                setTimeout(animateCounters, 1);
            } else {
                counter.innerText = target;
            }
        });
    }

    // Start counter animation when about section is in view
    const aboutSection = document.querySelector('#nosotros');
    if (aboutSection) {
        const observer = new IntersectionObserver((entries) => {
            if (entries[0].isIntersecting) {
                animateCounters();
                observer.unobserve(aboutSection);
            }
        }, { threshold: 0.5 });

        observer.observe(aboutSection);
    }

    // ========== CONTACT FORM ==========
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function (e) {
            e.preventDefault();

            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const phone = document.getElementById('phone').value;
            const message = document.getElementById('message').value;

            alert(`Gracias ${name}, hemos recibido tu mensaje. Nos pondremos en contacto contigo pronto.`);
            contactForm.reset();
        });
    }

    // ========== NEWSLETTER FORM ==========
    const newsletterForm = document.getElementById('newsletterForm');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function (e) {
            e.preventDefault();

            const email = this.querySelector('input').value;
            alert(`Gracias por suscribirte con el email: ${email}`);
            this.reset();
        });
    }

    // ========== PARALLAX EFFECT ==========
    window.addEventListener('scroll', function() {
        const scrolled = window.pageYOffset;
        const parallaxElements = document.querySelectorAll('.hero-background');

        parallaxElements.forEach(element => {
            element.style.transform = `translateY(${scrolled * 0.5}px)`;
        });
    });

    // ========== SCROLL TO TOP BUTTON ==========
    const createScrollTopButton = () => {
        const scrollBtn = document.createElement('button');
        scrollBtn.className = 'scroll-to-top';
        scrollBtn.innerHTML = '<i class="fas fa-arrow-up"></i>';
        scrollBtn.setAttribute('aria-label', 'Volver arriba');
        document.body.appendChild(scrollBtn);

        window.addEventListener('scroll', () => {
            if (window.pageYOffset > 300) {
                scrollBtn.classList.add('visible');
            } else {
                scrollBtn.classList.remove('visible');
            }
        });

        scrollBtn.addEventListener('click', () => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    };

    createScrollTopButton();

    // ========== TYPING EFFECT FOR HERO SUBTITLE ==========
    const typeWriter = (element, text, speed = 50) => {
        let i = 0;
        element.innerHTML = '';

        const type = () => {
            if (i < text.length) {
                element.innerHTML += text.charAt(i);
                i++;
                setTimeout(type, speed);
            }
        };

        type();
    };

    const heroSubtitle = document.querySelector('.hero-subtitle');
    if (heroSubtitle) {
        const originalText = heroSubtitle.textContent;
        setTimeout(() => {
            typeWriter(heroSubtitle, originalText, 100);
        }, 1500);
    }

    // ========== LOADING ANIMATION ==========
    window.addEventListener('load', () => {
        document.body.classList.add('loaded');
    });

    // ========== ACTIVE NAV LINK ON SCROLL ==========
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('nav ul li a');

    window.addEventListener('scroll', () => {
        let current = '';

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;

            if (window.pageYOffset >= sectionTop - 200) {
                current = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${current}`) {
                link.classList.add('active');
            }
        });
    });

    // ========== CONFIRMACIÓN DE CARGA ==========
    console.log('✅ Landing.js cargado completamente');
    console.log('📋 Resumen de elementos:');
    console.log('  - Sidebar:', !!sidebar ? '✓' : '✗');
    console.log('  - Modal:', !!modal ? '✓' : '✗');
    console.log('  - Botón Menú:', !!sidebarToggle ? '✓' : '✗');
    console.log('  - Botón Ingreso:', !!btnIngreso ? '✓' : '✗');
});

