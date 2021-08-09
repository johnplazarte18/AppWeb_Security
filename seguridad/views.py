from django.shortcuts import render

from .services import get_componentes,get_historial
# Create your views here.
def vwHistorial(request):
    context = {
        'historial': get_historial()
    }
    return render(request, "historial.html",context)

def vwConfiguracion(request):
    context = {
        'component': get_componentes()
    }
    #return render(requests, 'hello_user.html', context)
    return render(request, "configuracion.html",context)