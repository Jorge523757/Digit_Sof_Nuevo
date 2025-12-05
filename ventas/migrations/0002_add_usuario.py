# Generated manually for adding user fields

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ventas', '0001_initial'),  # Ajusta según tu última migración
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='usuario',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name='ventas_realizadas',
                to=settings.AUTH_USER_MODEL,
                verbose_name='Usuario'
            ),
        ),
    ]

