from unicodedata import name
from django.urls import path
from .views import agregarCarrusel, agregarProductoEstrella, crearPublicacion, publicacion_detalle, publicaciones


urlpatterns = [
    path('listablog/', publicaciones, name='lista_publicaciones'),
    path('blogPost/<id>', publicacion_detalle, name='publicacion_detalle'),
    path('crearPublicacion/', crearPublicacion, name='crear_publicacion'),
    path('crearCarrusel/', agregarCarrusel, name='agregar_carrusel'),
    path('crearProductoEstrella/', agregarProductoEstrella, name='agregar_prod_estrella')
]
