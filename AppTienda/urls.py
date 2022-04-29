from django.urls import include, path
from AppTienda import views
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


app_name = 'tienda'

urlpatterns = [
    #path('', views.inicio, name="Inicio"), 
    path('formaciones/', views.formaciones, name="Formaciones"),
    path('blog/', include('AppBlog.urls')),
    path('acercaDeNosotros/', views.acerca, name='acerca_de_nosotros'),

]
