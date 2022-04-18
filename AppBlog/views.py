from django.shortcuts import render
from .models import ImagenCarrusel, Post
# Create your views here.


def publicaciones(request):

    lista_publicaciones = Post.objects.all().order_by('-id')

    return render(request, 'AppBlog/listaPublicaciones.html', {'publicaciones': lista_publicaciones})


def publicacion_detalle(request, id):

    publicacion = Post.objects.get(id=id)

    
    return render(request, 'AppBlog/publicacionDetalle.html',{'titulo': publicacion.titulo,'subtitulo': publicacion.subtitulo, 'cuerpo': publicacion.cuerpo, 'fecha_creacion': publicacion.fecha_creacion,
     'autor': publicacion.autor, 'img_portada': publicacion.img_portada, 'fuente': publicacion.fuente, 'link_noticia': publicacion.link_noticia})


    