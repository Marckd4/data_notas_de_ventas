
from django.urls import path # es agregada para importar path crearla
from . import views # es agregado  manual 

urlpatterns = [
    path('', views.index, name='index')

]
