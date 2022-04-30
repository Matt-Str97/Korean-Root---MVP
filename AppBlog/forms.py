from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import ImagenCarrusel, Post, ProductoEstrella

class CrearPublicacionForm(forms.ModelForm):

    titulo = forms.CharField(max_length=70)
    subtitulo = forms.CharField(max_length=140)
    cuerpo = forms.CharField(widget=CKEditorWidget())
    fecha_creacion = forms.DateField(widget=forms.widgets.DateInput(attrs={'type':'date'}))
    autor = forms.CharField()
    img_portada = forms.ImageField(required=False)
    img_miniatura = forms.ImageField(required=False)
    fuente = forms.CharField(required=False)
    link_noticia = forms.CharField(required=False)

    class Meta:
        model = Post
        fields = '__all__'

class AgregarCarrusel(forms.ModelForm):

    class Meta:
        model = ImagenCarrusel
        fields = '__all__'


class AgregarProductoEstrella(forms.ModelForm):

    class Meta:
        model = ProductoEstrella
        fields = '__all__'