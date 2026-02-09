# 🔔 SISTEMA DE NOTIFICACIONES AUTOMÁTICAS - IMPLEMENTADO

## ✅ Sistema Completo Agregado al Proyecto

He implementado un **sistema completo de notificaciones automáticas** para tu proyecto DIGIT SOFT.

---

## 🎯 Funcionalidades Implementadas

### 1. ✅ Notificaciones al Administrador

**Cuándo se activan:**
- ✉️ Cuando llega una **nueva orden de servicio**
- 📧 Email automático con todos los detalles
- 🔔 Notificación in-app en el panel de administración

**Qué incluye:**
- Información completa del cliente
- Detalles del equipo
- Falla reportada
- Enlace directo para inspeccionar la orden

### 2. ✅ Notificaciones al Cliente

**Cuándo se activan:**
- 📱 Cada vez que cambia el **estado de su orden**
- ✅ Cuando el equipo está **listo para retirar**
- 🎉 Cuando el equipo es **entregado**

**Canales:**
- 📧 Email profesional con diseño HTML
- 🔔 Notificación in-app (si el cliente tiene cuenta)

### 3. ✅ Sistema de Demoras

**Monitoreo automático:**
- 🔍 Detecta órdenes con **demoras** respecto a la fecha compromiso
- ⚠️ Notifica al administrador automáticamente
- 📊 Registra la novedad en el historial de la orden

### 4. ✅ Recuperación de Contraseña

**Funcionalidad:**
- 🔐 Enlace seguro enviado por email
- ⏱️ Válido por 24 horas
- 🛡️ Sistema de tokens seguros

---

## 📁 Archivos Creados

### Servicios Backend:
```
ordenes/
├── notifications.py (Servicio principal de notificaciones)
└── management/
    └── commands/
        └── detectar_demoras.py (Comando para detectar demoras)
```

### Plantillas de Email:
```
templates/
└── emails/
    ├── nueva_orden_admin.html (Email al administrador)
    ├── cambio_estado_cliente.html (Actualización para cliente)
    ├── orden_lista.html (Equipo listo para retirar)
    └── recuperacion_password.html (Recuperación de contraseña)
```

---

## ⚙️ Configuración Requerida

### 1. Configurar Email en `settings.py`

Agrega estas líneas a tu archivo `settings.py`:

```python
# Configuración de Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # O tu servidor SMTP
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'tu_email@gmail.com'  # Tu email
EMAIL_HOST_PASSWORD = 'tu_contraseña_app'  # Contraseña de aplicación
DEFAULT_FROM_EMAIL = 'DIGIT SOFT <tu_email@gmail.com>'

# Email del administrador
ADMIN_EMAIL = 'admin@digitsoft.com'

# URL del sitio
SITE_URL = 'http://localhost:8000'  # Cambiar en producción
```

### 2. Configurar Gmail (Si usas Gmail)

1. Ve a tu cuenta de Google
2. Activa la **verificación en dos pasos**
3. Genera una **contraseña de aplicación**:
   - https://myaccount.google.com/apppasswords
   - Selecciona "Correo" y "Otro"
   - Copia la contraseña generada
4. Usa esa contraseña en `EMAIL_HOST_PASSWORD`

### 3. Configurar Tarea Programada (Opcional)

Para detectar demoras automáticamente, configura una tarea cron:

**Linux/Mac:**
```bash
# Editar crontab
crontab -e

# Agregar esta línea (ejecutar cada día a las 9 AM)
0 9 * * * cd /ruta/proyecto && python manage.py detectar_demoras
```

**Windows (Task Scheduler):**
1. Abre "Programador de tareas"
2. Crear tarea básica
3. Programa: Diario a las 9 AM
4. Acción: `python manage.py detectar_demoras`

---

## 🚀 Cómo Funciona

### Flujo de Notificaciones:

#### 1. Cliente crea una orden
```
Cliente → Sistema crea orden
    ↓
Admin recibe email + notificación in-app
    ↓
Cliente recibe confirmación por email
```

