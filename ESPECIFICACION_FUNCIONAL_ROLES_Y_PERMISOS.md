# 📋 ESPECIFICACIÓN FUNCIONAL: SISTEMA DE ROLES, PERMISOS Y FLUJOS DE TRABAJO

## 🎯 OBJETIVO

Crear una especificación funcional completa que sirva como guía de desarrollo para implementar un sistema que:

1. **Optimice la coordinación entre roles** mediante flujos de trabajo claros
2. **Mejore la comunicación del equipo** con notificaciones automáticas
3. **Garantice el cumplimiento de procedimientos** con validaciones
4. **Facilite la gestión de garantías y devoluciones** de productos

---

## 📑 ÍNDICE

1. [Roles del Sistema](#roles-del-sistema)
2. [Matriz de Permisos](#matriz-de-permisos)
3. [Flujos de Trabajo](#flujos-de-trabajo)
4. [Notificaciones por Rol](#notificaciones-por-rol)
5. [Módulos y Funcionalidades](#módulos-y-funcionalidades)
6. [Procesos Especiales](#procesos-especiales)
7. [Implementación Técnica](#implementación-técnica)
8. [Casos de Uso](#casos-de-uso)

---

## 1. ROLES DEL SISTEMA

### 1.1. ADMINISTRADOR

**Código del Sistema:** `ADMIN`

#### Responsabilidades Principales

1. **Coordinación y Supervisión**
   - Coordinar proyectos y asignar recursos
   - Supervisar personal y rendimiento
   - Gestionar incidentes y resolver problemas

2. **Gestión de Órdenes de Servicio**
   - Atender clientes iniciales
   - Registrar órdenes de servicio
   - Asignar técnicos verificando disponibilidad
   - Notificar técnicos sobre nuevas asignaciones

3. **Gestión de Garantías y Facturación**
   - Recibir notificaciones de trabajos completados
   - Gestionar garantías y devoluciones
   - Coordinar facturación

4. **Comunicación**
   - Recibir notificaciones de técnicos sobre estado de equipos
   - Comunicar al cliente el progreso
   - Resolver problemas de comunicación del equipo

5. **Reportes y Análisis**
   - Generar reportes de rendimiento técnico
   - Analizar métricas del sistema

#### Permisos de Acceso

✅ **Acceso Total:**
- Todos los módulos del sistema
- Gestión de usuarios
- Configuración del sistema
- Reportes completos

✅ **Operaciones CRUD:**
- Clientes, Técnicos, Proveedores
- Órdenes de Servicio
- Productos y Servicios
- Compras y Ventas
- Garantías

✅ **Funciones Especiales:**
- Asignar/reasignar técnicos
- Aprobar/rechazar solicitudes
- Gestionar contraseñas
- Configurar sistema

#### Información que Puede Ver

- ✅ Todos los datos de clientes
- ✅ Información completa de técnicos
- ✅ Historial de órdenes de servicio
- ✅ Inventario completo
- ✅ Reportes financieros
- ✅ Métricas de rendimiento
- ✅ Logs del sistema

#### Notificaciones que Recibe

1. **Alta Prioridad:**
   - ⚠️ Técnico completa trabajo (requiere facturación)
   - ⚠️ Problema crítico en equipo
   - ⚠️ Cliente solicita garantía
   - ⚠️ Orden atrasada

2. **Media Prioridad:**
   - 📢 Técnico actualiza estado de orden
   - 📢 Cliente solicita información
   - 📢 Stock bajo de productos
   - 📢 Nueva venta registrada

3. **Baja Prioridad:**
   - 📌 Recordatorio de seguimiento
   - 📌 Reporte periódico disponible
   - 📌 Backup completado

#### Interacciones con Otros Roles

**Con TÉCNICOS:**
- Asigna órdenes de servicio
- Recibe actualizaciones de progreso
- Aprueba solicitudes de repuestos
- Resuelve dudas técnicas

**Con CLIENTES:**
- Atiende solicitudes iniciales
- Comunica progreso de servicios
- Gestiona quejas y reclamos
- Aprueba garantías

**Con PROVEEDORES:**
- Gestiona compras
- Negocia precios
- Coordina entregas
- Resuelve problemas de calidad

---

### 1.2. TÉCNICO

**Código del Sistema:** `TECNICO`

#### Responsabilidades Principales

1. **Gestión de Órdenes de Servicio**
   - Recibir órdenes asignadas por administrador
   - Registrar observaciones de equipos
   - Notificar tiempos de resolución
   - Actualizar estado de la orden

2. **Ejecución de Servicios**
   - **Software:** Instalación, configuración, mantenimiento
   - **Infraestructura:** Redes, servidores, cableado
   - **Diseño Web:** Desarrollo, mantenimiento, SEO
   - **Soporte Técnico:** Diagnóstico, reparación, asesoría

3. **Documentación**
   - Registrar clientes nuevos
   - Documentar diagnósticos
   - Hacer observaciones técnicas
   - Generar reportes por servicio

4. **Comunicación**
   - Notificar al administrador sobre completitud
   - Informar problemas o retrasos
   - Solicitar repuestos o recursos
   - Comunicar al cliente (vía admin)

#### Permisos de Acceso

✅ **Módulos Accesibles:**
- Sus órdenes de servicio asignadas
- Clientes (solo lectura/creación)
- Catálogo de productos (consulta)
- Sus reportes de servicio
- Su perfil

✅ **Operaciones Permitidas:**
- Ver/editar órdenes asignadas
- Registrar nuevos clientes
- Actualizar estado de órdenes
- Generar reportes técnicos
- Solicitar repuestos

❌ **Operaciones Restringidas:**
- No puede eliminar órdenes
- No puede ver órdenes de otros técnicos (excepto consulta)
- No puede modificar precios
- No puede acceder a reportes financieros
- No puede gestionar usuarios

#### Información que Puede Ver

- ✅ Sus órdenes asignadas (completo)
- ✅ Datos de clientes relacionados
- ✅ Historial de sus servicios
- ✅ Catálogo de productos/repuestos
- ✅ Su rendimiento individual
- ⚠️ Órdenes de otros técnicos (solo consulta básica)
- ❌ Información financiera detallada

#### Notificaciones que Recibe

1. **Alta Prioridad:**
   - ⚠️ Nueva orden asignada
   - ⚠️ Orden urgente asignada
   - ⚠️ Cliente solicita actualización
   - ⚠️ Fecha de compromiso próxima

2. **Media Prioridad:**
   - 📢 Repuesto solicitado disponible
   - 📢 Administrador comentó la orden
   - 📢 Cliente aprobó presupuesto
   - 📢 Recordatorio de seguimiento

3. **Baja Prioridad:**
   - 📌 Nueva herramienta disponible
   - 📌 Actualización de procedimientos
   - 📌 Capacitación disponible

#### Interacciones con Otros Roles

**Con ADMINISTRADOR:**
- Recibe asignación de órdenes
- Reporta progreso y completitud
- Solicita recursos/repuestos
- Consulta dudas

**Con CLIENTES:**
- Contacto indirecto vía administrador
- Puede registrar clientes nuevos
- Documenta interacciones en la orden

**Con OTROS TÉCNICOS:**
- Puede consultar órdenes (solo lectura)
- Colaboración en casos complejos
- Intercambio de conocimiento

---

### 1.3. CLIENTE

**Código del Sistema:** `CLIENTE`

#### Responsabilidades Principales

1. **Solicitar Servicios**
   - Solicitar servicios técnicos
   - Describir problemas
   - Proporcionar información del equipo
   - Aprobar presupuestos

2. **Comprar Productos**
   - Explorar catálogo
   - Agregar al carrito
   - Realizar pedidos
   - Hacer seguimiento de órdenes

3. **Gestión de Garantías**
   - Solicitar garantías
   - Presentar factura y evidencia
   - Hacer seguimiento del proceso

4. **Seguimiento**
   - Ver estado de servicios
   - Recibir notificaciones
   - Consultar historial
   - Descargar facturas

#### Permisos de Acceso

✅ **Módulos Accesibles:**
- Catálogo de productos (tienda)
- Sus órdenes de servicio
- Su carrito de compras
- Sus facturas
- Sus garantías
- Su perfil

✅ **Operaciones Permitidas:**
- Ver catálogo de productos
- Comprar productos disponibles
- Solicitar servicios
- Ver estado de sus órdenes
- Solicitar garantías
- Actualizar su perfil

❌ **Operaciones Restringidas:**
- No puede ver datos de otros clientes
- No puede modificar precios
- No puede acceder al panel administrativo
- No puede ver inventario interno
- No puede gestionar usuarios

#### Información que Puede Ver

- ✅ Catálogo de productos públicos
- ✅ Sus órdenes de servicio
- ✅ Su historial de compras
- ✅ Sus facturas
- ✅ Estado de sus garantías
- ❌ Inventario interno
- ❌ Datos de otros clientes
- ❌ Información financiera del negocio

#### Notificaciones que Recibe

1. **Alta Prioridad:**
   - ⚠️ Orden de servicio lista para entrega
   - ⚠️ Garantía aprobada/rechazada
   - ⚠️ Acción requerida en pedido
   - ⚠️ Problema con su equipo

2. **Media Prioridad:**
   - 📢 Actualización de estado de orden
   - 📢 Presupuesto disponible
   - 📢 Producto solicitado disponible
   - 📢 Factura generada

3. **Baja Prioridad:**
   - 📌 Recordatorio de pago
   - 📌 Promociones disponibles
   - 📌 Nuevo producto en catálogo
   - 📌 Encuesta de satisfacción

#### Interacciones con Otros Roles

**Con ADMINISTRADOR:**
- Solicita servicios
- Consulta estado de órdenes
- Solicita garantías
- Reporta problemas

**Con TÉCNICO:**
- Contacto indirecto vía administrador
- Proporciona información del equipo
- Aprueba trabajos realizados

**Con PROVEEDOR:**
- Compra productos del catálogo
- Hace pedidos especiales
- Consulta disponibilidad

---

### 1.4. PROVEEDOR

**Código del Sistema:** `PROVEEDOR`

#### Responsabilidades Principales

1. **Gestión de Productos**
   - Mantener catálogo actualizado
   - Gestionar inventario
   - Definir precios
   - Publicar disponibilidad

2. **Ventas**
   - Vender productos del catálogo
   - Gestionar pedidos especiales
   - Ofrecer servicios en la nube
   - Negociar ventas corporativas

3. **Productos Ofrecidos**
   - Computadores y portátiles
   - Equipos corporativos
   - Impresoras multifuncionales
   - Cámaras de seguridad
   - Accesorios y cables
   - UPS y reguladores
   - Biométricos
   - Licenciamiento de software
   - Suministros de oficina

4. **Gestión de Pedidos**
   - Procesar pedidos
   - Coordinar despachos
   - Gestionar condiciones de pago
   - Hacer seguimiento de entregas

#### Permisos de Acceso

✅ **Módulos Accesibles:**
- Catálogo de productos (gestión)
- Sus ventas
- Inventario de sus productos
- Pedidos de clientes
- Reportes de sus ventas
- Su perfil

✅ **Operaciones Permitidas:**
- Gestionar sus productos (CRUD)
- Ver/procesar pedidos
- Actualizar inventario
- Configurar precios
- Generar reportes de ventas
- Buscar productos sostenibles

❌ **Operaciones Restringidas:**
- No puede ver productos de otros proveedores
- No puede acceder a datos de clientes (excepto compras)
- No puede gestionar usuarios
- No puede ver órdenes de servicio
- No puede acceder a reportes globales

#### Información que Puede Ver

- ✅ Sus productos y precios
- ✅ Su inventario
- ✅ Pedidos de sus productos
- ✅ Datos de clientes (solo para entregas)
- ✅ Sus ventas y reportes
- ⚠️ Catálogo general (solo lectura)
- ❌ Inventario de otros proveedores
- ❌ Datos financieros globales

#### Notificaciones que Recibe

1. **Alta Prioridad:**
   - ⚠️ Nuevo pedido recibido
   - ⚠️ Producto con stock crítico
   - ⚠️ Pedido urgente
   - ⚠️ Problema con entrega

2. **Media Prioridad:**
   - 📢 Cliente consulta disponibilidad
   - 📢 Pedido entregado confirmado
   - 📢 Pago recibido
   - 📢 Producto devuelto

3. **Baja Prioridad:**
   - 📌 Reporte de ventas disponible
   - 📌 Producto sin movimiento
   - 📌 Actualización de políticas
   - 📌 Evaluación de desempeño

#### Interacciones con Otros Roles

**Con ADMINISTRADOR:**
- Coordina compras corporativas
- Negocia precios
- Reporta problemas
- Recibe evaluaciones

**Con CLIENTE:**
- Vende productos
- Coordina entregas
- Procesa pedidos especiales
- Gestiona devoluciones

---

## 2. MATRIZ DE PERMISOS

### 2.1. Acceso por Módulo

| Módulo | Admin | Técnico | Cliente | Proveedor |
|--------|-------|---------|---------|-----------|
| **Dashboard General** | ✅ Total | ✅ Personal | ✅ Personal | ✅ Personal |
| **Usuarios** | ✅ CRUD | ❌ | ❌ | ❌ |
| **Clientes** | ✅ CRUD | ✅ Lectura/Crear | ❌ Su perfil | ❌ Solo ventas |
| **Técnicos** | ✅ CRUD | ✅ Lectura | ❌ | ❌ |
| **Proveedores** | ✅ CRUD | ❌ | ❌ | ✅ Su perfil |
| **Productos** | ✅ CRUD | ✅ Lectura | ✅ Catálogo | ✅ CRUD propios |
| **Inventario** | ✅ Total | ✅ Consulta | ❌ | ✅ Propio |
| **Órdenes Servicio** | ✅ CRUD | ✅ Asignadas | ✅ Propias | ❌ |
| **Compras** | ✅ CRUD | ❌ | ❌ | ✅ Lectura |
| **Ventas** | ✅ CRUD | ❌ | ✅ Propias | ✅ Propias |
| **Facturación** | ✅ Total | ⚠️ Generar | ✅ Propias | ⚠️ Propias |
| **Garantías** | ✅ CRUD | ✅ Evaluar | ✅ Solicitar | ❌ |
| **Reportes** | ✅ Todos | ✅ Personales | ✅ Personales | ✅ Propios |
| **Notificaciones** | ✅ Todas | ✅ Propias | ✅ Propias | ✅ Propias |
| **Configuración** | ✅ Total | ❌ | ❌ | ❌ |

**Leyenda:**
- ✅ Acceso completo
- ⚠️ Acceso limitado
- ❌ Sin acceso

### 2.2. Operaciones CRUD por Entidad

| Entidad | Admin | Técnico | Cliente | Proveedor |
|---------|-------|---------|---------|-----------|
| **Usuario** | CRUD | R | R (propio) | R (propio) |
| **Cliente** | CRUD | CR | R (propio) | R (limitado) |
| **Técnico** | CRUD | R | - | - |
| **Proveedor** | CRUD | - | - | RU (propio) |
| **Producto** | CRUD | R | R (catálogo) | CRUD (propios) |
| **Orden Servicio** | CRUD | RU (asignadas) | R (propias) | - |
| **Compra** | CRUD | - | - | R |
| **Venta** | CRUD | - | R (propias) | R (propias) |
| **Garantía** | CRUD | RU | CR | - |
| **Reporte** | CRUD | C (técnicos) | R (propios) | R (propios) |

**Leyenda:**
- **C**reate: Crear nuevos registros
- **R**ead: Leer/consultar registros
- **U**pdate: Actualizar registros
- **D**elete: Eliminar registros

### 2.3. Permisos Especiales

| Permiso | Admin | Técnico | Cliente | Proveedor |
|---------|-------|---------|---------|-----------|
| Asignar técnicos | ✅ | ❌ | ❌ | ❌ |
| Aprobar garantías | ✅ | ⚠️ Evaluar | ❌ | ❌ |
| Gestionar contraseñas | ✅ | ❌ | ⚠️ Propia | ⚠️ Propia |
| Ver reportes globales | ✅ | ❌ | ❌ | ❌ |
| Modificar precios | ✅ | ❌ | ❌ | ⚠️ Propios |
| Eliminar registros | ✅ | ❌ | ❌ | ⚠️ Propios |
| Configurar sistema | ✅ | ❌ | ❌ | ❌ |
| Gestionar usuarios | ✅ | ❌ | ❌ | ❌ |
| Procesar devoluciones | ✅ | ⚠️ Evaluar | ⚠️ Solicitar | ❌ |
| Generar facturas | ✅ | ⚠️ Propias | ❌ | ⚠️ Propias |

---

## 3. FLUJOS DE TRABAJO

### 3.1. Flujo: Orden de Servicio Técnico

```
┌─────────────────────────────────────────────────────────────────┐
│ FLUJO COMPLETO: ORDEN DE SERVICIO TÉCNICO                       │
└─────────────────────────────────────────────────────────────────┘

1. SOLICITUD INICIAL (Cliente → Administrador)
   ┌─────────────────────────────────────────────┐
   │ Cliente: Solicita servicio técnico          │
   │ - Describe el problema                      │
   │ - Proporciona datos del equipo             │
   └─────────────┬───────────────────────────────┘
                 │
                 ▼
   ┌─────────────────────────────────────────────┐
   │ Admin: Atiende solicitud inicial            │
   │ - Registra cliente (si es nuevo)            │
   │ - Crea orden de servicio                    │
   │ - Asigna número de orden                    │
   │ Estado: RECIBIDA                            │
   └─────────────┬───────────────────────────────┘
                 │
                 │ NOTIFICACIÓN → Cliente: "Orden #XXX registrada"
                 │

2. ASIGNACIÓN DE TÉCNICO (Administrador)
   ┌─────────────────────────────────────────────┐
   │ Admin: Asigna técnico                       │
   │ - Verifica disponibilidad                   │
   │ - Considera especialidad                    │
   │ - Asigna prioridad                          │
   │ - Define fecha de compromiso                │
   └─────────────┬───────────────────────────────┘
                 │
                 │ NOTIFICACIÓN → Técnico: "Nueva orden asignada #XXX"
                 │ NOTIFICACIÓN → Cliente: "Técnico asignado"
                 │

3. DIAGNÓSTICO (Técnico)
   ┌─────────────────────────────────────────────┐
   │ Técnico: Inicia diagnóstico                 │
   │ - Recibe orden de servicio                  │
   │ - Inspecciona equipo                        │
   │ - Registra observaciones                    │
   │ - Documenta estado físico                   │
   │ Estado: EN_DIAGNOSTICO                      │
   └─────────────┬───────────────────────────────┘
                 │
                 ▼
   ┌─────────────────────────────────────────────┐
   │ Técnico: Completa diagnóstico               │
   │ - Identifica problema                       │
   │ - Estima tiempo de reparación               │
   │ - Calcula costos                            │
   │ - Actualiza orden                           │
   │ Estado: DIAGNOSTICADA                       │
   └─────────────┬───────────────────────────────┘
                 │
                 │ NOTIFICACIÓN → Admin: "Diagnóstico completado #XXX"
                 │

4. APROBACIÓN DE PRESUPUESTO (Admin → Cliente)
   ┌─────────────────────────────────────────────┐
   │ Admin: Comunica presupuesto al cliente      │
   │ - Revisa diagnóstico                        │
   │ - Prepara presupuesto                       │
   │ - Contacta al cliente                       │
   └─────────────┬───────────────────────────────┘
                 │
                 │ NOTIFICACIÓN → Cliente: "Presupuesto disponible"
                 │
                 ▼
   ┌─────────────────────────────────────────────┐
   │ Cliente: Aprueba o rechaza                  │
   │ - Revisa costos                             │
   │ - Decide continuar                          │
   └─────────────┬───────────────────────────────┘
                 │
                 ├─ SI APRUEBA ──→ Continúa al paso 5
                 │
                 └─ SI RECHAZA ──→ Estado: CANCELADA
                                    NOTIFICACIÓN → Técnico, Admin

5. REPARACIÓN (Técnico)
   ┌─────────────────────────────────────────────┐
   │ Técnico: Ejecuta reparación                 │
   │ - Aplica solución                           │
   │ - Instala repuestos (si necesario)          │
   │ - Prueba funcionamiento                     │
   │ - Documenta trabajo realizado               │
   │ Estado: EN_REPARACION                       │
   └─────────────┬───────────────────────────────┘
                 │
                 ▼ (Actualiza estado periódicamente)
                 │
   ┌─────────────────────────────────────────────┐
   │ Técnico: Completa reparación                │
   │ - Verifica calidad                          │
   │ - Actualiza solución aplicada               │
   │ - Notifica completitud                      │
   │ Estado: REPARADA                            │
   └─────────────┬───────────────────────────────┘
                 │
                 │ NOTIFICACIÓN → Admin: "Reparación completada #XXX - Requiere facturación"
                 │

6. FACTURACIÓN Y ENTREGA (Administrador)
   ┌─────────────────────────────────────────────┐
   │ Admin: Genera factura                       │
   │ - Revisa trabajo completado                 │
   │ - Calcula total (diagnóstico + mano obra)   │
   │ - Genera factura                            │
   │ Estado: LISTA_ENTREGA                       │
   └─────────────┬───────────────────────────────┘
                 │
                 │ NOTIFICACIÓN → Cliente: "Su equipo está listo para entrega"
                 │
                 ▼
   ┌─────────────────────────────────────────────┐
   │ Cliente: Recoge equipo                      │
   │ - Revisa trabajo realizado                  │
   │ - Realiza pago                              │
   │ - Firma conformidad                         │
   └─────────────┬───────────────────────────────┘
                 │
                 ▼
   ┌─────────────────────────────────────────────┐
   │ Admin: Cierra orden                         │
   │ - Registra entrega                          │
   │ - Confirma pago                             │
   │ Estado: ENTREGADA                           │
   └─────────────────────────────────────────────┘

   NOTIFICACIÓN → Técnico: "Orden #XXX entregada exitosamente"
   NOTIFICACIÓN → Cliente: "Gracias por su preferencia - Garantía: 30 días"

┌─────────────────────────────────────────────────────────────────┐
│ ESTADOS ESPECIALES                                              │
├─────────────────────────────────────────────────────────────────┤
│ EN_ESPERA_REPUESTOS: Si faltan repuestos                       │
│ - Técnico solicita repuestos                                   │
│ - Admin procesa solicitud                                      │
│ - Sistema notifica cuando llegan repuestos                     │
│                                                                 │
│ EN_ESPERA_CLIENTE: Si cliente debe proporcionar información    │
│ - Técnico solicita datos/accesos                              │
│ - Admin contacta al cliente                                    │
│ - Sistema espera respuesta                                     │
└─────────────────────────────────────────────────────────────────┘
```

### 3.2. Flujo: Compra de Productos

```
┌─────────────────────────────────────────────────────────────────┐
│ FLUJO: COMPRA DE PRODUCTOS (E-COMMERCE)                        │
└─────────────────────────────────────────────────────────────────┘

1. EXPLORACIÓN (Cliente)
   ┌─────────────────────────────────────────────┐
   │ Cliente: Explora catálogo                   │
   │ - Busca productos                           │
   │ - Filtra por categoría                      │
   │ - Compara precios                           │
   │ - Lee especificaciones                      │
   └─────────────┬───────────────────────────────┘
                 │
                 ▼
2. CARRITO (Cliente)
   ┌─────────────────────────────────────────────┐
   │ Cliente: Agrega al carrito                  │
   │ - Selecciona cantidad                       │
   │ - Verifica disponibilidad                   │
   │ - Calcula subtotal                          │
   └─────────────┬───────────────────────────────┘
                 │
                 ▼
3. CHECKOUT (Cliente)
   ┌─────────────────────────────────────────────┐
   │ Cliente: Procesa compra                     │
   │ - Confirma productos                        │
   │ - Verifica dirección de entrega             │
   │ - Selecciona método de pago: EFECTIVO       │
   │ - Confirma pedido                           │
   └─────────────┬───────────────────────────────┘
                 │
                 │ SI HAY STOCK → Continúa
                 │ SI NO HAY STOCK → Pedido especial (paso 3a)
                 │
                 ▼
4. PROCESAMIENTO (Sistema → Proveedor)
   ┌─────────────────────────────────────────────┐
   │ Sistema: Procesa venta                      │
   │ - Genera número de venta                    │
   │ - Reserva productos                         │
   │ - Reduce stock                              │
   └─────────────┬───────────────────────────────┘
                 │
                 │ NOTIFICACIÓN → Proveedor: "Nueva venta #XXX"
                 │ NOTIFICACIÓN → Cliente: "Pedido confirmado #XXX"
                 │
                 ▼
5. PREPARACIÓN (Proveedor)
   ┌─────────────────────────────────────────────┐
   │ Proveedor: Prepara despacho                 │
   │ - Empaca productos                          │
   │ - Genera guía de despacho                   │
   │ - Coordina entrega                          │
   └─────────────┬───────────────────────────────┘
                 │
                 │ NOTIFICACIÓN → Cliente: "Su pedido está en camino"
                 │
                 ▼
6. ENTREGA Y FACTURACIÓN
   ┌─────────────────────────────────────────────┐
   │ Proveedor: Entrega productos                │
   │ - Cliente recibe productos                  │
   │ - Verifica contenido                        │
   │ - Paga (efectivo)                           │
   │ - Recibe factura                            │
   └─────────────────────────────────────────────┘

   NOTIFICACIÓN → Cliente: "Gracias por su compra"
   NOTIFICACIÓN → Admin: "Venta completada #XXX"

┌─────────────────────────────────────────────────────────────────┐
│ 3a. FLUJO ALTERNATIVO: PEDIDO SIN STOCK                        │
├─────────────────────────────────────────────────────────────────┤
│ Cliente: Solicita producto sin stock                           │
│ - Sistema muestra fecha estimada                               │
│ - Cliente acepta fecha acordada                                │
│ - Se registra pedido pendiente                                 │
│                                                                 │
│ NOTIFICACIÓN → Proveedor: "Pedido especial - Cliente espera"  │
│                                                                 │
│ Proveedor: Solicita producto                                   │
│ - Coordina con distribuidores                                  │
│ - Actualiza fecha estimada                                     │
│                                                                 │
│ NOTIFICACIÓN → Cliente: "Su producto llegará el [fecha]"      │
│                                                                 │
│ Cuando llega: Continúa desde paso 5                           │
└─────────────────────────────────────────────────────────────────┘
```

### 3.3. Flujo: Gestión de Garantías

```
┌─────────────────────────────────────────────────────────────────┐
│ FLUJO: GESTIÓN DE GARANTÍAS                                    │
└─────────────────────────────────────────────────────────────────┘

1. SOLICITUD (Cliente)
   ┌─────────────────────────────────────────────┐
   │ Cliente: Solicita garantía                  │
   │ - Presenta factura                          │
   │ - Describe el problema                      │
   │ - Proporciona evidencia (fotos/videos)      │
   │ - Sistema registra solicitud                │
   └─────────────┬───────────────────────────────┘
                 │
                 │ NOTIFICACIÓN → Admin: "Nueva solicitud de garantía"
                 │
                 ▼
2. VALIDACIÓN INICIAL (Administrador)
   ┌─────────────────────────────────────────────┐
   │ Admin: Valida requisitos                    │
   │ - Verifica factura válida                   │
   │ - Revisa periodo de garantía                │
   │ - Evalúa descripción del problema           │
   │ - Revisa evidencias                         │
   └─────────────┬───────────────────────────────┘
                 │
                 ├─ SI ES VÁLIDA → Continúa al paso 3
                 │
                 └─ SI NO ES VÁLIDA → Rechaza
                    ┌─────────────────────────────┐
                    │ Admin: Rechaza solicitud     │
                    │ - Explica motivo             │
                    │ Estado: RECHAZADA            │
                    └──────────────────────────────┘
                    NOTIFICACIÓN → Cliente: "Garantía no aplica - [Motivo]"

3. ASIGNACIÓN Y DIAGNÓSTICO (Admin → Técnico)
   ┌─────────────────────────────────────────────┐
   │ Admin: Asigna para análisis técnico         │
   │ - Asigna técnico especializado              │
   │ - Programa revisión                         │
   │ Estado: EN_ANALISIS                         │
   └─────────────┬───────────────────────────────┘
                 │
                 │ NOTIFICACIÓN → Técnico: "Análisis de garantía asignado"
                 │ NOTIFICACIÓN → Cliente: "Su caso está siendo evaluado"
                 │
                 ▼
   ┌─────────────────────────────────────────────┐
   │ Técnico: Evalúa el equipo                   │
   │ - Inspecciona el defecto                    │
   │ - Determina si es defecto de fábrica        │
   │ - Evalúa si cumple condiciones              │
   │ - Documenta hallazgos                       │
   │ - Genera informe técnico                    │
   └─────────────┬───────────────────────────────┘
                 │
                 │ NOTIFICACIÓN → Admin: "Informe técnico disponible"
                 │

4. DECISIÓN (Administrador)
   ┌─────────────────────────────────────────────┐
   │ Admin: Revisa informe técnico               │
   │ - Analiza hallazgos                         │
   │ - Verifica políticas de garantía            │
   │ - Toma decisión                             │
   └─────────────┬───────────────────────────────┘
                 │
                 ├─────────────────┬─────────────────┐
                 │                 │                 │
                 ▼ SI APLICA       ▼ NO APLICA      ▼ PARCIAL
                 │                 │                 │

5a. GARANTÍA APROBADA
   ┌─────────────────────────────────────────────┐
   │ Admin: Aprueba garantía                     │
   │ - Autoriza reemplazo/reparación             │
   │ - Genera nueva orden                        │
   │ Estado: APROBADA                            │
   └─────────────┬───────────────────────────────┘
                 │
                 │ NOTIFICACIÓN → Cliente: "Garantía aprobada"
                 │
                 ▼
   ┌─────────────────────────────────────────────┐
   │ Opciones de resolución:                     │
   ├─────────────────────────────────────────────┤
   │ A. CAMBIO DE EQUIPO                         │
   │    - Proveedor proporciona reemplazo        │
   │    - Se genera nueva factura                │
   │    - Cliente recibe equipo nuevo            │
   │                                             │
   │ B. CORRECCIÓN DE ERRORES                    │
   │    - Técnico repara sin costo               │
   │    - Se crea nueva orden de servicio        │
   │    - Proceso similar a orden normal         │
   │                                             │
   │ C. DEVOLUCIÓN DE DINERO (si aplica)         │
   │    - Se procesa reembolso                   │
   │    - Cliente devuelve producto              │
   │    - Se actualiza inventario                │
   └─────────────────────────────────────────────┘

   NOTIFICACIÓN → Cliente: "Su garantía ha sido resuelta"

5b. GARANTÍA NO APROBADA
   ┌─────────────────────────────────────────────┐
   │ Admin: Rechaza garantía                     │
   │ - Explica motivo detallado                  │
   │ - Ofrece solución con costo adicional       │
   │ Estado: NO_APLICA                           │
   └─────────────┬───────────────────────────────┘
                 │
                 │ NOTIFICACIÓN → Cliente: "Garantía no aprobada - [Explicación]"
                 │
                 ▼
   ┌─────────────────────────────────────────────┐
   │ Admin: Ofrece alternativa                   │
   │ - Presupuesta reparación con costo          │
   │ - Cliente decide si acepta                  │
   └─────────────┬───────────────────────────────┘
                 │
                 ├─ SI ACEPTA → Crea nueva orden de servicio
                 └─ SI RECHAZA → Devuelve equipo sin cambios

5c. GARANTÍA PARCIAL
   ┌─────────────────────────────────────────────┐
   │ Admin: Aprueba garantía parcial             │
   │ - Cubre parte del costo                     │
   │ - Cliente paga diferencia                   │
   │ - Se procesa como combinación               │
   └─────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ CONDICIONES PARA APROBACIÓN DE GARANTÍA                        │
├─────────────────────────────────────────────────────────────────┤
│ ✅ Equipo defectuoso de fábrica                                │
│ ✅ No cumple con expectativas especificadas                    │
│ ✅ Falla dentro del periodo de garantía                        │
│ ✅ No presenta daños por mal uso                               │
│ ✅ Cliente presenta factura original                           │
│ ✅ Evidencia del problema documentada                          │
│                                                                 │
│ ❌ Daño por mal uso del cliente                                │
│ ❌ Fuera del periodo de garantía                               │
│ ❌ Sin factura o evidencia                                     │
│ ❌ Producto alterado o reparado externamente                   │
└─────────────────────────────────────────────────────────────────┘
```

### 3.4. Flujo: Devoluciones de Productos

```
┌─────────────────────────────────────────────────────────────────┐
│ FLUJO: DEVOLUCIÓN DE PRODUCTOS                                  │
└─────────────────────────────────────────────────────────────────┘

1. SOLICITUD (Cliente)
   ┌─────────────────────────────────────────────┐
   │ Cliente: Solicita devolución                │
   │ - Accede a su historial de compras          │
   │ - Selecciona producto a devolver            │
   │ - Indica motivo de devolución               │
   │ - Sistema registra solicitud                │
   └─────────────┬───────────────────────────────┘
                 │
                 │ NOTIFICACIÓN → Admin: "Solicitud de devolución"
                 │
                 ▼
2. VALIDACIÓN (Administrador)
   ┌─────────────────────────────────────────────┐
   │ Admin: Valida solicitud                     │
   │ - Consulta servicios del cliente            │
   │ - Verifica factura y fecha de compra        │
   │ - Revisa estado del producto                │
   │ - Evalúa motivo de devolución               │
   └─────────────┬───────────────────────────────┘
                 │
                 ├─ SI ES VÁLIDA → Continúa al paso 3
                 │
                 └─ SI NO ES VÁLIDA → Rechaza
                    NOTIFICACIÓN → Cliente: "Devolución no procede - [Motivo]"

3. COORDINACIÓN DE DEVOLUCIÓN
   ┌─────────────────────────────────────────────┐
   │ Admin: Coordina devolución                  │
   │ - Programa recolección del producto         │
   │ - Informa al cliente el proceso             │
   │ - Prepara documentación                     │
   │ Estado: APROBADA                            │
   └─────────────┬───────────────────────────────┘
                 │
                 │ NOTIFICACIÓN → Cliente: "Devolución aprobada - Instrucciones"
                 │
                 ▼
4. RECEPCIÓN Y VERIFICACIÓN
   ┌─────────────────────────────────────────────┐
   │ Admin/Técnico: Recibe producto              │
   │ - Inspecciona estado del producto           │
   │ - Verifica embalaje original                │
   │ - Confirma accesorios completos             │
   │ - Documenta condición                       │
   └─────────────┬───────────────────────────────┘
                 │
                 ▼
5. PROCESAMIENTO
   ┌─────────────────────────────────────────────┐
   │ Admin: Procesa devolución                   │
   │ - Anula factura original                    │
   │ - Actualiza inventario (si aplica)          │
   │ - Procesa reembolso o cambio                │
   │ - Genera nota de crédito                    │
   │ Estado: COMPLETADA                          │
   └─────────────────────────────────────────────┘

   NOTIFICACIÓN → Cliente: "Devolución procesada exitosamente"
   NOTIFICACIÓN → Proveedor: "Producto devuelto - Actualizar inventario"

┌─────────────────────────────────────────────────────────────────┐
│ POLÍTICAS DE DEVOLUCIÓN                                        │
├─────────────────────────────────────────────────────────────────┤
│ ✅ Dentro de 7 días de la compra                               │
│ ✅ Producto en su embalaje original                            │
│ ✅ Sin signos de uso                                           │
│ ✅ Incluye todos los accesorios                                │
│ ✅ Presenta factura original                                   │
│                                                                 │
│ ❌ Productos personalizados                                    │
│ ❌ Software abierto o licencias activadas                      │
│ ❌ Productos dañados por el cliente                            │
└─────────────────────────────────────────────────────────────────┘
```

---

*Continúa en la siguiente sección...*

**Documento creado:** ESPECIFICACION_FUNCIONAL_ROLES_Y_PERMISOS.md (Parte 1/3)

