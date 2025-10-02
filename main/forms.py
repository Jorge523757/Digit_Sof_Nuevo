from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import UserProfile
import re

class CustomUserCreationForm(UserCreationForm):
    """Formulario personalizado para registro de usuarios"""
    
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Tu nombre',
            'id': 'first_name'
        }),
        label='Nombre'
    )
    
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Tu apellido',
            'id': 'last_name'
        }),
        label='Apellido'
    )
    
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Elige un nombre de usuario',
            'id': 'username'
        }),
        label='Nombre de Usuario'
    )
    
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'tu@email.com',
            'id': 'email'
        }),
        label='Correo Electrónico'
    )
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Crea una contraseña segura',
            'id': 'password1'
        }),
        label='Contraseña'
    )
    
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Confirma tu contraseña',
            'id': 'password2'
        }),
        label='Confirmar Contraseña'
    )
    
    terms = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(attrs={
            'class': 'checkbox-input',
            'id': 'terms'
        }),
        label='Acepto los términos y condiciones'
    )
    
    newsletter = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'checkbox-input',
            'id': 'newsletter'
        }),
        label='Quiero recibir noticias y actualizaciones'
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def clean_first_name(self):
        """Validar que el nombre solo contenga letras"""
        first_name = self.cleaned_data.get('first_name')
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', first_name):
            raise ValidationError('El nombre solo debe contener letras.')
        if len(first_name) < 2:
            raise ValidationError('El nombre debe tener al menos 2 caracteres.')
        return first_name.title()

    def clean_last_name(self):
        """Validar que el apellido solo contenga letras"""
        last_name = self.cleaned_data.get('last_name')
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', last_name):
            raise ValidationError('El apellido solo debe contener letras.')
        if len(last_name) < 2:
            raise ValidationError('El apellido debe tener al menos 2 caracteres.')
        return last_name.title()

    def clean_username(self):
        """Validar formato del username"""
        username = self.cleaned_data.get('username')
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            raise ValidationError('El username solo puede contener letras, números y guión bajo.')
        if len(username) < 3:
            raise ValidationError('El username debe tener al menos 3 caracteres.')
        if User.objects.filter(username=username).exists():
            raise ValidationError('Este nombre de usuario ya está en uso.')
        return username.lower()

    def clean_email(self):
        """Validar que el email no esté registrado"""
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Este correo electrónico ya está registrado.')
        return email.lower()

    def clean_password1(self):
        """Validar fuerza de la contraseña"""
        password1 = self.cleaned_data.get('password1')
        
        if len(password1) < 8:
            raise ValidationError('La contraseña debe tener al menos 8 caracteres.')
        
        # Verificar que tenga al menos una mayúscula
        if not re.search(r'[A-Z]', password1):
            raise ValidationError('La contraseña debe tener al menos una mayúscula.')
        
        # Verificar que tenga al menos una minúscula
        if not re.search(r'[a-z]', password1):
            raise ValidationError('La contraseña debe tener al menos una minúscula.')
        
        # Verificar que tenga al menos un número
        if not re.search(r'[0-9]', password1):
            raise ValidationError('La contraseña debe tener al menos un número.')
        
        # Verificar que tenga al menos un carácter especial
        if not re.search(r'[^A-Za-z0-9]', password1):
            raise ValidationError('La contraseña debe tener al menos un carácter especial.')
        
        return password1

    def save(self, commit=True):
        """Guardar usuario con información adicional"""
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        
        if commit:
            user.save()
            # Aquí podrías crear un perfil de usuario o enviar email de verificación
            
        return user


