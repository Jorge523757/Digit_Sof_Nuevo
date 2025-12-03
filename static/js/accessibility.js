// ========== ACCESSIBILITY WIDGET ==========
class AccessibilityWidget {
    constructor() {
        this.settings = {
            fontSize: 1,
            darkMode: false,
            highContrast: false,
            grayscale: false,
            highlightLinks: false,
            increasedSpacing: false,
            screenReader: false
        };

        this.init();
        this.loadSettings();
        this.setupKeyboardNavigation();
    }

    init() {
        console.log('🎯 Accessibility Widget initialized');

        // Establecer atributos ARIA
        this.setupARIA();

        // Toggle del panel
        this.setupToggle();

        // Botones de tamaño
        const fontLarge = document.getElementById('fontLarge');
        const fontSmall = document.getElementById('fontSmall');

        if (fontLarge) {
            fontLarge.addEventListener('click', (e) => {
                e.preventDefault();
                this.increaseFontSize();
            });
            fontLarge.setAttribute('aria-label', 'Aumentar tamaño de texto');
        }

        if (fontSmall) {
            fontSmall.addEventListener('click', (e) => {
                e.preventDefault();
                this.decreaseFontSize();
            });
            fontSmall.setAttribute('aria-label', 'Disminuir tamaño de texto');
        }

        // Botones de color
        const highContrast = document.getElementById('highContrast');
        const darkMode = document.getElementById('darkMode');
        const grayscale = document.getElementById('grayscale');

        if (highContrast) {
            highContrast.addEventListener('click', (e) => {
                e.preventDefault();
                this.toggleHighContrast();
            });
            highContrast.setAttribute('aria-label', 'Activar alto contraste');
        }

        if (darkMode) {
            darkMode.addEventListener('click', (e) => {
                e.preventDefault();
                this.toggleDarkMode();
            });
            darkMode.setAttribute('aria-label', 'Activar modo oscuro');
        }

        if (grayscale) {
            grayscale.addEventListener('click', (e) => {
                e.preventDefault();
                this.toggleGrayscale();
            });
            grayscale.setAttribute('aria-label', 'Activar escala de grises');
        }

        // Otras opciones
        const highlightLinks = document.getElementById('highlightLinks');
        const screenReader = document.getElementById('screenReader');
        const increasedSpacing = document.getElementById('increasedSpacing');

        if (highlightLinks) {
            highlightLinks.addEventListener('click', (e) => {
                e.preventDefault();
                this.toggleHighlightLinks();
            });
            highlightLinks.setAttribute('aria-label', 'Resaltar enlaces');
        }

        if (screenReader) {
            screenReader.addEventListener('click', (e) => {
                e.preventDefault();
                this.toggleScreenReader();
            });
            screenReader.setAttribute('aria-label', 'Activar lector de pantalla');
        }

        if (increasedSpacing) {
            increasedSpacing.addEventListener('click', (e) => {
                e.preventDefault();
                this.toggleIncreasedSpacing();
            });
            increasedSpacing.setAttribute('aria-label', 'Aumentar espaciado');
        }

        // Reset
        const resetBtn = document.getElementById('resetAccessibility');
        if (resetBtn) {
            resetBtn.addEventListener('click', (e) => {
                e.preventDefault();
                this.reset();
            });
            resetBtn.setAttribute('aria-label', 'Restablecer configuración de accesibilidad');
        }
    }

    setupARIA() {
        const panel = document.getElementById('accessibilityPanel');
        if (panel) {
            panel.setAttribute('role', 'toolbar');
            panel.setAttribute('aria-label', 'Herramientas de accesibilidad');
        }

        // Establecer roles para todos los botones
        document.querySelectorAll('.accessibility-btn, .reset-btn').forEach(btn => {
            btn.setAttribute('role', 'button');
            btn.setAttribute('tabindex', '0');
        });
    }

