# Generated by Django 5.0.6 on 2024-05-27 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0025_remove_stock_tienda_delete_tiendas'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarroCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoProducto', models.CharField(max_length=255)),
                ('nombreProducto', models.CharField(max_length=255)),
                ('valorCLP', models.IntegerField(null=True)),
                ('valorCLP_string', models.CharField(default='Nulo', max_length=255)),
                ('valorUSD', models.IntegerField(null=True)),
                ('valorUSD_string', models.CharField(default='Nulo', max_length=255)),
                ('marca', models.CharField(max_length=50)),
                ('tipoProducto', models.CharField(max_length=255)),
                ('cantidadAComprar', models.IntegerField(default=0)),
                ('NombreSegmento', models.CharField(default='Sin Segmento', max_length=255)),
            ],
        ),
    ]
