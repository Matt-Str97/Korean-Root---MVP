from django.shortcuts import redirect, render
from .models import ImagenCarrusel, Post, ProductoEstrella
from .forms import AgregarCarrusel, AgregarProductoEstrella, CrearPublicacionForm
from django.contrib import messages
# Create your views here.


def publicaciones(request):

    lista_publicaciones = Post.objects.all().order_by('-id')

    if lista_publicaciones.count() > 0:

        return render(request, 'AppBlog/listaPublicaciones.html', {'publicaciones': lista_publicaciones})

    else:
        
        messages.error(request, 'Aún no hay publicaciones en el blog.')
        return render(request, 'AppBlog/listaPublicaciones.html')


def publicacionDetalle(request, id):

    publicacion = Post.objects.get(id=id)

    
    return render(request, 'AppBlog/publicacionDetalle.html',{'titulo': publicacion.titulo,'subtitulo': publicacion.subtitulo, 'cuerpo': publicacion.cuerpo, 
    'fecha_creacion': publicacion.fecha_creacion, 'autor': publicacion.autor, 'img_portada': publicacion.img_portada, 'fuente': publicacion.fuente, 'link_noticia': publicacion.link_noticia})


def crearPublicacion(request):

    if request.method == 'POST':

        publicacion = CrearPublicacionForm(request.POST)

        if publicacion.is_valid():
                        
            info = publicacion.cleaned_data
            mi_publicacion = Post(titulo = info['titulo'], subtitulo = info['subtitulo'], cuerpo = info['cuerpo'], fecha_creacion = info['fecha_creacion'], autor = info['autor'], 
            img_portada = info['img_portada'], img_miniatura = info['img_miniatura'], fuente = info['fuente'], link_noticia = info['link_noticia'])

            mi_publicacion.save()

            messages.success(request, 'La publicacion fue creada con exito!')
            return redirect('lista_publicaciones')
    
    else:

        form = CrearPublicacionForm()

    return render(request,'AppBlog/nueva_publicacion.html', {'form': form})


def eliminarPublicacion(request,id):
    
    publicacion = Post.objects.get(id=id)
    publicacion.delete()

    messages.success(request, 'Se elimino la publicacion.')
    return redirect('lista_publicaciones')


def editarPublicacion(request,id):

    post = Post.objects.get(id=id)

    if request.method == 'POST':

        form = CrearPublicacionForm(request.POST)

        if form.is_valid():
                        
            info = form.cleaned_data
            post.titulo = info['titulo']
            post.subtitulo = info['subtitulo']
            post.cuerpo = info['cuerpo']
            post.fecha_creacion = info['fecha_creacion']
            post.autor = info['autor']
            post.img_portada = info['img_portada']
            post.img_miniatura = info['img_miniatura']
            post.fuente = info['fuente']
            post.link_noticia = info['link_noticia']
            post.save()

            messages.success(request, 'La publicacion fue editada con exito!')
            return redirect('lista_publicaciones')
    
    else:
        form = CrearPublicacionForm(initial= {'titulo': post.titulo, 'subtitulo': post.subtitulo, 'cuerpo': post.cuerpo, 'fecha_creacion': post.fecha_creacion, 'autor': post.autor, 
            'img_portada': post.img_portada, 'img_miniatura': post.img_miniatura, 'fuente': post.fuente, 'link_noticia': post.link_noticia})

    return render(request, 'AppBlog/editar_publicacion.html', {'form': form})


def agregarCarrusel(request):

    if request.method == 'POST':

        form = AgregarCarrusel(request.POST, request.FILES)

        if form.is_valid():

            info = form.cleaned_data
            mi_carrusel = ImagenCarrusel(titulo = info['titulo'], texto = info['texto'], imagen = info['imagen'])
            mi_carrusel.save()

            messages.success(request, 'Imagen agregada al carrusel!')
            return redirect('lista_publicaciones')
    
    else:
        form = AgregarCarrusel()

    return render(request, 'AppBlog/nuevo_carrusel.html', {'form': form})

def agregarProductoEstrella(request):

    if request.method == 'POST':

        form = AgregarProductoEstrella(request.POST, request.FILES)

        if form.is_valid():

            info = form.cleaned_data
            mi_producto = ProductoEstrella(titulo = info['titulo'], imagen = info['imagen'])
            mi_producto.save()

            messages.success(request, 'Producto estrella creado con exito!')
            return redirect('lista_publicaciones')
    
    else:
        form = AgregarProductoEstrella()

    return render(request, 'AppBlog/nuevo_prod_estrella.html', {'form': form})