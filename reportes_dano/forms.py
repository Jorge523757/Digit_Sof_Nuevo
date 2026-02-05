"""
DIGT SOFT - Formularios para Registro de Daños
"""

from django import forms
from .models import RegistroDano, ImagenDano


class RegistroDanoForm(forms.ModelForm):
    """Formulario básico para registrar daño"""

    class Meta:
        model = RegistroDano
        fields = ['descripcion_dano']
        widgets = {
            'descripcion_dano': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Describa el daño...',
            }),
        }


class ImagenDanoForm(forms.ModelForm):
    """Formulario para subir imágenes"""

    class Meta:
        model = ImagenDano
        fields = ['imagen']
        widgets = {
            'imagen': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',
            }),
        }


from django.forms import inlineformset_factory

ImagenDanoFormSet = inlineformset_factory(
    RegistroDano,
    ImagenDano,
    form=ImagenDanoForm,
    extra=3,
    max_num=5,
    can_delete=True
)

