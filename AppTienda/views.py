from django.shortcuts import render


# Create your views here.


def formaciones(request):

      return render(request, "AppTienda\\formacion.html")

def acerca(request):

      return render(request, "AppTienda\\acerca.html")

