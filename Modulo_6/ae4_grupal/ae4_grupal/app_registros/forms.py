from django import forms
from django.core.exceptions import ValidationError
from datetime import date

class EventoForm(forms.Form):
    nombre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre del evento'
        }),
        error_messages={
            'required': 'El nombre del evento es obligatorio.',
            'max_length': 'El nombre no puede exceder 100 caracteres.'
        }
    )
    fecha = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        }),
        error_messages={
            'required': 'La fecha del evento es obligatoria.',
            'invalid': 'Ingresa una fecha válida.'
        }
    )
    ubicacion = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ubicación del evento'
        }),
        error_messages={
            'required': 'La ubicación del evento es obligatoria.'
        }
    )
    
    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')
        if fecha and fecha < date.today():
            raise ValidationError("No se puede crear un evento en el pasado.")
        return fecha

class ParticipanteForm(forms.Form):
    nombre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre completo'
        }),
        error_messages={
            'required': 'El nombre es obligatorio.',
            'max_length': 'El nombre no puede exceder 100 caracteres.'
        }
    )
    correo = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'correo@ejemplo.com'
        }),
        error_messages={
            'required': 'El correo electrónico es obligatorio.',
            'invalid': 'Ingresa un correo electrónico válido.'
        }
    )