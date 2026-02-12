"""
DIGIT SOFT - Formularios de Reportes de Daño
Formularios para que los clientes reporten equipos dañados
"""

from django import forms
from .models import RegistroDano
from equipos.models import Equipo
from clientes.models import Cliente


class ReporteDanoForm(forms.ModelForm):
    """Formulario para reportar un equipo dañado"""

    class Meta:
        model = RegistroDano
        fields = ['equipo', 'descripcion_dano', 'tiempo_requerido_cliente']
        widgets = {
            'equipo': forms.Select(attrs={
                'class': 'form-control',
                'required': True
            }),
            'descripcion_dano': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Describa detalladamente el problema del equipo...',
                'required': True
            }),
            'tiempo_requerido_cliente': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Lo necesito en 3 días, urgente, etc.',
            }),
        }
        labels = {
            'equipo': '💻 Seleccione el equipo dañado',
            'descripcion_dano': '📝 Descripción del daño',
            'tiempo_requerido_cliente': '⏰ ¿Cuándo necesita el equipo?',
        }
        help_texts = {
            'descripcion_dano': 'Sea lo más específico posible sobre el problema',
            'tiempo_requerido_cliente': 'Opcional: Indique si tiene urgencia',
        }

    def __init__(self, *args, **kwargs):
        cliente = kwargs.pop('cliente', None)
        super().__init__(*args, **kwargs)

        # Filtrar solo los equipos del cliente
        if cliente:
            self.fields['equipo'].queryset = Equipo.objects.filter(
                cliente=cliente,
                activo=True
            )
        else:
            self.fields['equipo'].queryset = Equipo.objects.none()



