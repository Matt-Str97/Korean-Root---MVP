from django.urls import path
from AppTienda import views

urlpatterns = [
    path('formaciones/', views.formaciones, name="Formaciones"),
    path('registrarse/', views.crearUsuario, name="registro_usuario"),
]
