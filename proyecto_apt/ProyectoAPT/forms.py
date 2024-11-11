## USER CREATION FORM
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm, PasswordResetForm #importa autenticacion de forms
from .models import * #importa modelos
from django import forms #importa formularios
from typing import Any #Te entrega todo (preguntarle a chatgpt)
from django.utils import timezone
from datetime import datetime, timedelta, time
from django.core.validators import FileExtensionValidator
from django.conf import settings

# Set default values to use:
inicioB = ["",time(9,0), time(11,0), time(13,0), time(15,0), time(17,00), time(19,00)]
inicioA = ["", str(time(9,0).strftime('%H:%M:%S') + ' - ' + time(10,59).strftime('%H:%M:%S')), 
           str(time(11,0).strftime('%H:%M:%S') + ' - ' + time(12,59).strftime('%H:%M:%S')), 
           str(time(13,0).strftime('%H:%M:%S') + ' - ' + time(14,59).strftime('%H:%M:%S')), 
           str(time(15,0).strftime('%H:%M:%S') + ' - ' + time(16,59).strftime('%H:%M:%S')),
           str(time(17,0).strftime('%H:%M:%S') + ' - ' + time(18,59).strftime('%H:%M:%S'))]



from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import customuser
from captcha.fields import CaptchaField

class CustomUserCreationForm(UserCreationForm):
    captcha = CaptchaField(label='Ingrese el texto de la imagen')
    class Meta:
        model = customuser
        fields = ['first_name', 'last_name', 'email', 'rut', 'id_tipo_user', 'password1', 'password2', 'num_tel', 'fecha_nac', 'direccion', 'comuna', 'universidad', 'Certificado']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Si estamos editando un usuario existente y tiene comuna
        if self.instance and self.instance.comuna:
            # Convertir el campo comuna a un campo de texto de solo lectura
            self.fields['comuna'] = forms.CharField(
                initial=self.instance.comuna.nombreComuna,
                widget=forms.TextInput(attrs={
                    'class': 'form-control',
                    'readonly': True,
                    'id': 'id_comuna'
                })
            )
        else:
            # Si es un nuevo usuario, mantener el select normal
            self.fields['comuna'] = forms.ModelChoiceField(
                queryset=Comuna.objects.all().order_by('nombreComuna'),
                empty_label="Seleccione una comuna",
                required=False,
                widget=forms.Select(attrs={
                    'class': 'form-control',
                    'id': 'id_comuna'
                })
            )

        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Nombre'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Apellido'})

        self.fields['fecha_nac'] = forms.DateField(
            label="Seleccione su fecha!",
            required=True,
            widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'id_fecha_seleccionada', 'type': 'date', }),
        )
        self.fields['fecha_nac'].widget.attrs.update({'class': 'form-control', 'type':'date'})   
        self.fields['num_tel'].widget.attrs.update({'placeholder': 'Ingrese Número - 9 digitos','min':'4'})
        self.fields['direccion'].widget.attrs.update({'placeholder': 'Ingrese Su Direccion'})
        self.fields['rut'].widget.attrs.update({'placeholder': 'RUT'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Contraseña'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirmar Contraseña'})
        self.fields['universidad'].widget.attrs.update({'placeholder': 'Universidad'})
        self.fields['Certificado'].widget.attrs.update({
            'class': 'form-control',
            'accept': '.pdf,application/pdf',
            'placeholder': 'Seleccione un archivo PDF'
        })

    def clean(self):
        cleaned_data = super().clean()
        tipo_usuario = cleaned_data.get('id_tipo_user')
        documento = cleaned_data.get('Certificado')
        comuna = cleaned_data.get('comuna')
        
        # Validación del certificado para estudiantes
        if tipo_usuario and tipo_usuario.id == 2:  # ID para estudiante
            if not documento:
                raise forms.ValidationError(
                    "El documento PDF es obligatorio para estudiantes."
                )
        
        # Validación de comuna para no-staff
        if tipo_usuario and tipo_usuario.id != 1 and not comuna:  # Si no es staff
            self.add_error('comuna', 'Por favor seleccione una comuna')

        return cleaned_data



