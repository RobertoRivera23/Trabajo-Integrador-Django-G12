# Generated by Django 5.0.6 on 2024-07-02 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_merge_20240630_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugador',
            name='dni',
            field=models.IntegerField(verbose_name='DNI'),
        ),
        migrations.AlterField(
            model_name='representante',
            name='dni',
            field=models.IntegerField(verbose_name='DNI'),
        ),
    ]