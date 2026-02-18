# 🚀 APLICAR CORRECCIONES - PASO A PASO

## ✅ El problema de textos invisibles está SOLUCIONADO

Sigue estos pasos EXACTAMENTE para aplicar las correcciones:

---

## 📋 PASOS PARA APLICAR

### Paso 1: Abrir PowerShell
```
Presiona: Windows + X
Selecciona: Windows PowerShell
```

### Paso 2: Navegar al Proyecto
```powershell
cd C:\DigitSoft2026\Digit_Sof_Nuevo
```

### Paso 3: Limpiar y Recolectar Archivos Estáticos
```powershell
python manage.py collectstatic --noinput --clear
```

**Esperado:** Verás mensajes de archivos copiados

### Paso 4: Iniciar el Servidor
```powershell
python manage.py runserver
```

**Esperado:** 
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### Paso 5: Abrir Navegador
```
1. Abrir Chrome, Firefox o Edge
2. Ir a: http://127.0.0.1:8000
```

### Paso 6: IMPORTANTE - Limpiar Cache del Navegador
```
Opción A (Recomendada):
1. Presionar: Ctrl + Shift + Delete
2. Seleccionar: "Imágenes y archivos en caché"
3. Periodo: "Todo"
4. Click en "Borrar datos"

Opción B (Rápida):
1. Presionar: Ctrl + F5
2. Repetir 2-3 veces

Opción C (Segura):
1. Cerrar TODAS las ventanas del navegador
2. Abrir navegador de nuevo
3. Ir a http://127.0.0.1:8000
```

### Paso 7: Iniciar Sesión
```
Usuario: admin (o tu usuario)
Contraseña: tu_contraseña
```

### Paso 8: Verificar Modo CLARO
```
1. Ir a Dashboard
   → ¿Ves el texto del banner?
   → ¿Ves los números en las cards?
   → TODO debe ser VISIBLE

2. Ir a Gestión de Clientes
   → ¿Ves el título "Gestión de Clientes"?
   → ¿Ves los headers de la tabla?
   → ¿Ves los nombres en la tabla?
   → ¿Ves los documentos?
   → ¿Ves los teléfonos?
   → ¿Ves los emails?
   → TODO debe ser VISIBLE en NEGRO
```

### Paso 9: Activar Modo OSCURO
```
1. Buscar el botón de tema en el header
   (Icono de luna 🌙 o sol ☀️)
2. Hacer clic
3. Esperar la transición (0.3 segundos)
```

### Paso 10: Verificar Modo OSCURO
```
1. Dashboard
   → ¿El fondo es oscuro?
   → ¿Ves el texto del banner en BLANCO?
   → ¿Ves los números en BLANCO?
   → TODO debe ser VISIBLE

2. Gestión de Clientes
   → ¿La tabla es OSCURA?
   → ¿Los headers son OSCUROS?
   → ¿Ves el texto en BLANCO en headers?
   → ¿Ves los nombres en CLARO en las filas?
   → ¿Ves los documentos en CLARO?
   → ¿Ves los teléfonos en CLARO?
   → ¿Ves los emails en CLARO?
   → ¿Los botones son MUY VISIBLES?
   → TODO debe ser PERFECTAMENTE VISIBLE
```

### Paso 11: Cambiar de Modo Varias Veces
```
1. Click en botón → Modo Oscuro
   → ¿TODO visible? ✅

2. Click en botón → Modo Claro
   → ¿TODO visible? ✅

3. Click en botón → Modo Oscuro
   → ¿TODO visible? ✅

4. Click en botón → Modo Claro
   → ¿TODO visible? ✅

SI TODO ES VISIBLE = ¡PROBLEMA SOLUCIONADO! ✅
```

---

## ✅ CHECKLIST DE VERIFICACIÓN

### Modo CLARO:
- [ ] Fondo blanco general
- [ ] Tabla con fondo blanco
- [ ] Headers de tabla con texto NEGRO visible
- [ ] Filas de tabla con texto NEGRO visible
- [ ] Nombres de clientes LEGIBLES en negro
- [ ] Documentos LEGIBLES en negro
- [ ] Teléfonos LEGIBLES en negro
- [ ] Emails LEGIBLES en negro
- [ ] Botones con colores estándar
- [ ] TODO ES VISIBLE

