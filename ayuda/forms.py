"""
Formularios para el Sistema de Ayuda
"""

from django import forms
from .models import TicketAyuda, RespuestaTicket


class CrearTicketForm(forms.ModelForm):
    """Formulario para crear un nuevo ticket de ayuda"""
    
    class Meta:
        model = TicketAyuda
        fields = ['categoria', 'asunto', 'descripcion', 'prioridad', 'archivo']
        widgets = {
            'categoria': forms.Select(attrs={
                'class': 'form-select',
                'required': True
            }),
            'asunto': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Describe brevemente tu problema',
                'maxlength': 200,
                'required': True
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe detalladamente tu problema...',
                'rows': 6,
                'required': True
            }),
            'prioridad': forms.Select(attrs={
                'class': 'form-select'
            }),
            'archivo': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*,.pdf,.doc,.docx,.txt'
            })
        }
        labels = {
            'categoria': 'Categoría',
            'asunto': 'Asunto',
            'descripcion': 'Descripción del problema',
            'prioridad': 'Prioridad',
            'archivo': 'Archivo adjunto (opcional)'
        }
        help_texts = {
            'archivo': 'Puedes adjuntar imágenes, PDFs o documentos (máx. 5MB)',
            'prioridad': 'Selecciona la urgencia de tu solicitud'
        }


class ResponderTicketForm(forms.ModelForm):
    """Formulario para responder a un ticket"""
    
    class Meta:
        model = RespuestaTicket
        fields = ['mensaje', 'archivo']
        widgets = {
            'mensaje': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Escribe tu respuesta aquí...',
                'rows': 4,
                'required': True
            }),
            'archivo': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*,.pdf,.doc,.docx,.txt'
            })
        }
        labels = {
            'mensaje': 'Tu respuesta',
            'archivo': 'Archivo adjunto (opcional)'
        }


class BuscarFAQForm(forms.Form):
    """Formulario para buscar en las FAQs"""
    busqueda = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '🔍 Buscar en preguntas frecuentes...',
            'autocomplete': 'off'
        })
    )
    categoria = forms.ChoiceField(
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )

