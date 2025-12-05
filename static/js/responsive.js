/**
 * DIGITSOFT - Responsive JavaScript
 * Maneja la responsividad de todos los módulos
 */

(function() {
    'use strict';

    // ============================================
    // SIDEBAR RESPONSIVE
    // ============================================

    function initSidebarResponsive() {
        const sidebar = document.getElementById('sidebar');
        const sidebarOverlay = document.getElementById('sidebarOverlay');
        const closeSidebar = document.getElementById('closeSidebar');
        const toggleSidebar = document.getElementById('toggleSidebar');

        if (!sidebar) return;

        // Toggle sidebar en móvil
        if (toggleSidebar) {
            toggleSidebar.addEventListener('click', function() {
                sidebar.classList.add('show');
                if (sidebarOverlay) {
                    sidebarOverlay.classList.add('show');
                }
                document.body.style.overflow = 'hidden';
            });
        }

        // Cerrar sidebar
        if (closeSidebar) {
            closeSidebar.addEventListener('click', function() {
                closeSidebar();
            });
        }

        // Cerrar con overlay
        if (sidebarOverlay) {
            sidebarOverlay.addEventListener('click', function() {
                closeSidebarFunc();
            });
        }

        function closeSidebarFunc() {
            sidebar.classList.remove('show');
            if (sidebarOverlay) {
                sidebarOverlay.classList.remove('show');
            }
            document.body.style.overflow = '';
        }

        // Cerrar sidebar al cambiar a desktop
        window.addEventListener('resize', function() {
            if (window.innerWidth >= 992) {
                closeSidebarFunc();
            }
        });
    }

    // ============================================
    // TABLAS RESPONSIVE
    // ============================================

    function initTablesResponsive() {
        const tables = document.querySelectorAll('table:not(.table-responsive-mobile)');

        tables.forEach(function(table) {
            // Envolver tabla en contenedor responsive si no existe
            if (!table.parentElement.classList.contains('table-responsive')) {
                const wrapper = document.createElement('div');
                wrapper.className = 'table-responsive';
                table.parentNode.insertBefore(wrapper, table);
                wrapper.appendChild(table);
            }

            // Agregar data-label a las celdas para versión móvil
            if (window.innerWidth <= 768) {
                const headers = table.querySelectorAll('thead th');
                const rows = table.querySelectorAll('tbody tr');

                rows.forEach(function(row) {
                    const cells = row.querySelectorAll('td');
                    cells.forEach(function(cell, index) {
                        if (headers[index]) {
                            cell.setAttribute('data-label', headers[index].textContent);
                        }
                    });
                });
            }
        });
    }

    // ============================================
    // NAVEGACIÓN RESPONSIVE
    // ============================================

    function initNavResponsive() {
        const navbarToggler = document.querySelectorAll('.navbar-toggler');

        navbarToggler.forEach(function(toggler) {
            toggler.addEventListener('click', function() {
                const target = this.getAttribute('data-target') || this.getAttribute('data-bs-target');
                const collapse = document.querySelector(target);

                if (collapse) {
                    collapse.classList.toggle('show');
                }
            });
        });
    }

    // ============================================
    // TOOLTIPS EN MÓVIL
    // ============================================

    function initTooltipsResponsive() {
        if (window.innerWidth <= 768) {
            // Deshabilitar tooltips en móvil para evitar problemas de touch
            const tooltips = document.querySelectorAll('[data-bs-toggle="tooltip"]');
            tooltips.forEach(function(element) {
                element.removeAttribute('data-bs-toggle');
                element.removeAttribute('title');
            });
        }
    }

    // ============================================
    // DROPDOWN RESPONSIVE
    // ============================================

    function initDropdownResponsive() {
        const dropdowns = document.querySelectorAll('.dropdown-toggle');

        dropdowns.forEach(function(dropdown) {
            dropdown.addEventListener('click', function(e) {
                if (window.innerWidth <= 576) {
                    e.preventDefault();
                    const menu = this.nextElementSibling;
                    if (menu && menu.classList.contains('dropdown-menu')) {
                        menu.classList.toggle('show');
                    }
                }
            });
        });

        // Cerrar dropdown al hacer click fuera
        document.addEventListener('click', function(e) {
            if (!e.target.matches('.dropdown-toggle')) {
                const dropdownMenus = document.querySelectorAll('.dropdown-menu.show');
                dropdownMenus.forEach(function(menu) {
                    menu.classList.remove('show');
                });
            }
        });
    }

    // ============================================
    // MODAL RESPONSIVE
    // ============================================

    function initModalResponsive() {
        const modals = document.querySelectorAll('.modal');

        modals.forEach(function(modal) {
            modal.addEventListener('show.bs.modal', function() {
                if (window.innerWidth <= 576) {
                    // Ajustar modal para móvil
                    const modalDialog = modal.querySelector('.modal-dialog');
                    if (modalDialog) {
                        modalDialog.style.margin = '0.5rem';
                        modalDialog.style.maxWidth = 'calc(100% - 1rem)';
                    }
                }
            });
        });
    }

    // ============================================
    // BÚSQUEDA RESPONSIVE
    // ============================================

    function initSearchResponsive() {
        const searchInputs = document.querySelectorAll('input[type="search"], .search-bar input');

        searchInputs.forEach(function(input) {
            // Evitar zoom en iOS
            if (/iPhone|iPad|iPod/i.test(navigator.userAgent)) {
                input.style.fontSize = '16px';
            }

            // Limpiar búsqueda en móvil
            if (window.innerWidth <= 576) {
                const clearBtn = document.createElement('button');
                clearBtn.className = 'btn btn-link position-absolute end-0 top-50 translate-middle-y';
                clearBtn.innerHTML = '<i class="fas fa-times"></i>';
                clearBtn.style.display = 'none';

                input.parentElement.style.position = 'relative';
                input.parentElement.appendChild(clearBtn);

                input.addEventListener('input', function() {
                    clearBtn.style.display = this.value ? 'block' : 'none';
                });

                clearBtn.addEventListener('click', function() {
                    input.value = '';
                    this.style.display = 'none';
                    input.focus();
                });
            }
        });
    }

    // ============================================
    // CARDS RESPONSIVE
    // ============================================

    function initCardsResponsive() {
        const cardGroups = document.querySelectorAll('.card-group, .card-deck');

        cardGroups.forEach(function(group) {
            if (window.innerWidth <= 768) {
                group.classList.remove('card-group', 'card-deck');
                const cards = group.querySelectorAll('.card');
                cards.forEach(function(card) {
                    card.style.marginBottom = '1rem';
                });
            }
        });
    }

    // ============================================
    // PAGINACIÓN RESPONSIVE
    // ============================================

    function initPaginationResponsive() {
        const paginations = document.querySelectorAll('.pagination');

        paginations.forEach(function(pagination) {
            if (window.innerWidth <= 576) {
                const items = pagination.querySelectorAll('.page-item');
                const activeIndex = Array.from(items).findIndex(item =>
                    item.classList.contains('active')
                );

                items.forEach(function(item, index) {
                    // Mostrar solo: primero, anterior, activo, siguiente, último
                    const isFirst = index === 0;
                    const isLast = index === items.length - 1;
                    const isPrev = item.querySelector('.page-link')?.textContent.includes('Anterior');
                    const isNext = item.querySelector('.page-link')?.textContent.includes('Siguiente');
                    const isActive = item.classList.contains('active');

                    if (!isFirst && !isLast && !isPrev && !isNext && !isActive) {
                        item.style.display = 'none';
                    }
                });
            }
        });
    }

    // ============================================
    // FILTROS RESPONSIVE
    // ============================================

    function initFiltersResponsive() {
        if (window.innerWidth <= 768) {
            const filterSections = document.querySelectorAll('.filter-section, .filter-row');

            filterSections.forEach(function(section) {
                const inputs = section.querySelectorAll('.form-control, .form-select');
                inputs.forEach(function(input) {
                    input.classList.add('mb-2');
                });

                const buttons = section.querySelectorAll('.btn');
                buttons.forEach(function(button) {
                    button.classList.add('w-100', 'mb-2');
                });
            });
        }
    }

    // ============================================
    // TABLA ACCIONES RESPONSIVE
    // ============================================

    function initTableActionsResponsive() {
        if (window.innerWidth <= 576) {
            const actionCells = document.querySelectorAll('td .btn-group, td .action-buttons');

            actionCells.forEach(function(cell) {
                const buttons = cell.querySelectorAll('.btn');
                buttons.forEach(function(button) {
                    // Convertir botones a iconos solo
                    const icon = button.querySelector('i');
                    if (icon) {
                        const text = button.childNodes;
                        text.forEach(function(node) {
                            if (node.nodeType === Node.TEXT_NODE) {
                                node.remove();
                            }
                        });
                    }
                });
            });
        }
    }

    // ============================================
    // OPTIMIZACIÓN DE IMÁGENES
    // ============================================

    function initImagesResponsive() {
        const images = document.querySelectorAll('img:not(.img-fluid)');

        images.forEach(function(img) {
            img.classList.add('img-fluid');

            // Lazy loading
            if ('loading' in HTMLImageElement.prototype) {
                img.loading = 'lazy';
            }
        });
    }

    // ============================================
    // ORIENTACIÓN DEL DISPOSITIVO
    // ============================================

    function handleOrientationChange() {
        window.addEventListener('orientationchange', function() {
            // Recargar ciertas funciones al cambiar orientación
            setTimeout(function() {
                initTablesResponsive();
                initCardsResponsive();
                initPaginationResponsive();
            }, 200);
        });
    }

    // ============================================
    // TOUCH GESTURES
    // ============================================

    function initTouchGestures() {
        if ('ontouchstart' in window) {
            // Mejorar experiencia táctil
            const buttons = document.querySelectorAll('button, .btn, a');

            buttons.forEach(function(button) {
                button.addEventListener('touchstart', function() {
                    this.style.opacity = '0.7';
                });

                button.addEventListener('touchend', function() {
                    this.style.opacity = '1';
                });
            });
        }
    }

    // ============================================
    // VIEWPORT HEIGHT FIX (Para iOS)
    // ============================================

    function fixViewportHeight() {
        // Fix para 100vh en móviles
        const setVH = function() {
            const vh = window.innerHeight * 0.01;
            document.documentElement.style.setProperty('--vh', `${vh}px`);
        };

        setVH();
        window.addEventListener('resize', setVH);
        window.addEventListener('orientationchange', setVH);
    }

    // ============================================
    // INICIALIZACIÓN
    // ============================================

    function init() {
        // Esperar a que el DOM esté listo
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', initAll);
        } else {
            initAll();
        }
    }

    function initAll() {
        console.log('Iniciando responsive.js...');

        initSidebarResponsive();
        initTablesResponsive();
        initNavResponsive();
        initTooltipsResponsive();
        initDropdownResponsive();
        initModalResponsive();
        initSearchResponsive();
        initCardsResponsive();
        initPaginationResponsive();
        initFiltersResponsive();
        initTableActionsResponsive();
        initImagesResponsive();
        handleOrientationChange();
        initTouchGestures();
        fixViewportHeight();

        console.log('Responsive.js inicializado correctamente');

        // Re-inicializar en resize (con debounce)
        let resizeTimer;
        window.addEventListener('resize', function() {
            clearTimeout(resizeTimer);
            resizeTimer = setTimeout(function() {
                initTablesResponsive();
                initCardsResponsive();
                initPaginationResponsive();
                initFiltersResponsive();
            }, 250);
        });
    }

    // Iniciar
    init();

})();

