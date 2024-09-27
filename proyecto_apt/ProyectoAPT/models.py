from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

#TipoUsuario
class TipoUsuario(models.Model):
        id= models.CharField(primary_key=True, max_length=3)
        nombre_tipo_usuario = models.CharField(max_length=100)
        descripcion = models.CharField(max_length=100)
        def __str__(self):
            return str(self.nombre_tipo_usuario)
        
        
#MODELO DE USUARIO;
class customuser(AbstractUser):
        id= models.AutoField(primary_key= True)
        rut =  models.CharField(max_length=100, unique=True)
        id_tipo_user = models.ForeignKey(TipoUsuario, on_delete=models.SET_NULL,null=True)

        def rutt(self):
            return str(self.rut)

        def __str__(self):
            return str(self.id)