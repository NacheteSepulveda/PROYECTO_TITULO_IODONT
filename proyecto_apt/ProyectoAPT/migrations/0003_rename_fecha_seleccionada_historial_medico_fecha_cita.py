# Generated by Django 4.2.7 on 2024-10-21 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoAPT', '0002_historial_medico'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historial_medico',
            old_name='fecha_seleccionada',
            new_name='fecha_cita',
        ),
    ]
