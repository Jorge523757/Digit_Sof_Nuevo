"""
DIGT SOFT - Módulo de Técnicos
Forms - Formularios para gestión de técnicos
"""

from django import forms
from django.contrib.auth.models import User
from .models import Tecnico


class TecnicoForm(forms.ModelForm):
    """
    Formulario para crear y editar técnicos
    """
    
    # Campos opcionales para crear usuario
    crear_usuario = forms.BooleanField(
        required=False,
        initial=True,
        label="Crear usuario de acceso al sistema",
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        })
    )
    username = forms.CharField(
        max_length=150,
        required=False,
        label="Nombre de Usuario",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre de usuario para el sistema'
        })
    )
    password = forms.CharField(
        required=False,
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña para el sistema'
        })
    )

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

    def clean_username(self):
        """Valida que el nombre de usuario sea único si se va a crear usuario"""
        username = self.cleaned_data.get('username')
        crear_usuario = self.data.get('crear_usuario')

        if crear_usuario and username:
            if User.objects.filter(username=username).exists():
                raise forms.ValidationError('Este nombre de usuario ya existe. Por favor, elige otro.')

        return username

    def clean(self):
        """Validación general del formulario"""
        cleaned_data = super().clean()
        crear_usuario = cleaned_data.get('crear_usuario')
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        # Si se marca crear usuario, validar que se proporcionen username y password
        if crear_usuario:
            if not username:
                self.add_error('username', 'El nombre de usuario es obligatorio si deseas crear acceso al sistema.')
            if not password and not self.instance.pk:  # Solo requerido al crear
                self.add_error('password', 'La contraseña es obligatoria si deseas crear acceso al sistema.')

        return cleaned_data

    def save(self, commit=True):
        """Guarda el técnico y opcionalmente crea el usuario"""
        tecnico = super().save(commit=False)

        if commit:
            tecnico.save()

            # Si se marcó crear usuario y no tiene usuario vinculado
            crear_usuario = self.cleaned_data.get('crear_usuario')
            username = self.cleaned_data.get('username')
            password = self.cleaned_data.get('password')

            if crear_usuario and username:
                # Verificar si ya tiene usuario vinculado
                from usuarios.models import PerfilUsuario
                perfil_existente = PerfilUsuario.objects.filter(tecnico=tecnico).first()

                if not perfil_existente:
                    # Crear nuevo usuario
                    user = User.objects.create_user(
                        username=username,
                        email=tecnico.correo,
                        password=password,
                        first_name=tecnico.nombres,
                        last_name=tecnico.apellidos
                    )

                    # Actualizar perfil
                    perfil = user.perfil
                    perfil.tipo_usuario = 'TECNICO'
                    perfil.telefono = tecnico.telefono
                    perfil.documento = tecnico.numero_documento
                    perfil.tecnico = tecnico
                    perfil.save()

        return tecnico


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

