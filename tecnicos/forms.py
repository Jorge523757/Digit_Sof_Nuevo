"""
DIGT SOFT - Módulo de Técnicos
Forms - Formularios para gestión de técnicos
"""

from django import forms
from .models import Tecnico


class TecnicoForm(forms.ModelForm):
    """
    Formulario para crear y editar técnicos
    """
    
    class Meta:
        model = Tecnico
        fields = ['nombres', 'apellidos', 'numero_documento', 'telefono', 'correo', 'profesion', 'activo']
        widgets = {
            'nombres': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese los nombres',
                'required': True
            }),
            'apellidos': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese los apellidos',
                'required': True
            }),
            'numero_documento': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el número de documento',
                'required': True
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el teléfono',
                'required': True
            }),
            'correo': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el correo electrónico',
                'required': True
            }),
            'profesion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese la profesión',
                'required': True
            }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }
    
    def clean_numero_documento(self):
        """Valida que el número de documento sea único"""
        numero_documento = self.cleaned_data.get('numero_documento')
        tecnico_id = self.instance.pk if self.instance else None
        
        if Tecnico.objects.filter(numero_documento=numero_documento).exclude(pk=tecnico_id).exists():
            raise forms.ValidationError('Ya existe un técnico con este número de documento.')
        
        return numero_documento
    
    def clean_correo(self):
        """Valida el formato del correo electrónico"""
        correo = self.cleaned_data.get('correo')
        tecnico_id = self.instance.pk if self.instance else None
        
        if Tecnico.objects.filter(correo=correo).exclude(pk=tecnico_id).exists():
            raise forms.ValidationError('Ya existe un técnico con este correo electrónico.')
        
        return correo


class TecnicoBusquedaForm(forms.Form):
    """
    Formulario para búsqueda de técnicos
    """
    busqueda = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Buscar por nombre, documento, teléfono...',
            'id': 'busqueda'
        })
    )
    estado = forms.ChoiceField(
        required=False,
        choices=[('', 'Todos'), ('activo', 'Activos'), ('inactivo', 'Inactivos')],
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'estado'
        })
    )

