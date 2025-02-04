# Generated by Django 5.0.6 on 2024-05-20 14:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_marcas_segmentos_tiendas_tipoproductos_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoInterno', models.CharField(max_length=255)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.productosindividuales')),
                ('tienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.tiendas')),
            ],
        ),
    ]
