# 🌟 Sistema de Accesibilidad Web - DIGT SOFT

## 📋 Descripción General

Se ha implementado un sistema completo de accesibilidad web siguiendo las pautas **WCAG 2.1** (Web Content Accessibility Guidelines) nivel AA/AAA para hacer el sistema DIGT SOFT accesible para todos los usuarios, incluyendo personas con discapacidades visuales, motoras y cognitivas.

---

## ✨ Características Implementadas

### 1. 🎯 Widget de Accesibilidad Flotante

Un panel flotante accesible desde cualquier página que permite a los usuarios ajustar la experiencia visual según sus necesidades.

**Ubicación:** Botón flotante en la esquina inferior derecha (icono de accesibilidad universal ♿)

**Características del Widget:**
- Botón flotante con animación de pulso para llamar la atención
- Panel expandible con todas las opciones de accesibilidad
- Persistencia de configuración (las preferencias se guardan en localStorage)
- Totalmente navegable por teclado
- Compatible con lectores de pantalla

---

### 2. 📝 Opciones de Accesibilidad Disponibles

#### 🔤 Control de Tamaño de Texto
- **Aumentar Texto (A+)**: Incrementa el tamaño de fuente hasta 140%
  - Atajo de teclado: `Ctrl + Alt + +`
- **Reducir Texto (A-)**: Reduce el tamaño de fuente hasta 80%
  - Atajo de teclado: `Ctrl + Alt + -`
- Notificaciones visuales del porcentaje actual

#### 🎨 Modos Visuales

**Alto Contraste:**
- Aumenta el contraste visual al 150%
- Mejora la legibilidad para usuarios con baja visión
- Bordes más definidos y colores más intensos