#### 2. Administrador cambia estado
```
Admin cambia estado a "EN_REPARACION"
    ↓
Sistema detecta el cambio
    ↓
Cliente recibe email + notificación in-app
    ↓
Se registra en el historial
```

#### 3. Equipo listo para entregar
```
Admin cambia estado a "LISTA_ENTREGA"
    ↓
Sistema envía email especial al cliente
    ↓
Notificación destacada in-app
    ↓
Email incluye: costo total, garantía, instrucciones
```

#### 4. Detección de demoras
```
Sistema ejecuta detectar_demoras
    ↓
Revisa todas las órdenes activas
    ↓
Compara con fecha compromiso
    ↓
Si hay demora → Notifica al admin
    ↓
Registra novedad en la orden
```

---

## 📧 Ejemplos de Emails

### Email al Administrador (Nueva Orden):
```
🔔 Nueva Orden de Servicio
Orden: ORD-2026-00001

ACCIÓN REQUERIDA: Nueva orden que requiere atención inmediata

Cliente: Jorge Martínez
Email: jorge@email.com
Teléfono: 3001234567

Equipo: Laptop HP Pavilion
Falla: No enciende

[VER ORDEN COMPLETA] ← Botón
```

### Email al Cliente (Cambio de Estado):
```
📢 Actualización de su Orden
Orden: ORD-2026-00001

Estimado Jorge,

Su orden ha sido actualizada:

Estado: RECIBIDA → EN_REPARACION

Detalles: Su equipo está siendo reparado por nuestros técnicos.

[VER ESTADO COMPLETO] ← Botón
```

### Email al Cliente (Equipo Listo):
```
✅ ¡Su Equipo está Listo!
Orden: ORD-2026-00001

🎉 ¡Buenas Noticias!

Su Laptop HP Pavilion ha sido reparado exitosamente.

Costo Total: $150.000
🛡️ Garantía: 30 días

[VER DETALLES] ← Botón

Cómo Retirar:
Acérquese con su documento de identidad.
```

---

## 🧪 Cómo Probar

### 1. Probar Notificación al Administrador:

```bash
# En la shell de Django
python manage.py shell
```

```python
from ordenes.models import OrdenServicio
from ordenes.notifications import ServicioNotificaciones

# Obtener una orden
orden = OrdenServicio.objects.first()

# Enviar notificación
ServicioNotificaciones.notificar_nueva_orden_admin(orden)
```

### 2. Probar Cambio de Estado:

```python
from ordenes.notifications import ServicioNotificaciones

ServicioNotificaciones.notificar_cambio_estado_cliente(
    orden, 
    'RECIBIDA', 
    'EN_REPARACION',
    'Su equipo está siendo diagnosticado'
)
```

### 3. Probar Detección de Demoras:

```bash
python manage.py detectar_demoras
```

### 4. Probar Orden Lista:

```python
ServicioNotificaciones.notificar_orden_lista_entrega(orden)
```

---

## 📊 Panel de Admin - Novedades

### Ver Notificaciones:

El administrador verá en su panel:
- 🔔 Badge con número de notificaciones no leídas
- Lista de notificaciones ordenadas por prioridad
- Iconos y colores según el tipo
- Enlaces directos a las órdenes

### Registrar Novedades:

Cuando el admin edita una orden y detecta un problema:
```python
from ordenes.notifications import MonitorDemoras

MonitorDemoras.registrar_novedad(
    orden,
    tipo='INCIDENCIA',
    descripcion='Se requiere repuesto adicional',
    usuario=request.user
)
```

---

## 🎨 Tipos de Notificaciones

### Por Evento:

| Evento | Color | Icono | Prioridad |
|--------|-------|-------|-----------|
| Nueva Orden | Azul | 🔧 | Alta |
| Cambio Estado | Cyan | 🔄 | Media |
| Lista Entrega | Verde | ✅ | Alta |
| Demora | Amarillo | ⚠️ | Alta |
| Entregada | Verde | 🎉 | Baja |

