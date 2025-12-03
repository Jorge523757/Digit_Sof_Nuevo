"""
DIGT SOFT - Formularios del Módulo de Garantías
"""

from django import forms
from .models import Garantia, SeguimientoGarantia
from datetime import date, timedelta


class GarantiaForm(forms.ModelForm):
    """Formulario para registrar garantías"""

    class Meta:
        model = Garantia
        fields = [
            'nombre_comprador', 'cedula', 'telefono', 'correo_electronico',
            'producto', 'nombre_producto', 'numero_serie', 'modelo',
            'fecha_compra', 'factura_compra', 'lugar_compra',
            'fecha_inicio', 'fecha_vencimiento', 'meses_garantia',
            'estado', 'motivo_reclamacion', 'descripcion_problema',
            'solucion', 'fecha_resolucion', 'observaciones', 'cliente'
        ]
        widgets = {
            'nombre_comprador': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre completo del comprador',
                'required': True
            }),
            'cedula': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número de cédula',
                'required': True
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Teléfono de contacto',
                'required': True
            }),
            'correo_electronico': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'correo@ejemplo.com',
                'required': True
            }),
            'producto': forms.Select(attrs={
                'class': 'form-control',
                'required': True
            }),
            'nombre_producto': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del producto',
                'required': True
            }),
            'numero_serie': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número de serie del producto'
            }),
            'modelo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Modelo del producto'
            }),
            'fecha_compra': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'required': True
            }),
            'factura_compra': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número de factura'
            }),
            'lugar_compra': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Lugar donde se realizó la compra',
                'required': True
            }),
            'fecha_inicio': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'required': True
            }),
            'fecha_vencimiento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'required': True
            }),
            'meses_garantia': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '12',
                'min': '1',
                'value': '12'
            }),
            'estado': forms.Select(attrs={
                'class': 'form-control'
            }),
            'motivo_reclamacion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Motivo de la reclamación...'
            }),
            'descripcion_problema': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Descripción detallada del problema...'
            }),
            'solucion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Solución aplicada...'
            }),
            'fecha_resolucion': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'observaciones': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Observaciones adicionales...'
            }),
            'cliente': forms.Select(attrs={
                'class': 'form-control'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Si es nueva garantía, establecer fecha de inicio como hoy
        if not self.instance.pk:
            self.initial['fecha_inicio'] = date.today()
            self.initial['meses_garantia'] = 12

    def clean_cedula(self):
        """Valida el formato de la cédula"""
        cedula = self.cleaned_data.get('cedula')
        if cedula:
            cedula = cedula.strip()
            if not cedula.isdigit():
                raise forms.ValidationError('La cédula debe contener solo números.')
        return cedula

    def clean(self):
        """Validaciones adicionales"""
        cleaned_data = super().clean()
        fecha_compra = cleaned_data.get('fecha_compra')
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_vencimiento = cleaned_data.get('fecha_vencimiento')
        meses_garantia = cleaned_data.get('meses_garantia')

        # Validar que la fecha de inicio no sea anterior a la de compra
        if fecha_compra and fecha_inicio:
            if fecha_inicio < fecha_compra:
                raise forms.ValidationError('La fecha de inicio no puede ser anterior a la fecha de compra.')

        # Validar que la fecha de vencimiento sea posterior a la de inicio
        if fecha_inicio and fecha_vencimiento:
            if fecha_vencimiento <= fecha_inicio:
                raise forms.ValidationError('La fecha de vencimiento debe ser posterior a la fecha de inicio.')

        # Calcular fecha de vencimiento basada en meses de garantía si no está establecida
        if fecha_inicio and meses_garantia and not fecha_vencimiento:
            cleaned_data['fecha_vencimiento'] = fecha_inicio + timedelta(days=meses_garantia * 30)

        return cleaned_data


class BuscarGarantiaForm(forms.Form):
    """Formulario para búsqueda de garantías"""

    busqueda = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '🔍 Buscar por ID, producto, nombre, cédula...',
            'id': 'busqueda-garantia'
        })
    )
    estado = forms.ChoiceField(
        required=False,
        choices=[('', 'Todos los estados')] + list(Garantia.ESTADO_GARANTIA),
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    vigencia = forms.ChoiceField(
        required=False,
        choices=[
            ('', 'Todas'),
            ('vigente', 'Vigentes'),
            ('vencidas', 'Vencidas'),
            ('por_vencer', 'Por vencer (30 días)'),
        ],
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )


class SeguimientoGarantiaForm(forms.ModelForm):
    """Formulario para agregar seguimiento a garantías"""

    class Meta:
        model = SeguimientoGarantia
        fields = ['estado_nuevo', 'comentarios']
        widgets = {
            'estado_nuevo': forms.Select(attrs={
                'class': 'form-control',
                'required': True
            }),
            'comentarios': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Comentarios sobre el cambio de estado...',
                'required': True
            }),
        }

