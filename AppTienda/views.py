from django.shortcuts import render

# Create your views here.


def inicio(request):

      return render(request, "AppTienda\\inicio.html")

def formaciones(request):

      return render(request, "AppTienda\\formacion.html")