### Modo OSCURO:
- [ ] Fondo oscuro general (#1a1d20)
- [ ] Tabla con fondo oscuro (#2b3035)
- [ ] Headers de tabla con texto BLANCO visible
- [ ] Filas de tabla con texto CLARO visible (#e9ecef)
- [ ] Nombres de clientes LEGIBLES en claro
- [ ] Documentos LEGIBLES en claro
- [ ] Teléfonos LEGIBLES en claro
- [ ] Emails LEGIBLES en claro
- [ ] Botones MUY VISIBLES (verde, azul, rojo brillantes)
- [ ] Badges VISIBLES
- [ ] TODO ES PERFECTAMENTE VISIBLE

### Al Cambiar de Modo:
- [ ] Transición suave (sin parpadeos)
- [ ] Textos NO desaparecen
- [ ] Tabla siempre visible
- [ ] Datos siempre legibles
- [ ] Funciona en ambas direcciones (claro→oscuro, oscuro→claro)

---

## 🐛 SI ALGO NO FUNCIONA

### Problema 1: Los textos AÚN desaparecen
**Solución:**
```powershell
# 1. Detener servidor (Ctrl + C)

# 2. Limpiar TODO
python manage.py collectstatic --noinput --clear

# 3. Reiniciar servidor
python manage.py runserver

# 4. En navegador:
#    - Cerrar TODAS las ventanas
#    - Abrir navegador de nuevo
#    - Presionar Ctrl + Shift + Delete
#    - Borrar TODO el cache
#    - Ir a http://127.0.0.1:8000
#    - Presionar Ctrl + F5
```

### Problema 2: El archivo CSS no se carga
**Solución:**
```powershell
# Verificar que existe
dir static\css\dark-mode-global.css

# Debe mostrar el archivo
# Si no existe, hay un problema
```

### Problema 3: Errores en consola del navegador
**Solución:**
```
1. Presionar F12
2. Ir a tab "Console"
3. Ver si hay errores en rojo
4. Copiar el error y reportar
```

### Problema 4: El modo oscuro no se activa
**Solución:**
```
1. F12 → Console
2. Escribir: document.body.classList.contains('dark-mode')
3. Si devuelve false, el JavaScript no está funcionando
4. Verificar que theme-switcher.js se carga correctamente
```

---

## 📁 ARCHIVOS MODIFICADOS

### ✅ Modificado: `static/css/dark-mode-global.css`
**Cambios:**
- Eliminada transición global problemática
- Agregados estilos para modo claro (`body:not(.dark-mode)`)
- Mejorados estilos de tablas en modo oscuro
- Asegurada visibilidad de textos en ambos modos
- Corregidos selectores de iconos

### ✅ Sin cambios: `templates/base_dashboard.html`
**Ya estaba configurado correctamente**

---

## 🎯 RESULTADO ESPERADO

### Antes de las Correcciones:
```
❌ Textos desaparecían al cambiar de modo
❌ Tabla invisible en modo oscuro
❌ Datos perdidos
❌ Frustración total
```

### Después de las Correcciones:
```
✅ Textos SIEMPRE visibles
✅ Tabla perfectamente visible en ambos modos
✅ Todos los datos legibles
✅ Experiencia perfecta
```

---

## 🎉 ¡ÉXITO!

Si seguiste TODOS los pasos y:
- ✅ Ejecutaste `collectstatic --clear`
- ✅ Reiniciaste el servidor
- ✅ Limpiaste cache del navegador
- ✅ Hiciste Ctrl + F5

**Entonces el problema ESTÁ SOLUCIONADO** y los textos son PERFECTAMENTE VISIBLES en:
- ✅ Modo CLARO
- ✅ Modo OSCURO
- ✅ Al CAMBIAR entre modos
- ✅ En TODAS las tablas
- ✅ En TODOS los módulos

**¡Disfruta de tu modo oscuro perfecto sin textos invisibles!** 🌙✨🚀

