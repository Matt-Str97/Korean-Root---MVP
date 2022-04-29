from django.urls import path
from .views import agregarCarrusel, agregarProductoEstrella, crearPublicacion, editarCarrusel, editarProdEstrella, editarPublicacion, eliminarCarrusel, eliminarProdEstrella, eliminarPublicacion, imagenesCarrusel, publicacionDetalle, publicaciones, verProdEstrella, inicio

app_name = 'blog'

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('listablog/', publicaciones, name='lista_publicaciones'),
    path('blogPost/<id>', publicacionDetalle, name='publicacion_detalle'),
    path('crearPublicacion/', crearPublicacion, name='crear_publicacion'),
    path('eliminarPublicacion/<id>', eliminarPublicacion, name='eliminar_publicacion'),
    path('editarPublicacion/<id>', editarPublicacion, name='editar_publicacion'),
    path('crearCarrusel/', agregarCarrusel, name='crear_carrusel'),
    path('imagenesCarrusel/', imagenesCarrusel, name='imagenes_carrusel'),
    path('editarCarrusel/<id>', editarCarrusel, name='editar_carrusel'),
    path('eliminarCarrusel/<id>', eliminarCarrusel, name='eliminar_carrusel'),
    path('crearProductoEstrella/', agregarProductoEstrella, name='agregar_prod_estrella'),
    path('eliminarProdEstrella/<id>', eliminarProdEstrella, name='eliminar_prod_estrella'),
    path('editarProdEstrella/<id>', editarProdEstrella, name='editar_prod_estrella'),
    path('verProdEstrella/', verProdEstrella, name='ver_prod_estrella'),
]
