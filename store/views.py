from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from . import forms
from . import models
import requests
from datetime import datetime
import json
from api.models import ProductoVista
from django.urls import reverse
import uuid
from transbank.webpay.webpay_plus.transaction import Transaction, WebpayOptions
from transbank.common.integration_type import IntegrationType
import hashlib
from .forms import SignUpForm


# Create your views here.
options = WebpayOptions(
    commerce_code='597055555532',
    api_key='579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C',
    integration_type=IntegrationType.TEST
)

def iniciar_pago(request):
    carrito_items = models.Carrito.objects.all()

    if request.user.is_authenticated:
        total_compra = sum(item.producto.valorCLP * item.cantidad for item in carrito_items) - ((sum(item.producto.valorCLP * item.cantidad for item in carrito_items))*0.20)
    else:
        total_compra = sum(item.producto.valorCLP * item.cantidad for item in carrito_items)
 
    # Generar un buy_order de máximo 26 caracteres
    buy_order = str(uuid.uuid4()).replace('-', '')[:26]
    
    # Generar un session_id más corto y único usando una función de hash
    session_id = hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:61]
    
    return_url = request.build_absolute_uri(reverse('confirmar_pago'))

    transaction = Transaction(options)  # Crear instancia de Transaction con las opciones
    response = transaction.create(
        buy_order=buy_order,
        session_id=session_id,
        amount=total_compra,
        return_url=return_url
    )

    # Imprimir la respuesta de Transbank para verificar el contenido, incluido el token
    print("Respuesta de Transbank:", response)

    # Asegurar que el token esté presente en la respuesta antes de pasar a la plantilla
    if 'token' not in response or not response['token']:
        return render(request, 'error.html', {'message': 'Error al obtener el token de Transbank'})

    return render(request, 'redirect_to_webpay.html', {
        'url': response['url'],
        'token': response['token']
    })

def confirmar_pago(request):
    token = request.GET.get('token_ws')

    transaction = Transaction(options)  # Crear instancia de Transaction con las opciones
    response = transaction.commit(token=token)

    if response['status'] == 'AUTHORIZED':
        # Aquí puedes actualizar el estado del carrito o del pedido
        carrito_items = models.Carrito.objects.all()
        for item in carrito_items:
                producto = item.producto
                producto.stockDisponible -= item.cantidad
                producto.save()

        models.Carrito.objects.all().delete()  # Vaciar el carrito después del pago exitoso

    return render(request, 'resultado_pago.html', {
        'response': response
    })

def obtieneDolar():
    fecha_hoy = datetime.now()
    fecha_formateada = fecha_hoy.strftime("%Y-%m-%d")
    dolar = requests.get(f'https://si3.bcentral.cl/SieteRestWS/SieteRestWS.ashx?user=jos3.riquelme@outlook.com&pass=Benji1998.&firstdate={fecha_formateada}&timeseries=F073.TCO.PRE.Z.D&function=GetSeries').text
    dolar_response = json.loads(dolar)

    valorDolar = float(dolar_response["Series"]["Obs"][0]["value"])
    return valorDolar


def calculaDolar(valorProducto, valorDolar):
    valorDolar_Producto = round(valorProducto / valorDolar,2)
    return valorDolar_Producto

def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(ProductoVista, id=producto_id)
    carrito_item, created = models.Carrito.objects.get_or_create(producto=producto)
    if not created:
        carrito_item.cantidad += 1
    carrito_item.save()
    return redirect('carro')

def eliminar_del_carrito(request, item_id):
    carrito_item = get_object_or_404(models.Carrito, id=item_id)
    carrito_item.delete()
    return redirect('carro')

def home(request):
    if request.method == 'POST':
        form = forms.SubscripcionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if models.SubscripcionSemanal.objects.filter(CorreoSubscipcion=email).exists():
                # Si el correo ya existe, mostrar un mensaje de error
                return render(request, 'index.html', {
                    'form': form,
                    'mensaje_error': 'Este correo ya se encuentra suscrito a nuestro boletín.'
                })
            else:
                # Si el correo no existe, guardarlo en la base de datos
                models.SubscripcionSemanal.objects.create(CorreoSubscipcion=email)
                return render(request, 'index.html', {
                    'form': form,
                    'mensaje': 'Correo suscrito correctamente.'
                })
    else:
        form = forms.SubscripcionForm()   
    return render(request, 'index.html', {'form': form})


def herramientasManuales(request):
    productos = requests.get('http://localhost:8000/api/productos/?segmento=Herramientas+Manuales').json()      
    valorDolar = obtieneDolar()

    for i in productos['productos']:
        i['valorUSD'] = str(calculaDolar(i['valorCLP'],valorDolar))
        i['valorUSD_string'] = i['valorUSD']+" USD"

    return render(request, 'herramientasmanuales.html',{'productos':productos})

def materialesBasicos(request):
    productos = requests.get('http://localhost:8000/api/productos/?segmento=Materiales+Basicos').json()      
    valorDolar = obtieneDolar()

    for i in productos['productos']:
        i['valorUSD'] = str(calculaDolar(i['valorCLP'],valorDolar))
        i['valorUSD_string'] = i['valorUSD']+" USD"

    return render(request, 'materialesbasicos.html',{'productos':productos})    

def equiposSeguridad(request):
    productos = requests.get('http://localhost:8000/api/productos/?segmento=Equipos+de+Seguridad').json()      
    valorDolar = obtieneDolar()

    for i in productos['productos']:
        i['valorUSD'] = str(calculaDolar(i['valorCLP'],valorDolar))
        i['valorUSD_string'] = i['valorUSD']+" USD"

    return render(request, 'equiposseguridad.html',{'productos':productos})      

