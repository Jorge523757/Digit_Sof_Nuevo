from django.db import models

class Administrador(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    contraseña = models.CharField(max_length=42, blank=True, null=True)
    correo_electronico = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre
