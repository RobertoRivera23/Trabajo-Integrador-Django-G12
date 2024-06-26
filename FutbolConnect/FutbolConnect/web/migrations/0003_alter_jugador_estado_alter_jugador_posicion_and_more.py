from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_contacto_jugador_representante_remove_curso_alumnos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugador',
            name='estado',
            field=models.IntegerField(blank=True, choices=[(1, ' '), (2, 'Si'), (3, 'No')], null=True, verbose_name='Pase del club'),
        ),
        migrations.AlterField(
            model_name='jugador',
            name='posicion',
            field=models.IntegerField(blank=True, choices=[(1, ' '), (2, 'Arquero'), (3, 'Defensor Central'), (4, 'Lateral Izquierdo'), (5, 'Lateral Derecho'), (6, 'Mediocampista Central'), (7, 'Mediocampista Izquierdo'), (8, 'Mediocampista Derecho'), (9, 'Delantero')], null=True, verbose_name='Posición Contratada: '),
        ),
        migrations.AlterField(
            model_name='tipocontratos',
            name='posicion_contratado',
            field=models.IntegerField(choices=[(1, ' '), (2, 'Arquero'), (3, 'Defensor Central'), (4, 'Lateral Izquierdo'), (5, 'Lateral Derecho'), (6, 'Mediocampista Central'), (7, 'Mediocampista Izquierdo'), (8, 'Mediocampista Derecho'), (9, 'Delantero')], verbose_name='Posición Contratada '),
        ),
        migrations.AlterField(
            model_name='tipocontratos',
            name='tipo_contrato',
            field=models.IntegerField(choices=[(1, ' '), (2, 'Amateur'), (3, 'Profesional')], verbose_name='Amateur o Profesional'),
        ),
    ]
