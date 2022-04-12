from email.policy import default
from django.db import models


class Post(models.Model):
    titulo = models.CharField(max_length=70)
    subtitulo = models.CharField(max_length=140)
    cuerpo = models.TextField()
    fecha_creacion = models.DateTimeField()
    autor = models.CharField(max_length=50)
    img_portada = models.ImageField(upload_to='portadas_blog', default='portadadefault.jpg')
    img_miniatura = models.ImageField(upload_to='miniaturas_blog', default='miniaturadefault.jpg')

    def __str__(self):

        return f'{self.titulo}'

