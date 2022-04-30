from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Capacitacion(models.Model):

    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    fecha_inicio = models.DateTimeField()
    imagen_miniatura = models.ImageField(upload_to='miniaturas_capacitaciones', default = 'miniaturacapacitaciondefault.jpg')
    imagen_portada = models.ImageField(upload_to='portadas_capacitaciones', default = 'portadacapacitaciondefault.jpg')
    link_capacitacion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Carrito(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    producto = models.ManyToManyField(Capacitacion)
    total = models.IntegerField()

class Operaciones(models.Model):

    fecha_compra = models.DateField(auto_now=True, auto_now_add=False)
    producto = models.ManyToManyField(Capacitacion)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    