from django.contrib import admin
from .models import *

# Register your models here.



class usuariosAdmin(admin.ModelAdmin):
    # full_name= ('first_name'.join('last_name'))
    list_display = ['id', 'rut', 'getTipoUsuario', 'username', 'getfullname', 'getEmail', 'isSuperAdmin', 'descripcion', 'imageBlob'] #I want to get 'first_name' and last_name togheter
    def getfullname(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    def getTipoUsuario(self, obj):
        return f"{obj.id_tipo_user}"
    def getEmail(self, obj):
        return f"{obj.email}"
    def isSuperAdmin(self, obj):
        return f"{obj.is_superuser}"
    getEmail.short_description = 'E-mail'
    getTipoUsuario.short_description = 'Tipo de usuario'
    getfullname.short_description = 'Nombre del usuario'
    isSuperAdmin.short_description = 'Super admin?'

admin.site.register(customuser,usuariosAdmin)

class TipoUsuarioAdmin(admin.ModelAdmin): #Esto entrega 2 tipos de usuario
    fields = ["nombre_tipo_usuario", "descripcion"]

admin.site.register(TipoUsuario,TipoUsuarioAdmin)

class TipoUsuarioTratamiento(admin.ModelAdmin):
    fields= ['nombreTratamiento', 'descripcion']
admin.site.register(tipoTratamiento,TipoUsuarioTratamiento)

class HorariosAdmin(admin.ModelAdmin):
    fields= ['tipoTratamiento',
             'inicio',
             'fecha_seleccionada',
             'estudiante']
admin.site.register(horarios,HorariosAdmin)

class CitasAdmin(admin.ModelAdmin):
        fields= ['tipotratamiento',
             'inicio',
             'fecha_seleccionada',
             'estudiante']
admin.site.register(Cita,CitasAdmin)