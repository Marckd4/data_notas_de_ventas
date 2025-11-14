
from django.http import HttpResponse
from django.shortcuts import render
from .models import Pedido

def index(request):
    pedidos = Pedido.objects.all()
    return render(request, 'index.html', context={'pedidos': pedidos})



