"""
DIGITSOFT - URLs del Módulo de Ventas
"""

from django.urls import path
from . import views
from productos.views import ver_factura

app_name = 'ventas'

urlpatterns = [
    # Lista y búsqueda
    path('', views.ventas_lista, name='lista'),
    path('reportes/', views.ventas_reportes, name='reportes'),

    # CRUD
    path('crear/', views.venta_crear, name='crear'),
    path('<int:pk>/', views.venta_detalle, name='detalle'),
    path('<int:venta_id>/factura/', ver_factura, name='ver_factura'),
    path('<int:pk>/editar/', views.venta_editar, name='editar'),

    # Acciones
    path('<int:pk>/cambiar-estado/', views.venta_cambiar_estado, name='cambiar_estado'),

    # Reportes
    path('reporte/pdf/', views.venta_reporte_pdf, name='reporte_pdf'),
    path('reporte/excel/', views.venta_reporte_excel, name='reporte_excel'),
]
"""
DIGT SOFT - Formularios del Módulo de Ventas
"""

from django import forms
from django.forms import inlineformset_factory
from .models import Venta, DetalleVenta


class VentaForm(forms.ModelForm):
    """Formulario para crear y editar ventas"""

    class Meta:
        model = Venta
        fields = [
            'cliente', 'estado', 'canal_venta', 'metodo_pago',
            'descuento', 'impuestos', 'requiere_entrega',
            'direccion_entrega', 'observaciones', 'vendedor'
        ]
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-select'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'canal_venta': forms.Select(attrs={'class': 'form-select'}),
            'metodo_pago': forms.Select(attrs={'class': 'form-select'}),
            'descuento': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0'
            }),
            'impuestos': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0'
            }),
            'requiere_entrega': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'direccion_entrega': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2
            }),
            'observaciones': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
            'vendedor': forms.TextInput(attrs={'class': 'form-control'}),
        }


class DetalleVentaForm(forms.ModelForm):
    """Formulario para items de venta"""

    class Meta:
        model = DetalleVenta
        fields = ['producto', 'cantidad', 'precio_unitario', 'descuento_item', 'con_garantia']
        widgets = {
            'producto': forms.Select(attrs={'class': 'form-select'}),
            'cantidad': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1'
            }),
            'precio_unitario': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0'
            }),
            'descuento_item': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0'
            }),
            'con_garantia': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


# FormSet para manejar múltiples productos en una venta
DetalleVentaFormSet = inlineformset_factory(
    Venta,
    DetalleVenta,
    form=DetalleVentaForm,
    extra=1,
    min_num=1,
    validate_min=True,
    can_delete=True
)


class BuscarVentaForm(forms.Form):
    """Formulario para buscar y filtrar ventas"""

    busqueda = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Buscar por número de venta o cliente...'
        })
    )

    estado = forms.ChoiceField(
        required=False,
        choices=[('', 'Todos los estados')] + Venta.ESTADO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    canal = forms.ChoiceField(
        required=False,
        choices=[('', 'Todos los canales')] + Venta.CANAL_VENTA_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    fecha_desde = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        })
    )

    fecha_hasta = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        })
    )

