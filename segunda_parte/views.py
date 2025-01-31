from django.http import Http404, HttpResponse
from django.shortcuts import render

from segunda_parte.forms import PlatoTipicoForm
from .models import PlatoTipico

# Create your views here.

def index(request):
    platotipico = PlatoTipico.objects.all()
    # return HttpResponse(list(platotipico), safe=False)

    return render(
        request,
        'index.html',
        context={'segunda_parte': platotipico}
        
    )
def detalle(request, platotipico_id):
    try:
    
        platostipicos = PlatoTipico.objects.get(id=platotipico_id)

        return render(
            request,
            'detalle.html',
            context={'menu': platostipicos}
        )
    except PlatoTipico.DoesNotExist:
        raise Http404()

def formulario(request):
    form = PlatoTipicoForm()

    return render(
        request,
        'menu_form.html',
        {'form': form}
    )
    
