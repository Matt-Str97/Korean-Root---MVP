from django import forms
from ckeditor.widgets import CKEditorWidget

class CrearPublicacionForm(forms.Form):

    titulo = forms.CharField(max_length=70)
    subtitulo = forms.CharField(max_length=140)
    cuerpo = forms.CharField(widget=CKEditorWidget())
    fecha_creacion = forms.DateField(help_text='(mm/dd/aaaa) si no se ingresa un valor, se guardará la fecha actual.', required=False)
    autor = forms.CharField()
    img_portada = forms.ImageField(required=False)
    img_miniatura = forms.ImageField(required=False)
    fuente = forms.CharField(required=False)
    link_noticia = forms.CharField(required=False)

class AgregarCarrusel(forms.Form):

    titulo = forms.CharField(max_length=70)
    texto = forms.CharField(max_length=200)
    imagen = forms.ImageField()

class AgregarProductoEstrella(forms.Form):

    titulo = forms.CharField(max_length=50) 
    imagen = forms.ImageField()