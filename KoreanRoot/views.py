from django.shortcuts import render

# Create your views here.


def inicio(request):

      return render(request, "AppTienda\\inicio.html")

def prueba(request):

      return render(request, "AppTienda\\padre3.html")
