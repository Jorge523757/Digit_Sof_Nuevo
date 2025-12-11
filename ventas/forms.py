"""
DIGITSOFT - Formularios del Módulo de Ventas
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

    def clean_cliente(self):
        """Valida que se seleccione un cliente"""
        cliente = self.cleaned_data.get('cliente')
        if not cliente:
            raise forms.ValidationError('Debes seleccionar un cliente para la venta.')
        return cliente

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

    def clean_impuestos(self):
        """Valida los impuestos"""
        impuestos = self.cleaned_data.get('impuestos')
        if impuestos is None:
            return 0
        if impuestos < 0:
            raise forms.ValidationError('Los impuestos no pueden ser negativos.')
        return impuestos

    def clean(self):
        """Validaciones adicionales"""
        cleaned_data = super().clean()
        requiere_entrega = cleaned_data.get('requiere_entrega')
        direccion_entrega = cleaned_data.get('direccion_entrega')

        if requiere_entrega and not direccion_entrega:
            self.add_error('direccion_entrega', 'Si la venta requiere entrega, debes proporcionar la dirección.')

        return cleaned_data


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

    def clean_producto(self):
        """Valida que se seleccione un producto"""
        producto = self.cleaned_data.get('producto')
        if not producto:
            raise forms.ValidationError('Debes seleccionar un producto.')
        return producto

    def clean_cantidad(self):
        """Valida la cantidad"""
        cantidad = self.cleaned_data.get('cantidad')
        producto = self.cleaned_data.get('producto')

        if not cantidad or cantidad <= 0:
            raise forms.ValidationError('La cantidad debe ser mayor a cero.')

        # Validar stock disponible
        if producto and cantidad > producto.stock_actual:
            raise forms.ValidationError(
                f'Stock insuficiente. Solo hay {producto.stock_actual} unidades disponibles.'
            )

        return cantidad

    def clean_precio_unitario(self):
        """Valida el precio unitario"""
        precio = self.cleaned_data.get('precio_unitario')
        if not precio or precio <= 0:
            raise forms.ValidationError('El precio unitario debe ser mayor a cero.')
        return precio

    def clean_descuento_item(self):
        """Valida el descuento del item"""
        descuento = self.cleaned_data.get('descuento_item')
        if descuento is None:
            return 0
        if descuento < 0:
            raise forms.ValidationError('El descuento no puede ser negativo.')

        precio_unitario = self.cleaned_data.get('precio_unitario', 0)
        if descuento >= precio_unitario:
            raise forms.ValidationError('El descuento no puede ser igual o mayor al precio del producto.')

        return descuento


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