class CustomAuthenticationForm(AuthenticationForm):
    """Formulario personalizado para login"""
    
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Ingresa tu usuario o email',
            'id': 'username',
            'autocomplete': 'username'
        }),
        label='Usuario o Email'
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Ingresa tu contraseña',
            'id': 'password',
            'autocomplete': 'current-password'
        }),
        label='Contraseña'
    )
    
    remember_me = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'checkbox-input',
            'id': 'remember'
        }),
        label='Recordar sesión'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Permitir login con email o username
        self.fields['username'].label = 'Usuario o Email'

    def clean_username(self):
        """Permitir login con email o username"""
        username = self.cleaned_data.get('username')
        
        # Si contiene @, es un email
        if '@' in username:
            try:
                user = User.objects.get(email=username)
                return user.username
            except User.DoesNotExist:
                raise ValidationError('No existe una cuenta con este email.')
        
        return username


class ForgotPasswordForm(forms.Form):
    """Formulario para recuperación de contraseña"""
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'Ingresa tu correo electrónico',
            'id': 'email',
            'autocomplete': 'email'
        }),
        label='Correo Electrónico'
    )

    def clean_email(self):
        """Verificar que el email esté registrado"""
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            raise ValidationError('No existe una cuenta asociada a este correo electrónico.')
        return email.lower()


class CustomPasswordResetForm(forms.Form):
    """Formulario para establecer nueva contraseña"""
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Nueva contraseña',
            'id': 'password1'
        }),
        label='Nueva Contraseña'
    )
    
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Confirmar nueva contraseña',
            'id': 'password2'
        }),
        label='Confirmar Nueva Contraseña'
    )

    def clean_password1(self):
        """Validar fuerza de la nueva contraseña"""
        password1 = self.cleaned_data.get('password1')
        
        if len(password1) < 8:
            raise ValidationError('La contraseña debe tener al menos 8 caracteres.')
        
        if not re.search(r'[A-Z]', password1):
            raise ValidationError('La contraseña debe tener al menos una mayúscula.')
        
        if not re.search(r'[a-z]', password1):
            raise ValidationError('La contraseña debe tener al menos una minúscula.')
        
        if not re.search(r'[0-9]', password1):
            raise ValidationError('La contraseña debe tener al menos un número.')
        
        if not re.search(r'[^A-Za-z0-9]', password1):
            raise ValidationError('La contraseña debe tener al menos un carácter especial.')
        
        return password1

    def clean(self):
        """Verificar que las contraseñas coincidan"""
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError('Las contraseñas no coinciden.')
        
        return cleaned_data


class ContactForm(forms.Form):
    """Formulario de contacto mejorado"""
    
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Tu nombre completo',
            'id': 'name'
        }),
        label='Nombre Completo'
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'tu@email.com',
            'id': 'email'
        }),
        label='Correo Electrónico'
    )
    
    phone = forms.CharField(
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Tu número de teléfono (opcional)',
            'id': 'phone'
        }),
        label='Teléfono (Opcional)'
    )
    
    SUBJECT_CHOICES = [
        ('', 'Selecciona un tema'),
        ('cotizacion', 'Solicitar Cotización'),
        ('soporte', 'Soporte Técnico'),
        ('ventas', 'Información de Ventas'),
        ('desarrollo', 'Desarrollo de Software'),
        ('hosting', 'Servicios de Hosting'),
        ('otro', 'Otro')
    ]
    
    subject = forms.ChoiceField(
        choices=SUBJECT_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-input',
            'id': 'subject'
        }),
        label='Tema'
    )
    
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-input',
            'placeholder': 'Describe tu consulta o solicitud...',
            'id': 'message',
            'rows': 5
        }),
        label='Mensaje'
    )

    def clean_name(self):
        """Validar nombre"""
        name = self.cleaned_data.get('name')
        if len(name) < 2:
            raise ValidationError('El nombre debe tener al menos 2 caracteres.')
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', name):
            raise ValidationError('El nombre solo debe contener letras.')
        return name.title()

    def clean_phone(self):
        """Validar teléfono si se proporciona"""
        phone = self.cleaned_data.get('phone')
        if phone:
            # Remover espacios y caracteres no numéricos excepto + y -
            phone_clean = re.sub(r'[^\d+\-\s]', '', phone)
            if len(phone_clean) < 7:
                raise ValidationError('El número de teléfono no es válido.')
        return phone

    def clean_message(self):
        """Validar mensaje"""
        message = self.cleaned_data.get('message')
        if len(message) < 10:
            raise ValidationError('El mensaje debe tener al menos 10 caracteres.')
        return message