    setupToggle() {
        const toggleBtn = document.getElementById('accessibilityToggle');
        const closeBtn = document.getElementById('accessibilityClose');
        const panel = document.getElementById('accessibilityPanel');

        if (toggleBtn && panel) {
            // Abrir/Cerrar con botón toggle
            toggleBtn.addEventListener('click', (e) => {
                e.preventDefault();
                this.togglePanel();
            });

            // Cerrar con botón X
            if (closeBtn) {
                closeBtn.addEventListener('click', (e) => {
                    e.preventDefault();
                    this.closePanel();
                });
            }

            // Cerrar con ESC
            document.addEventListener('keydown', (e) => {
                if (e.key === 'Escape' && !panel.classList.contains('hidden')) {
                    this.closePanel();
                }
            });

            // Cerrar al hacer clic fuera
            document.addEventListener('click', (e) => {
                if (!panel.contains(e.target) &&
                    !toggleBtn.contains(e.target) &&
                    !panel.classList.contains('hidden')) {
                    this.closePanel();
                }
            });
        }
    }

    togglePanel() {
        const panel = document.getElementById('accessibilityPanel');
        const toggleBtn = document.getElementById('accessibilityToggle');

        if (panel && toggleBtn) {
            const isHidden = panel.classList.contains('hidden');

            if (isHidden) {
                this.openPanel();
            } else {
                this.closePanel();
            }
        }
    }

    openPanel() {
        const panel = document.getElementById('accessibilityPanel');
        const toggleBtn = document.getElementById('accessibilityToggle');

        if (panel && toggleBtn) {
            panel.classList.remove('hidden');
            toggleBtn.setAttribute('aria-expanded', 'true');
            toggleBtn.setAttribute('aria-label', 'Cerrar panel de accesibilidad');
        }
    }

    closePanel() {
        const panel = document.getElementById('accessibilityPanel');
        const toggleBtn = document.getElementById('accessibilityToggle');

        if (panel && toggleBtn) {
            panel.classList.add('hidden');
            toggleBtn.setAttribute('aria-expanded', 'false');
            toggleBtn.setAttribute('aria-label', 'Abrir panel de accesibilidad');
        }
    }

    setupKeyboardNavigation() {
        // Permitir navegación con teclado
        document.querySelectorAll('.accessibility-btn, .reset-btn').forEach(btn => {
            btn.addEventListener('keydown', (e) => {
                if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    btn.click();
                }
            });
        });

