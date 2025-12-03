// Menu lateral
document.addEventListener('DOMContentLoaded', function() {
    const sidebar = document.querySelector('.sidebar');
    const sidebarOverlay = document.querySelector('.sidebar-overlay');
    const menuToggle = document.getElementById('menuToggle');
    const closeSidebar = document.querySelector('.close-sidebar');
    const body = document.body;

    // Abrir menú lateral
    if (menuToggle) {
        menuToggle.addEventListener('click', function (e) {
            e.preventDefault();
            sidebar.classList.add('open');
            sidebarOverlay.classList.add('open');
            body.classList.add('menu-open');
        });
    }

    // Cerrar menú lateral
    if (closeSidebar) {
        closeSidebar.addEventListener('click', function () {
            sidebar.classList.remove('open');
            sidebarOverlay.classList.remove('open');
            body.classList.remove('menu-open');
        });
    }

    // Cerrar al hacer clic fuera
    if (sidebarOverlay) {
        sidebarOverlay.addEventListener('click', function () {
            sidebar.classList.remove('open');
            sidebarOverlay.classList.remove('open');
            body.classList.remove('menu-open');
        });
    }

    // Submenús
    const menuItems = document.querySelectorAll('.menu-item.with-submenu');
    menuItems.forEach(item => {
        item.addEventListener('click', function (e) {
            if (e.target.tagName === 'A') {
                e.preventDefault();
                this.classList.toggle('open');
                const submenu = this.querySelector('.submenu');
                submenu.style.display = submenu.style.display === 'block' ? 'none' : 'block';
            }
        });
    });
});