
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

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

# editar formulario 
    
def editar_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)

    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('pedidos:index')  # ← ARREGLADO
    else:
        form = PedidoForm(instance=pedido)

    return render(request, 'pedidos/editar.html', {'form': form})


# eliminar en formulario

def eliminar_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    
    if request.method == 'POST':
        pedido.delete()
        return redirect('pedidos:index')  # ← ESTO ARREGLA EL ERROR

    return render(request, 'pedidos/eliminar.html', {'pedido': pedido})
