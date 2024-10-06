# Importamos la libreria para el httpresponse
from django.http import HttpResponse
from django.shortcuts import render

# Definimos la función
def home(request):
    return render(request, 'home.html')    # Queremos que nos retorne un objeto de tipo response
                             # El objeto http response nos pide un parametro, este parametro es la respuesta que el queremos que el cliente vea