from django.urls import path
from AppTienda import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('formaciones/', views.formaciones, name="Formaciones"),
    path('registrarse/', views.crearUsuario, name="registro_usuario"),
    path('login/', views.loginRequest, name="login"),
    path('logout/', LogoutView.as_view(template_name = 'AppTienda/logout.html'), name = 'logout'),
]
