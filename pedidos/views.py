
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from pedidos.forms import PedidoForm
from .models import Pedido

def index(request):
    try:
        pedidos = Pedido.objects.all()
        return render(request, 'index.html', context={'pedidos': pedidos})

    except Pedido.DoesNotExist:
        raise Http404()


def formulario(request):
    if request.method == 'POST':
        form = PedidoForm( request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/pedidos')
    else:
        form = PedidoForm()
    
    return render(
        request,
        'pedido_form.html',
        {'form': form}
        
        
    )