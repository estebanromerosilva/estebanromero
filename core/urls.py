from django.urls import path
from .views import home, galeria, listado_pelicula, nueva_pelicula, modificar_pelicula, eliminar_pelicula, registro_usuario

urlpatterns = [
    path('', home, name="home"),
    path('galeria/', galeria, name="galeria"),
    path('listado-peliculas/', listado_pelicula, name="Listado_peliculas"),
    path('nueva-pelicula/', nueva_pelicula, name="nueva_pelicula"),
    path('modificar-pelicula/<id>/', modificar_pelicula, name="modificar_pelicula"),
    path('eliminar-pelicula/<id>/', eliminar_pelicula, name="eliminar_pelicula"),
    path('registro/', registro_usuario, name='registro_usuario'),
]