def fijaciones(request):
    productos = requests.get('http://localhost:8000/api/productos/?segmento=Fijaciones').json()      
    valorDolar = obtieneDolar()

    for i in productos['productos']:
        i['valorUSD'] = str(calculaDolar(i['valorCLP'],valorDolar))
        i['valorUSD_string'] = i['valorUSD']+" USD"

    return render(request, 'fijaciones.html',{'productos':productos})     

def equiposMedicion(request):
    productos = requests.get('http://localhost:8000/api/productos/?segmento=Equipos+de+Medicion').json()      
    valorDolar = obtieneDolar()

    for i in productos['productos']:
        i['valorUSD'] = str(calculaDolar(i['valorCLP'],valorDolar))
        i['valorUSD_string'] = i['valorUSD']+" USD"

    return render(request, 'equiposmedicion.html',{'productos':productos})         

def carro(request):
    carrito_items = models.Carrito.objects.all() 
    carrito_vacio = not carrito_items.exists()

    valorDolar = obtieneDolar()

    subtotal_compra_CLP = sum(item.producto.valorCLP * item.cantidad for item in carrito_items)
    subtotal_compra_CLP_string = "{:,}".format(subtotal_compra_CLP)

    subtotal_compra_USD = calculaDolar(subtotal_compra_CLP,valorDolar)
    subtotal_compra_USD_string = "{:,}".format(subtotal_compra_USD)+" USD"


    for i in carrito_items:
        i.valorUSD = str(calculaDolar(i.producto.valorCLP,valorDolar))
        i.valorUSD_string = i.valorUSD+" USD"

    descuento = 0
    if request.user.is_authenticated:
        descuento = subtotal_compra_CLP * 0.20  

    total_compra_CLP = subtotal_compra_CLP - descuento
    total_compra_CLP_string = "$"+"{:,}".format(total_compra_CLP)
    total_compra_USD = calculaDolar(total_compra_CLP,valorDolar)
    total_compra_USD_string = "{:,}".format(total_compra_USD)+" USD"
    descuento_CLP_string = "$"+"{:,}".format(descuento)
    descuento_USD = calculaDolar(descuento,valorDolar)
    descuento_USD_string = "{:,}".format(descuento_USD)+" USD"

    return render(request, 'carrodecompra.html',
                  {'carrito_items':carrito_items,
                   'carrito_vacio':carrito_vacio,
                   'subtotal_compra_CLP':subtotal_compra_CLP,
                   'subtotal_compra_CLP_string':subtotal_compra_CLP_string,
                   'subtotal_compra_USD':subtotal_compra_USD,
                   'subtotal_compra_USD_string' : subtotal_compra_USD_string,
                   'descuento':descuento,
                   'total_compra_CLP':total_compra_CLP,
                   'total_compra_CLP_string':total_compra_CLP_string,
                   'total_compra_USD':total_compra_USD,
                   'total_compra_USD_string' : total_compra_USD_string,       
                   'descuento_CLP_string':descuento_CLP_string,
                   'descuento_USD_string' : descuento_USD_string,             
                   })

def configuracion(request):
    return render(request, 'config.html')


def notificacion(request):
    return render(request, 'notificaciones.html')


def clientes(request):
    return render(request, 'clientes.html')

def clientes_registro(request):
    if request.method == 'GET':
        return render(request, 'clienteRegistro.html', {
            'form': forms.ClienteForm
        })
    else:
        try:
            form = forms.ClienteForm(request.POST)
            form.save()
            return render(request, 'clienteRegistro.html', {
                'form': forms.ClienteForm,
                'mensajeExito': 'Cliente se ha registrado correctamente'
            })
        except:
            return render(request, 'clienteRegistro.html', {
                'form': forms.ClienteForm,
                'error': 'Cliente ya se encuentra registrado'
            })


def clientes_actualizacion(request, RUT):
    if request.method == 'GET':
        cliente = get_object_or_404(models.Cliente, RUT=RUT)
        form = forms.ClienteForm(instance=cliente)
        return render(request, 'clienteActualizar.html', {
            'cliente': cliente,
            'form': form
        })
    else:
        try:
            cliente = get_object_or_404(models.Cliente, RUT=RUT)
            form = forms.ClienteForm(request.POST, instance=cliente)
            form.save()
            return redirect('clientesListado')
        except:
            return render(request, 'clienteActualizar.html', {
                'cliente': cliente,
                'form': form,
                'error': "Error al actualizar Cliente"
            })


def clientes_listado(request):
    if request.method == 'GET':
        clientes = models.Cliente.objects.all()
        clienteCantidad = clientes.count()
        return render(request, 'clienteListado.html', {
            'clientes': clientes,
            'clienteCantidad': clienteCantidad
        })
    else:
        eliminados = request.POST.getlist('eliminados')
        clientes = models.Cliente.objects.all()
        return render(request, 'clienteListado.html', {'clientes': clientes})

def clientes_eliminados(request):
    eliminados = request.POST.getlist('eliminados')
    for i in eliminados:
        models.Cliente.objects.filter(RUT=i).delete()        
    return redirect('clientesListado')

def inicioSesion(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'login.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o Contraseña incorrecta'
            })
        else:
            login(request, user)
            return redirect('home')


def signout(request):
    previous_page = request.META.get('HTTP_REFERER')
    logout(request)
    return redirect(previous_page  or 'home')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': SignUpForm()})
    else:
        form = SignUpForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password1'],
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    email=form.cleaned_data['email']
                )
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                form.add_error('username', 'Usuario ya existe')
        return render(request, 'signup.html', {'form': form})
