"""
DIGIT SOFT - Formularios de Órdenes de Servicio
Formularios para gestión de órdenes de servicio
"""

from django import forms
from .models import OrdenServicio
from tecnicos.models import Tecnico
from clientes.models import Cliente


class OrdenServicioForm(forms.ModelForm):
    """Formulario para crear/editar órdenes de servicio"""

    class Meta:
        model = OrdenServicio
        fields = [
            'cliente', 'tecnico_asignado', 'tipo_equipo', 'marca', 'modelo', 'serie',
            'falla_reportada', 'estado_fisico', 'accesorios_incluidos',
            'prioridad', 'fecha_compromiso', 'observaciones'
        ]
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'tecnico_asignado': forms.Select(attrs={'class': 'form-control'}),
            'tipo_equipo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Laptop, PC, Impresora'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'serie': forms.TextInput(attrs={'class': 'form-control'}),
            'falla_reportada': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'estado_fisico': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'accesorios_incluidos': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'prioridad': forms.Select(attrs={'class': 'form-control'}),
            'fecha_compromiso': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class AsignarTecnicoForm(forms.ModelForm):
    """Formulario para asignar técnico a una orden"""

    class Meta:
        model = OrdenServicio
        fields = ['tecnico_asignado', 'prioridad', 'fecha_compromiso', 'observaciones']
        widgets = {
            'tecnico_asignado': forms.Select(attrs={
                'class': 'form-control',
                'required': True
            }),
            'prioridad': forms.Select(attrs={
                'class': 'form-control'
            }),
            'fecha_compromiso': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
            'observaciones': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Observaciones adicionales...'
            }),
        }
        labels = {
            'tecnico_asignado': '🔧 Técnico Asignado',
            'prioridad': '⚡ Prioridad',
            'fecha_compromiso': '📅 Fecha de Compromiso',
            'observaciones': '📝 Observaciones',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar solo técnicos activos y no eliminados
        self.fields['tecnico_asignado'].queryset = Tecnico.objects.filter(
            activo=True,
            eliminado=False
        )


class DiagnosticoForm(forms.ModelForm):
    """Formulario para que el técnico ingrese el diagnóstico"""

    class Meta:
        model = OrdenServicio
        fields = [
            'diagnostico',
            'tiempo_estimado_reparacion',
            'estado',
            'costo_diagnostico',
            'costo_mano_obra',
            'observaciones'
        ]
        widgets = {
            'diagnostico': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Describa el diagnóstico del equipo...',
                'required': True
            }),
            'tiempo_estimado_reparacion': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Horas estimadas',
                'min': 1,
                'required': True
            }),
            'estado': forms.Select(attrs={
                'class': 'form-control'
            }),
            'costo_diagnostico': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'step': '0.01',
                'min': 0
            }),
            'costo_mano_obra': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'step': '0.01',
                'min': 0
            }),
            'observaciones': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Observaciones adicionales...'
            }),
        }
        labels = {
            'diagnostico': '🔍 Diagnóstico Técnico',
            'tiempo_estimado_reparacion': '⏱️ Tiempo Estimado (horas)',
            'estado': '📊 Estado de la Orden',
            'costo_diagnostico': '💰 Costo de Diagnóstico',
            'costo_mano_obra': '💰 Costo de Mano de Obra',
            'observaciones': '📝 Observaciones',
        }
        help_texts = {
            'tiempo_estimado_reparacion': 'Tiempo estimado en horas para completar la reparación',
            'costo_diagnostico': 'Costo del diagnóstico realizado',
            'costo_mano_obra': 'Costo estimado de la mano de obra',
        }
