from django.shortcuts import render
from django.http import JsonResponse


from .services import get_componentes,get_historial,estadoComponente
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
    return render(request, "configuracion.html",context)

def estadoComp(request):
    estado=0
    if request.POST['estado']=='true':
        estado=1

    params = {
    'componente_id': int(request.POST['componente_id']),
    'estado': estado
    }
    
    context = {
        'mensaje': estadoComponente(params)
    }
    return JsonResponse(context)

