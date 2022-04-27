from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import ImagenCarrusel, ProductoEstrella

class CrearPublicacionForm(forms.Form):

    titulo = forms.CharField(max_length=70)
    subtitulo = forms.CharField(max_length=140)
    cuerpo = forms.CharField(widget=CKEditorWidget())
    fecha_creacion = forms.DateField(help_text='Si no se ingresa un valor, se guardará la fecha actual.', required=False, widget=forms.widgets.DateInput(attrs={'type':'date'}))
    autor = forms.CharField()
    img_portada = forms.ImageField(required=False)
    img_miniatura = forms.ImageField(required=False)
    fuente = forms.CharField(required=False)
    link_noticia = forms.CharField(required=False)

class AgregarCarrusel(forms.ModelForm):

    class Meta:
        model = ImagenCarrusel
        fields = ['titulo', 'texto', 'imagen']


class AgregarProductoEstrella(forms.ModelForm):

    class Meta:
        model = ProductoEstrella
        fields = ['titulo', 'imagen']