from django.db import models


# Create your models here.

class ProductoVista (models.Model):
    codigoProducto = models.CharField(max_length=255)
    nombreProducto = models.CharField(max_length=255)
    valorCLP = models.IntegerField(null=True)
    valorCLP_string = models.CharField(max_length=255, default= "Nulo")
    marca = models.CharField(max_length=50)
    tipoProducto = models.CharField(max_length=255)
    stockDisponible = models.IntegerField(null=False, default= 0 )
    NombreSegmento = models.CharField(max_length=255, default="Sin Segmento")