---

## 🔒 Seguridad

### Recuperación de Contraseña:

```python
from ordenes.notifications import ServicioNotificaciones

ServicioNotificaciones.enviar_recordatorio_recuperacion_password(
    usuario,
    token='abc123...'
)
```

**Características:**
- ✅ Token único de un solo uso
- ✅ Válido por 24 horas
- ✅ Enlace seguro HTTPS
- ✅ Mensaje de advertencia si no fue solicitado

---

## 💡 Consejos de Uso

### 1. Personalizar Mensajes:

Edita `ordenes/notifications.py` en la función `notificar_cambio_estado_cliente` para personalizar los mensajes según cada estado.

### 2. Agregar Más Eventos:

Puedes agregar notificaciones para:
- Repuestos solicitados
- Técnico asignado
- Comentarios del cliente
- Recordatorios de pago

### 3. Estadísticas:

Monitorea las notificaciones:
```python
from usuarios.models import Notificacion

# Notificaciones no leídas
no_leidas = Notificacion.objects.filter(leida=False).count()

# Notificaciones por tipo
por_tipo = Notificacion.objects.values('tipo').annotate(count=Count('id'))
```

---

## ✅ Checklist de Implementación

- [x] Servicio de notificaciones creado
- [x] Plantillas de email diseñadas
- [x] Integración con vistas de órdenes
- [x] Sistema de detección de demoras
- [x] Comando para tareas programadas
- [x] Recuperación de contraseña
- [ ] Configurar email en settings.py
- [ ] Probar envío de emails
- [ ] Configurar tarea programada (opcional)
- [ ] Personalizar mensajes (opcional)

---

## 🚨 Solución de Problemas

### Los emails no se envían:

1. Verifica configuración SMTP en `settings.py`
2. Revisa que el email y contraseña sean correctos
3. Para Gmail, usa contraseña de aplicación
4. Verifica que TLS esté activado

### Las notificaciones no aparecen:

1. Verifica que el modelo Notificacion esté migrado
2. Comprueba que el usuario tenga cuenta
3. Revisa la consola de errores

### Las demoras no se detectan:

1. Ejecuta manualmente: `python manage.py detectar_demoras`
2. Verifica que las órdenes tengan `fecha_compromiso`
3. Revisa la configuración de timezone

---

## 📚 Documentación Adicional

### Clases Principales:

1. **ServicioNotificaciones**: Gestiona todas las notificaciones
2. **MonitorDemoras**: Detecta y registra demoras
3. **Notificacion** (modelo): Almacena notificaciones in-app

### Métodos Disponibles:

```python
ServicioNotificaciones.notificar_nueva_orden_admin(orden)
ServicioNotificaciones.notificar_cambio_estado_cliente(orden, estado_anterior, estado_nuevo, descripcion)
ServicioNotificaciones.notificar_demora_detectada(orden, dias_demora)
ServicioNotificaciones.notificar_orden_lista_entrega(orden)
ServicioNotificaciones.enviar_recordatorio_recuperacion_password(usuario, token)

MonitorDemoras.detectar_demoras()
MonitorDemoras.registrar_novedad(orden, tipo, descripcion, usuario)
```

---

## 🎉 Resultado Final

Ahora tu sistema DIGIT SOFT tiene:

✅ **Notificaciones automáticas al administrador** cuando llega una orden
✅ **Emails profesionales** a los clientes en cada cambio
✅ **Detección automática de demoras**
✅ **Registro de novedades** en el historial
✅ **Sistema de recuperación de contraseña**
✅ **Panel centralizado** de notificaciones
✅ **Plantillas HTML** profesionales y responsive

---

**Fecha de implementación:** 05/02/2026  
**Desarrollador:** GitHub Copilot  
**Sistema:** DIGIT SOFT - Gestión de Órdenes de Servicio

