# ✅ VERIFICACIÓN DE MODO OSCURO - TABLAS Y MÓDULOS

## 🎯 Guía de Verificación Completa

Esta guía te ayudará a verificar que el modo oscuro funciona perfectamente en TODOS los módulos, especialmente en las tablas.

---

## 🔍 CHECKLIST DE VERIFICACIÓN

### 1️⃣ Modo CLARO (Debe verse IGUAL que antes)

#### Dashboard:
- [ ] Banner "¡Bienvenido, admin!" en azul vibrante
- [ ] 4 tarjetas de estadísticas con fondo blanco
- [ ] Sección "Acciones Rápidas" con fondo blanco
- [ ] Sección "Actividad Reciente" con fondo blanco
- [ ] Sección "Tareas Pendientes" con fondo blanco
- [ ] Texto negro legible

#### Gestión de Clientes:
- [ ] Card header "Gestión de Clientes" en azul
- [ ] Filtros (Búsqueda, Documento, Estado) con fondo blanco
- [ ] Tabla con fondo blanco
- [ ] Headers de tabla con fondo gris claro
- [ ] Botones Verde (Ver), Azul (Editar), Rojo (Eliminar) visibles
- [ ] Badges "Activo" en verde, "Inactivo" en rojo visibles
- [ ] Texto negro legible
- [ ] Paginación funcionando

---

### 2️⃣ Modo OSCURO (Debe verse PERFECTAMENTE OSCURO Y LEGIBLE)

