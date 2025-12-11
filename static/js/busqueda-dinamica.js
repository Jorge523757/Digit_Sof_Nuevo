/**
 * BÚSQUEDA DINÁMICA DE PRODUCTOS
 * Búsqueda en tiempo real mientras el usuario escribe
 */

let searchTimeout = null;
let currentCategory = 'todas';

// Inicializar búsqueda dinámica
function initDynamicSearch() {
    const searchInput = document.querySelector('#searchInput, input[name="q"]');
    const categoryFilter = document.querySelector('#categoryFilter, select[name="categoria"]');
    const resultsContainer = document.querySelector('#productResults, .products-grid');

    if (!searchInput) return;

    // Búsqueda al escribir
    searchInput.addEventListener('input', function() {
        clearTimeout(searchTimeout);
        const query = this.value.trim();

        // Esperar 500ms después de que el usuario deje de escribir
        searchTimeout = setTimeout(() => {
            performSearch(query, currentCategory);
        }, 500);
    });

    // Filtro por categoría
    if (categoryFilter) {
        categoryFilter.addEventListener('change', function() {
            currentCategory = this.value;
            const query = searchInput.value.trim();
            performSearch(query, currentCategory);
        });
    }

    // Búsqueda al enviar formulario
    const searchForm = document.querySelector('form[role="search"], .search-form');
    if (searchForm) {
        searchForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const query = searchInput.value.trim();
            performSearch(query, currentCategory);
        });
    }
}

// Realizar búsqueda
async function performSearch(query, categoria = 'todas') {
    const resultsContainer = document.querySelector('#productResults, .products-grid, .row');
    const noResultsDiv = document.querySelector('.no-results, .empty-state');
    const loadingDiv = document.querySelector('.loading-search');

    if (!resultsContainer) return;

    // Mostrar loading
    showLoading(resultsContainer);

    try {
        // Construir URL
        let url = '/productos/api/buscar/?';
        if (query) url += `q=${encodeURIComponent(query)}&`;
        if (categoria && categoria !== 'todas') url += `categoria=${encodeURIComponent(categoria)}`;

        const response = await fetch(url);
        const data = await response.json();

        if (data.success) {
            displayResults(data.productos, resultsContainer);
            updateResultsCount(data.total);
        } else {
            showError('Error al buscar productos');
        }
    } catch (error) {
        console.error('Error en búsqueda:', error);
        showError('Error de conexión');
    }
}

// Mostrar loading
function showLoading(container) {
    container.innerHTML = `
        <div class="col-12 text-center py-5 loading-search">
            <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Buscando...</span>
            </div>
            <p class="mt-3 text-muted">Buscando productos...</p>
        </div>
    `;
}

// Mostrar resultados
function displayResults(productos, container) {
    if (productos.length === 0) {
        container.innerHTML = `
            <div class="col-12 text-center py-5 no-results">
                <i class="fas fa-search fa-3x text-muted mb-3"></i>
                <h4>No se encontraron productos</h4>
                <p class="text-muted">Intenta con otros términos de búsqueda</p>
                <button onclick="clearSearch()" class="btn btn-primary">
                    <i class="fas fa-redo"></i> Ver todos los productos
                </button>
            </div>
        `;
        return;
    }

    // Generar HTML de productos
    let html = '';
    productos.forEach(producto => {
        html += generateProductCard(producto);
    });

    container.innerHTML = html;

    // Reinicializar eventos de carrito si existen
    if (typeof initCartButtons === 'function') {
        initCartButtons();
    }
}

// Generar tarjeta de producto
function generateProductCard(producto) {
    const imagen = producto.imagen || '/static/images/no-image.png';
    const stockClass = producto.stock > 10 ? 'stock-high' : producto.stock > 0 ? 'stock-medium' : 'stock-low';
    const stockText = producto.stock > 0 ? `${producto.stock} disponibles` : 'Agotado';

    return `
        <div class="col-md-4 col-lg-3 mb-4 product-item" data-product-id="${producto.id}">
            <div class="product-card">
                <div class="product-image">
                    ${producto.imagen ? `<img src="${imagen}" alt="${producto.nombre}">` : '<i class="fas fa-image no-image"></i>'}
                </div>
                <div class="product-body p-3">
                    <h6 class="product-title">${producto.nombre}</h6>
                    ${producto.marca ? `<small class="text-muted">${producto.marca}</small>` : ''}
                    <div class="product-price mt-2">
                        <span class="price-sale">$${producto.precio.toFixed(2)}</span>
                    </div>
                    <div class="product-stock mt-2">
                        <span class="stock-badge ${stockClass}">
                            <i class="fas fa-box"></i> ${stockText}
                        </span>
                    </div>
                    <div class="product-actions mt-3">
                        <a href="${producto.url}" class="btn btn-sm btn-outline-primary">
                            <i class="fas fa-eye"></i> Ver
                        </a>
                        ${producto.stock > 0 ? `
                        <button onclick="agregarAlCarrito(${producto.id})" class="btn btn-sm btn-primary">
                            <i class="fas fa-cart-plus"></i> Agregar
                        </button>
                        ` : '<button class="btn btn-sm btn-secondary" disabled>Agotado</button>'}
                    </div>
                </div>
            </div>
        </div>
    `;
}

// Actualizar contador de resultados
function updateResultsCount(total) {
    const countElement = document.querySelector('#resultsCount, .results-count');
    if (countElement) {
        countElement.textContent = `${total} producto${total !== 1 ? 's' : ''} encontrado${total !== 1 ? 's' : ''}`;
    }
}

// Limpiar búsqueda
function clearSearch() {
    const searchInput = document.querySelector('#searchInput, input[name="q"]');
    const categoryFilter = document.querySelector('#categoryFilter, select[name="categoria"]');

    if (searchInput) searchInput.value = '';
    if (categoryFilter) categoryFilter.value = 'todas';

    currentCategory = 'todas';
    performSearch('', 'todas');
}

// Mostrar error
function showError(message) {
    const container = document.querySelector('#productResults, .products-grid, .row');
    if (container) {
        container.innerHTML = `
            <div class="col-12">
                <div class="alert alert-danger">
                    <i class="fas fa-exclamation-triangle"></i> ${message}
                </div>
            </div>
        `;
    }
}

// Inicializar al cargar la página
document.addEventListener('DOMContentLoaded', function() {
    initDynamicSearch();
    console.log('✅ Búsqueda dinámica inicializada');
});

// Exportar funciones
window.performSearch = performSearch;
window.clearSearch = clearSearch;