**Modo Oscuro:**
- Fondo oscuro (#1a1a1a) con texto claro
- Reduce la fatiga visual en ambientes con poca luz
- Ideal para sesiones largas de trabajo
- Atajo de teclado: `Ctrl + Alt + D`

**Escala de Grises:**
- Convierte toda la interfaz a escala de grises
- Útil para usuarios con daltonismo
- Elimina distracciones de color

#### 🔗 Mejoras de Navegación

**Resaltar Enlaces:**
- Enlaces con fondo amarillo (#FFFF00)
- Texto en negrita con subrayado
- Bordes visibles en hover
- Facilita la identificación de enlaces clickeables

**Espaciado Aumentado:**
- Interlineado doble (line-height: 2)
- Mayor espaciado entre letras (0.05em)
- Más margen entre párrafos y elementos
- Mejora la legibilidad para usuarios con dislexia

**Lector de Pantalla:**
- Optimización para NVDA, JAWS, y otros lectores de pantalla
- Anuncios ARIA en vivo para cambios dinámicos
- Navegación mejorada con landmarks

---

### 3. ⌨️ Atajos de Teclado

| Combinación | Acción |
|------------|--------|
| `Ctrl + Alt + +` | Aumentar tamaño de texto |
| `Ctrl + Alt + -` | Disminuir tamaño de texto |
| `Ctrl + Alt + D` | Alternar modo oscuro |
| `Ctrl + Alt + R` | Restablecer todas las configuraciones |
| `Tab` | Navegar entre elementos interactivos |
| `Enter` / `Espacio` | Activar botones y enlaces |
| `Esc` | Cerrar panel de accesibilidad |

---

### 4. 🎯 Mejoras de Navegación por Teclado

**Focus Visible:**
- Todos los elementos interactivos tienen un outline verde (#4CAF50) visible
- Box-shadow adicional para mayor visibilidad
- Offset de 2px para no cubrir el contenido

**Skip Link:**
- Enlace "Saltar al contenido principal" al inicio de cada página
- Visible solo cuando recibe el focus con teclado
- Permite a usuarios de teclado/lector omitir la navegación repetitiva

**Navegación Intuitiva:**
- Orden de tabulación lógico
- Todos los elementos interactivos son accesibles por teclado
- Indicadores visuales claros del elemento enfocado

---

### 5. 🏷️ Mejoras Semánticas ARIA

**Landmarks ARIA Automáticos:**
```html
<header role="banner">
<nav role="navigation" aria-label="Navegación principal">
<main role="main">
<aside role="complementary">
<footer role="contentinfo">
```

**Atributos ARIA en Elementos Interactivos:**
- `aria-label`: Etiquetas descriptivas para iconos y botones
- `aria-expanded`: Estado de paneles expandibles
- `aria-pressed`: Estado de botones toggle
- `aria-required`: Campos obligatorios en formularios
- `aria-invalid`: Campos con errores de validación
- `aria-live`: Regiones para anuncios dinámicos

**Región ARIA Live:**
```html
<div id="aria-live-region" aria-live="polite" aria-atomic="true">
  <!-- Anuncios para lectores de pantalla -->
</div>
```

---

### 6. 📱 Responsive y Móvil

- Widget adaptable a pantallas pequeñas
- Botón flotante redimensionable
- Panel de opciones con scroll optimizado
- Touch-friendly para dispositivos táctiles
- Notificaciones adaptativas al tamaño de pantalla

---

### 7. 💾 Persistencia de Configuración

Las preferencias del usuario se guardan automáticamente en `localStorage`:

```javascript
{
  fontSize: 1.2,           // Factor de tamaño (1 = 100%)
  darkMode: true,          // Modo oscuro activado
  highContrast: false,     // Alto contraste
  grayscale: false,        // Escala de grises
  highlightLinks: false,   // Resaltar enlaces
  increasedSpacing: false, // Espaciado aumentado
  screenReader: true       // Optimización para lector
}
```

Las configuraciones se cargan automáticamente en cada visita.

---

### 8. 🔔 Sistema de Notificaciones

Notificaciones visuales no intrusivas que informan al usuario sobre cambios:

- Aparecen en la esquina superior derecha
- Diseño atractivo con gradiente verde
- Desaparecen automáticamente después de 3 segundos
- Animaciones suaves de entrada y salida
- Accesibles para lectores de pantalla (role="alert")

---

### 9. 🖼️ Mejoras en Imágenes

**Verificación Automática:**
- Todas las imágenes son verificadas para `alt` text
- Lazy loading automático para mejor rendimiento
- Advertencias en consola para imágenes sin descripción
- Alt text por defecto: "Imagen decorativa"

---

### 10. 📝 Mejoras en Formularios

**Accesibilidad de Formularios:**
- Asociación automática de labels con inputs
- `aria-required` en campos obligatorios
- `aria-invalid` en campos con errores
- Advertencias en consola para inputs sin label
- Mensajes de error accesibles

---

## 🎨 Estilos CSS Personalizados

### Clases Aplicadas Dinámicamente:

```css
.dark-mode                 /* Modo oscuro */
.high-contrast            /* Alto contraste */
.grayscale                /* Escala de grises */
.highlight-links          /* Enlaces resaltados */
.increased-spacing        /* Espaciado aumentado */
.keyboard-navigation      /* Navegación por teclado activa */
```

### Responsive Design:

```css
@media (max-width: 768px) {
  /* Adaptaciones para tablet */
}

@media (max-width: 480px) {
  /* Adaptaciones para móvil */
}

@media (prefers-reduced-motion: reduce) {
  /* Animaciones reducidas para usuarios sensibles */
}
```

---

## 📊 Cumplimiento de Estándares

### ✅ WCAG 2.1 Nivel AA/AAA

**Principios WCAG:**

1. **Perceptible** ✅
   - Contraste de color adecuado (mínimo 4.5:1)
   - Textos alternativos para imágenes
   - Múltiples formas de presentar información

2. **Operable** ✅
   - Navegación completa por teclado
   - No hay trampas de teclado
   - Tiempo suficiente para leer contenido
   - Sin contenido que parpadea peligrosamente

3. **Comprensible** ✅
   - Lenguaje claro y simple
   - Navegación consistente
   - Mensajes de error claros
   - Etiquetas descriptivas

4. **Robusto** ✅
   - HTML semántico válido
   - Compatible con tecnologías asistivas
   - ARIA usado correctamente

---

## 🚀 Uso e Implementación

### Para Desarrolladores:

**1. Incluir en Templates:**

```django
{% load static %}

<!-- CSS de Accesibilidad -->
<link rel="stylesheet" href="{% static 'css/accessibility.css' %}">

<!-- Widget de Accesibilidad -->
{% include 'includes/accessibility_widget.html' %}

<!-- JavaScript de Accesibilidad -->
<script src="{% static 'js/accessibility.js' %}"></script>
```

**2. Templates Incluidos Automáticamente:**
- ✅ `base.html` - Template base principal
- ✅ `base_dashboard.html` - Template del dashboard
- ✅ Todas las páginas que extienden estos templates

### Para Usuarios:

**1. Acceder al Widget:**
   - Hacer clic en el botón flotante (♿) en la esquina inferior derecha
   - O usar navegación por teclado hasta alcanzar el botón

**2. Seleccionar Opciones:**
   - Hacer clic en las opciones deseadas
   - O navegar con Tab y activar con Enter/Espacio

**3. Restablecer:**
   - Botón "Restablecer Todo" en el panel
   - O usar `Ctrl + Alt + R`

---

## 🔍 Funciones JavaScript Principales

### Clase Principal:

```javascript
class AccessibilityWidget {
  constructor()                    // Inicialización
  init()                          // Configurar eventos
  setupARIA()                     // Configurar ARIA
  increaseFontSize()              // Aumentar texto
  decreaseFontSize()              // Reducir texto
  toggleDarkMode()                // Alternar modo oscuro
  toggleHighContrast()            // Alternar alto contraste
  toggleGrayscale()               // Alternar escala de grises
  toggleHighlightLinks()          // Alternar resaltado
  toggleIncreasedSpacing()        // Alternar espaciado
  toggleScreenReader()            // Alternar lector
  reset()                         // Restablecer todo
  saveSettings()                  // Guardar en localStorage
  loadSettings()                  // Cargar de localStorage
  showNotification(message)       // Mostrar notificación
  announceForScreenReader(message) // Anuncio ARIA live
}
```

### Funciones Auxiliares:

```javascript
detectKeyboardNavigation()      // Detectar uso de teclado
enhanceImageContrast()          // Mejorar imágenes
addARIALandmarks()              // Agregar landmarks
enhanceFormsAccessibility()     // Mejorar formularios
addSkipLink()                   // Agregar skip link
checkColorContrast()            // Verificar contraste
announcePageChange()            // Anunciar cambios
initAccessibilityEnhancements() // Inicializar mejoras
```

---

## 📈 Beneficios del Sistema

### Para Usuarios:
- ✅ Mayor comodidad de lectura
- ✅ Reducción de fatiga visual
- ✅ Navegación más rápida
- ✅ Experiencia personalizable
- ✅ Acceso universal al contenido

### Para el Negocio:
- ✅ Cumplimiento legal (leyes de accesibilidad)
- ✅ Mayor alcance de audiencia
- ✅ Mejor SEO (los motores de búsqueda valoran la accesibilidad)
- ✅ Imagen corporativa responsable
- ✅ Reducción de riesgo legal

### Para Desarrolladores:
- ✅ Código bien estructurado y comentado
- ✅ Fácil de mantener y extender
- ✅ Cumple con estándares internacionales
- ✅ Documentación completa
- ✅ Reutilizable en otros proyectos

---

## 🧪 Pruebas de Accesibilidad

### Herramientas Recomendadas:

1. **Navegadores:**
   - Chrome DevTools (Lighthouse Accessibility)
   - Firefox Accessibility Inspector
   - Edge Accessibility Tools

2. **Lectores de Pantalla:**
   - NVDA (Windows) - Gratuito
   - JAWS (Windows) - Comercial
   - VoiceOver (Mac/iOS) - Integrado
   - TalkBack (Android) - Integrado

3. **Validadores:**
   - WAVE (WebAIM)
   - aXe DevTools
   - Pa11y

4. **Pruebas Manuales:**
   - ✅ Navegación completa solo con teclado
   - ✅ Zoom del navegador al 200%
   - ✅ Deshabilitar CSS para verificar estructura
   - ✅ Usar lector de pantalla

---

## 📝 Checklist de Accesibilidad

### ✅ Completado:

- [x] Contraste de color adecuado
- [x] Tamaño de texto ajustable
- [x] Navegación por teclado completa
- [x] Focus visible en todos los elementos
- [x] Atributos ARIA correctos
- [x] Alt text en imágenes
- [x] Labels en formularios
- [x] Skip links
- [x] Landmarks semánticos
- [x] Responsive design
- [x] Sin trampas de teclado
- [x] Mensajes de error claros
- [x] Compatible con lectores de pantalla
- [x] Animaciones reducidas (prefers-reduced-motion)
- [x] Persistencia de configuración

---

## 🔧 Mantenimiento y Soporte

### Actualizar Configuraciones:

```javascript
// Acceder al widget globalmente
window.accessibilityWidget.settings

// Forzar guardar configuración
window.accessibilityWidget.saveSettings()

// Recargar configuración
window.accessibilityWidget.loadSettings()

// Resetear todo
window.accessibilityWidget.reset()
```

### Agregar Nuevas Funciones:

1. Agregar botón en `accessibility_widget.html`
2. Agregar estilos en `accessibility.css`
3. Agregar función en `accessibility.js`
4. Actualizar esta documentación

---

## 🌐 Compatibilidad

### Navegadores Soportados:
- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+
- ✅ Opera 76+

### Tecnologías Asistivas:
- ✅ NVDA 2020+
- ✅ JAWS 2019+
- ✅ VoiceOver (todas las versiones recientes)
- ✅ TalkBack (Android 9+)

---

## 📚 Referencias y Recursos

### Documentación Oficial:
- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [MDN Web Accessibility](https://developer.mozilla.org/en-US/docs/Web/Accessibility)
- [WebAIM Resources](https://webaim.org/)
- [WAI-ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/)

### Herramientas:
- [WAVE Browser Extension](https://wave.webaim.org/extension/)
- [axe DevTools](https://www.deque.com/axe/devtools/)
- [Lighthouse CI](https://github.com/GoogleChrome/lighthouse-ci)

---

## 📞 Soporte

Para preguntas o problemas relacionados con accesibilidad:

**Email:** accesibilidad@digitsoft.com.co  
**Teléfono:** (+57) 3215434380  
**Ubicación:** Calle 15 # 14-26, Duitama - Boyacá

---

## 🎉 Conclusión

El sistema de accesibilidad de DIGT SOFT representa un compromiso con la inclusión digital y el acceso universal. Cada usuario, independientemente de sus capacidades, puede acceder, navegar y utilizar el sistema de manera efectiva.

**Principio Fundamental:** *"La accesibilidad no es una característica opcional, es un derecho fundamental."*

---

**Última actualización:** 03 de Diciembre de 2025  
**Versión:** 1.0.0  
**Autor:** Equipo de Desarrollo DIGT SOFT

