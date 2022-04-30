from pyexpat import model
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from ckeditor.widgets import CKEditorWidget
from .models import Capacitacion

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
        
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class UserEditForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']

class FormacionCreationForm(forms.ModelForm):
    nombre = forms.CharField()
    precio = forms.IntegerField()
    descripcion = forms.CharField(widget=CKEditorWidget())
    fecha_inicio = forms.DateField(widget=forms.widgets.DateInput(attrs={'type':'date'}))
    imagen_miniatura = forms.ImageField()
    imagen_portada = forms.ImageField()
    link_capacitacion = forms.CharField()

    class Meta:
        model = Capacitacion
        fields = '__all__'