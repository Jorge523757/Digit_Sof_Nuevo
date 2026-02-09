"""
Modelo para tokens de recuperación de contraseña
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import random
import string


class TokenRecuperacion(models.Model):
    """Token de recuperación de contraseña con código de 6 dígitos"""

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tokens_recuperacion')
    codigo = models.CharField(max_length=6, unique=True)
    email = models.EmailField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_expiracion = models.DateTimeField()
    usado = models.BooleanField(default=False)
    ip_solicitud = models.GenericIPAddressField(null=True, blank=True)

    class Meta:
        ordering = ['-fecha_creacion']
        verbose_name = 'Token de Recuperación'
        verbose_name_plural = 'Tokens de Recuperación'

    def __str__(self):
        return f'{self.usuario.username} - {self.codigo} - {"Usado" if self.usado else "Activo"}'

    @property
    def esta_expirado(self):
        """Verifica si el token ya expiró (30 minutos)"""
        return timezone.now() > self.fecha_expiracion

    @property
    def es_valido(self):
        """Verifica si el token es válido (no usado y no expirado)"""
        return not self.usado and not self.esta_expirado

    @staticmethod
    def generar_codigo():
        """Genera un código aleatorio de 6 dígitos"""
        return ''.join(random.choices(string.digits, k=6))

    @classmethod
    def crear_token(cls, usuario, email, ip=None):
        """Crea un nuevo token de recuperación"""
        # Invalidar tokens anteriores del mismo usuario
        cls.objects.filter(usuario=usuario, usado=False).update(usado=True)

        # Generar código único
        while True:
            codigo = cls.generar_codigo()
            if not cls.objects.filter(codigo=codigo, usado=False).exists():
                break

        # Crear token con expiración de 30 minutos
        token = cls.objects.create(
            usuario=usuario,
            codigo=codigo,
            email=email,
            fecha_expiracion=timezone.now() + timezone.timedelta(minutes=30),
            ip_solicitud=ip
        )

        return token

    def marcar_usado(self):
        """Marca el token como usado"""
        self.usado = True
        self.save()

