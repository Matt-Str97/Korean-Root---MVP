from unicodedata import name
from django.urls import path
from .views import publicacion_detalle, publicaciones


urlpatterns = [
    path('listablog/', publicaciones, name='lista_publicaciones'),
    path('blogPost/<id>', publicacion_detalle, name='publicacion_detalle')
]
