from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def formaciones(request):

      return render(request, "AppTienda/formacion.html")

def crearUsuario(request):

      if request.method == 'POST':

            form = UserRegisterForm(request.POST)

            if form.is_valid():
                  form.save()
                  username = form.cleaned_data.get('username')                   
                  messages.success(request, f'Bienvenido {username}! tu cuenta fue creada con exito.')
                  return redirect('Inicio')
      else:           
            form = UserRegisterForm()
      
      return render(request, 'AppTienda/registro_usuario.html', {'form': form})
      
