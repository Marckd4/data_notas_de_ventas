
from django.urls import path # es agregada para importar path crearla
from . import views # es agregado  manual 


app_name = 'pedidos'

urlpatterns = [
    path('', views.index, name='index'),
    path('formulario/', views.formulario, name='formulario'),

]
