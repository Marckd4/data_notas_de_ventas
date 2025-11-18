
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



# resumen 

def resumen_traslado(request):
    pedidos = Pedido.objects.all().values(
        'cod_dun',
        'cod_sistema',
        'descripcion',
        'cant_enviada_bsf',
        'chofer',
        'factura_guia'
    )

    return render(request, 'pedidos/resumen.html', {'pedidos': pedidos})

#exportar excel

from openpyxl import Workbook
from django.http import HttpResponse

def exportar_excel(request):
    # Crear archivo Excel
    wb = Workbook()
    ws = wb.active
    ws.title = "Resumen Traslado"

    # Encabezados
    ws.append([
        "Cod_DUN",
        "Cod_Sistema",
        "Descripción",
        "Cant. Enviada",
        "Chofer",
        "Factura / Guía"
    ])

    # Datos desde DB
    pedidos = Pedido.objects.all()

    for p in pedidos:
        ws.append([
            p.cod_dun,
            p.cod_sistema,
            p.descripcion,
            p.cant_enviada_bsf,
            p.chofer,
            p.factura_guia
        ])

    # Respuesta HTTP para descargar
    response = HttpResponse(
        content_type='application/ms-excel'
    )
    response['Content-Disposition'] = 'attachment; filename="resumen_traslado.xlsx"'

    wb.save(response)
    return response
