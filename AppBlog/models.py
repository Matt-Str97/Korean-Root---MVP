from django.db import models
from ckeditor.fields import RichTextField

class Post(models.Model):
    titulo = models.CharField(max_length=70)
    subtitulo = models.CharField(max_length=140)
    cuerpo = RichTextField(blank = True, null = True)
    fecha_creacion = models.DateTimeField()
    autor = models.CharField(max_length=50)
    img_portada = models.ImageField(upload_to='portadas_blog', default='portadadefault.jpg')
    img_miniatura = models.ImageField(upload_to='miniaturas_blog', default='miniaturadefault.jpg')
    fuente = models.CharField(max_length=20, null= True, blank= True)
    link_noticia = models.CharField(max_length=255, null= True, blank= True)

    def __str__(self):
        return f'{self.titulo}'

class ImagenCarrusel(models.Model):
    titulo = models.CharField(max_length=70)
    texto = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='carrusel')

    def __str__(self):
        return f'{self.titulo}'

class ProductoEstrella(models.Model):
    titulo = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='productos_estrella')
    def __str__(self):
        return f'{self.titulo}'