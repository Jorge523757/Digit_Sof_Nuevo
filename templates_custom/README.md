# 🌐 Plantillas HTML Personalizadas

Esta carpeta contiene todos los archivos HTML (.html) personalizados del proyecto organizados por función.

---

## 📂 Estructura de Carpetas

### 🧪 01_HTML_PRUEBAS/
Archivos HTML para probar funcionalidades.

**Archivos típicos:**
- `test_*.html` - Páginas de prueba
- `prueba_*.html` - Tests de componentes

**Uso:**
```
1. Abre el archivo en el navegador
2. Prueba la funcionalidad
3. Verifica que funcione correctamente
```

**Ejemplo:**
- `test_carrito.html` - Probar el carrito de compras
- `test_botones_ecommerce.html` - Probar botones del e-commerce

---

### 🔍 02_HTML_DIAGNOSTICO/
Páginas HTML para diagnosticar problemas.

**Archivos típicos:**
- `diagnostico_*.html` - Herramientas de diagnóstico

**Uso:**
```
1. Abre la página en el navegador
2. La página ejecutará diagnósticos automáticamente
3. Verás reportes de estado
```

---

### ✅ 03_HTML_SOLUCIONES/
Páginas con soluciones a problemas comunes.

**Archivos típicos:**
- `SOLUCION_*.html` - Páginas con soluciones
- `limpiar_*.html` - Herramientas de limpieza

**Uso:**
```
1. Abre la página
2. Haz clic en los botones de solución
3. La solución se aplicará automáticamente
```

**Ejemplos:**
- `limpiar_carrito.html` - Limpiar el carrito
- `limpiar_localStorage.html` - Limpiar localStorage
- `SOLUCION_DEFINITIVA.html` - Solución general

---

### 📚 04_HTML_EJEMPLOS/
Ejemplos y demos del sistema.

**Archivos típicos:**
- `ecommerce_listo.html` - Ejemplo de e-commerce
- `RESUMEN_*.html` - Resúmenes visuales
- `SISTEMA_*.html` - Documentación de sistemas

**Uso:**
```
1. Abre el archivo
2. Revisa el ejemplo o documentación
3. Úsalo como referencia
```

---

### 📦 05_HTML_OTROS/
Archivos HTML variados.

**Archivos típicos:**
- `*_debug.html` - Páginas de debug
- Utilidades varias

---

## 🚀 Cómo Usar los Archivos HTML

### Método General:

#### 1. Abrir en Navegador:
```
Doble clic en el archivo .html
→ Se abre en tu navegador predeterminado
```

#### 2. Usar con Servidor Local:
```
# Si necesitas acceso a recursos del proyecto
1. Asegúrate de que el servidor Django esté corriendo
2. Copia el archivo a templates/
3. Accede vía URL de Django
```

---

## 📋 Archivos Más Utilizados

### Para Probar:
```
templates_custom/01_HTML_PRUEBAS/
├── test_carrito.html             → Probar carrito
├── test_carrito_debug.html       → Probar con debug
├── test_botones_ecommerce.html   → Probar botones
└── test_limpieza_carrito.html    → Probar limpieza
```

### Para Diagnosticar:
```
templates_custom/02_HTML_DIAGNOSTICO/
└── diagnostico_botones.html      → Diagnosticar botones
```

### Para Soluciones:
```
templates_custom/03_HTML_SOLUCIONES/
├── limpiar_carrito.html          → Limpiar carrito
├── limpiar_localStorage.html     → Limpiar localStorage
└── SOLUCION_DEFINITIVA.html      → Solución general
```

### Ejemplos:
```
templates_custom/04_HTML_EJEMPLOS/
├── ecommerce_listo.html          → E-commerce listo
├── RESUMEN_IMPLEMENTACION.html   → Resumen visual
└── SISTEMA_SEEDING_COMPLETADO.html → Sistema de datos
```

---

## 🎯 Casos de Uso

### 1. Probar el Carrito:
```
1. Abrir: test_carrito.html
2. Hacer pruebas
3. Verificar funcionamiento
```

### 2. Limpiar Datos:
```
1. Abrir: limpiar_localStorage.html
2. Hacer clic en "Limpiar"
3. Datos limpiados
```

