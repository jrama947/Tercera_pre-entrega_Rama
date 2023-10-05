from django import forms

class Formulario(forms.Form):

        Destino_Ciudad = forms.CharField(max_length=20)
        Destino_Pais =  forms.CharField(max_length=20)
        Destino_Categoria = forms.CharField(max_length=20)
        Destino_Popularidad = forms.IntegerField()
        Actividad_Nombre = forms.CharField(max_length=30)
        Actividad_Dificultad =  forms.CharField(max_length=30)
        Actividad_Duracion = forms.IntegerField()     
        Alojamiento_Nombre = forms.CharField(max_length=30)
        Alojamiento_Ciudad =  forms.CharField(max_length=20)
        Alojamiento_Pais =  forms.CharField(max_length=20)
        Alojamiento_Direccion =  forms.CharField(max_length=20)
        Alojamiento_Estrellas = forms.IntegerField()
        Atraccion_Nombre = forms.CharField(max_length=30)
        Atraccion_Ciudad =  forms.CharField(max_length=20)
        Atraccion_Categoria =  forms.CharField(max_length=20)


class Buscar(forms.Form):
        
        Destino_Ciudad = forms.CharField(max_length=20)

        