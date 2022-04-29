from django.shortcuts import render

# Create your views here.


def inicio(request):

      return render(request, "AppBlog/inicio.html")

def prueba(request):

      return render(request, "AppTienda/padre.html")
