from django.urls import path
from .views import agregarCarrusel, agregarProductoEstrella, crearPublicacion, editarCarrusel, editarPublicacion, eliminarCarrusel, eliminarPublicacion, imagenesCarrusel, publicacionDetalle, publicaciones


urlpatterns = [
    path('listablog/', publicaciones, name='lista_publicaciones'),
    path('blogPost/<id>', publicacionDetalle, name='publicacion_detalle'),
    path('crearPublicacion/', crearPublicacion, name='crear_publicacion'),
    path('eliminarPublicacion/<id>', eliminarPublicacion, name='eliminar_publicacion'),
    path('editarPublicacion/<id>', editarPublicacion, name='editar_publicacion'),
    path('crearCarrusel/', agregarCarrusel, name='crear_carrusel'),
    path('imagenesCarrusel/', imagenesCarrusel, name='imagenes_carrusel'),
    path('editarCarrusel/<id>', editarCarrusel, name='editar_carrusel'),
    path('eliminarCarrusel/<id>', eliminarCarrusel, name='eliminar_carrusel'),
    path('crearProductoEstrella/', agregarProductoEstrella, name='agregar_prod_estrella')
]
