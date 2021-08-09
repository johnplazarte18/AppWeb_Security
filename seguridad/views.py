from django.shortcuts import render

from .services import get_componentes
# Create your views here.
def vwHistorial(request):
    return render(request, "historial.html")

def vwConfiguracion(request):
    context = {
        'component': get_componentes()
    }
    #return render(requests, 'hello_user.html', context)
    return render(request, "configuracion.html",context)