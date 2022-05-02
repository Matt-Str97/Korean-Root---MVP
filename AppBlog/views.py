from django.shortcuts import redirect, render
from .models import ImagenCarrusel, Post, ProductoEstrella
from .forms import AgregarCarrusel, AgregarProductoEstrella, CrearPublicacionForm
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required


def inicio(request):
    
    carrusel = ImagenCarrusel.objects.all()

    carrusel_1 = carrusel[0]
    carrusel_2 = carrusel[1]
    carrusel_3 = carrusel[2]
    carrusel_4 = carrusel[3]
    carrusel_5 = carrusel[4]
    carrusel_6 = carrusel[5]
    carrusel = [carrusel_2, carrusel_3, carrusel_4, carrusel_5, carrusel_6]

    imagenes = ProductoEstrella.objects.all()

    posts = Post.objects.all()

    return render(request, 'AppBlog/inicio.html', {
    'imagenes': imagenes, 
    'publicaciones': posts, 
    'img_carrusel': carrusel, 
    'carrusel_1': carrusel_1,
    'carrusel_2': carrusel_2,
    'carrusel_3': carrusel_3,
    'carrusel_4': carrusel_4,
    'carrusel_5': carrusel_5,
    'carrusel_6': carrusel_6,
    })



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

# Publicaciones del blog
@staff_member_required
def crearPublicacion(request):

    if request.method == 'POST':

        publicacion = CrearPublicacionForm(request.POST, request.FILES)

        if publicacion.is_valid():
                        
            info = publicacion.cleaned_data
            mi_publicacion = Post(titulo = info['titulo'], subtitulo = info['subtitulo'], cuerpo = info['cuerpo'], fecha_creacion = info['fecha_creacion'], autor = info['autor'], 
            img_portada = info['img_portada'], img_miniatura = info['img_miniatura'], fuente = info['fuente'], link_noticia = info['link_noticia'])

            mi_publicacion.save()

            messages.success(request, 'La publicacion fue creada con exito!')
            return redirect('/blog/listablog/')
    
    else:

        form = CrearPublicacionForm()

    return render(request,'AppBlog/nueva_publicacion.html', {'form': form})

@staff_member_required
def eliminarPublicacion(request,id):
    
    publicacion = Post.objects.get(id=id)
    publicacion.delete()

    messages.success(request, 'Se elimino la publicacion.')
    return redirect('/blog/listablog/')

@staff_member_required
def editarPublicacion(request,id):

    post = Post.objects.get(id=id)

    if request.method == 'POST':

        form = CrearPublicacionForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
 
            post.save()

            messages.success(request, 'La publicacion fue editada con exito!')
            return redirect('/blog/listablog/')
    
    else:
        form = CrearPublicacionForm(instance=post)

    return render(request, 'AppBlog/editar_publicacion.html', {'form': form})

# Carrusel de imagenes
@staff_member_required
def agregarCarrusel(request):

    if request.method == 'POST':

        form = AgregarCarrusel(request.POST, request.FILES)

        if form.is_valid():

            info = form.cleaned_data
            mi_carrusel = ImagenCarrusel(titulo = info['titulo'], texto = info['texto'], imagen = info['imagen'])
            mi_carrusel.save()

            messages.success(request, 'Imagen agregada al carrusel!')
            return redirect('/blog/imagenesCarrusel/')
    
    else:
        form = AgregarCarrusel()

    return render(request, 'AppBlog/nuevo_carrusel.html', {'form': form})

@staff_member_required
def imagenesCarrusel(request):

    imagenes = ImagenCarrusel.objects.all()

    if imagenes.count() > 0:
        return render(request, 'AppBlog/imagenes_carrusel.html', {'imagenes': imagenes})
    else:
        messages.error(request, 'No hay imagenes en el carrusel')
        return render(request, 'AppBlog/imagenes_carrusel.html', {'imagenes': imagenes})

@staff_member_required
def editarCarrusel(request,id):

    carrusel = ImagenCarrusel.objects.get(id=id)

    if request.method == 'POST':

        form = AgregarCarrusel(request.POST, request.FILES, instance=carrusel)
        if form.is_valid():

            carrusel.save()

            messages.success (request, 'Se edito el carrusel con exito.')
            return redirect('/blog/imagenesCarrusel/')
    else:
        form = AgregarCarrusel(instance=carrusel)
    
    return render(request, 'AppBlog/editar_carrusel.html', {'form': form})

@staff_member_required
def eliminarCarrusel(request,id):
    imagen = ImagenCarrusel.objects.get(id=id)
    imagen.delete()

    messages.success(request, 'Se elimino la imagen del carrusel')
    return redirect('/blog/imagenesCarrusel/')
    

# Productos estrella
@staff_member_required
def agregarProductoEstrella(request):

    if request.method == 'POST':

        form = AgregarProductoEstrella(request.POST, request.FILES)

        if form.is_valid():

            info = form.cleaned_data
            mi_producto = ProductoEstrella(titulo = info['titulo'], imagen = info['imagen'], descripcion = info['descripcion'])
            mi_producto.save()

            messages.success(request, 'Producto estrella creado con exito!')
            return redirect('/blog/verProdEstrella/')
    
    else:
        form = AgregarProductoEstrella()

    return render(request, 'AppBlog/nuevo_prod_estrella.html', {'form': form})

@staff_member_required
def eliminarProdEstrella(request, id):
    producto = ProductoEstrella.objects.get(id=id)
    producto.delete()

    messages.success(request, 'Se elimino el producto estrella.')
    return redirect('/blog/verProdEstrella/')

@staff_member_required
def verProdEstrella(request):

    productos = ProductoEstrella.objects.all()
    if productos.count() > 0:
        return render(request, 'AppBlog/productos_estrella.html', {'productos': productos})
    else:
        messages.error(request, 'No hay productos estrella')
        return render(request, 'AppBlog/productos_estrella.html')

@staff_member_required
def editarProdEstrella(request, id):

    producto = ProductoEstrella.objects.get(id=id)

    if request.method == 'POST':

        form = AgregarProductoEstrella(request.POST, request.FILES, instance=producto)

        if form.is_valid():

            producto.save()

            messages.success(request, 'Producto editado con exito.')
            return redirect('/blog/verProdEstrella/')
    else:
        form = AgregarProductoEstrella(instance=producto)
    
    return render(request, 'AppBlog/editar_prod_estrella.html', {'form': form})
