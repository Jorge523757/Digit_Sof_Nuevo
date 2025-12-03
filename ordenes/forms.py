"""
DIGT SOFT - Formularios del Módulo de Órdenes de Servicio
"""

from django import forms
from django.forms import inlineformset_factory
from .models import OrdenServicio, RepuestoOrden
from tecnicos.models import Tecnico


class OrdenServicioForm(forms.ModelForm):
    """Formulario para crear y editar órdenes de servicio"""

    class Meta:
        model = OrdenServicio
        fields = [
            'cliente', 'tecnico_asignado', 'tipo_equipo', 'marca', 'modelo', 'serie',
            'falla_reportada', 'estado_fisico', 'accesorios_incluidos',
            'diagnostico', 'solucion_aplicada', 'estado', 'prioridad',
            'costo_diagnostico', 'costo_mano_obra', 'fecha_compromiso',
            'tiene_garantia', 'dias_garantia', 'observaciones', 'notas_internas'
        ]
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-select'}),
            'tecnico_asignado': forms.Select(attrs={'class': 'form-select'}),
            'tipo_equipo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Laptop, PC, Impresora'
            }),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'serie': forms.TextInput(attrs={'class': 'form-control'}),
            'falla_reportada': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Descripción de la falla reportada por el cliente'
            }),
            'estado_fisico': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'Estado físico del equipo al recibir'
            }),
            'accesorios_incluidos': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'Cargador, mouse, bolso, etc.'
            }),
            'diagnostico': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Diagnóstico técnico del problema'
            }),
            'solucion_aplicada': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Descripción de la solución aplicada'
            }),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'prioridad': forms.Select(attrs={'class': 'form-select'}),
            'costo_diagnostico': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0'
            }),
            'costo_mano_obra': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0'
            }),
            'fecha_compromiso': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
            'tiene_garantia': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'dias_garantia': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'notas_internas': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }


class RepuestoOrdenForm(forms.ModelForm):
    """Formulario para repuestos de orden"""

    class Meta:
        model = RepuestoOrden
        fields = ['producto', 'cantidad', 'precio_unitario']
        widgets = {
            'producto': forms.Select(attrs={'class': 'form-select'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'precio_unitario': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0'
            }),
        }


# FormSet para manejar múltiples repuestos
RepuestoOrdenFormSet = inlineformset_factory(
    OrdenServicio,
    RepuestoOrden,
    form=RepuestoOrdenForm,
    extra=1,
    can_delete=True
)


class BuscarOrdenForm(forms.Form):
    """Formulario para buscar y filtrar órdenes"""

    busqueda = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Buscar por número, cliente, marca, modelo...'
        })
    )

    estado = forms.ChoiceField(
        required=False,
        choices=[('', 'Todos los estados')] + OrdenServicio.ESTADO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    prioridad = forms.ChoiceField(
        required=False,
        choices=[('', 'Todas las prioridades')] + OrdenServicio.PRIORIDAD_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    tecnico = forms.ModelChoiceField(
        queryset=Tecnico.objects.filter(activo=True),
        required=False,
        empty_label='Todos los técnicos',
        widget=forms.Select(attrs={'class': 'form-select'})
    )

