from django import forms
from .models import Administrador

class AdministradorForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = ['nombre', 'contraseña', 'correo_electronico']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'contraseña': forms.PasswordInput(attrs={'class': 'form-control'}),
            'correo_electronico': forms.EmailInput(attrs={'class': 'form-control'}),
        }