class FichaClinicaForm(forms.ModelForm):
    class Meta:
        model = FichaClinica
        fields = ['nombre_contacto_emergencia', 'telefono_contacto_emergencia', 'motivo_consulta', 'sintomas_actuales', 'diagnostico', 'tratamiento_actual']

    def __init__(self, *args, **kwargs):
        super(FichaClinicaForm, self).__init__(*args, **kwargs)
        self.fields['nombre_contacto_emergencia'].widget.attrs.update({'placeholder': 'Persona en caso de emergencia'})

        self.fields['telefono_contacto_emergencia'].widget.attrs.update({'placeholder': 'Contacto de emergencia'})   

        self.fields['motivo_consulta'].widget.attrs.update({'placeholder': 'Ingrese Motivo'})
        self.fields['sintomas_actuales'].widget.attrs.update({'placeholder': 'Ingrese Sintomas'})
        self.fields['diagnostico'].widget.attrs.update({'placeholder': 'Ingrese Diagnostico'})


        

        

class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    def clean_username(self):
        email = self.cleaned_data.get('username')
        if not customuser.objects.filter(email=email).exists():
            raise forms.ValidationError("No existe un usuario con este email.")
        return email
    

    
class horariosForm(forms.ModelForm):
    # Generamos los intervalos de 15 minutos para que el usuario elija
    def generar_opciones_horario():
        opciones = []
        hora_actual = time(8, 0)  # Hora de inicio
        while hora_actual <= time(20, 0):  # Hora de fin
            opciones.append((hora_actual.strftime('%H:%M'), hora_actual.strftime('%H:%M')))
            hora_actual = (datetime.combine(date.today(), hora_actual) + timedelta(minutes=60)).time()
        return opciones

    inicio = forms.ChoiceField(
        choices=generar_opciones_horario(),
        label="Hora de Inicio",
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True  # Campo obligatorio
    )
    fin = forms.ChoiceField(
        choices=generar_opciones_horario(),
        label="Hora de Fin",
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True  # Campo obligatorio
    )

    class Meta:
        model = horarios
        fields = ['tipoTratamiento', 'inicio', 'fin']
        widgets = {
            'tipoTratamiento': forms.Select(attrs={
                'class': 'form-control'
            }),
        }

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tipoTratamiento'].label = "Tipo de Tratamiento"
        self.fields['tipoTratamiento'].required = True  # Campo obligatorio

        # Filtrar tratamientos basados en los del perfil del estudiante
        if user and user.tratamientos.exists():
            self.fields['tipoTratamiento'].queryset = user.tratamientos.all()
        else:
            self.fields['tipoTratamiento'].queryset = tipoTratamiento.objects.none()

    def clean(self):
        cleaned_data = super().clean()
        inicio = cleaned_data.get('inicio')
        fin = cleaned_data.get('fin')

        if inicio and fin:
            # Convertir los valores de las horas en objetos de tiempo para la comparación
            hora_inicio = datetime.strptime(inicio, '%H:%M').time()
            hora_fin = datetime.strptime(fin, '%H:%M').time()
            if hora_fin <= hora_inicio:
                self.add_error('fin', 'La hora de fin debe ser posterior a la hora de inicio')
        else:
            if not inicio:
                self.add_error('inicio', 'Este campo es obligatorio')
            if not fin:
                self.add_error('fin', 'Este campo es obligatorio')

        return cleaned_data

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields =[
            'tipotratamiento',
            'inicio',
            'fecha_seleccionada',
            'estudiante',
            'paciente']

    def __init__(self, *args: Any, **kwargs):
        super(CitaForm, self).__init__(*args, **kwargs)
        #Add tipo de tratamiento
        self.fields['tipotratamiento'] = forms.ModelChoiceField(
            queryset=tipoTratamiento.objects.all(),
            empty_label="Seleccione un Tratamiento",
            widget=forms.Select(attrs={'class':'form-control','id':'nombreTratamiento'})
        )
        self.fields['tipotratamiento'].label = "Tipo de tratamiento"

        self.fields['fecha_seleccionada'] = forms.DateField(
            label="Seleccione su fecha!",
            required=True,
            widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'id_fecha_seleccionada', 'type': 'date', }),

        )
        self.fields['fecha_seleccionada'].widget.attrs.update({'class': 'form-control', 'type':'date'})
        idTipoEstudiante = TipoUsuario.objects.filter(nombre_tipo_usuario='Estudiante').first()
        self.fields['estudiante'] = forms.ModelChoiceField(
            queryset=customuser.objects.filter(id_tipo_user=idTipoEstudiante), #Modificable
            empty_label=None,
            widget=forms.Select(attrs={'class':'form-control', 'hidden':True})
        )
        self.fields['estudiante'].label = "Estudiante"
        # Personalizar el label para mostrar el 'first_name'
        self.fields['estudiante'].label_from_instance = lambda obj: f"{obj.first_name} {obj.last_name}"

          # Modificar el campo inicio para aceptar time objects
        self.fields['inicio'] = forms.TimeField(
            label="Hora de inicio:",
            widget=forms.Select(
                attrs={'class': 'form-control', 'id': 'id_HorIni'},
                choices=[(str(time), str(time)) for time in inicioB[1:]]  # Convertir a string
            ),
            required=True
        )
        
        self.fields['estudiante'].widget.attrs.update({'placeholder': 'Estudiante', 'hidden':True})
        self.fields['paciente'].widget.attrs.update({'placeholder': 'Paciente', 'hidden':True})


