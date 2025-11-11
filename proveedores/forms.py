"""
DIGT SOFT - Formularios del Módulo de Proveedores
"""

from django import forms
from .models import Proveedor


class ProveedorForm(forms.ModelForm):
    """Formulario para crear y editar proveedores"""

    class Meta:
        model = Proveedor
        fields = [
            'nombre_empresa', 'nit', 'nombre_contacto', 'telefono', 'email',
            'direccion', 'ciudad', 'pais', 'productos_servicios',
            'condiciones_pago', 'tiempo_entrega', 'calificacion',
            'activo', 'observaciones'
        ]
        widgets = {
            'nombre_empresa': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de la empresa'
            }),
            'nit': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'NIT sin puntos ni guiones'
            }),
            'nombre_contacto': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del contacto principal'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+57 3001234567'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'correo@empresa.com'
            }),
            'direccion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Dirección completa'
            }),
            'ciudad': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ciudad'
            }),
            'pais': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'País'
            }),
            'productos_servicios': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Descripción de productos o servicios que ofrece'
            }),
            'condiciones_pago': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 30 días, Contado'
            }),
            'tiempo_entrega': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 3-5 días hábiles'
            }),
            'calificacion': forms.Select(attrs={
                'class': 'form-select'
            }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'observaciones': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Observaciones adicionales'
            }),
        }


class BuscarProveedorForm(forms.Form):
    """Formulario para buscar y filtrar proveedores"""

    busqueda = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Buscar por nombre, NIT, contacto...'
        })
    )

    calificacion = forms.ChoiceField(
        required=False,
        choices=[('', 'Todas las calificaciones')] + Proveedor.CALIFICACION_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )

    estado = forms.ChoiceField(
        required=False,
        choices=[
            ('', 'Todos'),
            ('activo', 'Activos'),
            ('inactivo', 'Inactivos'),
        ],
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )

