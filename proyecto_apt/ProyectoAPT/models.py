from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

#TipoUsuario
class TipoUsuario(models.Model):
        id= models.BigAutoField(primary_key=True)
        nombre_tipo_usuario = models.CharField(max_length=100)
        descripcion = models.CharField(max_length=100)
        def __str__(self):
            return str(self.nombre_tipo_usuario)
        # DICT
        #2.Estudiante
        #1.Paciente
        
        
#MODELO DE USUARIO;
class customuser(AbstractUser):
        id= models.BigAutoField(primary_key= True)
        rut =  models.CharField(max_length=100, unique=True)
        id_tipo_user = models.ForeignKey(TipoUsuario, on_delete=models.SET_NULL,null=True)
        descripcion = models.TextField(null=True)
        imageBlob = models.ImageField(upload_to='imagenes_usuario/', blank=True, null=True)
        def rutt(self):
            return str(self.rut)

        def __str__(self):
            return str(self.id)
        
class tipoTratamiento(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombreTratamiento= models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return str(self.id)
        
class horarios(models.Model):
    id = models.BigAutoField(primary_key=True)
    tipoTratamiento = models.ForeignKey(tipoTratamiento, on_delete = models.SET_NULL, null=True, default=None)
    inicio = models.TimeField()
    fecha_seleccionada = models.DateField()
    estudiante = models.ForeignKey(customuser, on_delete=models.SET_NULL, null=True, default=None)
    def __str__(self):
         return str(self.id)
    
