from django.shortcuts import render
from .models import Post
# Create your views here.


def publicaciones(request):

    lista_publicaciones = Post.objects.all()
    print('--------------------')
    print(lista_publicaciones)

    return render(request, 'AppBlog/listaPublicaciones.html', {'publicaciones': lista_publicaciones})