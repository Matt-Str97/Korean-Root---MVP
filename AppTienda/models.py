from django.db import models

# Create your models here.


class Capacitacion(models.Model):

    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    fecha_inicio = models.DateField(auto_now=False, auto_now_add=False, null = True, blank = True)
    imagen_miniatura = models.ImageField(upload_to='miniaturas_capacitaciones', default = 'miniaturacapacitaciondefault.jpg')
    imagen_portada = models.ImageField(upload_to='portadas_capacitaciones', default = 'portadacapacitaciondefault.jpg')
    link_capacitacion = models.CharField(max_length=255)


class Carrito(models.Model):

    producto = models.ManyToManyField(Capacitacion)
    total = models.IntegerField()

class Operaciones(models.Model):

    fecha_compra = models.DateField(auto_now=False, auto_now_add=False)
    producto = models.ManyToManyField(Capacitacion)
    