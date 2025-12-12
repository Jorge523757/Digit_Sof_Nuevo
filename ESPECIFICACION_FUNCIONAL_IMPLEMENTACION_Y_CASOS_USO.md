# 📋 ESPECIFICACIÓN FUNCIONAL: IMPLEMENTACIÓN TÉCNICA Y CASOS DE USO

## 6. IMPLEMENTACIÓN TÉCNICA

### 6.1. Estructura de Modelos

#### A. Modelo de Usuario y Perfil

```python
# usuarios/models.py

class PerfilUsuario(models.Model):
    """
    Perfil extendido del usuario con información de rol y permisos
    """
    TIPO_USUARIO_CHOICES = [
        ('ADMIN', 'Administrador'),
        ('CLIENTE', 'Cliente'),
        ('TECNICO', 'Técnico'),
        ('PROVEEDOR', 'Proveedor'),
    ]
    
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='perfil'
    )
    
    tipo_usuario = models.CharField(
        max_length=10,
        choices=TIPO_USUARIO_CHOICES,
        default='CLIENTE'
    )
    
    # Información adicional
    telefono = models.CharField(max_length=15, blank=True)
    direccion = models.TextField(blank=True)
    documento = models.CharField(max_length=20, blank=True)
    foto = models.ImageField(upload_to='usuarios/', blank=True, null=True)
    
    # Control de acceso
    bloqueado = models.BooleanField(default=False)
    motivo_bloqueo = models.TextField(blank=True)
    intentos_login = models.IntegerField(default=0)
    ultimo_acceso = models.DateTimeField(null=True, blank=True)
    
    # Relaciones con entidades específicas
    cliente = models.ForeignKey(
        'clientes.Cliente',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='usuario_perfil'
    )
    
    tecnico = models.ForeignKey(
        'tecnicos.Tecnico',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='usuario_perfil'
    )
    
    # Preferencias de notificaciones
    notificaciones_email = models.BooleanField(default=True)
    notificaciones_push = models.BooleanField(default=True)
    notificaciones_sms = models.BooleanField(default=False)
    
    # Metadata
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Perfil de Usuario"
        verbose_name_plural = "Perfiles de Usuario"
    
    def __str__(self):
        return f"{self.user.get_full_name()} - {self.get_tipo_usuario_display()}"
    
    # Métodos de verificación de rol
    def es_admin(self):
        return self.tipo_usuario == 'ADMIN' or self.user.is_superuser
    
    def es_tecnico(self):
        return self.tipo_usuario == 'TECNICO'
    
    def es_cliente(self):
        return self.tipo_usuario == 'CLIENTE'
    
    def es_proveedor(self):
        return self.tipo_usuario == 'PROVEEDOR'
    
    def puede_ver_orden(self, orden):
        """Verifica si el usuario puede ver una orden específica"""
        if self.es_admin():
            return True
        if self.es_tecnico():
            return orden.tecnico_asignado == self.tecnico
        if self.es_cliente():
            return orden.cliente == self.cliente
        return False
    
    def puede_editar_orden(self, orden):
        """Verifica si el usuario puede editar una orden"""
        if self.es_admin():
            return True
        if self.es_tecnico():
            return orden.tecnico_asignado == self.tecnico
        return False
```

#### B. Modelo de Notificación

