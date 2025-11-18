from django.forms import ModelForm
from .models import Pedido

class PedidoForm(ModelForm):
    class Meta:
        model = Pedido    # ← aquí va en minúsculas
        fields = '__all__'
