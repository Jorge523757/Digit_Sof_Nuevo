# 📜 Scripts JavaScript Personalizados

Esta carpeta contiene todos los scripts JavaScript (.js) personalizados del proyecto organizados por función.

---

## 📂 Estructura de Carpetas

### 🔍 01_JS_DIAGNOSTICO/
Scripts JavaScript para diagnosticar problemas del sistema.

**Archivos típicos:**
- `diagnostico_*.js` - Scripts de diagnóstico
- `diagnosticar_*.js` - Scripts de diagnóstico de componentes

**Uso:**
```javascript
// Abrir consola del navegador (F12)
// Copiar y pegar el contenido del script
// Presionar Enter
```

**Ejemplo:**
```javascript
// En la consola del navegador:
// 1. Abrir DIAGNOSTICAR_IMAGENES_CARRITO.js
// 2. Copiar todo el contenido
// 3. Pegar en la consola
// 4. Ver el diagnóstico
```

---

### 🛒 02_JS_CARRITO/
Scripts para probar y limpiar el carrito de compras.

**Archivos típicos:**
- `LIMPIAR_CARRITO_*.js` - Limpiar el carrito
- `*_carrito_*.js` - Scripts relacionados con el carrito
- `test_carrito_*.js` - Pruebas del carrito

**Uso:**
```javascript
// Para limpiar el carrito:
// 1. F12 (Consola)
// 2. Copiar contenido de LIMPIAR_CARRITO_RAPIDO.js
// 3. Pegar y Enter
// 4. El carrito se limpiará
```

---

### 🐛 03_JS_DEBUG/
Scripts para debugging y depuración.

**Archivos típicos:**
- `DEBUG_*.js` - Scripts de debug
- `test_*.js` - Scripts de prueba

**Uso:**
```javascript
// Para debug:
// 1. F12 (Consola)
// 2. Copiar script de DEBUG
// 3. Pegar y ejecutar
// 4. Ver información de debug
```

---

### ✅ 04_JS_SOLUCIONES/
Scripts con soluciones inmediatas a problemas comunes.

**Archivos típicos:**
- `EJECUTAR_*.js` - Scripts de ejecución inmediata
- `SOLUCION_*.js` - Soluciones a problemas

**Uso:**
```javascript
// Para aplicar una solución:
// 1. F12 (Consola)
// 2. Copiar EJECUTAR_SOLUCION_*.js
// 3. Pegar y Enter
// 4. La solución se aplicará automáticamente
```

---

### 📦 05_JS_OTROS/
Scripts JavaScript variados.

---

## 🚀 Cómo Usar los Scripts

### Método General:
1. **Abrir la consola del navegador:** Presiona `F12`
2. **Ir a la pestaña "Console"**
3. **Abrir el archivo .js** que necesites
4. **Copiar todo el contenido** del archivo
5. **Pegar en la consola** del navegador
6. **Presionar Enter**

### Ejemplo Práctico:

#### Para Diagnosticar el Carrito:
```javascript
// 1. F12 → Console
// 2. Abrir: static_custom/01_JS_DIAGNOSTICO/DIAGNOSTICAR_IMAGENES_CARRITO.js
// 3. Copiar todo (Ctrl+A, Ctrl+C)
// 4. Pegar en consola (Ctrl+V)
// 5. Enter
// Verás un diagnóstico completo del carrito
```

#### Para Limpiar el Carrito:
```javascript
// 1. F12 → Console
// 2. Abrir: static_custom/02_JS_CARRITO/LIMPIAR_CARRITO_RAPIDO.js
// 3. Copiar y pegar en consola
// 4. Enter
// El carrito se limpiará automáticamente
```

---

## 📋 Scripts Más Utilizados

### Para Diagnosticar:
```
static_custom/01_JS_DIAGNOSTICO/
├── DIAGNOSTICAR_IMAGENES_CARRITO.js  → Diagnóstico de imágenes
├── diagnostico_carrito_consola.js    → Diagnóstico general
└── DIAGNOSTICO_Y_SOLUCION_COMPLETA.js → Diagnóstico + solución
```

### Para el Carrito:
```
static_custom/02_JS_CARRITO/
├── LIMPIAR_CARRITO_RAPIDO.js         → Limpiar carrito rápido
├── LIMPIAR_Y_PROBAR_CARRITO.js       → Limpiar y probar
└── test_carrito_sistema.js           → Probar sistema de carrito
```

### Para Soluciones:
```
static_custom/04_JS_SOLUCIONES/
├── EJECUTAR_SOLUCION_DEFINITIVA.js   → Solución definitiva
├── EJECUTAR_EN_CONSOLA.js            → Ejecución inmediata
└── SOLUCION_FORZADA_IMAGENES.js      → Solución de imágenes
```

---

## ⚠️ Precauciones

### Scripts de DIAGNOSTICO:
- ✅ Solo lectura
- ✅ No modifican datos
- ✅ Seguros de ejecutar

