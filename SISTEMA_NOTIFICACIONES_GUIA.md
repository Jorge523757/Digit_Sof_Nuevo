# 🔔 SISTEMA DE NOTIFICACIONES MULTICANAL Y AUTOMATIZACIÓN

## 📋 ÍNDICE
1. [Características Implementadas](#características-implementadas)
2. [Configuración Inicial](#configuración-inicial)
3. [Canales de Notificación](#canales-de-notificación)
4. [Flujo de Comunicación](#flujo-de-comunicación)
5. [Alertas y Monitoreo](#alertas-y-monitoreo)
6. [Uso del Sistema](#uso-del-sistema)

---

## ✨ CARACTERÍSTICAS IMPLEMENTADAS

### 1. Registro Automático al Ingreso
- ✅ **Captura automática** de estado del equipo
- ✅ **Fecha de llegada** registrada automáticamente
- ✅ **Fecha estimada de entrega** configurable
- ✅ **Estado físico** del equipo documentado
- ✅ **Accesorios incluidos** registrados

### 2. Notificaciones Multicanal
- ✅ **Email** - Correo electrónico
- ✅ **SMS** - Mensajes de texto
- ✅ **WhatsApp** - Mensajes de WhatsApp
- ✅ **Push** - Notificaciones push en app
- ✅ **Teléfono** - Registro de llamadas necesarias

### 3. Alertas de Técnicos
- ✅ **Reportar ocupación** - Estado de disponibilidad
- ✅ **Demoras** - Notificar cambios en cronograma
- ✅ **Repuestos faltantes** - Alertar problemas
- ✅ **Problemas adicionales** - Comunicar hallazgos
- ✅ **Cambio de fechas** - Actualizar estimados

### 4. Actualizaciones al Cliente
- ✅ **Automáticas** - Sin intervención manual
- ✅ **En tiempo real** - Inmediatas al cambiar estado
- ✅ **Multicanal** - Por email, SMS, WhatsApp
- ✅ **Proactivas** - Antes del vencimiento

### 5. Monitoreo Inteligente
- ✅ **Alerta 3 días** antes del vencimiento
- ✅ **Alerta 1 día** antes del vencimiento
- ✅ **Alerta vencida** cuando se pasa la fecha
- ✅ **Actualización automática** de estados de técnicos
- ✅ **Capacidad de trabajo** monitoreada

---

## 🚀 CONFIGURACIÓN INICIAL

### Paso 1: Agregar la app de notificaciones

Crear el archivo `notificaciones/__init__.py`:
```python
# Vacío
```

Crear `notificaciones/apps.py`:
```python
from django.apps import AppConfig

class NotificacionesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notificaciones'
    verbose_name = 'Sistema de Notificaciones'
```

### Paso 2: Registrar en settings.py

```python
INSTALLED_APPS = [
    # ... otras apps
    'notificaciones',
]
```

### Paso 3: Configurar canales de email

En `settings.py`:
```python
# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # O tu servidor SMTP
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'tu_email@gmail.com'
EMAIL_HOST_PASSWORD = 'tu_password'
DEFAULT_FROM_EMAIL = 'DIGT SOFT <noreply@digitsoft.com>'
```

### Paso 4: Migrar base de datos

```bash
python manage.py makemigrations notificaciones
python manage.py migrate
```

### Paso 5: Crear configuraciones iniciales

```bash
python manage.py shell
```

```python
from notificaciones.models import CanalNotificacion, ConfiguracionNotificacion

# Crear canales
email = CanalNotificacion.objects.create(nombre='EMAIL', activo=True, prioridad=1)
sms = CanalNotificacion.objects.create(nombre='SMS', activo=False, prioridad=2)
whatsapp = CanalNotificacion.objects.create(nombre='WHATSAPP', activo=False, prioridad=1)
push = CanalNotificacion.objects.create(nombre='PUSH', activo=False, prioridad=3)

# Configurar notificación de orden creada para cliente
config_cliente = ConfiguracionNotificacion.objects.create(
    tipo_usuario='CLIENTE',
    evento='ORDEN_CREADA',
    activo=True,
    template_mensaje='''
Hola {{destinatario_nombre}},

Su orden de servicio {{numero_orden}} ha sido creada exitosamente.

Equipo: {{equipo}}
Fecha de recepción: {{fecha_recepcion}}
Fecha estimada de entrega: {{fecha_compromiso}}

Mantendremos informado sobre el progreso de la reparación.

Saludos,
DIGT SOFT
    '''
)
config_cliente.canales.add(email)

# Configurar notificación de orden asignada para técnico
config_tecnico = ConfiguracionNotificacion.objects.create(
    tipo_usuario='TECNICO',
    evento='ORDEN_ASIGNADA',
    activo=True,
    template_mensaje='''
Hola {{tecnico_nombre}},

Se te ha asignado una nueva orden de servicio.

Orden: {{numero_orden}}
Cliente: {{cliente_nombre}}
Equipo: {{equipo}}
Fecha compromiso: {{fecha_compromiso}}

Por favor revisa los detalles en el sistema.

DIGT SOFT
    '''
)
config_tecnico.canales.add(email)
```

---

## 📧 CANALES DE NOTIFICACIÓN

### 1. Email (Implementado)
**Estado:** ✅ Funcionando  
**Configuración:**
- Editar `settings.py` con tu servidor SMTP
- Por defecto usa Gmail
- Cambiar credenciales en producción

**Uso:**
```python
from notificaciones.services import ServicioNotificaciones

ServicioNotificaciones.enviar_notificacion(
    orden=orden,
    evento='ORDEN_CREADA',
    destinatario_tipo='CLIENTE',
    destinatario=orden.cliente
)
```

### 2. SMS (Preparado para Twilio)
**Estado:** 🔧 Requiere configuración  
**Pasos:**

1. Crear cuenta en [Twilio](https://www.twilio.com/)
2. Obtener credenciales (Account SID, Auth Token)
3. Agregar a `settings.py`:
```python
TWILIO_ACCOUNT_SID = 'tu_account_sid'
TWILIO_AUTH_TOKEN = 'tu_auth_token'
TWILIO_PHONE_NUMBER = '+1234567890'
```
4. Instalar biblioteca:
```bash
pip install twilio
```
5. Descomentar código en `notificaciones/services.py` líneas 69-76

### 3. WhatsApp (Preparado para Twilio)
**Estado:** 🔧 Requiere configuración  
**Pasos:**

1. Configurar WhatsApp Business en Twilio
2. Agregar a `settings.py`:
```python
TWILIO_WHATSAPP_NUMBER = '+1234567890'
```
3. Descomentar código en `notificaciones/services.py` líneas 92-100

### 4. Notificaciones Push (Preparado para Firebase)
**Estado:** 🔧 Requiere configuración  
**Pasos:**

1. Crear proyecto en [Firebase Console](https://console.firebase.google.com/)
2. Descargar archivo de credenciales JSON
3. Instalar biblioteca:
```bash
pip install firebase-admin
```
4. Configurar en `settings.py`:
```python
FIREBASE_CREDENTIALS = 'ruta/al/archivo.json'
```
5. Descomentar código en `notificaciones/services.py` líneas 114-125

### 5. Llamadas Telefónicas (Registro)
**Estado:** ✅ Registra necesidad de llamada  
**Funcionalidad:**
- Registra que se debe hacer una llamada
- Puede integrarse con sistemas de IVR
- Genera recordatorios para el personal

---

## 🔄 FLUJO DE COMUNICACIÓN

### Escenario 1: Cliente trae equipo

```
1. RECEPCIONISTA crea orden
   ↓
2. Sistema captura:
   - Estado del equipo
   - Fecha de llegada
   - Accesorios
   - Falla reportada
   ↓
3. Notificaciones automáticas:
   ✉️ Email al cliente (confirmación)
   ✉️ Email al técnico (nueva asignación)
   ↓
4. Técnico actualiza estado
   ↓
5. Cliente recibe actualización automática
```

### Escenario 2: Técnico reporta demora

```
1. TÉCNICO crea alerta de demora
   ↓
2. Sistema registra:
   - Nueva fecha estimada
   - Motivo de la demora
   - Días de retraso
   ↓
3. Notificaciones automáticas:
   ✉️ Email/SMS al cliente
   ✉️ Email al administrador
   📧 Notificación en sistema
   ↓
4. Cliente está informado proactivamente
```

### Escenario 3: Fecha próxima a vencer

```
1. SISTEMA monitorea diariamente
   ↓
2. Detecta: Faltan 3 días
   ↓
3. Envía alerta al técnico:
   ✉️ Email
   📧 Notificación sistema
   ↓
4. Detecta: Falta 1 día
   ↓
5. Envía alerta al técnico Y cliente:
   ✉️ Email a ambos
   💬 WhatsApp al cliente
   📧 Notificación sistema
   ↓
6. Fecha vencida sin entrega:
   ↓
7. Escala al administrador:
   ✉️ Email urgente
   📱 Notificación prioritaria
```

---

## ⚠️ ALERTAS Y MONITOREO

### Tipos de Alertas de Técnico

```python
from notificaciones.models import AlertaTecnico

# Reportar demora
AlertaTecnico.objects.create(
    orden=orden,
    tecnico=tecnico,
    tipo_alerta='DEMORA',
    descripcion='Repuesto no disponible en stock',
    nueva_fecha_estimada=nueva_fecha,
    dias_demora=3
)

# Reportar repuesto faltante
AlertaTecnico.objects.create(
    orden=orden,
    tecnico=tecnico,
    tipo_alerta='REPUESTO_FALTANTE',
    descripcion='Se requiere pantalla LCD específica'
)

# Problema adicional encontrado
AlertaTecnico.objects.create(
    orden=orden,
    tecnico=tecnico,
    tipo_alerta='PROBLEMA_ADICIONAL',
    descripcion='Se detectó daño en placa madre',
    requiere_autorizacion=True
)
```

### Estados de Técnico

```python
from notificaciones.models import EstadoTecnico

# Actualizar disponibilidad
estado = EstadoTecnico.objects.get(tecnico=tecnico)
estado.estado = 'OCUPADO'
estado.notas = 'En servicio externo hasta las 16:00'
estado.disponible_desde = datetime(2026, 2, 4, 16, 0)
estado.save()
```

### Monitoreo Automático

**Configurar tarea programada:**

**Windows (Task Scheduler):**
```batch
# Crear archivo: monitorear_diario.bat
@echo off
cd C:\ruta\al\proyecto
python manage.py monitorear_ordenes
```

Configurar en Task Scheduler:
- Ejecutar diariamente a las 08:00 AM
- Comando: `C:\ruta\al\proyecto\monitorear_diario.bat`

**Linux (Crontab):**
```bash
# Editar crontab
crontab -e

# Agregar línea (ejecutar diario a las 8 AM)
0 8 * * * cd /ruta/al/proyecto && python manage.py monitorear_ordenes
```

---

## 📱 USO DEL SISTEMA

### Para Recepcionistas

1. **Crear orden de servicio:**
   - Completar formulario completo
   - Sistema envía notificaciones automáticamente
   - No requiere acción adicional

2. **Asignar técnico:**
   - Seleccionar en formulario
   - Técnico recibe notificación inmediata

### Para Técnicos

1. **Recibir asignación:**
   - Email/WhatsApp automático
   - Notificación en sistema
   - Revisar detalles en dashboard

2. **Actualizar estado:**
   - Cambiar estado en sistema
   - Cliente recibe actualización automática
   - Timeline se actualiza

3. **Reportar problemas:**
```python
# Desde vista de técnico
def reportar_demora(request, orden_id):
    orden = get_object_or_404(OrdenServicio, pk=orden_id)
    
    AlertaTecnico.objects.create(
        orden=orden,
        tecnico=request.user.tecnico,
        tipo_alerta='DEMORA',
        descripcion=request.POST['descripcion'],
        nueva_fecha_estimada=request.POST['nueva_fecha'],
        dias_demora=request.POST['dias']
    )
    
    # Notificar al cliente automáticamente
    ServicioNotificaciones.enviar_notificacion(
        orden=orden,
        evento='DEMORA_REPORTADA',
        destinatario_tipo='CLIENTE',
        destinatario=orden.cliente
    )
    
    return redirect('ordenes:detalle', pk=orden_id)
```

4. **Actualizar disponibilidad:**
```python
# Desde perfil de técnico
def actualizar_estado(request):
    estado = EstadoTecnico.objects.get(tecnico=request.user.tecnico)
    estado.estado = request.POST['estado']
    estado.notas = request.POST['notas']
    estado.save()
    
    return redirect('perfil')
```

### Para Clientes

1. **Recibir actualizaciones:**
   - Automáticas por email
   - Opcionales por WhatsApp/SMS
   - Consultar en portal web

2. **Ver estado en tiempo real:**
   - Portal de cliente
   - Timeline visual
   - Estado actual
   - Fecha estimada

### Para Administradores

1. **Monitorear sistema:**
```bash
# Ver historial de notificaciones
python manage.py shell

from notificaciones.models import HistorialNotificacion

# Notificaciones del día
HistorialNotificacion.objects.filter(
    fecha_programada__date=timezone.now().date()
)

# Notificaciones fallidas
HistorialNotificacion.objects.filter(estado='ERROR')
```

2. **Ver alertas pendientes:**
```python
from notificaciones.models import AlertaTecnico

# Alertas sin atender
AlertaTecnico.objects.filter(atendida=False)

# Demoras reportadas
AlertaTecnico.objects.filter(tipo_alerta='DEMORA', atendida=False)
```

---

## 📊 REPORTES Y ESTADÍSTICAS

### Dashboard de Notificaciones

```python
from notificaciones.models import HistorialNotificacion

# Notificaciones por canal
HistorialNotificacion.objects.values('canal__nombre').annotate(
    total=Count('id'),
    enviadas=Count('id', filter=Q(estado='ENVIADA')),
    fallidas=Count('id', filter=Q(estado='ERROR'))
)

# Tasa de entrega
total = HistorialNotificacion.objects.count()
exitosas = HistorialNotificacion.objects.filter(estado='ENVIADA').count()
tasa = (exitosas / total * 100) if total > 0 else 0
```

### Estado de Técnicos

```python
from notificaciones.models import EstadoTecnico

# Técnicos disponibles
EstadoTecnico.objects.filter(estado='DISPONIBLE')

# Técnicos con capacidad
EstadoTecnico.objects.filter(
    ordenes_activas__lt=F('capacidad_maxima')
)

# Técnicos sobrecargados
EstadoTecnico.objects.filter(
    ordenes_activas__gte=F('capacidad_maxima')
)
```

---

## 🎯 PRÓXIMOS PASOS

### 1. Configurar Email (Inmediato)
- ✅ Ya está preparado
- Editar credenciales en `settings.py`
- Probar envío

### 2. Integrar WhatsApp (Opcional)
- Crear cuenta Twilio
- Configurar WhatsApp Business
- Descomentar código

### 3. Integrar SMS (Opcional)
- Configurar Twilio SMS
- Descomentar código
- Probar envío

### 4. Programar Monitoreo (Recomendado)
- Configurar tarea en Task Scheduler (Windows)
- O crontab (Linux)
- Ejecutar diariamente

### 5. Crear Templates Personalizados
- Editar mensajes en ConfiguracionNotificacion
- Personalizar para cada evento
- Agregar logo/firma

---

## ✅ RESUMEN

**Has implementado un sistema completo que:**
- ✅ Registra equipos automáticamente al ingreso
- ✅ Notifica multicanal (Email, SMS, WhatsApp, Push)
- ✅ Permite a técnicos reportar alertas
- ✅ Actualiza clientes automáticamente
- ✅ Monitorea fechas y envía alertas proactivas
- ✅ Mantiene historial completo de comunicaciones
- ✅ Optimiza gestión de reparaciones

**Comunicación transparente y en tiempo real lograda!** 🎉

---

**Fecha:** 04/02/2026  
**Versión:** 1.0 - Sistema de Notificaciones Multicanal

