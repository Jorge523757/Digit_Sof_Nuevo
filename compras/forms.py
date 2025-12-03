"""
DIGT SOFT - Formularios del Módulo de Compras
"""

from django import forms
from .models import Compra, DetalleCompra
from proveedores.models import Proveedor


class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = [
            'proveedor', 'fecha_entrega_esperada', 'estado', 'metodo_pago',
            'impuestos', 'descuento', 'observaciones', 'responsable'
        ]
        widgets = {
            'proveedor': forms.Select(attrs={'class': 'form-select'}),
            'fecha_entrega_esperada': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'metodo_pago': forms.Select(attrs={'class': 'form-select'}),
            'impuestos': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0'
            }),
            'descuento': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0'
            }),
            'observaciones': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
            'responsable': forms.TextInput(attrs={'class': 'form-control'}),
        }


class BuscarCompraForm(forms.Form):
    busqueda = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Buscar por número o proveedor...'
        })
    )

    estado = forms.ChoiceField(
        required=False,
        choices=[('', 'Todos los estados')] + Compra.ESTADO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    proveedor = forms.ModelChoiceField(
        queryset=Proveedor.objects.filter(activo=True),
        required=False,
        empty_label='Todos los proveedores',
        widget=forms.Select(attrs={'class': 'form-select'})
    )