#### Dashboard:
- [ ] Banner "¡Bienvenido, admin!" en azul OSCURO
- [ ] 4 tarjetas de estadísticas con fondo GRIS OSCURO (#2b3035)
- [ ] Números en BLANCO (#ffffff)
- [ ] Labels en gris claro (#adb5bd)
- [ ] Iconos coloridos (azul, amarillo, verde, rojo)
- [ ] Sección "Acciones Rápidas" con fondo OSCURO
- [ ] Sección "Actividad Reciente" con fondo OSCURO
- [ ] Cards oscuras (#2b3035)
- [ ] Items de actividad oscuros (#343a40)
- [ ] Títulos en BLANCO
- [ ] Descripciones en gris claro
- [ ] Sección "Tareas Pendientes" con fondo OSCURO
- [ ] Items de tareas oscuros
- [ ] TODO el texto legible

#### Gestión de Clientes:
- [ ] Card header "Gestión de Clientes" en azul OSCURO (#1e3a5f)
- [ ] Título "Gestión de Clientes" en BLANCO
- [ ] Botón "Registrar Nuevo Cliente" en azul BRILLANTE (#4dabf7)
- [ ] Filtros con fondo OSCURO:
  - [ ] Campo "Búsqueda General" oscuro (#343a40)
  - [ ] Select "Documento" oscuro (#343a40)
  - [ ] Select "Estado" oscuro (#343a40)
  - [ ] Botón "Buscar" azul brillante (#4dabf7)
  - [ ] Botón "X" (limpiar) visible
- [ ] Card de tabla con fondo OSCURO (#2b3035)
- [ ] Tabla "Listado de Clientes":
  - [ ] Header oscuro (#343a40) con texto BLANCO
  - [ ] Columnas: ID, NOMBRE Y APELLIDO, Nº DOCUMENTO, TELÉFONO, CORREO ELECTRÓNICO, DIRECCIÓN, ESTADO, ACCIONES
  - [ ] Filas oscuras (#2b3035) con texto CLARO (#e9ecef)
  - [ ] Filas alternas (#323841) para mejor lectura
  - [ ] Hover en filas funcional (#343a40)
  - [ ] Datos de clientes LEGIBLES:
    * Nombres en blanco/claro
    * Documentos legibles
    * Teléfonos legibles
    * Emails legibles
    * Direcciones legibles
  - [ ] Badges de estado MUY VISIBLES:
    * "Activo" en verde BRILLANTE (#51cf66)
    * "Inactivo" en rojo BRILLANTE (#ff6b6b)
  - [ ] Botones de acción MUY VISIBLES:
    * Botón "Ver" verde BRILLANTE (#51cf66)
    * Botón "Editar" azul BRILLANTE (#4dabf7)
    * Botón "Eliminar" rojo BRILLANTE (#ff6b6b)
  - [ ] Iconos en botones visibles
  - [ ] Bordes de tabla visibles (#495057)
- [ ] Información de tabla oscura:
  - [ ] "Información: Se encontraron XX clientes en el sistema" legible
  - [ ] Fondo cyan semi-transparente
- [ ] Paginación oscura y funcional

#### Productos:
- [ ] Card header oscuro (#1e3a5f)
- [ ] Tabla oscura (#2b3035)
- [ ] Headers oscuros (#343a40)
- [ ] Datos de productos legibles:
  - [ ] Nombres de productos
  - [ ] Códigos
  - [ ] Precios en blanco/claro
  - [ ] Stock legible
  - [ ] Categorías legibles
- [ ] Botones visibles
- [ ] Badges de stock visibles

#### Órdenes de Servicio:
- [ ] Card header oscuro
- [ ] Tabla oscura
- [ ] Headers oscuros
- [ ] Datos de órdenes legibles:
  - [ ] Números de orden
  - [ ] Clientes
  - [ ] Técnicos
  - [ ] Fechas legibles
  - [ ] Estados con badges coloridos
  - [ ] Equipos
- [ ] Botones de acción visibles

#### Ventas:
- [ ] Card header oscuro
- [ ] Tabla oscura
- [ ] Headers oscuros
- [ ] Datos de ventas legibles:
  - [ ] Números de venta
  - [ ] Clientes
  - [ ] Fechas
  - [ ] Totales en BLANCO
  - [ ] Estados
- [ ] Botones visibles

#### Usuarios:
- [ ] Card header oscuro
- [ ] Tabla oscura
- [ ] Headers oscuros
- [ ] Datos de usuarios legibles:
  - [ ] Nombres
  - [ ] Emails
  - [ ] Roles/Permisos
  - [ ] Estados
- [ ] Botones de gestión visibles

---

## 🎨 COLORES QUE DEBES VER EN MODO OSCURO

### Fondos:
```
Body general:        #1a1d20  (gris muy oscuro)
Cards:               #2b3035  (gris oscuro)
Headers de cards:    #1e3a5f  (azul oscuro)
Inputs y selects:    #343a40  (gris medio oscuro)
Headers de tabla:    #343a40  (gris medio oscuro)
Filas de tabla:      #2b3035  (gris oscuro)
Filas alternas:      #323841  (gris intermedio)
```

### Textos:
```
Títulos (h1-h6):     #ffffff  (blanco puro)
Texto normal:        #e9ecef  (blanco/gris muy claro)
Texto secundario:    #adb5bd  (gris claro)
Placeholders:        #adb5bd  (gris claro)
Headers de tabla:    #ffffff  (blanco puro)
Datos en tabla:      #e9ecef  (blanco/gris muy claro)
```

### Botones:
```
Primary:             #4dabf7  (azul brillante)
Success (Ver):       #51cf66  (verde brillante)
Danger (Eliminar):   #ff6b6b  (rojo brillante)
Warning:             #ffd43b  (amarillo brillante)
Info:                #22b8cf  (cyan brillante)
```

### Badges:
```
Activo/Success:      #51cf66  (verde brillante)
Inactivo/Danger:     #ff6b6b  (rojo brillante)
Warning:             #ffd43b  (amarillo brillante con texto negro)
Info:                #22b8cf  (cyan brillante)
```

### Bordes:
```
Cards:               #495057  (gris medio)
Tablas:              #495057  (gris medio)
Inputs:              #495057  (gris medio)
```

---

## 🚨 PROBLEMAS COMUNES Y SOLUCIONES

### Problema 1: El modo oscuro no se activa
**Solución:**
1. Borrar cache del navegador (Ctrl + Shift + Delete)
2. Hard refresh (Ctrl + F5)
3. Verificar que el botón de tema esté visible en el header

### Problema 2: Algunos elementos siguen blancos
**Solución:**
1. Inspeccionar con F12
2. Verificar que el `<body>` tenga la clase `dark-mode`
3. Ejecutar en consola: `python manage.py collectstatic --noinput`
4. Recargar página

### Problema 3: Los botones en tablas no se ven
**Solución:**
1. Limpiar cache
2. Verificar que `dark-mode-global.css` se esté cargando
3. Revisar en Network tab de F12

### Problema 4: El texto en tablas es difícil de leer
**Solución:**
1. Verificar que los estilos se apliquen correctamente
2. Inspeccionar elementos específicos
3. El texto debe ser #e9ecef o #ffffff

---

## 📸 COMPARACIÓN VISUAL

### MODO CLARO:
```
Dashboard:
- Fondo blanco general
- Cards blancas con sombra sutil
- Texto negro
- Botones con colores Bootstrap estándar
- Tablas blancas

Gestión de Clientes:
- Card blanca
- Header azul estándar (#0d6efd)
- Tabla blanca con headers gris claro
- Texto negro
- Botones estándar
```

### MODO OSCURO:
```
Dashboard:
- Fondo gris muy oscuro (#1a1d20)
- Cards grises oscuras (#2b3035)
- Texto blanco/claro
- Botones con colores brillantes
- Tablas oscuras

Gestión de Clientes:
- Card oscura (#2b3035)
- Header azul oscuro (#1e3a5f)
- Tabla oscura (#2b3035)
- Headers oscuros (#343a40)
- Texto blanco/claro
- Botones MUY BRILLANTES y visibles
- Badges coloridos destacados
- Enlaces azul brillante
```

---

## ✅ CONFIRMACIÓN FINAL

Si puedes marcar TODOS los checkboxes anteriores, entonces:

✅ El modo oscuro está funcionando PERFECTAMENTE
✅ Las tablas son 100% oscuras y legibles
✅ Todos los elementos son visibles
✅ No hay texto perdido o invisible
✅ Los botones y badges son muy visibles
✅ La experiencia es profesional y cómoda

---

## 🎯 PASOS PARA VERIFICAR AHORA

1. **Iniciar servidor:**
   ```powershell
   cd C:\DigitSoft2026\Digit_Sof_Nuevo
   python manage.py collectstatic --noinput
   python manage.py runserver
   ```

2. **Abrir navegador:**
   ```
   http://127.0.0.1:8000
   ```

3. **Iniciar sesión como admin**

4. **Verificar MODO CLARO:**
   - Ir a Dashboard → Verificar que todo se ve normal (blanco)
   - Ir a Clientes → Verificar tabla blanca
   - Ir a Productos → Verificar tabla blanca

5. **Activar MODO OSCURO:**
   - Hacer clic en el botón de tema (☀️/🌙)

6. **Verificar MODO OSCURO:**
   - Ir a Dashboard → Verificar que TODO es oscuro
   - Ir a Clientes → Verificar tabla OSCURA con botones MUY VISIBLES
   - Ir a Productos → Verificar tabla OSCURA
   - Ir a Órdenes → Verificar tabla OSCURA
   - Ir a Ventas → Verificar tabla OSCURA
   - Ir a Usuarios → Verificar tabla OSCURA

7. **Verificar elementos específicos:**
   - Hover en filas de tabla (debe cambiar a #343a40)
   - Click en botones (deben funcionar)
   - Ver badges de estado (deben ser muy visibles)
   - Leer todos los datos (deben ser legibles)

---

## 🎉 ¡ÉXITO!

Si todo está marcado, el modo oscuro está **PERFECTO** y listo para usar. 🌙✨

