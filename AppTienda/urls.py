from django.urls import path
from AppTienda import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('capacitaciones/', views.capacitaciones, name="capacitaciones"),
    path('capacitacionDetalle/<id>', views.capacitacionDetalle, name="capacitacion_detalle"),
    path('agregarProducto/<id>', views.agregarProducto, name="agregar_producto"),
    path('registrarse/', views.crearUsuario, name="registro_usuario"),
    path('login/', views.loginRequest, name="login"),
    path('logout/', LogoutView.as_view(template_name = 'AppTienda/logout.html'), name = 'logout'),
]