### Scripts de CARRITO:
- ⚡ Pueden modificar el localStorage
- ⚡ Limpian el carrito (no es permanente en BD)
- ⚡ Seguros pero lee antes de ejecutar

### Scripts de SOLUCIONES:
- ⚠️ Modifican el comportamiento del sistema
- ⚠️ Aplican cambios inmediatos
- ⚠️ Lee las instrucciones del script antes de ejecutar

### Scripts de DEBUG:
- ✅ Generalmente seguros
- ✅ Solo muestran información
- ✅ Útiles para desarrollo

---

## 🎯 Flujo de Trabajo Típico

### 1. Hay un Problema con el Carrito:
```javascript
// Paso 1: Diagnosticar
// Ejecutar: DIAGNOSTICAR_IMAGENES_CARRITO.js
// Ver qué está fallando

// Paso 2: Limpiar (si es necesario)
// Ejecutar: LIMPIAR_CARRITO_RAPIDO.js

// Paso 3: Probar
// Agregar un producto
// Verificar que funcione
```

### 2. Las Imágenes No Aparecen:
```javascript
// Paso 1: Diagnóstico
// Ejecutar: DIAGNOSTICAR_IMAGENES_CARRITO.js
// Ver qué imagen falta

// Paso 2: Aplicar Solución
// Ejecutar: SOLUCION_FORZADA_IMAGENES.js
// Las imágenes se forzarán a aparecer

// Paso 3: Verificar
// Abrir el carrito
// Comprobar que se vean las imágenes
```

---

## 🔄 Agregar Nuevos Scripts

1. Crea tu script `.js` en la raíz del proyecto
2. Nómbralo según la función:
   - `diagnostico_*.js` → `01_JS_DIAGNOSTICO/`
   - `*_carrito_*.js` → `02_JS_CARRITO/`
   - `debug_*.js` → `03_JS_DEBUG/`
   - `ejecutar_*.js`, `solucion_*.js` → `04_JS_SOLUCIONES/`
   - Otros → `05_JS_OTROS/`
3. Ejecuta `ORGANIZAR_DOCS.bat` desde la raíz
4. El script se moverá automáticamente

---

## 📊 Estadísticas

Total de scripts JavaScript: **~10 archivos**

Distribución:
- 🔍 Diagnóstico: 3 scripts
- 🛒 Carrito: 3 scripts
- 🐛 Debug: 1 script
- ✅ Soluciones: 3 scripts
- 📦 Otros: ~0 scripts

---

## 🔗 Enlaces Relacionados

- **Documentación:** `docs/README.md`
- **Scripts BAT:** `scripts/README.md`
- **Utilidades Python:** `utils/README.md`
- **Guías de soluciones:** `docs/02_SOLUCIONES/`

---

## 📝 Plantilla de Script

### Para Crear un Nuevo Script de Diagnóstico:

```javascript
// ==============================================
// DIAGNÓSTICO DE [COMPONENTE]
// Archivo: diagnostico_[nombre].js
// ==============================================

console.clear();
console.log('%c=== DIAGNÓSTICO DE [COMPONENTE] ===', 
    'font-size: 20px; color: blue; font-weight: bold');

// 1. Verificar elemento
const elemento = document.getElementById('miElemento');
console.log('Elemento existe:', !!elemento);

// 2. Verificar datos
const datos = localStorage.getItem('miDato');
console.log('Datos:', datos);

// 3. Verificar funciones
console.log('Función disponible:', typeof window.miFuncion);

// 4. Resumen
console.log('\n%c=== RESUMEN ===', 'color: green; font-weight: bold');
console.log('✅ Diagnóstico completado');
```

---

## 🆘 Ayuda

Si un script no funciona:

1. **Verifica que estés en la página correcta**
   - Los scripts de carrito solo funcionan en páginas con carrito
   - Los scripts de productos solo funcionan en páginas de productos

2. **Abre correctamente la consola**
   - Presiona F12
   - Ve a la pestaña "Console"
   - Asegúrate de no tener errores previos

3. **Copia el script completo**
   - Abre el archivo .js
   - Selecciona todo (Ctrl+A)
   - Copia (Ctrl+C)
   - Pega en consola (Ctrl+V)
   - Enter

4. **Verifica los mensajes de error**
   - La consola mostrará mensajes rojos si hay errores
   - Lee el error para entender qué falló

---

## 💡 Consejos

### Para Mejor Uso:
- ✅ Lee los comentarios dentro de cada script
- ✅ Ejecuta primero los scripts de diagnóstico
- ✅ Guarda los resultados del diagnóstico antes de aplicar soluciones
- ✅ Recarga la página después de aplicar una solución

### Para Desarrollo:
- ✅ Usa scripts de debug durante el desarrollo
- ✅ Los scripts de diagnóstico son excelentes para entender problemas
- ✅ Puedes modificar los scripts según tus necesidades

---

**Última actualización:** 2025-11-28
**Versión:** 1.0
**Total de scripts:** ~10 archivos JavaScript

