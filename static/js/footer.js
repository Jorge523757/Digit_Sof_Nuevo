// Manejo del newsletter
document.addEventListener('DOMContentLoaded', function() {
    const newsletterForm = document.getElementById('newsletterForm');
    
    if (newsletterForm) {
        newsletterForm.onsubmit = function (e) {
            e.preventDefault();
            const email = this.querySelector('input').value;
            
            // Validación básica del email
            if (email && email.includes('@') && email.includes('.')) {
                alert(`Gracias por suscribirte con el correo: ${email}`);
                this.reset();
            } else {
                alert('Por favor, ingresa un correo electrónico válido.');
            }
            return false;
        }
    }
});