```python
# usuarios/models.py

class Notificacion(models.Model):
    """
    Sistema de notificaciones para usuarios
    """
    PRIORIDAD_CHOICES = [
        ('CRITICA', 'Crítica'),
        ('ALTA', 'Alta'),
        ('MEDIA', 'Media'),
        ('BAJA', 'Baja'),
    ]
    
    TIPO_CHOICES = [
        ('ORDEN_ASIGNADA', 'Orden Asignada'),
        ('ORDEN_ACTUALIZADA', 'Orden Actualizada'),
        ('ORDEN_COMPLETADA', 'Orden Completada'),
        ('GARANTIA_SOLICITUD', 'Solicitud de Garantía'),
        ('GARANTIA_APROBADA', 'Garantía Aprobada'),
        ('GARANTIA_RECHAZADA', 'Garantía Rechazada'),
        ('PEDIDO_NUEVO', 'Nuevo Pedido'),
        ('PEDIDO_DESPACHADO', 'Pedido Despachado'),
        ('PAGO_RECIBIDO', 'Pago Recibido'),
        ('STOCK_CRITICO', 'Stock Crítico'),
        ('SISTEMA', 'Notificación del Sistema'),
    ]
    
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notificaciones'
    )
    
    tipo = models.CharField(max_length=30, choices=TIPO_CHOICES)
    prioridad = models.CharField(
        max_length=10,
        choices=PRIORIDAD_CHOICES,
        default='MEDIA'
    )
    
    titulo = models.CharField(max_length=200)
    mensaje = models.TextField()
    
    # Enlaces relacionados
    url = models.CharField(max_length=500, blank=True)
    
    # IDs de entidades relacionadas (para referencia)
    orden_id = models.IntegerField(null=True, blank=True)
    venta_id = models.IntegerField(null=True, blank=True)
    garantia_id = models.IntegerField(null=True, blank=True)
    
    # Estado
    leida = models.BooleanField(default=False)
    fecha_leida = models.DateTimeField(null=True, blank=True)
    
    # Canal de envío
    enviada_email = models.BooleanField(default=False)
    enviada_sms = models.BooleanField(default=False)
    enviada_push = models.BooleanField(default=False)
    
    # Metadata
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Notificación"
        verbose_name_plural = "Notificaciones"
        ordering = ['-fecha_creacion']
    
    def __str__(self):
        return f"{self.usuario.username} - {self.titulo}"
    
    def marcar_leida(self):
        """Marca la notificación como leída"""
        if not self.leida:
            self.leida = True
            self.fecha_leida = timezone.now()
            self.save()
    
    def get_prioridad_color(self):
        """Retorna el color según la prioridad"""
        colores = {
            'CRITICA': 'danger',
            'ALTA': 'warning',
            'MEDIA': 'info',
            'BAJA': 'secondary',
        }
        return colores.get(self.prioridad, 'secondary')
    
    def get_prioridad_icono(self):
        """Retorna el icono según la prioridad"""
        iconos = {
            'CRITICA': '🔴',
            'ALTA': '⚠️',
            'MEDIA': '📢',
            'BAJA': '📌',
        }
        return iconos.get(self.prioridad, '📌')
```

### 6.2. Sistema de Decoradores

#### A. Decoradores de Permisos

```python
# usuarios/decorators.py

from functools import wraps
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied


def admin_required(view_func):
    """
    Decorador que requiere que el usuario sea administrador
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, 'Debes iniciar sesión.')
            return redirect('usuarios:login')
        
        if not (request.user.is_superuser or 
                (hasattr(request.user, 'perfil') and 
                 request.user.perfil.tipo_usuario == 'ADMIN')):
            messages.error(request, 'Solo administradores pueden acceder.')
            return redirect('dashboard:index')
        
        return view_func(request, *args, **kwargs)
    return wrapper


def tecnico_required(view_func):
    """
    Decorador que requiere que el usuario sea técnico
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, 'Debes iniciar sesión.')
            return redirect('usuarios:login')
        
        if not (hasattr(request.user, 'perfil') and 
                request.user.perfil.tipo_usuario == 'TECNICO'):
            messages.error(request, 'Solo técnicos pueden acceder.')
            return redirect('dashboard:index')
        
        return view_func(request, *args, **kwargs)
    return wrapper


def cliente_required(view_func):
    """
    Decorador que requiere que el usuario sea cliente
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, 'Debes iniciar sesión.')
            return redirect('usuarios:login')
        
        if not (hasattr(request.user, 'perfil') and 
                request.user.perfil.tipo_usuario == 'CLIENTE'):
            messages.error(request, 'Solo clientes pueden acceder.')
            return redirect('dashboard:index')
        
        return view_func(request, *args, **kwargs)
    return wrapper


def proveedor_required(view_func):
    """
    Decorador que requiere que el usuario sea proveedor
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, 'Debes iniciar sesión.')
            return redirect('usuarios:login')
        
        if not (hasattr(request.user, 'perfil') and 
                request.user.perfil.tipo_usuario == 'PROVEEDOR'):
            messages.error(request, 'Solo proveedores pueden acceder.')
            return redirect('dashboard:index')
        
        return view_func(request, *args, **kwargs)
    return wrapper


def roles_required(*roles):
    """
    Decorador que permite múltiples roles
    Uso: @roles_required('ADMIN', 'TECNICO')
    """
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                messages.warning(request, 'Debes iniciar sesión.')
                return redirect('usuarios:login')
            
            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)
            
            if not hasattr(request.user, 'perfil'):
                messages.error(request, 'Tu usuario no tiene perfil asignado.')
                return redirect('dashboard:index')
            
            if request.user.perfil.tipo_usuario not in roles:
                messages.error(request, 'No tienes permisos para acceder.')
                return redirect('dashboard:index')
            
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator


def puede_ver_orden(view_func):
    """
    Decorador que verifica si el usuario puede ver una orden específica
    La vista debe recibir orden_id como parámetro
    """
    @wraps(view_func)
    def wrapper(request, orden_id, *args, **kwargs):
        from ordenes.models import OrdenServicio
        
        if not request.user.is_authenticated:
            messages.warning(request, 'Debes iniciar sesión.')
            return redirect('usuarios:login')
        
        try:
            orden = OrdenServicio.objects.get(id=orden_id)
        except OrdenServicio.DoesNotExist:
            messages.error(request, 'Orden no encontrada.')
            return redirect('ordenes:lista')
        
        # Verificar permisos
        if request.user.is_superuser:
            return view_func(request, orden_id, *args, **kwargs)
        
        if hasattr(request.user, 'perfil'):
            if request.user.perfil.puede_ver_orden(orden):
                return view_func(request, orden_id, *args, **kwargs)
        
        messages.error(request, 'No tienes permisos para ver esta orden.')
        return redirect('ordenes:lista')
    
    return wrapper
```

