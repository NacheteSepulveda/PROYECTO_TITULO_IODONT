# Generated by Django 4.2.7 on 2024-11-07 03:41

import ProyectoAPT.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoAPT', '0002_comuna_alter_horarios_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comuna',
            name='id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='fecha_nac',
            field=models.DateField(blank=True, null=True, validators=[ProyectoAPT.models.validar_fecha_nacimiento]),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='num_tel',
            field=models.CharField(max_length=9, null=True, validators=[django.core.validators.MinLengthValidator(9, message='Asegúrate de que el numero tenga al menos 9 digitos'), django.core.validators.RegexValidator(message='Ingresa un número válido de 9 dígitos', regex='^\\d{9}$')]),
        ),
        migrations.AlterModelTable(
            name='comuna',
            table='proyectoapt_comuna',
        ),
    ]
