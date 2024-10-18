from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

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
        
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El usuario debe tener un email')
        email = self.normalize_email(email)
        extra_fields.setdefault('username', email.split('@')[0])  # Generar un username a partir del email
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('username', email.split('@')[0])

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True.')

        return self.create_user(email, password, **extra_fields)
        
#MODELO DE USUARIO;
class customuser(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    email = models.EmailField(unique=True)
    rut = models.CharField(max_length=100, unique=True)
    id_tipo_user = models.ForeignKey('TipoUsuario', on_delete=models.SET_NULL, null=True)
    descripcion = models.TextField(null=True)
    imageBlob = models.ImageField(upload_to='imagenes_usuario/', blank=True, null=True)
    fecha_nac = models.DateField(null=True)
    num_tel = models.IntegerField(null=True)
    direccion = models.TextField(null=True)

    USERNAME_FIELD = 'email'  # Usar email para el inicio de sesión
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        if not self.username:  # Generar un username basado en el email
            self.username = self.email.split('@')[0]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email
    
        
class tipoTratamiento(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombreTratamiento= models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return str(self.id)
        

    
class FichaClinica(models.Model):
    idFicha = models.BigAutoField(primary_key=True)
    paciente = models.ForeignKey(customuser, on_delete=models.SET_NULL, null=True, default=None)
    tratamiento = models.ForeignKey(tipoTratamiento, on_delete=models.SET_NULL, null=True, default=None)
    fecha_ultima_consulta = models.DateField(null=True)
    motivo_consulta = models.TextField(null=True)
    sintomas_actuales = models.TextField(null=True)
    diagnostico = models.TextField(null=True)
    tratamiento_actual = models.TextField(null=True)
    proxima_cita = models.DateField(null=True)
    nombre_contacto_emergencia = models.TextField(null=True)
    telefono_contacto_emergencia = models.IntegerField(null=True)

    def __str__(self):
        return str(self.idFicha)




class horarios(models.Model):
    id = models.BigAutoField(primary_key=True)
    tipoTratamiento = models.ForeignKey(tipoTratamiento, on_delete = models.SET_NULL, null=True, default=None)
    inicio = models.TimeField()
    fecha_seleccionada = models.DateField()
    estudiante = models.ForeignKey(customuser, on_delete=models.SET_NULL, null=True, default=None, related_name="horarios_estudiante")
    paciente = models.ForeignKey(customuser, on_delete=models.SET_NULL, null=True, default=None, related_name="horarios_paciente_views")
    ficha_clinica = models.ForeignKey(FichaClinica, on_delete=models.SET_NULL, null=True, blank=True)
    def _str_(self):
         return str(self.id)
    
    def __str__(self):
        return f"Cita con {self.paciente} el {self.fecha_seleccionada} a las {self.inicio}"


    def __str__(self):
        return f"Ficha Clínica de {self.paciente.email} - Última consulta: {self.fecha_ultima_consulta}"

# models.py

class Cita(models.Model):
    paciente = models.ForeignKey(customuser, on_delete=models.CASCADE, related_name='citas_paciente')
    estudiante = models.ForeignKey(customuser, on_delete=models.CASCADE, related_name='citas_estudiante')
    tipotratamiento = models.ForeignKey(tipoTratamiento, on_delete=models.SET_NULL, null=True)
    fecha_seleccionada = models.DateField()
    inicio = models.TimeField()

    def __str__(self):
        return f"Cita de {self.paciente.email} con {self.estudiante.email} para {self.tipotratamiento.nombreTratamiento} el {self.fecha_seleccionada} a las {self.inicio}"

