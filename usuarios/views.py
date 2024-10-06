from django.shortcuts import render

# Create your views here.
def usuariolist(request):    # Recibimos un objeto de tipo request por parte del cliente
    return render(request, 'usuariolist.html')