"""
DIGIT SOFT - Módulo de Clientes
Forms con Validaciones Profesionales
"""

from django import forms
from .models import Cliente
from core.validators import (
    validar_nombre,
    validar_telefono_colombiano,
    validar_cedula,
    validar_email_profesional,
    validar_direccion
)


class ClienteForm(forms.ModelForm):
    """Formulario para crear y editar clientes con validaciones mejoradas"""

    class Meta:
        model = Cliente
        fields = ['nombres', 'apellidos', 'numero_documento', 'telefono', 'correo', 'direccion', 'activo']
        widgets = {
            'nombres': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '👤 Ingrese los nombres del cliente',
                'required': True,
                'autocomplete': 'given-name'
            }),
            'apellidos': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '👤 Ingrese los apellidos del cliente',
                'required': True,
                'autocomplete': 'family-name'
            }),
            'numero_documento': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '🪪 Ejemplo: 1234567890',
                'required': True,
                'pattern': '[0-9]+',
                'autocomplete': 'off'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '📱 Ejemplo: 3001234567',
                'required': True,
                'type': 'tel',
                'autocomplete': 'tel'
            }),
            'correo': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': '📧 ejemplo@correo.com',
                'required': True,
                'type': 'email',
                'autocomplete': 'email'
            }),
            'direccion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '📍 Calle 123 #45-67, Ciudad, Departamento',
                'rows': 3,
                'required': True,
                'maxlength': 300
            }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
        labels = {
            'nombres': '👤 Nombres',
            'apellidos': '👤 Apellidos',
            'numero_documento': '🪪 Número de Documento',
            'telefono': '📱 Teléfono',
            'correo': '📧 Correo Electrónico',
            'direccion': '📍 Dirección',
            'activo': '✓ Cliente Activo',
        }
        help_texts = {
            'nombres': 'Solo letras y espacios (mínimo 2 caracteres)',
            'apellidos': 'Solo letras y espacios (mínimo 2 caracteres)',
            'numero_documento': 'Cédula colombiana (6-10 dígitos)',
            'telefono': 'Teléfono colombiano (7 dígitos fijo o 10 celular)',
            'correo': 'Correo electrónico válido',
            'direccion': 'Dirección completa con números',
        }

    def clean_nombres(self):
        """Validar nombres con validador personalizado"""
        nombres = self.cleaned_data.get('nombres', '').strip()
        if not nombres:
            raise forms.ValidationError('⚠️ Este campo es obligatorio')

        try:
            validar_nombre(nombres)
        except forms.ValidationError as e:
            raise forms.ValidationError(str(e))

        return nombres.title()

    def clean_apellidos(self):
        """Validar apellidos con validador personalizado"""
        apellidos = self.cleaned_data.get('apellidos', '').strip()
        if not apellidos:
            raise forms.ValidationError('⚠️ Este campo es obligatorio')

        try:
            validar_nombre(apellidos)
        except forms.ValidationError as e:
            raise forms.ValidationError(str(e))

        return apellidos.title()

    def clean_numero_documento(self):
        """Validar número de documento"""
        documento = self.cleaned_data.get('numero_documento', '').strip()
        if not documento:
            raise forms.ValidationError('⚠️ Este campo es obligatorio')

        try:
            validar_cedula(documento)
        except forms.ValidationError as e:
            raise forms.ValidationError(str(e))

        # Verificar duplicados
        if Cliente.objects.filter(numero_documento=documento).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('🪪 Ya existe un cliente con este número de documento')

        return documento

    def clean_telefono(self):
        """Validar teléfono"""
        telefono = self.cleaned_data.get('telefono', '').strip()
        if not telefono:
            raise forms.ValidationError('⚠️ Este campo es obligatorio')

        try:
            validar_telefono_colombiano(telefono)
        except forms.ValidationError as e:
            raise forms.ValidationError(str(e))

        return telefono

    def clean_correo(self):
        """Validar correo electrónico"""
        correo = self.cleaned_data.get('correo', '').strip().lower()
        if not correo:
            raise forms.ValidationError('⚠️ Este campo es obligatorio')

        try:
            validar_email_profesional(correo)
        except forms.ValidationError as e:
            raise forms.ValidationError(str(e))

        # Verificar duplicados
        if Cliente.objects.filter(correo=correo).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('📧 Ya existe un cliente con este correo electrónico')

        return correo

    def clean_direccion(self):
        """Validar dirección"""
        direccion = self.cleaned_data.get('direccion', '').strip()
        if not direccion:
            raise forms.ValidationError('⚠️ Este campo es obligatorio')

        try:
            validar_direccion(direccion)
        except forms.ValidationError as e:
            raise forms.ValidationError(str(e))

        return direccion.title()

    def clean(self):
        """Validación global del formulario"""
        cleaned_data = super().clean()

        # Verificar que nombres y apellidos no sean iguales
        nombres = cleaned_data.get('nombres', '')
        apellidos = cleaned_data.get('apellidos', '')

        if nombres and apellidos and nombres.lower() == apellidos.lower():
            raise forms.ValidationError(
                '⚠️ Los nombres y apellidos no pueden ser idénticos'
            )

        return cleaned_data

