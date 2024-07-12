from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name = 'home'),
    path('herramientas-manuales/',views.herramientasManuales, name = 'herramientasManuales'), 
    path('materiales-basicos/',views.materialesBasicos, name = 'materialesBasicos'), 
    path('equipos-de-seguridad/',views.equiposSeguridad, name = 'equiposSeguridad'), 
    path('fijaciones/',views.fijaciones, name = 'fijaciones'), 
    path('equipos-de-medicion/',views.equiposMedicion, name = 'equiposMedicion'), 
    path('carro/',views.carro, name = 'carro'), 
    path('signup/',views.signup, name = 'signup'),
    path('login/', views.inicioSesion, name = 'inicioSesion'),    
    path('clientes/',views.clientes, name = 'clientes'),
    path('clientes/registro',views.clientes_registro, name = 'clientesRegistro'),
    path('clientes/listado',views.clientes_listado, name = 'clientesListado'),
    path('clientes/user/<str:RUT>',views.clientes_actualizacion, name = 'clientesActualizado' ),
    path('clientes/listado/eliminacion',views.clientes_eliminados, name = 'clientesEliminacion'),
    path('settings/',views.configuracion, name = 'configuracion'),
    path('alerts/',views.notificacion, name = 'notificacion'),
    path('logout/',views.signout, name = 'logout' ),
    path('agregar_al_carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar_del_carrito/<int:item_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('iniciar_pago/', views.iniciar_pago, name='iniciar_pago'),
    path('confirmar_pago/',views.confirmar_pago, name='confirmar_pago')
]