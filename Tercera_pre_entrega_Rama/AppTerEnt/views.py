from django.shortcuts import render
from .models import Destinos, Actividades, Alojamientos, Atracciones
from AppTerEnt.forms import Formulario, Buscar

# Create your views here.

def inicio(request):
    return render(request, "AppTerEnt/index.html")

def destinos(request):
    return render(request, "AppTerEnt/destinos.html")

def atracciones(request):
    return render(request, "AppTerEnt/atracciones.html")

def actividades(request):
    return render(request, "AppTerEnt/actividades.html")

def alojamientos(request):
    return render(request, "AppTerEnt/alojamientos.html")


def formulario(request):
 
      if request.method == "POST":
 
            miFormulario = Formulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  destino = Destinos(city = request.POST['Destino_Ciudad'], country = request.POST['Destino_Pais'], category = request.POST['Destino_Categoria'], popularity = request.POST['Destino_Popularidad'])
                  actividad = Actividades(name = request.POST['Actividad_Nombre'], difficulty = request.POST['Actividad_Dificultad'], duration = request.POST['Actividad_Duracion'])
                  alojamiento = Alojamientos(name = request.POST['Alojamiento_Nombre'], city = request.POST['Alojamiento_Ciudad'], country = request.POST['Alojamiento_Pais'], adress = request.POST['Alojamiento_Direccion'], stars = request.POST['Alojamiento_Estrellas'])
                  atraccion = Atracciones(name = request.POST['Atraccion_Nombre'], city = request.POST['Atraccion_Ciudad'], category = request.POST['Atraccion_Categoria'])
                  destino.save()
                  actividad.save()
                  alojamiento.save()
                  atraccion.save()

                  return render(request, "AppTerEnt/index.html")
      else:
            miFormulario = Formulario()
 
      return render(request, "AppTerEnt/formulario.html", {"miFormulario": miFormulario})

def buscar(request):
 
      if request.method == "POST":
 
            miFormulario = Buscar(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data

                  destinos = Destinos.objects.filter(city__icontains=informacion["Destino_Ciudad"])

                  return render(request, "AppTerEnt/lista.html", {"destinos": destinos})
      else:
            miFormulario = Buscar()
 
      return render(request, "AppTerEnt/mostrar.html", {"miFormulario": miFormulario})

def mostrar(request):
     pass

