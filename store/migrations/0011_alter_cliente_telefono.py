# Generated by Django 4.2.6 on 2023-11-20 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_remove_cliente_dv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='Telefono',
            field=models.CharField(max_length=9, null=True),
        ),
    ]