### 6.3. Sistema de Notificaciones

#### A. Servicio de Notificaciones

```python
# usuarios/services.py

from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from .models import Notificacion
import logging

logger = logging.getLogger(__name__)


class NotificacionService:
    """
    Servicio centralizado para gestionar notificaciones
    """
    
    @staticmethod
    def crear_notificacion(usuario, tipo, titulo, mensaje, prioridad='MEDIA',
                          url='', orden_id=None, venta_id=None, garantia_id=None):
        """
        Crea una nueva notificación para un usuario
        """
        try:
            notificacion = Notificacion.objects.create(
                usuario=usuario,
                tipo=tipo,
                titulo=titulo,
                mensaje=mensaje,
                prioridad=prioridad,
                url=url,
                orden_id=orden_id,
                venta_id=venta_id,
                garantia_id=garantia_id
            )
            
            # Enviar por canales configurados
            NotificacionService._enviar_por_canales(notificacion)
            
            return notificacion
        
        except Exception as e:
            logger.error(f"Error al crear notificación: {str(e)}")
            return None
    
    @staticmethod
    def _enviar_por_canales(notificacion):
        """
        Envía la notificación por los canales configurados
        """
        perfil = notificacion.usuario.perfil
        
        # Email
        if perfil.notificaciones_email:
            NotificacionService._enviar_email(notificacion)
        
        # SMS (si está habilitado y configurado)
        if perfil.notificaciones_sms:
            NotificacionService._enviar_sms(notificacion)
        
        # Push (si está habilitado)
        if perfil.notificaciones_push:
            NotificacionService._enviar_push(notificacion)
    
    @staticmethod
    def _enviar_email(notificacion):
        """
        Envía notificación por email
        """
        try:
            send_mail(
                subject=notificacion.titulo,
                message=notificacion.mensaje,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[notificacion.usuario.email],
                fail_silently=True
            )
            notificacion.enviada_email = True
            notificacion.save()
        except Exception as e:
            logger.error(f"Error al enviar email: {str(e)}")
    
    @staticmethod
    def _enviar_sms(notificacion):
        """
        Envía notificación por SMS (placeholder)
        """
        # Implementar integración con servicio SMS
        pass
    
    @staticmethod
    def _enviar_push(notificacion):
        """
        Envía notificación push (placeholder)
        """
        # Implementar integración con servicio push
        pass
    
    @staticmethod
    def notificar_orden_asignada(orden):
        """
        Notifica al técnico cuando se le asigna una orden
        """
        if not orden.tecnico_asignado:
            return
        
        usuario = orden.tecnico_asignado.usuario_perfil.first().user
        
        prioridad = 'ALTA' if orden.prioridad == 'URGENTE' else 'MEDIA'
        
        NotificacionService.crear_notificacion(
            usuario=usuario,
            tipo='ORDEN_ASIGNADA',
            titulo=f'Nueva orden asignada: #{orden.numero_orden}',
            mensaje=f'Se te ha asignado una orden de servicio para {orden.cliente.nombre_completo}. '
                   f'Equipo: {orden.tipo_equipo} {orden.marca}. '
                   f'Prioridad: {orden.get_prioridad_display()}.',
            prioridad=prioridad,
            url=f'/ordenes/{orden.id}/',
            orden_id=orden.id
        )
    
    @staticmethod
    def notificar_orden_completada(orden):
        """
        Notifica al administrador cuando un técnico completa una orden
        """
        admins = User.objects.filter(
            perfil__tipo_usuario='ADMIN'
        ) | User.objects.filter(is_superuser=True)
        
        for admin in admins:
            NotificacionService.crear_notificacion(
                usuario=admin,
                tipo='ORDEN_COMPLETADA',
                titulo=f'Orden completada: #{orden.numero_orden}',
                mensaje=f'El técnico {orden.tecnico_asignado.nombre_completo} ha completado '
                       f'la orden de servicio #{orden.numero_orden}. Requiere facturación.',
                prioridad='ALTA',
                url=f'/ordenes/{orden.id}/',
                orden_id=orden.id
            )
    
    @staticmethod
    def notificar_garantia_solicitud(garantia):
        """
        Notifica al administrador sobre nueva solicitud de garantía
        """
        admins = User.objects.filter(
            perfil__tipo_usuario='ADMIN'
        ) | User.objects.filter(is_superuser=True)
        
        for admin in admins:
            NotificacionService.crear_notificacion(
                usuario=admin,
                tipo='GARANTIA_SOLICITUD',
                titulo=f'Nueva solicitud de garantía',
                mensaje=f'El cliente {garantia.cliente.nombre_completo} ha solicitado una garantía '
                       f'para {garantia.producto.nombre}.',
                prioridad='ALTA',
                url=f'/garantias/{garantia.id}/',
                garantia_id=garantia.id
            )
    
    @staticmethod
    def notificar_pedido_nuevo(pedido, proveedor):
        """
        Notifica al proveedor sobre un nuevo pedido
        """
        usuario = proveedor.usuario_perfil.first().user
        
        NotificacionService.crear_notificacion(
            usuario=usuario,
            tipo='PEDIDO_NUEVO',
            titulo=f'Nuevo pedido: #{pedido.numero_venta}',
            mensaje=f'Has recibido un nuevo pedido de {pedido.cliente.nombre_completo}. '
                   f'Total: ${pedido.total_venta:,.0f}',
            prioridad='ALTA',
            url=f'/ventas/{pedido.id}/',
            venta_id=pedido.id
        )
```

