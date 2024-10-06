from django.shortcuts import render
from .models import Usuario

# Create your views here.     # Recibimos un objeto de tipo request por parte del cliente
def usuariolist(request):
    # Creamos una variable get_usuaruio le indicamos que haga la consulta a la clase modelo Usuario
    get_usuarios = Usuario.objects.all()    # Trae toda la data de esta tabla Usuario

    # Creamos una diccionario que represente la data
    data = {
        'get_usuarios': get_usuarios
    }
    
    return render(request, 'usuariolist.html', data)    # con data como parametro pedimos que envie esta data (diccionario a usuariolist.html)