/**
 * Dashboard JavaScript - Sistema DIGIT SOFT
 * Maneja la funcionalidad interactiva del dashboard principal
 */

(function() {
    'use strict';

    console.log('🎯 Dashboard JS: Iniciando...');

    // ==================== CONFIGURACIÓN ====================
    const CONFIG = {
        refreshInterval: 60000, // 60 segundos
        animationDelay: 100,
        debug: true
    };

    // ==================== UTILIDADES DE DEBUG ====================
    function log(message, type = 'info') {
        if (!CONFIG.debug) return;

        const styles = {
            info: 'color: #037dc4; font-weight: bold;',
            success: 'color: #27ae60; font-weight: bold;',
            warning: 'color: #f39c12; font-weight: bold;',
            error: 'color: #e74c3c; font-weight: bold;'
        };

        console.log(`%c[Dashboard] ${message}`, styles[type] || styles.info);
    }

    // ==================== ANIMACIONES DE ENTRADA ====================
    function initAnimations() {
        log('Inicializando animaciones de entrada', 'info');

        // Animar tarjetas de estadísticas
        const statCards = document.querySelectorAll('.stat-card');
        if (statCards.length > 0) {
            log(`Encontradas ${statCards.length} tarjetas de estadísticas`, 'success');
            statCards.forEach((card, index) => {
                setTimeout(() => {
                    card.style.opacity = '0';
                    card.style.transform = 'translateY(20px)';
                    card.style.transition = 'all 0.5s ease';

                    setTimeout(() => {
                        card.style.opacity = '1';
                        card.style.transform = 'translateY(0)';
                    }, 50);
                }, index * CONFIG.animationDelay);
            });
        } else {
            log('No se encontraron tarjetas de estadísticas', 'warning');
        }

        // Animar actividades
        const activityItems = document.querySelectorAll('.activity-item');
        if (activityItems.length > 0) {
            log(`Encontrados ${activityItems.length} items de actividad`, 'success');
            activityItems.forEach((item, index) => {
                setTimeout(() => {
                    item.style.opacity = '0';
                    item.style.transform = 'translateX(-20px)';
                    item.style.transition = 'all 0.4s ease';

                    setTimeout(() => {
                        item.style.opacity = '1';
                        item.style.transform = 'translateX(0)';
                    }, 50);
                }, (statCards.length * CONFIG.animationDelay) + (index * 80));
            });
        } else {
            log('No se encontraron items de actividad', 'warning');
        }

        // Animar tareas
        const taskItems = document.querySelectorAll('.task-item');
        if (taskItems.length > 0) {
            log(`Encontradas ${taskItems.length} tareas`, 'success');
            taskItems.forEach((item, index) => {
                setTimeout(() => {
                    item.style.opacity = '0';
                    item.style.transform = 'translateX(20px)';
                    item.style.transition = 'all 0.4s ease';

                    setTimeout(() => {
                        item.style.opacity = '1';
                        item.style.transform = 'translateX(0)';
                    }, 50);
                }, (statCards.length * CONFIG.animationDelay) + (index * 80));
            });
        } else {
            log('No se encontraron tareas', 'warning');
        }
    }

    // ==================== CONTADOR ANIMADO ====================
    function animateNumbers() {
        log('Iniciando animación de números', 'info');

        const statNumbers = document.querySelectorAll('.stat-number');

        statNumbers.forEach(element => {
            const text = element.textContent.trim();
            // Extraer el número (puede tener $ o , o .)
            const match = text.match(/[\d,.]+/);

            if (!match) {
                log(`No se pudo extraer número de: "${text}"`, 'warning');
                return;
            }

            const numberStr = match[0].replace(/,/g, '');
            const finalValue = parseFloat(numberStr);

            if (isNaN(finalValue)) {
                log(`Valor no numérico: "${text}"`, 'warning');
                return;
            }

            // Determinar si es dinero
            const isCurrency = text.includes('$');
            const duration = 1000;
            const steps = 30;
            const stepValue = finalValue / steps;
            const stepDuration = duration / steps;

            let currentValue = 0;
            let currentStep = 0;

            element.textContent = isCurrency ? '$0.00' : '0';

            const interval = setInterval(() => {
                currentStep++;
                currentValue += stepValue;

                if (currentStep >= steps) {
                    currentValue = finalValue;
                    clearInterval(interval);
                }

                if (isCurrency) {
                    element.textContent = `$${currentValue.toFixed(2)}`;
                } else {
                    element.textContent = Math.round(currentValue);
                }
            }, stepDuration);

            log(`Animando número: ${text} (final: ${finalValue})`, 'success');
        });
    }

    // ==================== ACTUALIZACIÓN DE TIEMPO ====================
    function updateTimestamps() {
        const timestamps = document.querySelectorAll('.activity-time');

        if (timestamps.length === 0) return;

        log(`Actualizando ${timestamps.length} timestamps`, 'info');

        // Aquí podrías implementar lógica para actualizar los tiempos relativos
        // Por ahora solo los dejamos como están
    }

    // ==================== QUICK ACTIONS INTERACTIVIDAD ====================
    function initQuickActions() {
        log('Inicializando acciones rápidas', 'info');

        const quickActions = document.querySelectorAll('.quick-action');

        quickActions.forEach(action => {
            action.addEventListener('mouseenter', function() {
                const icon = this.querySelector('i');
                if (icon) {
                    icon.style.transform = 'scale(1.2) rotate(5deg)';
                    icon.style.transition = 'transform 0.3s ease';
                }
            });

            action.addEventListener('mouseleave', function() {
                const icon = this.querySelector('i');
                if (icon) {
                    icon.style.transform = 'scale(1) rotate(0deg)';
                }
            });
        });

        log(`${quickActions.length} acciones rápidas configuradas`, 'success');
    }

    // ==================== TOOLTIPS MEJORADOS ====================
    function initTooltips() {
        log('Inicializando tooltips', 'info');

        // Agregar tooltips a iconos de estadísticas
        const statIcons = document.querySelectorAll('.stat-icon');
        statIcons.forEach(icon => {
            icon.setAttribute('title', 'Ver detalles');
            icon.style.cursor = 'pointer';

            icon.addEventListener('click', function() {
                const card = this.closest('.stat-card');
                const label = card.querySelector('.stat-label');
                if (label) {
                    log(`Click en estadística: ${label.textContent}`, 'info');
                    // Aquí podrías agregar funcionalidad adicional
                }
            });
        });

        log(`${statIcons.length} tooltips agregados`, 'success');
    }

    // ==================== REFRESH DE DATOS ====================
    function setupAutoRefresh() {
        log(`Auto-refresh configurado cada ${CONFIG.refreshInterval/1000} segundos`, 'info');

        setInterval(() => {
            log('Actualizando datos del dashboard...', 'info');
            updateTimestamps();

            // Aquí podrías hacer una llamada AJAX para actualizar datos
            // Por ahora solo actualizamos timestamps
        }, CONFIG.refreshInterval);
    }

    // ==================== MANEJO DE ERRORES ====================
    function initErrorHandling() {
        window.addEventListener('error', function(e) {
            log(`Error detectado: ${e.message}`, 'error');
            console.error('Detalles del error:', e);
        });

        log('Manejo de errores configurado', 'success');
    }

    // ==================== DETECCIÓN DE ELEMENTOS ====================
    function detectElements() {
        log('=== DETECCIÓN DE ELEMENTOS ===', 'info');

        const elements = {
            'Welcome Banner': document.querySelector('.welcome-banner'),
            'Stat Cards': document.querySelectorAll('.stat-card'),
            'Quick Actions': document.querySelectorAll('.quick-action'),
            'Activity Items': document.querySelectorAll('.activity-item'),
            'Task Items': document.querySelectorAll('.task-item'),
            'Content Cards': document.querySelectorAll('.content-card')
        };

        Object.entries(elements).forEach(([name, element]) => {
            if (element) {
                const count = element.length !== undefined ? element.length : 1;
                log(`✓ ${name}: ${count} encontrado(s)`, 'success');
            } else {
                log(`✗ ${name}: NO encontrado`, 'warning');
            }
        });

        log('=== FIN DETECCIÓN ===', 'info');
    }

    // ==================== RESPONSIVE BEHAVIOR ====================
    function handleResponsive() {
        const handleResize = () => {
            const width = window.innerWidth;
            log(`Viewport: ${width}px`, 'info');

            if (width < 768) {
                log('Vista móvil activada', 'info');
                // Ajustes para móvil si es necesario
            } else if (width < 1200) {
                log('Vista tablet activada', 'info');
            } else {
                log('Vista escritorio activada', 'info');
            }
        };

        window.addEventListener('resize', debounce(handleResize, 250));
        handleResize(); // Ejecutar al inicio
    }

    // ==================== UTILITY: DEBOUNCE ====================
    function debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }

    // ==================== INICIALIZACIÓN PRINCIPAL ====================
    function init() {
        log('=================================', 'info');
        log('🚀 DASHBOARD INITIALIZATION START', 'info');
        log('=================================', 'info');

        try {
            // Detectar elementos del DOM
            detectElements();

            // Inicializar características
            initErrorHandling();
            initAnimations();
            initQuickActions();
            initTooltips();
            handleResponsive();

            // Animar números después de un pequeño delay
            setTimeout(() => {
                animateNumbers();
            }, 500);

            // Configurar auto-refresh
            setupAutoRefresh();

            log('=================================', 'success');
            log('✅ DASHBOARD LISTO Y OPERATIVO', 'success');
            log('=================================', 'success');

        } catch (error) {
            log(`ERROR EN INICIALIZACIÓN: ${error.message}`, 'error');
            console.error('Stack trace:', error);
        }
    }

    // ==================== AUTO-INICIO ====================
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
        log('Esperando DOMContentLoaded...', 'info');
    } else {
        log('DOM ya cargado, iniciando inmediatamente', 'info');
        init();
    }

})();