---

## 7. CASOS DE USO DETALLADOS

### 7.1. Caso de Uso: Administrador Asigna Técnico

**Actor Principal:** Administrador

**Precondiciones:**
- Administrador ha iniciado sesión
- Existe una orden de servicio registrada
- Existen técnicos disponibles en el sistema

**Flujo Principal:**

1. Admin accede al módulo de Órdenes de Servicio
2. Sistema muestra lista de órdenes con filtros
3. Admin selecciona orden sin técnico asignado
4. Sistema muestra detalles de la orden
5. Admin hace clic en "Asignar Técnico"
6. Sistema muestra lista de técnicos disponibles con:
   - Nombre del técnico
   - Especialidad
   - Órdenes activas actuales
   - Disponibilidad
   - Calificación promedio
7. Admin filtra por especialidad (si necesario)
8. Admin selecciona técnico apropiado
9. Admin define prioridad de la orden
10. Admin establece fecha de compromiso
11. Admin hace clic en "Asignar"
12. Sistema valida la asignación
13. Sistema actualiza la orden:
    - Asigna técnico
    - Cambia estado a "ASIGNADA"
    - Registra fecha de asignación
14. Sistema envía notificación al técnico
15. Sistema envía notificación al cliente
16. Sistema muestra mensaje de confirmación
17. Admin puede ver la orden actualizada

**Flujos Alternativos:**

**7a. Técnico no disponible:**
- En paso 8, Admin selecciona técnico ocupado
- Sistema muestra advertencia: "Técnico tiene X órdenes activas"
- Admin puede continuar o seleccionar otro

**12a. Error en validación:**
- Sistema detecta problema (ej: técnico sin perfil activo)
- Sistema muestra error específico
- Admin corrige y reintenta

**Postcondiciones:**
- Orden asignada correctamente
- Técnico notificado
- Cliente informado
- Registro en auditoría

---

### 7.2. Caso de Uso: Técnico Actualiza Estado de Orden

**Actor Principal:** Técnico

**Precondiciones:**
- Técnico ha iniciado sesión
- Técnico tiene órdenes asignadas

**Flujo Principal:**

