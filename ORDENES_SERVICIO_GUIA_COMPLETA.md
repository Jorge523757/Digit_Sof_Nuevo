# 🔧 SISTEMA DE ÓRDENES DE SERVICIO - GUÍA COMPLETA

## 📋 ÍNDICE
1. [Características Implementadas](#características-implementadas)
2. [Generación de Datos de Prueba](#generación-de-datos-de-prueba)
3. [Uso del Sistema](#uso-del-sistema)
4. [Funcionalidades Detalladas](#funcionalidades-detalladas)
5. [Sistema de Notificaciones](#sistema-de-notificaciones)

---

## ✨ CARACTERÍSTICAS IMPLEMENTADAS

### 🎨 Diseño Mejorado en Azul
- ✅ **Sin colores rosa** - Todo el diseño usa colores azules, verdes y naranjas
- ✅ **Gradientes profesionales** - Azul oscuro (#1e3c72) a azul claro (#00b4d8)
- ✅ **Animaciones suaves** - Transiciones y efectos visuales modernos
- ✅ **Responsive** - Se adapta a móviles y tablets

### 📝 Gestión Completa de Órdenes
- ✅ **Crear órdenes** con formulario completo
- ✅ **Editar órdenes** existentes
- ✅ **Cambiar estados** con registro en historial
- ✅ **Búsqueda avanzada** por múltiples criterios
- ✅ **Filtros por fecha** - Buscar por rango de fechas
- ✅ **Paginación mejorada** con diseño moderno

### 📊 Registro y Seguimiento
- ✅ **Timeline de estados** - Historial visual completo
- ✅ **Registro de técnicos** - Quién hizo cada cambio
- ✅ **Fechas importantes**:
  - Fecha de recepción del equipo
  - Fecha de revisión inicial
  - Fecha estimada de entrega
  - Fecha real de entrega
  - Días en servicio (calculado automático)

### 🔔 Sistema de Notificaciones
- ✅ **Notificación al crear orden** - Cliente recibe confirmación
- ✅ **Notificación al cambiar estado** - Actualización automática
- ✅ **Mensajes personalizados** según el estado
- ✅ **Iconos y colores** según tipo de notificación

### 📈 Estadísticas en Tiempo Real
- ✅ **Total de órdenes**
- ✅ **Órdenes en proceso**
- ✅ **Listas para entrega**
- ✅ **Órdenes entregadas**

---

## 🎲 GENERACIÓN DE DATOS DE PRUEBA

### Opción 1: Usar el Script Automático (RECOMENDADO)

1. **Ejecutar el script batch:**
   ```
   GENERAR_DATOS_ORDENES.bat
   ```

2. **El script generará automáticamente:**
   - 20 órdenes de servicio con datos realistas
   - Estados variados (desde recibidas hasta entregadas)
   - Historial completo de cada orden
   - Seguimientos con fechas y responsables

3. **Los datos se guardan en MySQL permanentemente**
   - NO se borran al reiniciar el servidor
   - NO se borran al hacer migraciones
   - Permanecen hasta que los elimines manualmente

### Opción 2: Manual con Python

```bash
python generar_datos_ordenes.py
```

### ⚠️ IMPORTANTE: Requisitos Previos

Antes de generar órdenes, necesitas tener:
- ✅ **Clientes** en la base de datos
- ✅ **Técnicos** en la base de datos (opcional)

Si no tienes clientes, ejecuta primero:
```bash
python generar_datos_faker.py
```

---

## 🚀 USO DEL SISTEMA

### 1️⃣ Crear Nueva Orden de Servicio

1. **Acceder al sistema:**
   - URL: `http://localhost:8000/ordenes/`
   - Click en **"Nueva Orden de Servicio"**

2. **Completar el formulario:**
   
   **Sección 1: Cliente**
   - Seleccionar cliente (con buscador Select2)
   - Asignar técnico (opcional)

   **Sección 2: Equipo**
   - Tipo de equipo (Laptop, PC, Impresora, etc.)
   - Marca y modelo
   - Número de serie (opcional)
   - Accesorios incluidos

   **Sección 3: Problema**
   - Falla reportada por el cliente (OBLIGATORIO)
   - Estado físico del equipo al recibirlo

   **Sección 4: Diagnóstico**
   - Diagnóstico técnico (opcional al crear)
   - Solución aplicada (opcional al crear)

   **Sección 5: Estado y Prioridad**
   - Estado inicial (por defecto: RECIBIDA)
   - Prioridad (BAJA, MEDIA, ALTA, URGENTE)
   - Fecha estimada de entrega

   **Sección 6: Costos**
   - Costo de diagnóstico
   - Costo de mano de obra
   - Repuestos se agregan después

   **Sección 7: Garantía**
   - Incluye garantía (Sí/No)
   - Días de garantía (por defecto: 30)
   - Observaciones
   - Notas internas (solo para personal)

3. **Guardar:**
   - Click en **"Crear Orden de Servicio"**
   - El sistema asigna automáticamente el número de orden
   - Se crea el primer seguimiento automáticamente
   - Se envía notificación al cliente

### 2️⃣ Ver Detalle de Orden

1. **Desde el listado:**
   - Click en el número de orden o en "Ver detalles"

2. **Información mostrada:**
   
   **Columna Izquierda:**
   - 👤 Información del cliente completa
   - 💻 Detalles del equipo
   - ⚠️ Falla reportada
   - 🔍 Diagnóstico y solución
   - 📜 **Timeline de estados** (historial visual)

   **Columna Derecha:**
   - 👨‍🔧 Técnico responsable
   - 📅 Fechas importantes
   - 💰 Desglose de costos
   - ⚡ Acciones rápidas

### 3️⃣ Cambiar Estado de Orden

**Opción A: Desde el Detalle**
1. Click en **"Cambiar Estado"**
2. Seleccionar nuevo estado
3. Escribir descripción del cambio
4. Guardar

**Opción B: Desde Editar**
1. Click en **"Editar Orden"**
2. Cambiar el estado
3. Automáticamente pide descripción del cambio
4. Guardar cambios

**Estados disponibles:**
- 🔵 RECIBIDA - Equipo recién recibido
- 🟠 EN_DIAGNOSTICO - Técnico revisando
- 🔵 DIAGNOSTICADA - Problema identificado
- 🟠 EN_REPARACION - Equipo en reparación
- 🟢 REPARADA - Reparación completada
- 🟣 EN_ESPERA_REPUESTOS - Esperando piezas
- 🟡 EN_ESPERA_CLIENTE - Esperando aprobación/pago
- 🔵 LISTA_ENTREGA - Lista para retirar
- 🟢 ENTREGADA - Equipo entregado al cliente
- ⚫ CANCELADA - Orden cancelada

**Cada cambio de estado:**
- ✅ Se registra en el historial
- ✅ Se guarda fecha y hora exacta
- ✅ Se registra quién hizo el cambio
- ✅ Se envía notificación al cliente
- ✅ Se actualiza el timeline visual

### 4️⃣ Buscar Órdenes

**Búsqueda Simple:**
- Ingresar texto en el campo de búsqueda
- Busca en: número de orden, cliente, marca, modelo, equipo

**Filtros Avanzados:**
- **Por estado:** Seleccionar estado específico
- **Por prioridad:** Filtrar por urgencia
- **Por cliente:** Nombre del cliente
- **Por técnico:** Técnico asignado
- **Por equipo:** Tipo de equipo
- **Por fechas:** Rango de fechas (desde - hasta)

**Ejemplo de búsqueda por fecha:**
1. Seleccionar fecha desde: `01/01/2026`
2. Seleccionar fecha hasta: `31/01/2026`
3. Click en "Buscar"
4. Muestra todas las órdenes de enero

---

## 📱 FUNCIONALIDADES DETALLADAS

### 📊 Historial de Estados (Timeline)

Cada orden tiene un **timeline visual** que muestra:

```
🔵 RECIBIDA
   └─ 04/02/2026 10:30
   └─ Equipo recibido: Laptop HP Pavilion
   └─ Responsable: Juan Técnico

🟠 EN_DIAGNOSTICO
   └─ 05/02/2026 09:15
   └─ Iniciado diagnóstico de problema de pantalla
   └─ Responsable: Juan Técnico

🟠 EN_REPARACION
   └─ 06/02/2026 14:20
   └─ Cambio de pantalla LCD, limpieza interna
   └─ Responsable: Juan Técnico

🟢 LISTA_ENTREGA
   └─ 08/02/2026 16:45
   └─ Reparación completada, equipo probado OK
   └─ Responsable: Juan Técnico
```

### 👨‍🔧 Registro de Técnicos

Para cada orden se registra:
- **Técnico asignado** - Responsable principal
- **Quién hizo cada cambio** - En el historial
- **Fecha de recepción** - Cuándo se recibió el equipo
- **Fecha de revisión** - Cuándo inició el diagnóstico
- **Fecha de entrega** - Cuándo se entregó al cliente

### 💰 Sistema de Costos

**Cálculo automático:**
- Costo de diagnóstico
- Costo de mano de obra
- Costo de repuestos
- **TOTAL** = Suma automática de los tres

**Visualización:**
- Desglose detallado en el detalle
- Total destacado en grande
- Indicador de pago (pagado/pendiente)

### 🔔 Notificaciones Automáticas

**Cuándo se envían:**
1. Al crear una orden nueva
2. Al cambiar el estado
3. Cuando está lista para entrega
4. Al entregar el equipo

**Tipos de mensajes:**
- 📘 Orden creada: "Su equipo ha sido recibido"
- 🔄 Cambio de estado: "El estado cambió a..."
- ✅ Lista para entrega: "¡Su equipo está listo!"
- 🎉 Entregada: "Gracias por confiar en nosotros"

**Personalización:**
- Icono según el tipo
- Color según la urgencia
- Link directo al detalle de la orden

---

## 🎨 DISEÑO Y COLORES

### Paleta de Colores (Sin Rosa)

**Azules:**
- Principal: `#1e3c72` (Azul oscuro)
- Secundario: `#2a5298` (Azul medio)
- Acento: `#00b4d8` (Azul cyan)

**Complementarios:**
- Naranja: `#ff6b35` (Para alertas/advertencias)
- Verde: `#06d6a0` (Para éxito/completado)
- Amarillo: `#f7931e` (Para en proceso)

**Estados:**
- Recibida: Azul `#1e3c72`
- En Revisión: Naranja `#ff6b35`
- En Reparación: Amarillo `#f7931e`
- Lista: Cyan `#00b4d8`
- Entregada: Verde `#06d6a0`

---

## 🔄 DATOS Y MYSQL

### ¿Por Qué No Se Borran los Datos?

Los datos generados con el script **se guardan permanentemente** en MySQL porque:

1. **Se escriben en la base de datos real** (no en memoria)
2. **MySQL persiste los datos** en disco
3. **Las migraciones no borran datos** (solo modifican estructura)
4. **Git no incluye la base de datos** (solo código)

### Para Mantener Datos al Hacer Push a GitHub:

Los datos **NO se suben a GitHub** porque:
- La base de datos MySQL está en tu computadora
- Solo se sube el código fuente
- Cada persona que clone el repo debe generar sus propios datos

### Solución: Fixtures o Datos Iniciales

Para compartir datos con otros desarrolladores:

**Opción 1: Exportar fixtures**
```bash
python manage.py dumpdata ordenes --indent 2 > ordenes_fixtures.json
```

**Opción 2: Script de datos**
- Ya lo tienes: `generar_datos_ordenes.py`
- Cada persona ejecuta el script después de clonar
- Genera datos de prueba automáticamente

---

## 📝 RESUMEN DE ARCHIVOS CREADOS

### Templates (HTML):
- ✅ `templates/ordenes/crear.html` - Formulario de creación
- ✅ `templates/ordenes/editar.html` - Formulario de edición
- ✅ `templates/ordenes/detalle.html` - Vista detallada con timeline

### Scripts:
- ✅ `generar_datos_ordenes.py` - Generador de datos
- ✅ `GENERAR_DATOS_ORDENES.bat` - Ejecutor automático

### CSS:
- ✅ `static/css/ordenes-modern.css` - Estilos modernos en azul

### Funcionalidades en Views:
- ✅ `orden_crear()` - Crear con notificaciones
- ✅ `orden_editar()` - Editar con seguimiento
- ✅ `orden_cambiar_estado()` - Cambiar estado con notificaciones
- ✅ `orden_detalle()` - Vista completa con historial

---

## 🎉 ¡TODO LISTO!

Ahora tienes un sistema completo de órdenes de servicio con:

✅ Diseño profesional en azul (sin rosa)
✅ Creación y edición de órdenes
✅ Búsqueda avanzada con filtros de fecha
✅ Historial completo con timeline visual
✅ Registro de técnicos y responsables
✅ Sistema de notificaciones automáticas
✅ Generador de datos de prueba
✅ Datos que persisten en MySQL
✅ Paginación moderna
✅ Responsive design

**Para empezar:**
1. Ejecuta `GENERAR_DATOS_ORDENES.bat`
2. Inicia el servidor: `python manage.py runserver`
3. Visita: `http://localhost:8000/ordenes/`
4. ¡Disfruta del sistema!

---

**Creado por:** DIGT SOFT Development Team  
**Fecha:** 04/02/2026  
**Versión:** 2.0 - Sistema Completo de Órdenes

