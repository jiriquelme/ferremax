from django.contrib import admin
from . import models

# Definir clases de administrador personalizadas
class MarcasAdmin(admin.ModelAdmin):
    list_display = ('NombreMarca',)
    search_fields = ('NombreMarca',)

class ProductosIndividualesAdmin(admin.ModelAdmin):
    list_display = ('codigoProducto', 'nombreProducto', 'valorProducto', 'marca', 'tipoProducto')
    search_fields = ('codigoProducto', 'marca')
    list_filter = ('marca', 'tipoProducto')

class SegmentosAdmin(admin.ModelAdmin):
    list_display = ('NombreSegmento',)
    search_fields = ('NombreSegmento',)

class StockAdmin(admin.ModelAdmin):
    list_display = ('codigoInterno', 'producto', 'cantidad')
    search_fields = ('producto',)

class TipoProductosAdmin(admin.ModelAdmin):
    list_display = ('nombreTipoProducto','SegmentoProducto')
    search_fields = ('nombreTipoProducto','SegmentoProducto')

# Registrar los modelos con sus clases de administrador personalizadas
admin.site.register(models.Segmentos, SegmentosAdmin)
admin.site.register(models.Marcas, MarcasAdmin)
admin.site.register(models.TipoProductos, TipoProductosAdmin)
admin.site.register(models.ProductosIndividuales, ProductosIndividualesAdmin)
admin.site.register(models.Stock, StockAdmin)

