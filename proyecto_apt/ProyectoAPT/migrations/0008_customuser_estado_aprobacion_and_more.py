# Generated by Django 4.2.7 on 2024-10-31 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoAPT', '0007_alter_customuser_direccion'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='estado_aprobacion',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('aprobado', 'Aprobado'), ('rechazado', 'Rechazado')], default='pendiente', max_length=10),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='num_tel',
            field=models.IntegerField(null=True),
        ),
    ]
