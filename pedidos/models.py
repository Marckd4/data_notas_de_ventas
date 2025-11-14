from django.db import models

class Pedido(models.Model):
    fecha_solicitud = models.DateField()
    cod_dun = models.CharField(max_length=50)
    cod_ean = models.CharField(max_length=50)
    cod_sistema = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255)

    area_solicitud = models.CharField(max_length=100)
    nombre_solicitante = models.CharField(max_length=100)

    cantidad_solicitada = models.IntegerField()

    status_prioridades = models.CharField(max_length=50)

    cant_enviada_bsf = models.IntegerField(default=0)
    chofer = models.CharField(max_length=100, blank=True, null=True)

    factura_guia = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.descripcion} - {self.cod_sistema}"