class BaseUserRegistrationForm(UserCreationForm):
    """Formulario base para registro con perfil de usuario"""
    
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Tu nombre',
        }),
        label='Nombre'
    )
    
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Tu apellido',
        }),
        label='Apellido'
    )
    
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'tu@email.com',
        }),
        label='Correo Electrónico'
    )
    
    documento = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Número de documento',
        }),
        label='Documento de Identidad'
    )
    
    telefono = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Teléfono de contacto',
        }),
        label='Teléfono'
    )
    
    direccion = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Dirección completa',
        }),
        label='Dirección'
    )
    
    fecha_nacimiento = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-input',
            'type': 'date',
        }),
        label='Fecha de Nacimiento'
    )
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'Nombre de usuario'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'Contraseña'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'Confirmar contraseña'
        })


class ClienteRegistrationForm(BaseUserRegistrationForm):
    """Formulario específico para registro de clientes"""
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        
        if commit:
            user.save()
            profile = user.profile
            profile.role = 'cliente'
            profile.documento = self.cleaned_data['documento']
            profile.telefono = self.cleaned_data['telefono']
            profile.direccion = self.cleaned_data['direccion']
            profile.fecha_nacimiento = self.cleaned_data.get('fecha_nacimiento')
            profile.save()
        
        return user


class ProveedorRegistrationForm(BaseUserRegistrationForm):
    """Formulario específico para registro de proveedores"""
    
    nit = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'NIT de la empresa',
        }),
        label='NIT'
    )
    
    razon_social = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Razón social de la empresa',
        }),
        label='Razón Social'
    )
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        
        if commit:
            user.save()
            profile = user.profile
            profile.role = 'proveedor'
            profile.documento = self.cleaned_data['documento']
            profile.telefono = self.cleaned_data['telefono']
            profile.direccion = self.cleaned_data['direccion']
            profile.fecha_nacimiento = self.cleaned_data.get('fecha_nacimiento')
            profile.nit = self.cleaned_data['nit']
            profile.razon_social = self.cleaned_data['razon_social']
            profile.save()
        
        return user


class AdministradorRegistrationForm(BaseUserRegistrationForm):
    """Formulario específico para registro de administradores"""
    
    codigo_admin = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Código de administrador',
        }),
        label='Código de Administrador',
        help_text='Código especial requerido para crear cuenta de administrador'
    )
    
    def clean_codigo_admin(self):
        """Validar código de administrador"""
        codigo = self.cleaned_data.get('codigo_admin')
        # Código secreto para crear administradores
        if codigo != 'DIGITSOFT2025':
            raise ValidationError('Código de administrador incorrecto.')
        return codigo
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.is_staff = True  # Dar permisos de staff
        
        if commit:
            user.save()
            profile = user.profile
            profile.role = 'administrador'
            profile.documento = self.cleaned_data['documento']
            profile.telefono = self.cleaned_data['telefono']
            profile.direccion = self.cleaned_data['direccion']
            profile.fecha_nacimiento = self.cleaned_data.get('fecha_nacimiento')
            profile.save()
        
        return user


class RoleSelectionForm(forms.Form):
    """Formulario para seleccionar el tipo de usuario a registrar"""
    
    ROLE_CHOICES = [
        ('cliente', 'Cliente - Realizar compras y solicitar servicios'),
        ('proveedor', 'Proveedor - Suministrar productos y servicios'),
        ('administrador', 'Administrador - Gestionar el sistema (requiere código)'),
    ]
    
    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        widget=forms.RadioSelect(attrs={
            'class': 'role-option'
        }),
        label='Tipo de cuenta',
        required=True
    )