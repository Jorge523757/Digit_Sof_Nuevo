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
        if not email:
            raise forms.ValidationError('El correo electrónico es obligatorio.')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo electrónico ya está registrado. Por favor, usa otro correo o inicia sesión.')
        # Validar formato de email
        if '@' not in email or '.' not in email.split('@')[-1]:
            raise forms.ValidationError('Por favor, ingresa un correo electrónico válido.')
        return email.lower()

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError('El nombre de usuario es obligatorio.')
        if len(username) < 4:
            raise forms.ValidationError('El nombre de usuario debe tener al menos 4 caracteres.')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Este nombre de usuario ya está en uso. Por favor, elige otro.')
        # No permitir espacios
        if ' ' in username:
            raise forms.ValidationError('El nombre de usuario no puede contener espacios.')
        return username

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if not telefono:
            raise forms.ValidationError('El teléfono es obligatorio.')
        # Eliminar caracteres no numéricos
        telefono_limpio = ''.join(filter(str.isdigit, telefono))
        if len(telefono_limpio) < 10:
            raise forms.ValidationError('El teléfono debe tener al menos 10 dígitos.')
        return telefono

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name:
            raise forms.ValidationError('Los nombres son obligatorios.')
        if len(first_name) < 2:
            raise forms.ValidationError('Los nombres deben tener al menos 2 caracteres.')
        return first_name.strip().title()

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name:
            raise forms.ValidationError('Los apellidos son obligatorios.')
        if len(last_name) < 2:
            raise forms.ValidationError('Los apellidos deben tener al menos 2 caracteres.')
        return last_name.strip().title()

    def clean_direccion(self):
        direccion = self.cleaned_data.get('direccion')
        if not direccion:
            raise forms.ValidationError('La dirección es obligatoria.')
        if len(direccion) < 10:
            raise forms.ValidationError('Por favor, ingresa una dirección completa (mínimo 10 caracteres).')
        return direccion.strip()

    def clean_documento(self):
        documento = self.cleaned_data.get('documento')
        if not documento:
            raise forms.ValidationError('El número de documento es obligatorio.')
        if len(documento) < 5:
            raise forms.ValidationError('El número de documento debe tener al menos 5 caracteres.')
        if Cliente.objects.filter(numero_documento=documento).exists():
            raise forms.ValidationError('Este documento ya está registrado. Si ya tienes una cuenta, inicia sesión.')
        return documento.strip().upper()

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError('Las contraseñas no coinciden. Por favor, verifica e inténtalo de nuevo.')
            if len(password1) < 8:
                raise forms.ValidationError('La contraseña debe tener al menos 8 caracteres.')
            if password1.isdigit():
                raise forms.ValidationError('La contraseña no puede ser completamente numérica.')
            if password1.lower() == self.cleaned_data.get('username', '').lower():
                raise forms.ValidationError('La contraseña no puede ser igual al nombre de usuario.')

        return password2

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


