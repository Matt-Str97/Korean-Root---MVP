from django.urls import path
from AppTienda import views

urlpatterns = [
    path('', views.inicio, name="Inicio"), 
    path('formaciones/', views.formaciones, name="Formaciones"),

]
