from django import forms
from django.forms import ModelForm
from .models import Pelicula
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class PeliculaForm(ModelForm):

    nombre = forms.CharField(min_length=2, max_length=200)
    duracion = forms.IntegerField(min_value=60, max_value=240)

    class Meta:
        model = Pelicula
        fields = ('nombre', 'duracion', 'anio', 'genero', 'fecha_estreno', 'sinopsis', 'imagen')

        widgets = {
            'fecha_estreno':forms.SelectDateWidget(years=range(1945, 2021))
        }

class CustomUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

    
