"""
DIGT SOFT - Sistema de Notificaciones Multicanal
Gestión automatizada de comunicaciones con técnicos y clientes
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class CanalNotificacion(models.Model):
    """Canales de comunicación disponibles"""
    TIPO_CHOICES = [
        ('EMAIL', 'Correo Electrónico'),
        ('SMS', 'Mensaje de Texto'),
        ('WHATSAPP', 'WhatsApp'),
        ('PUSH', 'Notificación Push'),
        ('TELEFONO', 'Llamada Telefónica'),
    ]

    nombre = models.CharField(max_length=50, choices=TIPO_CHOICES, unique=True)
    activo = models.BooleanField(default=True)
    prioridad = models.IntegerField(default=1)  # 1 = más alta

    class Meta:
        verbose_name = "Canal de Notificación"
        verbose_name_plural = "Canales de Notificación"
        ordering = ['prioridad']

    def __str__(self):
        return self.get_nombre_display()


class ConfiguracionNotificacion(models.Model):
    """Configuración de notificaciones por tipo de usuario"""
    TIPO_USUARIO_CHOICES = [
        ('TECNICO', 'Técnico'),
        ('CLIENTE', 'Cliente'),
        ('ADMINISTRADOR', 'Administrador'),
    ]

    EVENTO_CHOICES = [
        ('ORDEN_CREADA', 'Orden Creada'),
        ('ORDEN_ASIGNADA', 'Orden Asignada a Técnico'),
        ('INICIO_DIAGNOSTICO', 'Inicio de Diagnóstico'),
        ('DIAGNOSTICO_COMPLETADO', 'Diagnóstico Completado'),
        ('INICIO_REPARACION', 'Inicio de Reparación'),
        ('REPARACION_COMPLETADA', 'Reparación Completada'),
        ('DEMORA_REPORTADA', 'Demora Reportada'),
        ('LISTA_ENTREGA', 'Lista para Entrega'),
        ('EQUIPO_ENTREGADO', 'Equipo Entregado'),
        ('ALERTA_FECHA_VENCIMIENTO', 'Alerta de Fecha Próxima a Vencer'),
    ]

    tipo_usuario = models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES)
    evento = models.CharField(max_length=50, choices=EVENTO_CHOICES)
    canales = models.ManyToManyField(CanalNotificacion)
    activo = models.BooleanField(default=True)
    template_mensaje = models.TextField(help_text="Usar {variables} para personalizar")

    class Meta:
        verbose_name = "Configuración de Notificación"
        verbose_name_plural = "Configuraciones de Notificaciones"
        unique_together = ['tipo_usuario', 'evento']

    def __str__(self):
        return f"{self.get_tipo_usuario_display()} - {self.get_evento_display()}"


class EstadoTecnico(models.Model):
    """Estado de disponibilidad del técnico"""
    ESTADO_CHOICES = [
        ('DISPONIBLE', 'Disponible'),
        ('OCUPADO', 'Ocupado'),
        ('EN_SERVICIO', 'En Servicio Externo'),
        ('NO_DISPONIBLE', 'No Disponible'),
        ('VACACIONES', 'De Vacaciones'),
    ]

    from tecnicos.models import Tecnico

    tecnico = models.OneToOneField(Tecnico, on_delete=models.CASCADE, related_name='estado_actual')
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='DISPONIBLE')
    ordenes_activas = models.IntegerField(default=0)
    capacidad_maxima = models.IntegerField(default=5, help_text="Máximo de órdenes simultáneas")
    notas = models.TextField(blank=True, help_text="Razón del estado actual")
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    disponible_desde = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Estado de Técnico"
        verbose_name_plural = "Estados de Técnicos"

    def __str__(self):
        return f"{self.tecnico.nombre_completo} - {self.get_estado_display()}"

    @property
    def puede_recibir_ordenes(self):
        """Verifica si el técnico puede recibir más órdenes"""
        return (
            self.estado == 'DISPONIBLE' and
            self.ordenes_activas < self.capacidad_maxima
        )

    @property
    def porcentaje_capacidad(self):
        """Calcula el porcentaje de capacidad utilizada"""
        if self.capacidad_maxima == 0:
            return 0
        return int((self.ordenes_activas / self.capacidad_maxima) * 100)


class AlertaTecnico(models.Model):
    """Alertas y reportes del técnico sobre órdenes"""
    TIPO_ALERTA_CHOICES = [
        ('DEMORA', 'Demora en Reparación'),
        ('REPUESTO_FALTANTE', 'Repuesto Faltante'),
        ('PROBLEMA_ADICIONAL', 'Problema Adicional Encontrado'),
        ('EQUIPO_NO_REPARABLE', 'Equipo No Reparable'),
        ('REQUIERE_AUTORIZACION', 'Requiere Autorización Cliente'),
        ('CAMBIO_FECHA', 'Cambio de Fecha Estimada'),
        ('DISPONIBILIDAD', 'Cambio de Disponibilidad'),
    ]

    from ordenes.models import OrdenServicio
    from tecnicos.models import Tecnico

    orden = models.ForeignKey(OrdenServicio, on_delete=models.CASCADE, related_name='alertas', null=True, blank=True)
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE, related_name='alertas')
    tipo_alerta = models.CharField(max_length=30, choices=TIPO_ALERTA_CHOICES)
    descripcion = models.TextField()
    nueva_fecha_estimada = models.DateTimeField(null=True, blank=True)
    dias_demora = models.IntegerField(null=True, blank=True)
    requiere_atencion = models.BooleanField(default=True)
    atendida = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_atencion = models.DateTimeField(null=True, blank=True)
    atendida_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Alerta de Técnico"
        verbose_name_plural = "Alertas de Técnicos"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f"{self.get_tipo_alerta_display()} - {self.tecnico.nombre_completo}"


class HistorialNotificacion(models.Model):
    """Registro de todas las notificaciones enviadas"""
    ESTADO_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('ENVIADA', 'Enviada'),
        ('ENTREGADA', 'Entregada'),
        ('LEIDA', 'Leída'),
        ('ERROR', 'Error'),
    ]

    from ordenes.models import OrdenServicio

    orden = models.ForeignKey(OrdenServicio, on_delete=models.CASCADE, related_name='notificaciones', null=True, blank=True)
    destinatario_tipo = models.CharField(max_length=20)  # TECNICO, CLIENTE, ADMIN
    destinatario_id = models.IntegerField()
    destinatario_nombre = models.CharField(max_length=200)
    canal = models.ForeignKey(CanalNotificacion, on_delete=models.PROTECT)
    evento = models.CharField(max_length=50)
    asunto = models.CharField(max_length=200)
    mensaje = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='PENDIENTE')
    fecha_programada = models.DateTimeField(default=timezone.now)
    fecha_envio = models.DateTimeField(null=True, blank=True)
    fecha_entrega = models.DateTimeField(null=True, blank=True)
    fecha_lectura = models.DateTimeField(null=True, blank=True)
    error_mensaje = models.TextField(blank=True)
    intentos = models.IntegerField(default=0)
    metadatos = models.JSONField(default=dict, blank=True)

    class Meta:
        verbose_name = "Historial de Notificación"
        verbose_name_plural = "Historial de Notificaciones"
        ordering = ['-fecha_programada']
        indexes = [
            models.Index(fields=['estado', 'fecha_programada']),
            models.Index(fields=['orden', 'destinatario_tipo']),
        ]

    def __str__(self):
        return f"{self.canal.nombre} - {self.destinatario_nombre} - {self.get_estado_display()}"


class MonitoreoOrden(models.Model):
    """Monitoreo automático de fechas y estados de órdenes"""
    from ordenes.models import OrdenServicio

    orden = models.OneToOneField(OrdenServicio, on_delete=models.CASCADE, related_name='monitoreo')
    fecha_inicio_monitoreo = models.DateTimeField(auto_now_add=True)
    alerta_3_dias = models.BooleanField(default=False, help_text="Alerta 3 días antes del vencimiento")
    alerta_1_dia = models.BooleanField(default=False, help_text="Alerta 1 día antes del vencimiento")
    alerta_vencida = models.BooleanField(default=False, help_text="Alerta cuando se vence")
    ultima_actualizacion_cliente = models.DateTimeField(null=True, blank=True)
    notificaciones_enviadas = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Monitoreo de Orden"
        verbose_name_plural = "Monitoreo de Órdenes"

    def __str__(self):
        return f"Monitoreo - {self.orden.numero_orden}"

    @property
    def dias_hasta_vencimiento(self):
        """Calcula días hasta la fecha de compromiso"""
        if not self.orden.fecha_compromiso:
            return None
        diferencia = self.orden.fecha_compromiso - timezone.now()
        return diferencia.days

    @property
    def requiere_alerta(self):
        """Verifica si requiere enviar alerta"""
        dias = self.dias_hasta_vencimiento
        if dias is None:
            return False

        if dias <= 1 and not self.alerta_1_dia:
            return True
        if dias <= 3 and not self.alerta_3_dias:
            return True
        if dias < 0 and not self.alerta_vencida:
            return True

        return False


class NotificacionEmail(models.Model):
    """Notificaciones por correo electrónico"""
    TIPO_NOTIFICACION_CHOICES = [
        ('REPORTE_CLIENTE', 'Envío de reporte de cliente'),
        ('ASIGNACION_TECNICO', 'Envío de equipo'),
        ('ORDEN_SERVICIO_CLIENTE', 'Orden de Servicio'),
        ('DIAGNOSTICO_COMPLETADO', 'Diagnóstico Completado'),
        ('EQUIPO_LISTO', 'Equipo Listo para Entrega'),
    ]

    ESTADO_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('ENVIADO', 'Enviado'),
        ('ERROR', 'Error'),
    ]

    destinatario = models.EmailField(verbose_name="Correo destinatario")
    asunto = models.CharField(max_length=200, verbose_name="Asunto")
    contenido_texto = models.TextField(verbose_name="Contenido texto plano")
    contenido_html = models.TextField(blank=True, verbose_name="Contenido HTML")
    tipo_notificacion = models.CharField(
        max_length=30,
        choices=TIPO_NOTIFICACION_CHOICES,
        verbose_name="Tipo"
    )
    orden_servicio = models.ForeignKey(
        'ordenes.OrdenServicio',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='emails_enviados',
        verbose_name="Orden de servicio"
    )
    enviado = models.BooleanField(default=False, verbose_name="Enviado")
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='PENDIENTE',
        verbose_name="Estado"
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    fecha_envio = models.DateTimeField(null=True, blank=True, verbose_name="Fecha de envío")
    error_mensaje = models.TextField(blank=True, verbose_name="Mensaje de error")

    class Meta:
        verbose_name = "Notificación por Email"
        verbose_name_plural = "Notificaciones por Email"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f"{self.get_tipo_notificacion_display()} - {self.destinatario}"


class NotificacionWeb(models.Model):
    """Notificaciones en la plataforma web"""
    TIPO_CHOICES = [
        ('INFO', 'Información'),
        ('SUCCESS', 'Éxito'),
        ('WARNING', 'Advertencia'),
        ('DANGER', 'Peligro'),
        ('PRIMARY', 'Primario'),
    ]

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notificaciones_web',
        verbose_name="Usuario"
    )
    titulo = models.CharField(max_length=200, verbose_name="Título")
    mensaje = models.TextField(verbose_name="Mensaje")
    tipo = models.CharField(
        max_length=10,
        choices=TIPO_CHOICES,
        default='INFO',
        verbose_name="Tipo"
    )
    icono = models.CharField(
        max_length=50,
        default='fa-bell',
        verbose_name="Icono",
        help_text="Clase de Font Awesome"
    )
    url = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="URL de acción",
        help_text="URL a la que redirigir al hacer clic"
    )
    orden_servicio = models.ForeignKey(
        'ordenes.OrdenServicio',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='notificaciones_web',
        verbose_name="Orden de servicio"
    )
    leida = models.BooleanField(default=False, verbose_name="Leída")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    fecha_lectura = models.DateTimeField(null=True, blank=True, verbose_name="Fecha de lectura")

    class Meta:
        verbose_name = "Notificación Web"
        verbose_name_plural = "Notificaciones Web"
        ordering = ['-fecha_creacion']
        indexes = [
            models.Index(fields=['usuario', 'leida']),
            models.Index(fields=['fecha_creacion']),
        ]

    def __str__(self):
        return f"{self.titulo} - {self.usuario.username}"

    def marcar_leida(self):
        """Marca la notificación como leída"""
        if not self.leida:
            self.leida = True
            self.fecha_lectura = timezone.now()
            self.save()
