# Generated by Django 5.0.6 on 2024-06-20 21:13

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clausula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clausula', models.CharField(max_length=100, unique=True, verbose_name='Clausula')),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellido')),
                ('dni', models.IntegerField(unique=True, verbose_name='DNI')),
                ('estado', models.IntegerField(blank=True, choices=[(1, 'Si'), (2, 'No')], null=True, unique=True, verbose_name='Pase del club')),
                ('mail', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail: ')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Paises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(max_length=100, unique=True, verbose_name='País')),
                ('ciudad', models.CharField(blank=True, max_length=100, null=True, verbose_name='Ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Posicion_Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posicion', models.CharField(max_length=100, unique=True, verbose_name='Posición')),
            ],
        ),
        migrations.CreateModel(
            name='Representante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellido')),
                ('dni', models.IntegerField(unique=True, verbose_name='DNI')),
                ('cuit', models.BigIntegerField(unique=True, validators=[django.core.validators.MinValueValidator(9999999999), django.core.validators.MaxValueValidator(9999999999)], verbose_name='CUIT')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='inscripcion',
            name='alumno',
        ),
        migrations.RemoveField(
            model_name='curso',
            name='alumnos',
        ),
        migrations.RemoveField(
            model_name='curso',
            name='docente',
        ),
        migrations.RemoveField(
            model_name='inscripcion',
            name='curso',
        ),
        migrations.AlterModelTable(
            name='inscripcion',
            table='inscripcion',
        ),
        migrations.AddField(
            model_name='inscripcion',
            name='jugador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.jugador'),
        ),
        migrations.AddField(
            model_name='inscripcion',
            name='posicion_jugador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.posicion_jugador'),
        ),
        migrations.CreateModel(
            name='TipoContratos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('descripcion', models.CharField(max_length=200, verbose_name='Descripción')),
                ('tipo_contrato', models.IntegerField(choices=[(1, 'Amateur'), (2, 'Profesional')], verbose_name='Amateur o Profesional')),
                ('fecha_inicio', models.DateField(verbose_name='Fecha de inicio')),
                ('fecha_fin', models.DateField(verbose_name='Fecha de finalización')),
                ('clausula', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.clausula')),
            ],
        ),
        migrations.DeleteModel(
            name='Alumno',
        ),
        migrations.DeleteModel(
            name='Docente',
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
    ]
