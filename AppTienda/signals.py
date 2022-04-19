from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Carrito


@receiver(post_save, sender=User)
def crear_carrito(sender, instance, created, **kwargs):
    if created:
        Carrito.objects.create(usuario=instance, total = 0)