class HistorialForm(forms.ModelForm):
    class Meta:
         model = Historial_Medico
         fields =['medicamentos',
                  'diagnostico']

    def __init__(self, *args: Any, **kwargs):
        super(HistorialForm, self).__init__(*args, **kwargs)
        self.fields['medicamentos'].widget.attrs.update({'placeholder': 'Ingrese Medicamentos'})
        self.fields['diagnostico'].widget.attrs.update({'placeholder': 'Tratamiento Actual'})



class ModificarPerfil(forms.ModelForm):
    tratamientos = forms.ModelMultipleChoiceField(
        queryset=tipoTratamiento.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = customuser
        fields = ['imageBlob', 'first_name', 'last_name', 'rut', 'fecha_nac', 'universidad', 'email', 'descripcion', 'num_tel', 'direccion', 'comuna', 'tratamientos']

    def __init__(self, *args, **kwargs):
        super(ModificarPerfil, self).__init__(*args, **kwargs)
        
        # Si existe una instancia y tiene comuna
        if self.instance and self.instance.comuna:
            comuna_actual = self.instance.comuna
            # Convertir el campo comuna a un campo de texto de solo lectura
            self.fields['comuna'] = forms.CharField(
                initial=comuna_actual.nombreComuna,
                widget=forms.TextInput(attrs={
                    'class': 'form-control',
                    'readonly': True,
                    'id': 'id_comuna',
                })
            )
            # Forzar el valor mostrado
            self.initial['comuna'] = comuna_actual.nombreComuna
        
        # Si existe una instancia (el usuario), asigna el nombre de la universidad
        if self.instance:
            if self.instance.universidad:
                self.fields['universidad'].initial = self.instance.universidad.nombre

        # Configuración de otros campos
        self.fields['imageBlob'].widget.attrs.update({'placeholder': 'Subir imagen'})
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Ingrese su nombre', 'readonly': True})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Ingrese Apellido', 'readonly': True})
        self.fields['rut'].widget.attrs.update({'placeholder': 'Ingrese Rut', 'readonly': True})
        self.fields['fecha_nac'].widget.attrs.update({'placeholder': 'Ingrese su fecha de nacimiento', 'readonly': True})
        self.fields['email'].widget.attrs.update({'placeholder': 'Ingrese su correo electrónico', 'readonly': True})
        self.fields['num_tel'].widget.attrs.update({'placeholder': 'Ingrese su número de teléfono'})
        self.fields['descripcion'].widget.attrs.update({'placeholder': 'Descripción (Se enviará al paciente)'})
        self.fields['direccion'].widget.attrs.update({'placeholder': 'Ingrese su dirección'})

        # Configurar campos de solo lectura para universidad
        self.fields['universidad'].widget.attrs.update({'readonly': True})
        self.fields['tratamientos'].widget.attrs.update({'class': 'form-check-input tratamientos-checkbox'})

    def clean(self):
        cleaned_data = super().clean()
        # Mantener el objeto Comuna original
        if self.instance and self.instance.comuna:
            cleaned_data['comuna'] = self.instance.comuna
        return cleaned_data
        


