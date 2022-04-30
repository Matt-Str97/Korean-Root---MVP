from django.urls import path
from AppTienda import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('capacitaciones/', views.capacitaciones, name="capacitaciones"),
    path('capacitacionDetalle/<id>', views.capacitacionDetalle, name="capacitacion_detalle"),
    path('nuevaCapacitacion/', views.crearCapacitacion, name="nueva_capacitacion"),
    path('eliminarCapacitacion/<id>', views.eliminarCapacitacion, name="eliminar_capacitacion"),
    path('editarCapacitacion/<id>', views.editarCapacitacion, name="editar_capacitacion"),
    path('agregarProducto/<id>', views.agregarProducto, name="agregar_producto"),
    path('eliminarProducto/<id>', views.eliminarProducto, name="eliminar_producto"),
    path('carrito/', views.verCarrito, name="carrito"),
    path('comprar/', views.comprar, name="comprar"),
    path('misCapacitaciones/', views.misCursos, name="mis_capacitaciones"),
    path('registrarse/', views.crearUsuario, name="registro_usuario"),
    path('login/', views.loginRequest, name="login"),
    path('perfil/', views.editarUsuario, name="editar_usuario"),
    path('logout/', LogoutView.as_view(template_name = 'AppTienda/logout.html'), name = 'logout'),
    path('acercaDeNosotros/', views.acerca, name='acerca_de_nosotros'),
]
