# Generated by Django 4.2.7 on 2024-10-31 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoAPT', '0008_customuser_estado_aprobacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='num_tel',
            field=models.IntegerField(max_length=9, null=True),
        ),
    ]
