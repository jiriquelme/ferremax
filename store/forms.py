from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from . import models
import re
from django.core.exceptions import ValidationError

def validate_no_numbers(value):
    if any(char.isdigit() for char in value):
        raise ValidationError('No se permiten números en este campo.')

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label="Nombre de Usuario",
        widget=forms.TextInput(attrs={'class': 'form-control wide-input', 'placeholder': 'Nombre de Usuario'})
    )
    first_name = forms.CharField(
        label="Nombre", 
        max_length=32, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
        validators=[validate_no_numbers]  # Validación personalizada para no permitir números
    )
    last_name = forms.CharField(
        label="Apellido", 
        max_length=32, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
        validators=[validate_no_numbers]  # Validación personalizada para no permitir números
    )
    email = forms.EmailField(
        label="Correo Electrónico", 
        max_length=64, 
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo Electrónico'})
    )
    password1 = forms.CharField(
        label="Contraseña", 
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'})
    )
    password2 = forms.CharField(
        label="Repita Contraseña", 
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repita Contraseña'})
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def clean(self):
        cleaned_data = super().clean()
        for field in self.fields:
            if not cleaned_data.get(field):
                self.add_error(field, f'{self.fields[field].label} no puede estar vacío.')
        return cleaned_data

class ClienteForm(ModelForm):
    class Meta:
        model = models.Cliente
        fields = ['RUT','Nombre','Apellido','Direccion','Telefono','Correo']




class SubscripcionForm(forms.Form):
    email = forms.EmailField(
        label='Correo Electrónico', 
        widget=forms.EmailInput(attrs={'placeholder': 'Ingresa tu correo electrónico','style':'width: 15rem'}),

    )


