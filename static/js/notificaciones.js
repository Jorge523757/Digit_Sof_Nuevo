/**
 * DIGITSOFT - Sistema de Notificaciones
 * Manejo de notificaciones en tiempo real
 */

console.log('📢 [Notificaciones] Módulo cargado');

// Configuración
const NOTIFICACIONES_CONFIG = {
    url: '/usuarios/notificaciones/json/',
    intervalo: 30000, // 30 segundos
    maxNotificaciones: 10
};

// Estado
let notificacionesTimer = null;

/**
 * Cargar notificaciones desde el servidor
 */
function cargarNotificaciones() {
    console.log('📢 [Notificaciones] Cargando notificaciones...');

    fetch(NOTIFICACIONES_CONFIG.url)
        .then(response => {
            console.log('📢 [Notificaciones] Respuesta recibida:', response.status);

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            return response.json();
        })
        .then(data => {
            console.log('📢 [Notificaciones] Datos recibidos:', data);
            actualizarUINotificaciones(data);
        })
        .catch(error => {
            console.error('❌ [Notificaciones] Error al cargar:', error);
            mostrarErrorNotificaciones(error);
        });
}

/**
 * Actualizar la interfaz con las notificaciones
 */
function actualizarUINotificaciones(data) {
    const badge = document.getElementById('notif-count');
    const lista = document.getElementById('notificaciones-lista');

    if (!badge || !lista) {
        console.error('❌ [Notificaciones] Elementos DOM no encontrados');
        return;
    }

    // Actualizar badge contador
    badge.textContent = data.count || 0;
    badge.style.display = (data.count && data.count > 0) ? 'inline' : 'none';

    console.log(`📢 [Notificaciones] Badge actualizado: ${data.count} no leídas`);

    // Limpiar lista actual
    lista.innerHTML = '';

    // Verificar si hay notificaciones
    if (!data.notificaciones || data.notificaciones.length === 0) {
        lista.innerHTML = `
            <li>
                <span class="dropdown-item-text text-muted text-center py-3">
                    <i class="fas fa-bell-slash"></i><br>
                    Sin notificaciones nuevas
                </span>
            </li>
        `;
        console.log('📢 [Notificaciones] No hay notificaciones nuevas');
        return;
    }

    // Agregar notificaciones a la lista
    data.notificaciones.forEach((notif, index) => {
        console.log(`📢 [Notificaciones] Agregando notificación ${index + 1}:`, notif.titulo);

        const li = document.createElement('li');
        const iconColor = `text-${notif.color || 'info'}`;
        const url = notif.url && notif.url !== '' ? notif.url : '#';

        li.innerHTML = `
            <a class="dropdown-item notificacion-item" 
               href="${url}" 
               data-notif-id="${notif.id}"
               style="white-space: normal; padding: 12px 15px; border-left: 3px solid transparent;">
                <div class="d-flex align-items-start gap-2">
                    <i class="fas ${notif.icono || 'fa-bell'} ${iconColor}" 
                       style="margin-top: 3px; font-size: 18px;"></i>
                    <div style="flex: 1;">
                        <strong style="font-size: 14px; color: #212529;">${notif.titulo}</strong><br>
                        <small class="text-muted" style="font-size: 12px;">${notif.mensaje}</small><br>
                        <small class="text-muted" style="font-size: 11px;">
                            <i class="fas fa-clock"></i> Hace ${notif.tiempo}
                        </small>
                    </div>
                </div>
            </a>
        `;

        // Agregar evento de click para marcar como leída
        const link = li.querySelector('a');
        link.addEventListener('click', function(e) {
            if (url !== '#') {
                marcarNotificacionLeida(notif.id);
            }
        });

        // Efecto hover
        link.addEventListener('mouseenter', function() {
            this.style.backgroundColor = '#f8f9fa';
            this.style.borderLeftColor = notif.color ? getBorderColor(notif.color) : '#007bff';
        });

        link.addEventListener('mouseleave', function() {
            this.style.backgroundColor = '';
            this.style.borderLeftColor = 'transparent';
        });

        lista.appendChild(li);
    });

    console.log('✅ [Notificaciones] UI actualizada correctamente');
}

/**
 * Mostrar error en las notificaciones
 */
function mostrarErrorNotificaciones(error) {
    const lista = document.getElementById('notificaciones-lista');

    if (!lista) return;

    lista.innerHTML = `
        <li>
            <span class="dropdown-item-text text-danger text-center py-3">
                <i class="fas fa-exclamation-triangle"></i><br>
                Error al cargar notificaciones
                <br><small>${error.message}</small>
            </span>
        </li>
    `;
}

/**
 * Marcar notificación como leída
 */
function marcarNotificacionLeida(notifId) {
    console.log(`📢 [Notificaciones] Marcando notificación ${notifId} como leída`);

    fetch(`/usuarios/notificaciones/${notifId}/marcar-leida/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            console.log('✅ [Notificaciones] Marcada como leída');
            // Recargar notificaciones después de un breve delay
            setTimeout(cargarNotificaciones, 500);
        }
    })
    .catch(error => {
        console.error('❌ [Notificaciones] Error al marcar como leída:', error);
    });
}

/**
 * Obtener cookie por nombre (para CSRF token)
 */
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

/**
 * Obtener color del borde según el color de Bootstrap
 */
function getBorderColor(colorName) {
    const colores = {
        'primary': '#007bff',
        'secondary': '#6c757d',
        'success': '#28a745',
        'danger': '#dc3545',
        'warning': '#ffc107',
        'info': '#17a2b8',
        'light': '#f8f9fa',
        'dark': '#343a40'
    };
    return colores[colorName] || '#007bff';
}

/**
 * Inicializar sistema de notificaciones
 */
function inicializarNotificaciones() {
    console.log('📢 [Notificaciones] Inicializando sistema...');

    // Verificar que los elementos existen
    const badge = document.getElementById('notif-count');
    const lista = document.getElementById('notificaciones-lista');
    const dropdown = document.getElementById('dropdownNotificaciones');

    if (!badge || !lista || !dropdown) {
        console.error('❌ [Notificaciones] Elementos DOM no encontrados');
        console.log('- Badge:', badge ? '✅' : '❌');
        console.log('- Lista:', lista ? '✅' : '❌');
        console.log('- Dropdown:', dropdown ? '✅' : '❌');
        return;
    }

    console.log('✅ [Notificaciones] Elementos DOM verificados');

    // Cargar notificaciones inmediatamente
    cargarNotificaciones();

    // Configurar actualización periódica
    if (notificacionesTimer) {
        clearInterval(notificacionesTimer);
    }

    notificacionesTimer = setInterval(cargarNotificaciones, NOTIFICACIONES_CONFIG.intervalo);
    console.log(`✅ [Notificaciones] Actualización automática cada ${NOTIFICACIONES_CONFIG.intervalo / 1000}s`);

    // Recargar cuando se abre el dropdown
    dropdown.addEventListener('click', function() {
        console.log('📢 [Notificaciones] Dropdown abierto, recargando...');
        cargarNotificaciones();
    });
}

// Inicializar cuando el DOM esté listo
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', inicializarNotificaciones);
} else {
    inicializarNotificaciones();
}

// Exponer funciones globalmente para depuración
window.notificacionesDebug = {
    cargar: cargarNotificaciones,
    marcarLeida: marcarNotificacionLeida,
    config: NOTIFICACIONES_CONFIG
};

console.log('📢 [Notificaciones] Módulo inicializado. Usa window.notificacionesDebug para depuración');

