"""
Sistema de Reacciones para Productos
"""
from django.db import models
from django.conf import settings
from productos.models import Producto


class ReaccionProducto(models.Model):
    """Reacciones (me gusta/no me gusta) de usuarios a productos"""
    
    TIPO_REACCION = [
        ('like', 'Me gusta'),
        ('dislike', 'No me gusta'),
    ]
    
    producto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE,
        related_name='reacciones',
        verbose_name="Producto"
    )
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Usuario"
    )
    session_id = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="ID de sesión"
    )
    tipo = models.CharField(
        max_length=10,
        choices=TIPO_REACCION,
        verbose_name="Tipo de reacción"
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    
    class Meta:
        verbose_name = "Reacción de Producto"
        verbose_name_plural = "Reacciones de Productos"
        unique_together = [['producto', 'usuario'], ['producto', 'session_id']]
        ordering = ['-fecha_creacion']
    
    def __str__(self):
        return f"{self.get_tipo_display()} - {self.producto.nombre_producto}"
    
    @classmethod
    def obtener_contadores(cls, producto_id):
        """Obtiene el conteo de likes y dislikes de un producto"""
        reacciones = cls.objects.filter(producto_id=producto_id)
        likes = reacciones.filter(tipo='like').count()
        dislikes = reacciones.filter(tipo='dislike').count()
        return {'likes': likes, 'dislikes': dislikes, 'total': likes + dislikes}

