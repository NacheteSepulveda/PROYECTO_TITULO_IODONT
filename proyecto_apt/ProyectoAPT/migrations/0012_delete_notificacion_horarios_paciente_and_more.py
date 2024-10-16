# Generated by Django 4.2.7 on 2024-10-16 02:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoAPT', '0011_rename_id_notificacion_idnoti'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Notificacion',
        ),
        migrations.AddField(
            model_name='horarios',
            name='paciente',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='horarios_paciente_views', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='horarios',
            name='estudiante',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='horarios_estudiante', to=settings.AUTH_USER_MODEL),
        ),
    ]
