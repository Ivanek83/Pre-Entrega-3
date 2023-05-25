from django.urls import path
from . import views

app_name = 'home'


urlpatterns = [
    path('', views.index, name='index'),
    path('Subir-Articulo/', views.subir_articulo, name='subir-articulo'),
    path('Cargar-Autor/', views.cargar_autor, name='cargar-autor'),
    path('Identificar-Medio/', views.identificar_medio , name='identificar-medio'),
    path('Mostrar-Datos/', views.mostrar_datos , name='mostrar-datos'),
]


# Creo este comentario para probar la rama
# Otro TEST