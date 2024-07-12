from django.contrib import admin
from . import models

# Register your models here.
class APIAdmin(admin.ModelAdmin):
    list_display = ('codigoProducto','nombreProducto','valorCLP','marca','tipoProducto','stockDisponible','NombreSegmento')
    search_fields = ('NombreMarca',)

# Registrar los modelos con sus clases de administrador personalizadas
admin.site.register(models.ProductoVista, APIAdmin)

