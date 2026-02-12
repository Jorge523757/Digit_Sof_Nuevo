"""
DIGIT SOFT - Formularios de Técnicos
Formularios para gestión de técnicos
"""

from django import forms
from django.core.validators import RegexValidator
from .models import Tecnico


class TecnicoForm(forms.ModelForm):
    """Formulario para crear/editar técnicos"""

    class Meta:
        model = Tecnico
        fields = [
            'nombres', 'apellidos', 'numero_documento',
            'telefono', 'correo', 'profesion', 'activo'
        ]
        widgets = {
            'nombres': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombres del técnico',
                'required': True
            }),
            'apellidos': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellidos del técnico',
                'required': True
            }),
            'numero_documento': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número de documento',
                'required': True
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+57 300 123 4567',
                'required': True
            }),
            'correo': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'correo@ejemplo.com',
                'required': True
            }),
            'profesion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Técnico en Sistemas',
                'required': True
            }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
        labels = {
            'nombres': '👤 Nombres',
            'apellidos': '👤 Apellidos',
            'numero_documento': '🆔 Número de Documento',
            'telefono': '📱 Teléfono',
            'correo': '📧 Correo Electrónico',
            'profesion': '💼 Profesión',
            'activo': '✅ Activo',
        }


class TecnicoFiltroForm(forms.Form):
    """Formulario para filtrar técnicos"""

    ESTADO_CHOICES = [
        ('', 'Todos los estados'),
        ('habilitado', 'Habilitado'),
        ('inhabilitado', 'Inhabilitado'),
        ('eliminado', 'Eliminado'),
    ]

    busqueda = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Buscar por ID, teléfono, correo...',
        }),
        label='🔍 Buscar'
    )

    estado = forms.ChoiceField(
        required=False,
        choices=ESTADO_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control'
        }),
        label='📊 Estado'
    )

