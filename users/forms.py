from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CrearUsuario(UserCreationForm):
    email = forms.EmailField()

    class Meta: # Clase que django reconoce en forms y models
        model = User
        fields = ["username", "email", "password1", "password2"] # Agregar los datos que debe registrar
