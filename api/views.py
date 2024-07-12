from typing import Any
from django.http import HttpRequest
from rest_framework import viewsets
from .serializer import ProductoSerializer
from .models import ProductoVista
from django.views import View
from django.http.response import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

class ProductoView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            productos = list(ProductoVista.objects.filter(id=id).values())
            if len(productos) > 0:
                producto = productos[0]
                datos = {'message:': "Success", 'producto': producto}
            else:
                datos = {'message': "Producto no encontrado..."}
            return JsonResponse(datos)
        else:
            segmento = request.GET.get('segmento', None)
            if segmento:
                productos = list(ProductoVista.objects.filter(NombreSegmento=segmento).values())
            else:
                productos = list(ProductoVista.objects.values())
            if len(productos) > 0:
                datos = {'message:': "Success", 'productos': productos}
            else:
                datos = {'message': "Productos no encontrados..."}
            return JsonResponse(datos)

    def post(self, request):
        jd = json.loads(request.body)
        ProductoVista.objects.create(
            codigoProducto=jd['codigoProducto'],
            nombreProducto=jd['nombreProducto'],
            valorCLP=jd['valorCLP'],
            marca=jd['marca'],
            tipoProducto=jd['tipoProducto'],
            stockDisponible=jd['stockDisponible'],
            NombreSegmento=jd['NombreSegmento']
        )
        datos = {'message': "Success..."}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        productos = list(ProductoVista.objects.filter(id=id).values())
        if len(productos) > 0:
            producto = ProductoVista.objects.get(id=id)
            producto.codigoProducto = jd['codigoProducto']
            producto.nombreProducto = jd['nombreProducto']
            producto.valorCLP = jd['valorCLP']
            producto.marca = jd['marca']
            producto.tipoProducto = jd['tipoProducto']
            producto.stockDisponible = jd['stockDisponible']
            producto.NombreSegmento = jd['NombreSegmento']
            producto.save()
            datos = {'message': "Success..."}
        else:
            datos = {'message': "Producto no encontrado..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        productos = list(ProductoVista.objects.filter(id=id).values())
        if len(productos) > 0:
            ProductoVista.objects.filter(id=id).delete()
            datos = {'message': "Success..."}
        else:
            datos = {'message': "Producto no encontrado..."}
        return JsonResponse(datos)
