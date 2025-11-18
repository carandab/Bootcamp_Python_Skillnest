from django import forms
from django.core.exceptions import ValidationError
from datetime import date
from .models import Evento


class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre', 'fecha', 'hora', 'ubicacion', 'capacidad', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del evento'
            }),
            'fecha': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'ubicacion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ubicación del evento'
            }),
            'hora': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time',
                'id': 'hora',
            }),
            'capacidad': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'id': 'capacidad',
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'descripcion',
                'rows': 3,
            }),
        }
        error_messages = {
            'nombre': {
                'required': 'El nombre del evento es obligatorio.',
                'max_length': 'El nombre no puede exceder 200 caracteres.'
            },
            'fecha': {
                'required': 'La fecha del evento es obligatoria.',
                'invalid': 'Ingresa una fecha válida.'
            },
            'ubicacion': {
                'required': 'La ubicación del evento es obligatoria.'
            }
        }

    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')
        if fecha and fecha < date.today():
            raise ValidationError("No se puede crear un evento en el pasado.")
        return fecha
