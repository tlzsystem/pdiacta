from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = [
            'identificacion',
            'nombres',
            'apellido_paterno',
            'apellido_materno',
            'direccion',
            'comuna',
            'telefono',
        ]

        widgets = {
            'identificacion':forms.TextInput(attrs={
                'class': 'form-control', 'required': 'true'
            }),
            'nombres':forms.TextInput(attrs={
                'class':'form-control', 'required':'true'
            }),
            'apellido_paterno': forms.TextInput(attrs={
                'class': 'form-control', 'required': 'true'
            }),
            'apellido_materno': forms.TextInput(attrs={
                'class': 'form-control', 'required': 'true'
            }),
            'direccion': forms.TextInput(attrs={
                'class': 'form-control', 'required': 'true'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control', 'required': 'true'
            }),
        }