from django.db import models
from api.models import ProductoVista

# Create your models here.
class Cliente(models.Model):
    RUT = models.IntegerField(null=True, unique=True)
    Nombre = models.CharField(max_length=255, null=True)
    Apellido = models.CharField(max_length=255, null=True)
    Direccion = models.CharField(max_length=255, null=True)
    Telefono = models.IntegerField(null=True)
    Correo = models.CharField(max_length=255, null=True)

    def __str__(self):
        return  self.RUT + " | " + self.Nombre + " " + self.Apellido

class Segmentos (models.Model):
    NombreSegmento = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Segmentos'
        verbose_name_plural = 'Segmentos'

    def __str__(self):
        return self.NombreSegmento

class TipoProductos (models.Model):
    nombreTipoProducto = models.CharField(max_length=255)
    SegmentoProducto = models.ForeignKey(Segmentos, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'TipoProductos'
        verbose_name_plural = 'TipoProductos'

    def __str__(self):
        return self.nombreTipoProducto


class Marcas (models.Model):
    NombreMarca = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Marcas'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.NombreMarca

class ProductosIndividuales (models.Model):
    codigoProducto = models.CharField(max_length=255, null= False)
    nombreProducto = models.CharField(max_length=255)
    valorProducto = models.IntegerField(null=True)
    marca = models.ForeignKey(Marcas, on_delete=models.CASCADE)
    tipoProducto = models.ForeignKey(TipoProductos, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'ProductosIndividuales'
        verbose_name_plural = 'ProductosIndividuales'

    def __str__(self):
        return self.nombreProducto

class Stock (models.Model):
    codigoInterno = models.CharField(max_length=255)
    producto = models.ForeignKey(ProductosIndividuales, on_delete=models.CASCADE)
    cantidad = models.IntegerField(null=False, default= 0 )

    class Meta:
        verbose_name = 'Stock'
        verbose_name_plural = 'Stock'


class Carrito(models.Model):
    producto = models.ForeignKey(ProductoVista, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'Carrito'
        verbose_name_plural = 'Carrito'  

    def __str__(self):
        return self.producto

class SubscripcionSemanal(models.Model):
    CorreoSubscipcion = models.EmailField(unique=True)
    FechaSubscripcion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'CorreosSuscritos'
        verbose_name_plural = 'CorreosSuscritos'    

    def __str__(self):
        return self.CorreoSubscipcion