### 3. Diagnosticar Problemas:
```
1. Abrir: diagnostico_botones.html
2. Ver reporte automático
3. Identificar problema
```

### 4. Ver Ejemplos:
```
1. Abrir: ecommerce_listo.html
2. Revisar implementación
3. Usar como referencia
```

---

## ⚠️ Consideraciones

### Archivos de Prueba:
- ✅ Seguros de usar
- ✅ No modifican la base de datos
- ✅ Útiles para development

### Archivos de Soluciones:
- ⚡ Pueden modificar localStorage
- ⚡ Algunas soluciones son permanentes
- ⚡ Lee las instrucciones antes de usar

### Archivos de Ejemplos:
- ✅ Solo lectura
- ✅ Documentación visual
- ✅ Referencias útiles

---

## 🔄 Agregar Nuevos Archivos

1. Crea tu archivo `.html` en la raíz del proyecto
2. Nómbralo según la función:
   - `test_*.html` → `01_HTML_PRUEBAS/`
   - `diagnostico_*.html` → `02_HTML_DIAGNOSTICO/`
   - `limpiar_*.html`, `solucion_*.html` → `03_HTML_SOLUCIONES/`
   - `ecommerce_*.html`, `resumen_*.html` → `04_HTML_EJEMPLOS/`
   - Otros → `05_HTML_OTROS/`
3. Ejecuta `ORGANIZAR_DOCS.bat` desde la raíz
4. El archivo se moverá automáticamente

---

## 📊 Estadísticas

Total de archivos HTML: **12 archivos**

Distribución:
- 🧪 Pruebas: 4 archivos
- 🔍 Diagnóstico: 1 archivo
- ✅ Soluciones: 3 archivos
- 📚 Ejemplos: 3 archivos
- 📦 Otros: 1 archivo

---

## 🔗 Enlaces Relacionados

- **Documentación:** `docs/README.md`
- **Scripts BAT:** `scripts/README.md`
- **Scripts JavaScript:** `static_custom/README.md`
- **Utilidades Python:** `utils/README.md`

---

## 💡 Tips

### Para Desarrollo:
- ✅ Usa archivos de prueba para validar funcionalidades
- ✅ Los archivos de diagnóstico son útiles para debugging
- ✅ Revisa los ejemplos antes de implementar algo nuevo

### Para Producción:
- ⚠️ No uses estos archivos en producción
- ⚠️ Son para desarrollo y testing
- ⚠️ Muévelos a `templates/` de Django si necesitas usarlos

### Para Mantener Orden:
- ✅ Agrupa archivos similares
- ✅ Usa nombres descriptivos
- ✅ Documenta qué hace cada archivo en comentarios HTML

---

## 📝 Plantilla de Archivo HTML

### Para Crear un Nuevo HTML de Prueba:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test - [Componente]</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
        }
        .test-section {
            border: 1px solid #ddd;
            padding: 20px;
            margin: 20px 0;
            border-radius: 5px;
        }
        button {
            padding: 10px 20px;
            margin: 5px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h1>🧪 Test de [Componente]</h1>
    
    <div class="test-section">
        <h2>Test 1</h2>
        <button onclick="test1()">Ejecutar Test 1</button>
        <div id="result1"></div>
    </div>
    
    <script>
        function test1() {
            console.log('Ejecutando test 1...');
            // Tu código de prueba aquí
            document.getElementById('result1').textContent = 'Test completado ✅';
        }
    </script>
</body>
</html>
```

---

## 🆘 Ayuda

Si un archivo no funciona:

1. **Verifica que el navegador soporte JavaScript**
   - Todos los archivos usan JavaScript
   - Habilita JavaScript en tu navegador

2. **Revisa la consola del navegador**
   - F12 → Console
   - Verás mensajes de error si algo falla

3. **Asegúrate de tener datos**
   - Algunos archivos necesitan que el carrito tenga productos
   - Otros necesitan que el sistema esté inicializado

4. **Lee los comentarios en el HTML**
   - Cada archivo tiene instrucciones en comentarios
   - Revisa el código fuente para entender cómo usarlo

---

**Última actualización:** 2025-11-28
**Versión:** 1.0
**Total de archivos:** 12 archivos HTML