1. Técnico accede a "Mis Órdenes"
2. Sistema muestra órdenes asignadas ordenadas por prioridad
3. Técnico selecciona orden a actualizar
4. Sistema muestra detalles completos:
   - Datos del cliente
   - Información del equipo
   - Historial de cambios
   - Diagnóstico actual
5. Técnico hace clic en "Actualizar Estado"
6. Sistema muestra formulario con:
   - Estado actual (readonly)
   - Nuevo estado (dropdown)
   - Campo de observaciones
   - Tiempo estimado de resolución
   - Necesita repuestos (checkbox)
7. Técnico selecciona nuevo estado
8. Técnico ingresa observaciones detalladas
9. Si cambió a "DIAGNOSTICADA":
   - Técnico ingresa diagnóstico completo
   - Técnico calcula costo estimado
   - Técnico define tiempo de reparación
10. Si necesita repuestos:
    - Técnico lista repuestos requeridos
    - Sistema cambia estado a "EN_ESPERA_REPUESTOS"
11. Técnico hace clic en "Guardar Cambios"
12. Sistema valida la información
13. Sistema actualiza la orden:
    - Cambia estado
    - Registra observaciones
    - Actualiza timestamp
    - Crea registro en seguimiento
14. Sistema envía notificación al administrador
15. Si orden completada:
    - Sistema notifica que requiere facturación
16. Sistema muestra confirmación
17. Técnico ve orden actualizada

**Flujos Alternativos:**

**9a. Cliente debe aprobar presupuesto:**
- Estado cambia a "DIAGNOSTICADA"
- Sistema marca como "Esperando aprobación"
- Admin recibe notificación para contactar cliente

**13a. Orden completada:**
- Estado cambia a "REPARADA"
- Sistema solicita confirmar calidad
- Técnico verifica lista de chequeo
- Sistema notifica a admin con alta prioridad

**Postcondiciones:**
- Orden actualizada
- Historial registrado
- Notificaciones enviadas
- Métricas actualizadas

---

### 7.3. Caso de Uso: Cliente Solicita Garantía

**Actor Principal:** Cliente

**Precondiciones:**
- Cliente ha iniciado sesión
- Cliente tiene productos comprados
- Producto está dentro del periodo de garantía

**Flujo Principal:**

1. Cliente accede a "Mis Compras"
2. Sistema muestra historial de compras
3. Cliente selecciona producto con problema
4. Sistema muestra detalles de la compra:
   - Producto
   - Fecha de compra
   - Factura
   - Estado de garantía
5. Cliente hace clic en "Solicitar Garantía"
6. Sistema muestra formulario:
   - Producto (readonly)
   - Factura (readonly)
   - Descripción del problema (textarea)
   - Tipo de problema (dropdown)
   - Adjuntar evidencias (file upload)
7. Cliente describe el problema detalladamente
8. Cliente selecciona tipo de problema:
   - Defecto de fábrica
   - No funciona como esperado
   - Daño en transporte
   - Otro
9. Cliente adjunta fotos o videos del problema
10. Cliente hace clic en "Enviar Solicitud"
11. Sistema valida:
    - Garantía vigente
    - Factura válida
    - Campos requeridos completos
12. Sistema crea solicitud de garantía:
    - Genera número de caso
    - Estado: "PENDIENTE_EVALUACION"
    - Registra evidencias
13. Sistema envía notificación al administrador
14. Sistema envía confirmación al cliente con:
    - Número de caso
    - Pasos siguientes
    - Tiempo estimado de respuesta
15. Cliente ve solicitud en "Mis Garantías"

**Flujos Alternativos:**

**11a. Garantía vencida:**
- Sistema detecta que garantía expiró
- Sistema muestra mensaje explicativo
- Sistema ofrece servicio técnico con costo
- Cliente puede aceptar o cancelar

**11b. Sin evidencias adjuntas:**
- Sistema advierte sobre falta de evidencias
- Cliente puede continuar o adjuntar
- Si continúa, evaluación puede demorar más

**Postcondiciones:**
- Solicitud de garantía registrada
- Admin notificado
- Cliente informado
- Caso con número de seguimiento

---

*Documento completo*

**Archivos creados:**
1. ESPECIFICACION_FUNCIONAL_ROLES_Y_PERMISOS.md (Parte 1)
2. ESPECIFICACION_FUNCIONAL_NOTIFICACIONES_Y_MODULOS.md (Parte 2)
3. ESPECIFICACION_FUNCIONAL_IMPLEMENTACION_Y_CASOS_USO.md (Parte 3)

