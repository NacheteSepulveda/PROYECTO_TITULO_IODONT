from django.db import migrations

def load_comunas(apps, schema_editor):
    Comuna = apps.get_model('ProyectoAPT', 'Comuna')
    comunas_rm = [
        {'id': '13101', 'nombre': 'Santiago'},
        {'id': '13102', 'nombre': 'Cerrillos'},
        {'id': '13103', 'nombre': 'Cerro Navia'},
        {'id': '13104', 'nombre': 'Conchalí'},
        {'id': '13105', 'nombre': 'El Bosque'},
        {'id': '13106', 'nombre': 'Estación Central'},
        {'id': '13107', 'nombre': 'Huechuraba'},
        {'id': '13108', 'nombre': 'Independencia'},
        {'id': '13109', 'nombre': 'La Cisterna'},
        {'id': '13110', 'nombre': 'La Florida'},
        {'id': '13111', 'nombre': 'La Granja'},
        {'id': '13112', 'nombre': 'La Pintana'},
        {'id': '13113', 'nombre': 'La Reina'},
        {'id': '13114', 'nombre': 'Las Condes'},
        {'id': '13115', 'nombre': 'Lo Barnechea'},
        {'id': '13116', 'nombre': 'Lo Espejo'},
        {'id': '13117', 'nombre': 'Lo Prado'},
        {'id': '13118', 'nombre': 'Macul'},
        {'id': '13119', 'nombre': 'Maipú'},
        {'id': '13120', 'nombre': 'Ñuñoa'},
        {'id': '13121', 'nombre': 'Pedro Aguirre Cerda'},
        {'id': '13122', 'nombre': 'Peñalolén'},
        {'id': '13123', 'nombre': 'Providencia'},
        {'id': '13124', 'nombre': 'Pudahuel'},
        {'id': '13125', 'nombre': 'Quilicura'},
        {'id': '13126', 'nombre': 'Quinta Normal'},
        {'id': '13127', 'nombre': 'Recoleta'},
        {'id': '13128', 'nombre': 'Renca'},
        {'id': '13129', 'nombre': 'San Joaquín'},
        {'id': '13130', 'nombre': 'San Miguel'},
        {'id': '13131', 'nombre': 'San Ramón'},
        {'id': '13132', 'nombre': 'Vitacura'},
        {'id': '13201', 'nombre': 'Puente Alto'},
        {'id': '13202', 'nombre': 'Pirque'},
        {'id': '13203', 'nombre': 'San José de Maipo'},
        {'id': '13301', 'nombre': 'Colina'},
        {'id': '13302', 'nombre': 'Lampa'},
        {'id': '13303', 'nombre': 'Tiltil'},
        {'id': '13401', 'nombre': 'San Bernardo'},
        {'id': '13402', 'nombre': 'Buin'},
        {'id': '13403', 'nombre': 'Calera de Tango'},
        {'id': '13404', 'nombre': 'Paine'},
        {'id': '13501', 'nombre': 'Melipilla'},
        {'id': '13502', 'nombre': 'Alhué'},
        {'id': '13503', 'nombre': 'Curacaví'},
        {'id': '13504', 'nombre': 'María Pinto'},
        {'id': '13505', 'nombre': 'San Pedro'},
        {'id': '13601', 'nombre': 'Talagante'},
        {'id': '13602', 'nombre': 'El Monte'},
        {'id': '13603', 'nombre': 'Isla de Maipo'},
        {'id': '13604', 'nombre': 'Padre Hurtado'},
        {'id': '13605', 'nombre': 'Peñaflor'}
    ]
    
    for comuna in comunas_rm:
        Comuna.objects.create(id=comuna['id'], nombreComuna=comuna['nombre'])

def reverse_load_comunas(apps, schema_editor):
    Comuna = apps.get_model('ProyectoAPT', 'Comuna')
    Comuna.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('ProyectoAPT', '0003_alter_comuna_id_alter_customuser_descripcion_and_more'),
    ]

    operations = [
        migrations.RunPython(load_comunas, reverse_load_comunas),
    ] 