"""
DIGT SOFT - Módulo de Usuarios
Forms - Formularios de Registro y Gestión
"""

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import PerfilUsuario
from clientes.models import Cliente


class RegistroClienteForm(UserCreationForm):
    """Formulario de registro para clientes"""

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'correo@ejemplo.com'
        })
    )
    first_name = forms.CharField(
        max_length=100,
        required=True,
        label="Nombres",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingresa tus nombres'
        })
    )
    last_name = forms.CharField(
        max_length=100,
        required=True,
        label="Apellidos",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingresa tus apellidos'
        })
    )
    telefono = forms.CharField(
        max_length=15,
        required=True,
        label="Teléfono",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '+52 123 456 7890'
        })
    )
    direccion = forms.CharField(
        required=True,
        label="Dirección",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Ingresa tu dirección completa',
            'rows': 3
        })
    )
    documento = forms.CharField(
        max_length=20,
        required=True,
        label="Número de Documento",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'RFC o INE'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Elige un nombre de usuario'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Contraseña segura'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirma tu contraseña'
        })

        # Personalizar etiquetas
        self.fields['username'].label = "Nombre de Usuario"
        self.fields['email'].label = "Correo Electrónico"
        self.fields['password1'].label = "Contraseña"
        self.fields['password2'].label = "Confirmar Contraseña"

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo electrónico ya está registrado.')
        return email

    def clean_documento(self):
        documento = self.cleaned_data.get('documento')
        if Cliente.objects.filter(numero_documento=documento).exists():
            raise forms.ValidationError('Este documento ya está registrado.')
        return documento

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()

            # Crear el perfil de usuario
            perfil = user.perfil
            perfil.tipo_usuario = 'CLIENTE'
            perfil.telefono = self.cleaned_data['telefono']
            perfil.direccion = self.cleaned_data['direccion']
            perfil.documento = self.cleaned_data['documento']
            perfil.save()

            # Crear el registro en la tabla de clientes
            cliente = Cliente.objects.create(
                nombres=self.cleaned_data['first_name'],
                apellidos=self.cleaned_data['last_name'],
                numero_documento=self.cleaned_data['documento'],
                telefono=self.cleaned_data['telefono'],
                correo=self.cleaned_data['email'],
                direccion=self.cleaned_data['direccion'],
                activo=True
            )

            # Vincular el cliente con el perfil
            perfil.cliente = cliente
            perfil.save()

        return user


class PerfilUsuarioForm(forms.ModelForm):
    """Formulario para editar perfil de usuario"""

    class Meta:
        model = PerfilUsuario
        fields = ['telefono', 'direccion', 'documento', 'foto']
        widgets = {
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'documento': forms.TextInput(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
        }


class UsuarioCrearForm(UserCreationForm):
    """Formulario para que administradores creen nuevos usuarios"""

    email = forms.EmailField(
        required=True,
        label="Correo Electrónico",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'correo@ejemplo.com'
        })
    )
    first_name = forms.CharField(
        max_length=100,
        required=True,
        label="Nombres",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombres del usuario'
        })
    )
    last_name = forms.CharField(
        max_length=100,
        required=True,
        label="Apellidos",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Apellidos del usuario'
        })
    )
    is_staff = forms.BooleanField(
        required=False,
        label="¿Es personal autorizado (Staff)?",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    is_active = forms.BooleanField(
        required=False,
        initial=True,
        label="¿Usuario activo?",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de usuario'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo electrónico ya está registrado.')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.is_staff = self.cleaned_data.get('is_staff', False)
        user.is_active = self.cleaned_data.get('is_active', True)

        if commit:
            user.save()

        return user


class RecuperarPasswordForm(forms.Form):
    """Formulario para solicitar recuperación de contraseña"""

    email = forms.EmailField(
        required=True,
        label="Correo Electrónico",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingresa tu correo electrónico',
            'autofocus': True
        }),
        help_text='Ingresa el correo con el que te registraste'
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError('No existe ninguna cuenta con este correo electrónico.')
        return email


class ResetPasswordForm(forms.Form):
    """Formulario para resetear la contraseña con token"""

    new_password1 = forms.CharField(
        required=True,
        label="Nueva Contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingresa tu nueva contraseña',
            'minlength': '8'
        }),
        min_length=8,
        help_text='La contraseña debe tener al menos 8 caracteres'
    )

    new_password2 = forms.CharField(
        required=True,
        label="Confirmar Nueva Contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirma tu nueva contraseña',
            'minlength': '8'
        }),
        min_length=8
    )

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('new_password1')
        password2 = cleaned_data.get('new_password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden.')

        return cleaned_data


