# Generated manually for Pedido models

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),  # Ajustar según la última migración
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pedido', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('procesando', 'Procesando'), ('completado', 'Completado'), ('cancelado', 'Cancelado'), ('facturado', 'Facturado')], default='pendiente', max_length=20)),
                ('total', models.DecimalField(decimal_places=2, max_digits=12)),
                ('notas_cliente', models.TextField(blank=True, help_text='Notas adicionales del cliente', null=True)),
                ('procesado_por', models.CharField(blank=True, help_text='Administrador que procesa el pedido', max_length=100, null=True)),
                ('fecha_procesamiento', models.DateTimeField(blank=True, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ventas.cliente')),
            ],
            options={
                'ordering': ['-fecha_pedido'],
            },
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=12)),
                ('subtotal', models.DecimalField(decimal_places=2, editable=False, max_digits=12)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='ventas.pedido')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ventas.producto')),
            ],
        ),
    ]