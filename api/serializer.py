# serializer.py
from rest_framework import serializers
from .models import ProductoVista

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoVista
        fields = '__all__'  # O lista de campos específicos que quieres serializar
