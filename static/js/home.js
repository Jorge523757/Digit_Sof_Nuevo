document.addEventListener('DOMContentLoaded', function() {
    // Animación de contadores
    function animateCounters() {
        const counters = document.querySelectorAll('.counter');
        const speed = 200;

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

    // Lanzar animación cuando la sección "nosotros" sea visible
    let animationTriggered = false;
    function checkScroll() {
        const aboutSection = document.getElementById('nosotros');
        if (aboutSection) {
            const sectionPosition = aboutSection.getBoundingClientRect().top;
            const screenPosition = window.innerHeight / 1.3;

            if (sectionPosition < screenPosition && !animationTriggered) {
                animateCounters();
                animationTriggered = true;
            }
        }
    }

    window.addEventListener('scroll', checkScroll);

    // Filtrado de productos
    const filterBtns = document.querySelectorAll('.filter-btn');
    filterBtns.forEach(btn => {
        btn.addEventListener('click', function () {
            // Remover clase active de todos los botones
            filterBtns.forEach(btn => btn.classList.remove('active'));
            // Añadir clase active al botón clickeado
            this.classList.add('active');
            // Aquí iría la lógica para filtrar los productos
            const filter = this.getAttribute('data-filter');
            console.log('Filtrar por:', filter);
        });
    });

    // Manejo del formulario de contacto
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.onsubmit = function (e) {
            e.preventDefault();
            
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const phone = document.getElementById('phone').value;
            const message = document.getElementById('message').value;

            // Validaciones básicas
            if (!name.trim()) {
                alert('Por favor, ingresa tu nombre.');
                return;
            }

            if (!email.includes('@') || !email.includes('.')) {
                alert('Por favor, ingresa un correo electrónico válido.');
                return;
            }

            if (!message.trim()) {
                alert('Por favor, ingresa tu mensaje.');
                return;
            }

            alert('Mensaje enviado con éxito. Nos pondremos en contacto pronto.');
            this.reset();
            return false;
        }
    }
});