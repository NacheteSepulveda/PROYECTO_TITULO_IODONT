# Generated by Django 4.2.7 on 2024-10-09 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoAPT', '0006_customuser_descripcion_customuser_imageblob'),
    ]

    operations = [
        migrations.RenameField(
            model_name='horarios',
            old_name='HoraInicial',
            new_name='inicio',
        ),
    ]
