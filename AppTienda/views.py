from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import FormacionCreationForm, UserRegisterForm, UserEditForm
from .models import Capacitacion, Operaciones
from django.contrib.admin.views.decorators import staff_member_required

# Creacion de usuario y login
def crearUsuario(request):

      if request.method == 'POST':

            form = UserRegisterForm(request.POST)

            if form.is_valid():
                  form.save()
                  username = form.cleaned_data.get('username')                   
                  messages.success(request, f'Bienvenido {username}! tu cuenta fue creada con exito. Ya podes iniciar sesion')
                  return redirect('login')
      else:           
            form = UserRegisterForm()
      
      return render(request, 'AppTienda/registro_usuario.html', {'form': form})
      
def loginRequest(request):

      if request.method == 'POST':

            form = AuthenticationForm(request, data = request.POST)

            if form.is_valid():

                  data = form.cleaned_data
                  user = authenticate(username = data['username'], password = data['password'])

                  if user is not None:
                        login(request, user)
                        messages.success(request, f'Bienvenido {user.username}!')
                        
                        return redirect('Inicio')
                  else:
                        form = AuthenticationForm()
                        messages.error(request, 'Los datos ingresados no son correctos.')

                        return render(request, 'AppTienda/login.html', {'form': form})
            else:
                  form = AuthenticationForm()
                  messages.error(request, 'Los datos ingresados no son validos.')

                  return render(request, 'AppTienda/login.html', {'form': form})
      else:
            form = AuthenticationForm()
      
      return render(request, 'AppTienda/login.html', {'form': form})

# Capacitaciones
def capacitaciones(request):
    
      cursos_lista = Capacitacion.objects.all()

      return render(request, 'AppTienda/formacion.html', {'cursos_lista': cursos_lista})

def capacitacionDetalle(request,id):

      curso = Capacitacion.objects.get(id=id)

      return render(request, 'AppTienda/formacionDetalle.html', {'curso': curso})

@staff_member_required
def crearCapacitacion(request):

      if request.method == 'POST':

            form = FormacionCreationForm(request.POST, request.FILES)

            if form.is_valid():
                  info = form.cleaned_data
                  nuevaCapacitacion = Capacitacion(nombre=info['nombre'],precio=info['precio'],descripcion=info['descripcion'],fecha_inicio=info['fecha_inicio'],
                  imagen_miniatura=info['imagen_miniatura'],imagen_portada=info['imagen_portada'],link_capacitacion=info['link_capacitacion'])

                  nuevaCapacitacion.save()

                  messages.success(request, 'capacitacion creada con exito!')
                  return redirect('capacitaciones')
      else:
            form = FormacionCreationForm()

      return render(request, 'AppTienda/crearFormacion.html', {'form': form})

@staff_member_required
def eliminarCapacitacion(request,id):
      formacion = Capacitacion.objects.get(id=id)
      formacion.delete()

      messages.success(request, 'Formacion eliminada.')
      return redirect('capacitaciones')

@staff_member_required
def editarCapacitacion(request,id):
      capacitacion = Capacitacion.objects.get(id=id)
      
      if request.method == 'POST':

            form = FormacionCreationForm(request.POST, request.FILES, instance=capacitacion)

            if form.is_valid():

                  capacitacion.save()

                  messages.success(request, 'capacitacion editada con exito!')
                  return redirect('capacitaciones')
      else:
            form = FormacionCreationForm(instance=capacitacion)

      return render(request, 'AppTienda/editarFormacion.html', {'form': form})

# Carrito
@login_required
def agregarProducto(request, id):

      usuario = request.user
      producto = Capacitacion.objects.get(id=id)
      carritoUser = usuario.carrito
      productos = Capacitacion.objects.filter(carrito__usuario_id=usuario.id)
      productosUser = Capacitacion.objects.filter(operaciones__usuario_id=usuario.id)
      if producto not in productos:
            if producto not in productosUser:
                  carritoUser.producto.add(producto)
                  carritoUser.total += producto.precio
                  carritoUser.save()
                  messages.success(request, f'el producto {producto.nombre} fue agregado a su carrito!')
            
                  return redirect('capacitaciones')
            else:
                  messages.error(request, f'Usted ya posee el producto {producto.nombre}')
                  return redirect('capacitaciones')
      else:
            messages.error(request, f'el producto {producto.nombre} ya esta en su carrito')
            
            return redirect('capacitaciones')

@login_required
def verCarrito(request):

      usuario = request.user
      productos = Capacitacion.objects.filter(carrito__usuario_id=usuario.id)
      cantidad = productos.count()

      if cantidad > 0:
            return render(request, 'AppTienda/carrito.html', {'productos': productos, 'total': usuario.carrito.total})
      else:

            return render(request, 'AppTienda/carrito.html')


@login_required
def eliminarProducto(request, id):

      usuario = request.user
      producto = Capacitacion.objects.get(id=id)
      carritoUser = usuario.carrito
      carritoUser.total -= producto.precio
      carritoUser.save()
      carritoUser.producto.remove(producto)

      return redirect('carrito')


@login_required
def comprar(request):

      usuario = request.user
      carritoUser = usuario.carrito
      productos = Capacitacion.objects.filter(carrito__usuario_id=usuario.id)
      
      for item in productos:

            nuevaOperacion = Operaciones(usuario = usuario)
            nuevaOperacion.save()
            nuevaOperacion.producto.add(item)
            carritoUser.total -= item.precio
            carritoUser.save()
            carritoUser.producto.remove(item)

      messages.success(request, f'Felicidades {usuario.username} por tu compra!')
      return redirect('Inicio')

# Perfil del usuario
@login_required
def misCursos(request):

      usuario = request.user
      productos = Capacitacion.objects.filter(operaciones__usuario_id = usuario.id)

      if productos: 
            
            return render(request, 'AppTienda/mis_capacitaciones.html', {'productos': productos})
      else:
            messages.error(request, 'Usted no posee ninguna capacitacion')
            return redirect('Inicio')

@login_required
def editarUsuario(request):

      usuario = request.user

      if request.method == 'POST':
            form = UserEditForm(request.POST)

            if form.is_valid():
                  info = form.cleaned_data

                  usuario.email = info['email']
                  usuario.first_name = info['first_name']
                  usuario.last_name = info['last_name']
                  usuario.password1 = info['password1']
                  usuario.password2 = info['password2']
                  usuario.save()

                  messages.success(request, 'Perfil editado con exito.')
                  return redirect('Inicio')

      else:
            form = UserEditForm(initial={'email': usuario.email,'first_name': usuario.first_name,'last_name': usuario.last_name})
            
      return render(request, 'AppTienda/perfil_usuario.html', {'form': form})

# About us
def acerca(request):

      return render(request, "AppTienda/acerca.html")

