"""
DIGITSOFT - Módulo de Usuarios
Models - Perfil de Usuario Extendido y Notificaciones
"""

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class PerfilUsuario(models.Model):
    """
    Perfil extendido de usuario con información adicional
    y gestión de acceso al sistema
    """

    TIPO_USUARIO_CHOICES = [
        ('ADMIN', 'Administrador'),
        ('CLIENTE', 'Cliente'),
        ('TECNICO', 'Técnico'),
        ('PROVEEDOR', 'Proveedor'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    tipo_usuario = models.CharField(
        max_length=10,
        choices=TIPO_USUARIO_CHOICES,
        default='CLIENTE',
        verbose_name="Tipo de Usuario"
    )

    # Información adicional
    telefono = models.CharField(max_length=15, blank=True, verbose_name="Teléfono")
    direccion = models.TextField(blank=True, verbose_name="Dirección")
    documento = models.CharField(max_length=20, blank=True, verbose_name="Documento")
    foto = models.ImageField(upload_to='usuarios/', blank=True, null=True, verbose_name="Foto de Perfil")

    # Control de acceso
    activo = models.BooleanField(default=True, verbose_name="Usuario Activo")
    bloqueado = models.BooleanField(default=False, verbose_name="Usuario Bloqueado")
    motivo_bloqueo = models.TextField(blank=True, verbose_name="Motivo del Bloqueo")
    fecha_bloqueo = models.DateTimeField(blank=True, null=True, verbose_name="Fecha de Bloqueo")

    # Relación con modelos específicos
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

    # Metadatos
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Última Actualización")

    class Meta:
        verbose_name = "Perfil de Usuario"
        verbose_name_plural = "Perfiles de Usuarios"
        ordering = ['-fecha_registro']
        db_table = 'usuarios_perfil'

    def __str__(self):
        return f"{self.user.username} - {self.get_tipo_usuario_display()}"

    def bloquear(self, motivo=""):
        """Bloquea el acceso del usuario al sistema"""
        self.bloqueado = True
        self.motivo_bloqueo = motivo
        self.user.is_active = False
        from django.utils import timezone
        self.fecha_bloqueo = timezone.now()
        self.save()
        self.user.save()

    def desbloquear(self):
        """Desbloquea el acceso del usuario al sistema"""
        self.bloqueado = False
        self.motivo_bloqueo = ""
        self.fecha_bloqueo = None
        self.user.is_active = True
        self.save()
        self.user.save()

    @property
    def nombre_completo(self):
        return f"{self.user.first_name} {self.user.last_name}".strip() or self.user.username


@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    """Crea automáticamente un perfil cuando se crea un usuario"""
    if created:
        PerfilUsuario.objects.create(user=instance)


@receiver(post_save, sender=User)
def guardar_perfil_usuario(sender, instance, **kwargs):
    """Guarda el perfil cuando se guarda el usuario"""
    if hasattr(instance, 'perfil'):
        instance.perfil.save()

# ==============================================
# MODELO DE NOTIFICACIONES
# ==============================================

class Notificacion(models.Model):
    """
    Modelo para gestionar notificaciones del sistema
    """

    TIPO_CHOICES = [
        ('INFO', 'Información'),
        ('WARNING', 'Advertencia'),
        ('SUCCESS', 'Éxito'),
        ('ERROR', 'Error'),
        ('VENTA', 'Venta'),
        ('ORDEN', 'Orden de Servicio'),
        ('COMPRA', 'Compra'),
        ('SISTEMA', 'Sistema'),
    ]

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notificaciones',
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

    # Control
    leida = models.BooleanField(default=False, verbose_name="Leída")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    fecha_lectura = models.DateTimeField(null=True, blank=True, verbose_name="Fecha de Lectura")

    # Enlace opcional
    url = models.CharField(max_length=500, blank=True, verbose_name="URL de referencia")

    # Información adicional
    icono = models.CharField(max_length=50, blank=True, verbose_name="Icono Font Awesome")
    color = models.CharField(max_length=20, blank=True, verbose_name="Color")

    class Meta:
        verbose_name = "Notificación"
        verbose_name_plural = "Notificaciones"
        ordering = ['-fecha_creacion']
        indexes = [
            models.Index(fields=['usuario', 'leida']),
            models.Index(fields=['-fecha_creacion']),
        ]

    def __str__(self):
        return f"{self.titulo} - {self.usuario.username}"

    def marcar_como_leida(self):
        """Marca la notificación como leída"""
        if not self.leida:
            self.leida = True
            self.fecha_lectura = timezone.now()
            self.save()

    @property
    def tiempo_transcurrido(self):
        """Retorna el tiempo transcurrido desde la creación"""
        from django.utils.timesince import timesince
        return timesince(self.fecha_creacion)

    def get_icono(self):
        """Retorna el icono según el tipo"""
        iconos = {
            'INFO': 'fa-info-circle',
            'WARNING': 'fa-exclamation-triangle',
            'SUCCESS': 'fa-check-circle',
            'ERROR': 'fa-times-circle',
            'VENTA': 'fa-shopping-cart',
            'ORDEN': 'fa-tools',
            'COMPRA': 'fa-box',
            'SISTEMA': 'fa-cog',
        }
        return self.icono or iconos.get(self.tipo, 'fa-bell')

    def get_color(self):
        """Retorna el color según el tipo"""
        colores = {
            'INFO': 'info',
            'WARNING': 'warning',
            'SUCCESS': 'success',
            'ERROR': 'danger',
            'VENTA': 'primary',
            'ORDEN': 'secondary',
            'COMPRA': 'dark',
            'SISTEMA': 'info',
        }
        return self.color or colores.get(self.tipo, 'info')



# ==============================================
# MODELO DE RECUPERACIÓN DE CONTRASEÑA
# ==============================================
from django.utils import timezone
import uuid
from datetime import timedelta


class PasswordResetToken(models.Model):
    """Token para recuperación de contraseña"""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='password_reset_tokens')
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    used = models.BooleanField(default=False)
    used_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Token de Recuperación"
        verbose_name_plural = "Tokens de Recuperación"
        ordering = ['-created_at']
        db_table = 'usuarios_password_reset_token'

    def __str__(self):
        return f"Token para {self.user.username} - {'Usado' if self.used else 'Activo'}"

    def is_valid(self):
        """Verifica si el token es válido (no usado y no expirado)"""
        if self.used:
            return False

        # Token válido por 24 horas
        expiry_time = self.created_at + timedelta(hours=24)
        return timezone.now() < expiry_time

    def mark_as_used(self):
        """Marca el token como usado"""
        self.used = True
        self.used_at = timezone.now()
        self.save()

    @classmethod
    def create_token(cls, user):
        """Crea un nuevo token para el usuario"""
        # Invalidar tokens anteriores no usados
        cls.objects.filter(user=user, used=False).update(used=True)

        # Crear nuevo token
        return cls.objects.create(user=user)


