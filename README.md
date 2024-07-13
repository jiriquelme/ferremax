## Bienvenido a Ferremax - Tu Ferretería en Línea

### Descripción del Proyecto

Ferremax es una página web de ecommerce dedicada a la venta de productos de ferretería. Está desarrollada utilizando el framework Django con Python y está conectada a una base de datos MySQL para gestionar los productos y pedidos de los clientes.

### Características Principales

- **Framework:** Desarrollado en Django con Python.
- **Base de Datos:** Utiliza MySQL para almacenar y gestionar los datos de productos y pedidos.
- **API Interna:** Alimenta la página web con información directamente desde la base de datos.
- **Conversión de Moneda:** Utiliza la API del Banco Central para convertir el valor del peso chileno a dólares en tiempo real.
- **Pago Seguro:** Implementa la API de Transbank para simular y gestionar los pagos seguros de los productos.

### Requisitos del Sistema

Para utilizar Ferremax, asegúrate de tener instalado:

- Python 3.x
- Django 3.x
- MySQL
- Acceso a Internet para las consultas a las APIs externas.

### Instalación y Configuración

1. Clona el repositorio desde GitHub: `git clone https://github.com/tuusuario/ferremax.git`
2. Crea un entorno virtual y activa el entorno.
3. Instala las dependencias: `pip install -r requirements.txt`
4. Configura tu base de datos MySQL en `settings.py`.
5. Ejecuta las migraciones: `python manage.py migrate`
6. Inicia el servidor: `python manage.py runserver`

### Notas

Se debe establecer apropiadamente en el archivo settings.py la ruta de la base de datos a utilizar, y una vez establecida, ejecutar las migraciones. Esto creará la base de datos de la misma estructura que el proyecto necesita.

¡Gracias por usar Ferremax!
