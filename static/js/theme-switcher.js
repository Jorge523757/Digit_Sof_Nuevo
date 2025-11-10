// Theme Switcher - Sistema de cambio de tema claro/oscuro

class ThemeSwitcher {
    constructor() {
        this.theme = localStorage.getItem('theme') || 'light';
        this.init();
    }

    init() {
        // Aplicar tema guardado
        this.applyTheme(this.theme);

        // Crear botón de cambio de tema
        this.createToggleButton();

        // Crear indicador de tema por módulo
        this.createModuleIndicator();

        // Event listeners
        this.attachEventListeners();
    }

    createToggleButton() {
        const button = document.createElement('button');
        button.className = 'theme-toggle';
        button.setAttribute('aria-label', 'Cambiar tema');
        button.innerHTML = `
            <i class="fas fa-moon"></i>
            <i class="fas fa-sun"></i>
            <span class="theme-tooltip">Cambiar tema</span>
        `;
        document.body.appendChild(button);
        this.toggleButton = button;
    }

    createModuleIndicator() {
        const moduleName = this.getCurrentModuleName();
        if (!moduleName) return;

        const indicator = document.createElement('div');
        indicator.className = 'module-theme-indicator';
        indicator.innerHTML = `
            <i class="fas fa-palette"></i>
            <span>${moduleName}</span>
            <i class="fas fa-${this.theme === 'dark' ? 'moon' : 'sun'}"></i>
        `;

        const container = document.querySelector('.container-fluid, .container');
        if (container) {
            container.style.position = 'relative';
            container.insertBefore(indicator, container.firstChild);
            this.moduleIndicator = indicator;
        }
    }

    getCurrentModuleName() {
        const path = window.location.pathname;
        const modules = {
            '/clientes': 'Gestión de Clientes',
            '/tecnicos': 'Gestión de Técnicos',
            '/ordenes': 'Órdenes de Servicio',
            '/productos': 'Gestión de Productos',
            '/proveedores': 'Gestión de Proveedores',
            '/garantias': 'Gestión de Garantías',
            '/compras': 'Gestión de Compras',
            '/ventas': 'Gestión de Ventas',
            '/facturacion': 'Facturación',
            '/equipos': 'Gestión de Equipos',
            '/capacitaciones': 'Capacitaciones',
            '/dashboard': 'Dashboard'
        };

        for (const [route, name] of Object.entries(modules)) {
            if (path.includes(route)) {
                return name;
            }
        }
        return null;
    }

    attachEventListeners() {
        this.toggleButton.addEventListener('click', () => this.toggleTheme());

        // Escuchar cambios de tema desde otros tabs
        window.addEventListener('storage', (e) => {
            if (e.key === 'theme') {
                this.theme = e.newValue;
                this.applyTheme(this.theme);
                this.updateModuleIndicator();
            }
        });

        // Detectar preferencia del sistema
        const darkModeMediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
        darkModeMediaQuery.addEventListener('change', (e) => {
            if (!localStorage.getItem('theme')) {
                this.theme = e.matches ? 'dark' : 'light';
                this.applyTheme(this.theme);
                this.updateModuleIndicator();
            }
        });
    }

    toggleTheme() {
        this.theme = this.theme === 'light' ? 'dark' : 'light';
        this.applyTheme(this.theme);
        this.saveTheme();
        this.updateModuleIndicator();
        this.animateToggle();
    }

    applyTheme(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        document.body.setAttribute('data-theme', theme);

        // Actualizar meta theme-color para navegadores móviles
        this.updateMetaThemeColor(theme);
    }

    saveTheme() {
        localStorage.setItem('theme', this.theme);

        // Emitir evento personalizado para otros componentes
        window.dispatchEvent(new CustomEvent('themeChanged', {
            detail: { theme: this.theme }
        }));
    }

    updateMetaThemeColor(theme) {
        let metaThemeColor = document.querySelector('meta[name="theme-color"]');
        if (!metaThemeColor) {
            metaThemeColor = document.createElement('meta');
            metaThemeColor.name = 'theme-color';
            document.head.appendChild(metaThemeColor);
        }
        metaThemeColor.content = theme === 'dark' ? '#1a1d20' : '#ffffff';
    }

    updateModuleIndicator() {
        if (this.moduleIndicator) {
            const icon = this.moduleIndicator.querySelector('i:last-child');
            if (icon) {
                icon.className = `fas fa-${this.theme === 'dark' ? 'moon' : 'sun'}`;
            }
        }
    }

    animateToggle() {
        this.toggleButton.style.transform = 'scale(1.2) rotate(360deg)';
        setTimeout(() => {
            this.toggleButton.style.transform = '';
        }, 300);
    }

    // Método para obtener el tema actual
    getCurrentTheme() {
        return this.theme;
    }

    // Método para forzar un tema específico
    setTheme(theme) {
        if (theme === 'light' || theme === 'dark') {
            this.theme = theme;
            this.applyTheme(theme);
            this.saveTheme();
            this.updateModuleIndicator();
        }
    }
}

// Inicializar el theme switcher cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', function() {
    window.themeSwitcher = new ThemeSwitcher();

    // Añadir clase de animación de entrada
    setTimeout(() => {
        const toggleButton = document.querySelector('.theme-toggle');
        if (toggleButton) {
            toggleButton.style.opacity = '1';
            toggleButton.style.transform = 'scale(1)';
        }
    }, 500);
});

// Prevenir FOUC (Flash of Unstyled Content)
(function() {
    const theme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', theme);
})();

// Exportar para uso global
window.ThemeSwitcher = ThemeSwitcher;