        // Atajos de teclado globales
        document.addEventListener('keydown', (e) => {
            // Ctrl + Alt + R para resetear
            if (e.ctrlKey && e.altKey && e.key === 'r') {
                e.preventDefault();
                this.reset();
            }
            // Ctrl + Alt + D para modo oscuro
            if (e.ctrlKey && e.altKey && e.key === 'd') {
                e.preventDefault();
                this.toggleDarkMode();
            }
            // Ctrl + Alt + + para aumentar texto
            if (e.ctrlKey && e.altKey && e.key === '+') {
                e.preventDefault();
                this.increaseFontSize();
            }
            // Ctrl + Alt + - para disminuir texto
            if (e.ctrlKey && e.altKey && e.key === '-') {
                e.preventDefault();
                this.decreaseFontSize();
            }
        });
    }

    increaseFontSize() {
        if (this.settings.fontSize < 1.4) {
            this.settings.fontSize += 0.1;
            this.applyFontSize();
            this.saveSettings();
            const percentage = Math.round(this.settings.fontSize * 100);
            this.showNotification(`✓ Texto aumentado al ${percentage}%`);
            this.updateARIA('fontLarge', `Tamaño actual: ${percentage}%`);
        } else {
            this.showNotification('⚠️ Tamaño máximo alcanzado (140%)');
        }
    }

    decreaseFontSize() {
        if (this.settings.fontSize > 0.8) {
            this.settings.fontSize -= 0.1;
            this.applyFontSize();
            this.saveSettings();
            const percentage = Math.round(this.settings.fontSize * 100);
            this.showNotification(`✓ Texto reducido al ${percentage}%`);
            this.updateARIA('fontSmall', `Tamaño actual: ${percentage}%`);
        } else {
            this.showNotification('⚠️ Tamaño mínimo alcanzado (80%)');
        }
    }

    applyFontSize() {
        document.documentElement.style.fontSize = (16 * this.settings.fontSize) + 'px';
    }

    toggleDarkMode() {
        this.settings.darkMode = !this.settings.darkMode;
        const btn = document.getElementById('darkMode');

        if (this.settings.darkMode) {
            document.body.classList.add('dark-mode');
            if (btn) {
                btn.classList.add('active');
                btn.setAttribute('aria-pressed', 'true');
            }

            // Desactivar otros modos
            this.settings.highContrast = false;
            this.settings.grayscale = false;
            document.body.classList.remove('high-contrast', 'grayscale');

            const hcBtn = document.getElementById('highContrast');
            const gsBtn = document.getElementById('grayscale');
            if (hcBtn) {
                hcBtn.classList.remove('active');
                hcBtn.setAttribute('aria-pressed', 'false');
            }
            if (gsBtn) {
                gsBtn.classList.remove('active');
                gsBtn.setAttribute('aria-pressed', 'false');
            }

            this.showNotification('🌙 Modo oscuro activado');
        } else {
            document.body.classList.remove('dark-mode');
            if (btn) {
                btn.classList.remove('active');
                btn.setAttribute('aria-pressed', 'false');
            }
            this.showNotification('☀️ Modo oscuro desactivado');
        }

        this.saveSettings();
    }

    toggleHighContrast() {
        this.settings.highContrast = !this.settings.highContrast;
        const btn = document.getElementById('highContrast');

        if (this.settings.highContrast) {
            document.body.classList.add('high-contrast');
            if (btn) {
                btn.classList.add('active');
                btn.setAttribute('aria-pressed', 'true');
            }

            // Desactivar otros modos
            this.settings.darkMode = false;
            this.settings.grayscale = false;
            document.body.classList.remove('dark-mode', 'grayscale');

            const dmBtn = document.getElementById('darkMode');
            const gsBtn = document.getElementById('grayscale');
            if (dmBtn) {
                dmBtn.classList.remove('active');
                dmBtn.setAttribute('aria-pressed', 'false');
            }
            if (gsBtn) {
                gsBtn.classList.remove('active');
                gsBtn.setAttribute('aria-pressed', 'false');
            }

            this.showNotification('⚫⚪ Alto contraste activado');
        } else {
            document.body.classList.remove('high-contrast');
            if (btn) {
                btn.classList.remove('active');
                btn.setAttribute('aria-pressed', 'false');
            }
            this.showNotification('⚫⚪ Alto contraste desactivado');
        }

        this.saveSettings();
    }

    toggleGrayscale() {
        this.settings.grayscale = !this.settings.grayscale;
        const btn = document.getElementById('grayscale');

        if (this.settings.grayscale) {
            document.body.classList.add('grayscale');
            if (btn) {
                btn.classList.add('active');
                btn.setAttribute('aria-pressed', 'true');
            }

            // Desactivar otros modos
            this.settings.darkMode = false;
            this.settings.highContrast = false;
            document.body.classList.remove('dark-mode', 'high-contrast');

            const dmBtn = document.getElementById('darkMode');
            const hcBtn = document.getElementById('highContrast');
            if (dmBtn) {
                dmBtn.classList.remove('active');
                dmBtn.setAttribute('aria-pressed', 'false');
            }
            if (hcBtn) {
                hcBtn.classList.remove('active');
                hcBtn.setAttribute('aria-pressed', 'false');
            }

            this.showNotification('🎨 Escala de grises activada');
        } else {
            document.body.classList.remove('grayscale');
            if (btn) {
                btn.classList.remove('active');
                btn.setAttribute('aria-pressed', 'false');
            }
            this.showNotification('🎨 Escala de grises desactivada');
        }

        this.saveSettings();
    }

    toggleHighlightLinks() {
        this.settings.highlightLinks = !this.settings.highlightLinks;
        const btn = document.getElementById('highlightLinks');

        if (this.settings.highlightLinks) {
            document.body.classList.add('highlight-links');
            if (btn) {
                btn.classList.add('active');
                btn.setAttribute('aria-pressed', 'true');
            }
            this.showNotification('🔗 Enlaces resaltados');
        } else {
            document.body.classList.remove('highlight-links');
            if (btn) {
                btn.classList.remove('active');
                btn.setAttribute('aria-pressed', 'false');
            }
            this.showNotification('🔗 Enlaces normales');
        }

        this.saveSettings();
    }

    toggleScreenReader() {
        this.settings.screenReader = !this.settings.screenReader;
        const btn = document.getElementById('screenReader');

        if (btn) {
            btn.classList.toggle('active');
            btn.setAttribute('aria-pressed', this.settings.screenReader ? 'true' : 'false');
        }

        if (this.settings.screenReader) {
            this.showNotification('🔊 Lector de pantalla activado');
            this.announceForScreenReader('Lector de pantalla activado. Navegación mejorada habilitada.');
        } else {
            this.showNotification('🔇 Lector de pantalla desactivado');
        }

        this.saveSettings();
    }

    toggleIncreasedSpacing() {
        this.settings.increasedSpacing = !this.settings.increasedSpacing;
        const btn = document.getElementById('increasedSpacing');

        if (this.settings.increasedSpacing) {
            document.body.classList.add('increased-spacing');
            if (btn) {
                btn.classList.add('active');
                btn.setAttribute('aria-pressed', 'true');
            }
            this.showNotification('↔️ Espaciado aumentado');
        } else {
            document.body.classList.remove('increased-spacing');
            if (btn) {
                btn.classList.remove('active');
                btn.setAttribute('aria-pressed', 'false');
            }
            this.showNotification('↔️ Espaciado normal');
        }

        this.saveSettings();
    }

    reset() {
        // Remover todas las clases
        document.body.classList.remove(
            'dark-mode',
            'high-contrast',
            'grayscale',
            'highlight-links',
            'increased-spacing'
        );

        // Resetear tamaño de fuente
        document.documentElement.style.fontSize = '16px';

        // Remover activos de botones y actualizar ARIA
        document.querySelectorAll('.accessibility-btn, .reset-btn').forEach(btn => {
            btn.classList.remove('active');
            btn.setAttribute('aria-pressed', 'false');
        });

        // Resetear settings
        this.settings = {
            fontSize: 1,
            darkMode: false,
            highContrast: false,
            grayscale: false,
            highlightLinks: false,
            increasedSpacing: false,
            screenReader: false
        };

        this.saveSettings();
        this.showNotification('🔄 Configuración restablecida al 100%');
        this.announceForScreenReader('Todas las configuraciones de accesibilidad han sido restablecidas');
    }

    updateARIA(buttonId, message) {
        const btn = document.getElementById(buttonId);
        if (btn) {
            btn.setAttribute('aria-label', message);
        }
    }

    announceForScreenReader(message) {
        // Crear región ARIA live para anuncios
        let liveRegion = document.getElementById('aria-live-region');

        if (!liveRegion) {
            liveRegion = document.createElement('div');
            liveRegion.id = 'aria-live-region';
            liveRegion.setAttribute('aria-live', 'polite');
            liveRegion.setAttribute('aria-atomic', 'true');
            liveRegion.style.position = 'absolute';
            liveRegion.style.left = '-10000px';
            liveRegion.style.width = '1px';
            liveRegion.style.height = '1px';
            liveRegion.style.overflow = 'hidden';
            document.body.appendChild(liveRegion);
        }

        // Limpiar y agregar nuevo mensaje
        liveRegion.textContent = '';
        setTimeout(() => {
            liveRegion.textContent = message;
        }, 100);
    }

    saveSettings() {
        try {
            localStorage.setItem('accessibilitySettings', JSON.stringify(this.settings));
        } catch (e) {
            console.error('Error saving settings:', e);
        }
    }

    loadSettings() {
        try {
            const saved = localStorage.getItem('accessibilitySettings');
            if (saved) {
                this.settings = JSON.parse(saved);
                console.log('📥 Configuración de accesibilidad cargada:', this.settings);

                // Aplicar configuración guardada
                if (this.settings.fontSize !== 1) {
                    this.applyFontSize();
                }

                if (this.settings.darkMode) {
                    document.body.classList.add('dark-mode');
                    const btn = document.getElementById('darkMode');
                    if (btn) {
                        btn.classList.add('active');
                        btn.setAttribute('aria-pressed', 'true');
                    }
                }

                if (this.settings.highContrast) {
                    document.body.classList.add('high-contrast');
                    const btn = document.getElementById('highContrast');
                    if (btn) {
                        btn.classList.add('active');
                        btn.setAttribute('aria-pressed', 'true');
                    }
                }

                if (this.settings.grayscale) {
                    document.body.classList.add('grayscale');
                    const btn = document.getElementById('grayscale');
                    if (btn) {
                        btn.classList.add('active');
                        btn.setAttribute('aria-pressed', 'true');
                    }
                }

                if (this.settings.highlightLinks) {
                    document.body.classList.add('highlight-links');
                    const btn = document.getElementById('highlightLinks');
                    if (btn) {
                        btn.classList.add('active');
                        btn.setAttribute('aria-pressed', 'true');
                    }
                }

                if (this.settings.increasedSpacing) {
                    document.body.classList.add('increased-spacing');
                    const btn = document.getElementById('increasedSpacing');
                    if (btn) {
                        btn.classList.add('active');
                        btn.setAttribute('aria-pressed', 'true');
                    }
                }

                if (this.settings.screenReader) {
                    const btn = document.getElementById('screenReader');
                    if (btn) {
                        btn.classList.add('active');
                        btn.setAttribute('aria-pressed', 'true');
                    }
                }

                // Anunciar si hay preferencias activas
                const activeSettings = this.getActiveSettingsCount();
                if (activeSettings > 0) {
                    console.log(`✅ ${activeSettings} configuración(es) de accesibilidad activa(s)`);
                }
            }
        } catch (e) {
            console.error('❌ Error loading settings:', e);
        }
    }

    getActiveSettingsCount() {
        let count = 0;
        if (this.settings.fontSize !== 1) count++;
        if (this.settings.darkMode) count++;
        if (this.settings.highContrast) count++;
        if (this.settings.grayscale) count++;
        if (this.settings.highlightLinks) count++;
        if (this.settings.increasedSpacing) count++;
        if (this.settings.screenReader) count++;
        return count;
    }

    showNotification(message) {
        // Remover notificación anterior si existe
        const existing = document.querySelector('.accessibility-notification');
        if (existing) {
            existing.remove();
        }

        // Crear elemento de notificación
        const notification = document.createElement('div');
        notification.className = 'accessibility-notification';
        notification.setAttribute('role', 'alert');
        notification.setAttribute('aria-live', 'assertive');

        // Estilos responsivos
        const isMobile = window.innerWidth <= 768;
        const notificationStyles = `
            position: fixed;
            top: ${isMobile ? '20px' : '100px'};
            right: ${isMobile ? '50%' : '120px'};
            ${isMobile ? 'transform: translateX(50%);' : ''}
            background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
            color: white;
            padding: ${isMobile ? '12px 18px' : '15px 25px'};
            border-radius: 8px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.3);
            z-index: 10000;
            animation: slideInRight 0.3s ease;
            font-weight: 600;
            font-size: ${isMobile ? '0.9rem' : '1rem'};
            max-width: ${isMobile ? '90%' : '300px'};
            text-align: center;
            border: 2px solid rgba(255, 255, 255, 0.3);
        `;

        notification.style.cssText = notificationStyles;
        notification.textContent = message;
        document.body.appendChild(notification);

        // Remover después de 3 segundos
        setTimeout(() => {
            notification.style.animation = 'slideOutRight 0.3s ease';
            setTimeout(() => {
                if (notification.parentNode) {
                    notification.remove();
                }
            }, 300);
        }, 3000);
    }
}

// Inicializar cuando el DOM esté listo
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() {
        window.accessibilityWidget = new AccessibilityWidget();
        console.log('♿ Widget de Accesibilidad listo');
    });
} else {
    window.accessibilityWidget = new AccessibilityWidget();
    console.log('♿ Widget de Accesibilidad listo');
}

