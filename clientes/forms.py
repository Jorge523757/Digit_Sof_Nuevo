"""
DIGIT SOFT - Módulo de Clientes
Forms
"""

from django import forms
from django.core.validators import RegexValidator
from .models import Cliente
import re


class ClienteForm(forms.ModelForm):
    """Formulario para crear y editar clientes con validaciones mejoradas"""

    # Validadores personalizados
    telefono_validator = RegexValidator(
        regex=r'^\+?[\d\s\-\(\)]{7,20}$',
        message='Ingrese un número de teléfono válido (7-20 caracteres, puede incluir +, espacios, guiones y paréntesis)'
    )

    documento_validator = RegexValidator(
        regex=r'^[0-9]{5,20}$',
        message='El documento debe contener entre 5 y 20 dígitos numéricos'
    )

    class Meta:
        model = Cliente
        fields = ['nombres', 'apellidos', 'numero_documento', 'telefono', 'correo', 'direccion', 'activo']
        widgets = {
            'nombres': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese los nombres',
                'required': True,
                'minlength': 2,
                'maxlength': 100,
                'pattern': '[A-Za-zÁÉÍÓÚáéíóúÑñ ]+',
                'title': 'Solo se permiten letras y espacios'
            }),
            'apellidos': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese los apellidos',
                'required': True,
                'minlength': 2,
                'maxlength': 100,
                'pattern': '[A-Za-zÁÉÍÓÚáéíóúÑñ ]+',
                'title': 'Solo se permiten letras y espacios'
            }),
            'numero_documento': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ejemplo: 1234567890',
                'required': True,
                'pattern': '[0-9]{5,20}',
                'title': 'Ingrese un documento válido (solo números, 5-20 dígitos)',
                'maxlength': 20
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+57 300 000 0000',
                'required': True,
                'type': 'tel',
                'title': 'Ingrese un teléfono válido'
            }),
            'correo': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'correo@ejemplo.com',
                'required': True,
                'type': 'email',
                'title': 'Ingrese un correo electrónico válido'
            }),
            'direccion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Dirección completa (calle, número, ciudad, departamento)',
                'rows': 3,
                'required': True,
                'minlength': 10,
                'maxlength': 300
            }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
        labels = {
            'nombres': 'Nombres *',
            'apellidos': 'Apellidos *',
            'numero_documento': 'Número de Documento *',
            'telefono': 'Teléfono *',
            'correo': 'Correo Electrónico *',
            'direccion': 'Dirección *',
            'activo': 'Cliente Activo',
        }

    def clean_nombres(self):
        """Validar que los nombres solo contengan letras y espacios"""
        nombres = self.cleaned_data.get('nombres', '').strip()
        if not nombres:
            raise forms.ValidationError('Este campo es obligatorio.')
        if len(nombres) < 2:
            raise forms.ValidationError('Los nombres deben tener al menos 2 caracteres.')
        if not re.match(r'^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$', nombres):
            raise forms.ValidationError('Los nombres solo pueden contener letras y espacios.')
        return nombres.title()  # Capitalizar cada palabra

    def clean_apellidos(self):
        """Validar que los apellidos solo contengan letras y espacios"""
        apellidos = self.cleaned_data.get('apellidos', '').strip()
        if not apellidos:
            raise forms.ValidationError('Este campo es obligatorio.')
        if len(apellidos) < 2:
            raise forms.ValidationError('Los apellidos deben tener al menos 2 caracteres.')
        if not re.match(r'^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$', apellidos):
            raise forms.ValidationError('Los apellidos solo pueden contener letras y espacios.')
        return apellidos.title()  # Capitalizar cada palabra

    def clean_numero_documento(self):
        """Validar formato del documento y unicidad"""
        documento = self.cleaned_data.get('numero_documento', '').strip()
        if not documento:
            raise forms.ValidationError('Este campo es obligatorio.')
        if not documento.isdigit():
            raise forms.ValidationError('El documento debe contener solo números.')
        if len(documento) < 5 or len(documento) > 20:
            raise forms.ValidationError('El documento debe tener entre 5 y 20 dígitos.')

        # Verificar unicidad (excluyendo el cliente actual si estamos editando)
        queryset = Cliente.objects.filter(numero_documento=documento)
        if self.instance.pk:
            queryset = queryset.exclude(pk=self.instance.pk)
        if queryset.exists():
            raise forms.ValidationError('Ya existe un cliente con este número de documento.')

        return documento

    def clean_telefono(self):
        """Validar formato del teléfono"""
        telefono = self.cleaned_data.get('telefono', '').strip()
        if not telefono:
            raise forms.ValidationError('Este campo es obligatorio.')

        # Validar que tenga al menos 7 caracteres (sin contar espacios y símbolos)
        numeros = re.sub(r'[^\d]', '', telefono)
        if len(numeros) < 7:
            raise forms.ValidationError('El teléfono debe tener al menos 7 dígitos.')
        if len(numeros) > 15:
            raise forms.ValidationError('El teléfono no puede tener más de 15 dígitos.')

        return telefono

    def clean_correo(self):
        """Validar formato del correo electrónico"""
        correo = self.cleaned_data.get('correo', '').strip().lower()
        if not correo:
            raise forms.ValidationError('Este campo es obligatorio.')

        # Validación adicional de formato
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, correo):
            raise forms.ValidationError('Ingrese un correo electrónico válido.')

        return correo

    def clean_direccion(self):
        """Validar que la dirección tenga longitud mínima"""
        direccion = self.cleaned_data.get('direccion', '').strip()
        if not direccion:
            raise forms.ValidationError('Este campo es obligatorio.')
        if len(direccion) < 10:
            raise forms.ValidationError('La dirección debe tener al menos 10 caracteres.')
        if len(direccion) > 300:
            raise forms.ValidationError('La dirección no puede exceder 300 caracteres.')
        return direccion
