"""
DIGT SOFT - Modelo de Token de Recuperación de Contraseña
"""

from django.db import models
from django.contrib.auth.models import User
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

