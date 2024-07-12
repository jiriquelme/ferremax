from django.urls import path,include
from rest_framework import routers
from api import views
from .views import ProductoView

"""
router = routers.DefaultRouter()
router.register(r'producto',views.ProductoViewSet)
"""

urlpatterns = [
    #path('',include(router.urls))
    path('productos/', ProductoView.as_view(), name="lista_productos"),
    path('productos/<int:id>', ProductoView.as_view(), name="lista_productos_proceso")
]