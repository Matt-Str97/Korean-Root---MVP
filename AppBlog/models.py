from email.policy import default
from django.db import models


class Post(models.Model):
    titulo = models.CharField(max_length=70)
    subtitulo = models.CharField(max_length=140)
    cuerpo = models.TextField()
    fecha_creacion = models.DateTimeField()
    autor = models.CharField(max_length=50)
    img_portada = models.ImageField(upload_to='portadas', height_field=None, width_field=None, default='portadadefault.jpg')
    img_miniatura = models.ImageField(upload_to='miniaturas', height_field=None, width_field=None, default='miniaturadefault.jpg')

