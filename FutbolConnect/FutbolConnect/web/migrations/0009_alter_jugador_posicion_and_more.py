# Generated by Django 5.0.6 on 2024-07-02 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_alter_jugador_dni_alter_representante_dni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugador',
            name='posicion',
            field=models.IntegerField(blank=True, choices=[(1, ' '), (2, 'Arquero'), (3, 'Defensor Central'), (4, 'Lateral Izquierdo'), (5, 'Lateral Derecho'), (6, 'Mediocampista Central'), (7, 'Mediocampista Izquierdo'), (8, 'Mediocampista Derecho'), (9, 'Delantero')], null=True, verbose_name='Posición '),
        ),
        migrations.AlterField(
            model_name='tipocontratos',
            name='posicion_contratado',
            field=models.IntegerField(choices=[(1, ' '), (2, 'Arquero'), (3, 'Defensor Central'), (4, 'Lateral Izquierdo'), (5, 'Lateral Derecho'), (6, 'Mediocampista Central'), (7, 'Mediocampista Izquierdo'), (8, 'Mediocampista Derecho'), (9, 'Delantero')], verbose_name='Posición Contratada'),
        ),
        migrations.AlterField(
            model_name='tipocontratos',
            name='tipo_contrato',
            field=models.IntegerField(choices=[(1, 'Amateur'), (2, 'Profesional')], verbose_name='Tipo de contrato'),
        ),
    ]