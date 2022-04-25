from unicodedata import name
from django.urls import path
from .views import agregarCarrusel, agregarProductoEstrella, crearPublicacion, editarPublicacion, eliminarPublicacion, publicacionDetalle, publicaciones, ver_carrusel

app_name = 'blog'

urlpatterns = [
    path('listablog/', publicaciones, name='lista_publicaciones'),
    path('blogPost/<id>', publicacionDetalle, name='publicacion_detalle'),
    path('crearPublicacion/', crearPublicacion, name='crear_publicacion'),
    path('eliminarPublicacion/<id>', eliminarPublicacion, name='eliminar_publicacion'),
    path('editarPublicacion/<id>', editarPublicacion, name='editar_publicacion'),
    path('crearCarrusel/', agregarCarrusel, name='agregar_carrusel'),
    path('verCarrusel/', ver_carrusel, name='agregar_carrusel'),
    path('crearProductoEstrella/', agregarProductoEstrella, name='agregar_prod_estrella')
]
