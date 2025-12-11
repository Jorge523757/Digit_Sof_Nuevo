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

    def clean_proveedor(self):
        """Valida que se seleccione un proveedor"""
        proveedor = self.cleaned_data.get('proveedor')
        if not proveedor:
            raise forms.ValidationError('Debes seleccionar un proveedor para la compra.')
        if not proveedor.activo:
            raise forms.ValidationError('El proveedor seleccionado está inactivo. Por favor, selecciona otro.')
        return proveedor

    def clean_fecha_entrega_esperada(self):
        """Valida la fecha de entrega"""
        from datetime import date
        fecha = self.cleaned_data.get('fecha_entrega_esperada')
        if fecha:
            if fecha < date.today():
                raise forms.ValidationError('La fecha de entrega no puede ser anterior a hoy.')
        return fecha

    def clean_impuestos(self):
        """Valida los impuestos"""
        impuestos = self.cleaned_data.get('impuestos')
        if impuestos is None:
            return 0
        if impuestos < 0:
            raise forms.ValidationError('Los impuestos no pueden ser negativos.')
        if impuestos > 100:
            raise forms.ValidationError('Los impuestos no pueden ser mayores al 100%.')
        return impuestos

    def clean_descuento(self):
        """Valida el descuento"""
        descuento = self.cleaned_data.get('descuento')
        if descuento is None:
            return 0
        if descuento < 0:
            raise forms.ValidationError('El descuento no puede ser negativo.')
        if descuento > 100:
            raise forms.ValidationError('El descuento no puede ser mayor al 100%.')
        return descuento

    def clean_responsable(self):
        """Valida el responsable"""
        responsable = self.cleaned_data.get('responsable')
        if responsable:
            responsable = responsable.strip()
            if len(responsable) < 3:
                raise forms.ValidationError('El nombre del responsable debe tener al menos 3 caracteres.')
        return responsable


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

