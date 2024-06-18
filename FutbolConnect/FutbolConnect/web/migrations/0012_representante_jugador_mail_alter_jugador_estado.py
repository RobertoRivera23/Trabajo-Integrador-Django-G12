# Generated by Django 5.0.6 on 2024-06-18 19:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_alter_tipocontratos_tipo_contrato'),
    ]

    operations = [
        migrations.CreateModel(
            name='Representante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellido')),
                ('dni', models.IntegerField(unique=True, verbose_name='DNI')),
                ('cuit', models.IntegerField(unique=True, validators=[django.core.validators.MinValueValidator(11), django.core.validators.MaxValueValidator(11)], verbose_name='CUIT')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='jugador',
            name='mail',
            field=models.EmailField(blank=True, max_length=254, verbose_name='E-mail: '),
        ),
        migrations.AlterField(
            model_name='jugador',
            name='Estado',
            field=models.IntegerField(choices=[(1, 'Si'), (2, 'No')], default=2, unique=True, verbose_name='Pase del club'),
            preserve_default=False,
        ),
    ]