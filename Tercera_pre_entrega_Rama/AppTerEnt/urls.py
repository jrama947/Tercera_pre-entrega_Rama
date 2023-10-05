from django.urls import path
from .views import inicio, destinos, atracciones, actividades, alojamientos, formulario, buscar, mostrar

urlpatterns = [
    path('inicio/', inicio, name = "Inicio"),
    path('destinos/', destinos, name = "Destinos"),
    path('atracciones/', atracciones, name = "Atracciones"),
    path('actividades/', actividades, name = "Actividades"),
    path('alojamientos/', alojamientos, name = "Alojamientos"),
    path('formulario/', formulario, name = "Formulario"),
    path('buscar/', buscar, name = "Buscar"),
    path('mostrar/', mostrar, name = "Mostrar"),

]
