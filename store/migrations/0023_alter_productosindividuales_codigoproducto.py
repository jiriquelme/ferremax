# Generated by Django 5.0.6 on 2024-05-26 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_stock_cantidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productosindividuales',
            name='codigoProducto',
            field=models.CharField(max_length=256),
        ),
    ]