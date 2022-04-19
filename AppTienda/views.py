from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .models import Capacitacion, Carrito

def formaciones(request):

      return render(request, "AppTienda/formacion.html")

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


def capacitaciones(request):

      cursos_lista = Capacitacion.objects.all()

      return render(request, 'AppTienda/formacion.html', {'cursos_lista': cursos_lista})

def capacitacionDetalle(request,id):

      curso = Capacitacion.objects.get(id=id)

      return render(request, 'AppTienda/formacionDetalle.html', {'curso': curso})


@login_required
def agregarProducto(request, id):

      usuario = request.user
      producto = Capacitacion.objects.get(id=id)
      carritoUser = usuario.carrito
      productos = Capacitacion.objects.filter(carrito__usuario_id=usuario.id)

      if producto not in productos:
            carritoUser.producto.add(producto)

            messages.success(request, f'el producto {producto.nombre} fue agregado a su carrito!')
      
            return redirect('capacitaciones')
      else:
            messages.error(request, f'el producto {producto.nombre} ya esta en su carrito')
            
            return redirect('capacitaciones')
