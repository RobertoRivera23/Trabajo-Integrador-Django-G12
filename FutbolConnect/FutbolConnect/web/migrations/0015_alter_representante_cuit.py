# Generated by Django 5.0.6 on 2024-06-18 19:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0014_alter_representante_cuit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='representante',
            name='cuit',
            field=models.BigIntegerField(unique=True, validators=[django.core.validators.MinValueValidator(9999999999), django.core.validators.MaxValueValidator(99999999999)], verbose_name='CUIT'),
        ),
    ]