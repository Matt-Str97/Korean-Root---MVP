from django.urls import path
from .views import publicaciones


urlpatterns = [
    path('listablog/', publicaciones, name='lista_publicaciones')
]
