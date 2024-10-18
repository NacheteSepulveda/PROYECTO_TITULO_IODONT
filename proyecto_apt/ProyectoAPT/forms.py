## USER CREATION FORM
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm, PasswordResetForm #importa autenticacion de forms
from .models import * #importa modelos
from django import forms #importa formularios
from typing import Any #Te entrega todo (preguntarle a chatgpt)
from django.utils import timezone
from datetime import datetime, timedelta, time

# Set default values to use:
inicioB = ["",time(9,0),time(9,30), time(10,0), time(10,30), time(11,0), time(11,30), time(12,0), time(12,30), time(13,0), time(13,30), time(14,0), time(14,30), time(15,0), time(15,30), time(16,0), time(16,30)]

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import customuser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = customuser
        fields = ['first_name', 'last_name', 'email', 'rut', 'id_tipo_user', 'password1', 'password2', 'num_tel', 'fecha_nac', 'direccion']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Nombre'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Apellido'})

        self.fields['fecha_nac'] = forms.DateField(
            label="Seleccione su fecha!",
            required=True,
            widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'id_fecha_seleccionada', 'type': 'date', }),

        )
        self.fields['fecha_nac'].widget.attrs.update({'class': 'form-control', 'type':'date'})   

        self.fields['num_tel'].widget.attrs.update({'placeholder': 'Ingrese Numero'})
        self.fields['direccion'].widget.attrs.update({'placeholder': 'Ingrese Su Direccion'})
        self.fields['rut'].widget.attrs.update({'placeholder': 'RUT'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Contraseña'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirmar Contraseña'})


class FichaClinicaForm(forms.ModelForm):
    class Meta:
        model = FichaClinica
        fields = ['nombre_contacto_emergencia', 'telefono_contacto_emergencia', 'fecha_ultima_consulta', 'motivo_consulta', 'sintomas_actuales', 'diagnostico', 'tratamiento_actual', 'proxima_cita']

    def __init__(self, *args, **kwargs):
        super(FichaClinicaForm, self).__init__(*args, **kwargs)
        self.fields['nombre_contacto_emergencia'].widget.attrs.update({'placeholder': 'Persona en caso de emergencia'})

        self.fields['telefono_contacto_emergencia'].widget.attrs.update({'placeholder': 'Contacto de emergencia'})
        self.fields['fecha_ultima_consulta'].widget.attrs.update({'placeholder': 'Apellido'})

        self.fields['fecha_ultima_consulta'] = forms.DateField(
            label="Indique Fecha de la Ultima Consulta",
            required=True,
            widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'id_fecha_seleccionada', 'type': 'date', }),

        )
        self.fields['fecha_ultima_consulta'].widget.attrs.update({'class': 'form-control', 'type':'date'})   

        self.fields['motivo_consulta'].widget.attrs.update({'placeholder': 'Ingrese Motivo'})
        self.fields['sintomas_actuales'].widget.attrs.update({'placeholder': 'Ingrese Sintomas'})
        self.fields['diagnostico'].widget.attrs.update({'placeholder': 'Tratamiento Actual'})

        self.fields['proxima_cita'] = forms.DateField(
            label="Indique su proxima cita",
            required=True,
            widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'id_fecha_seleccionada', 'type': 'date', }),

        )


        

        

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
    class Meta:
         model = horarios
         fields =['tipoTratamiento',
                  'inicio',
                  'fecha_seleccionada',
                  'estudiante']

    def __init__(self, *args: Any, **kwargs):
        super(horariosForm, self).__init__(*args, **kwargs)
        #Add tipo de tratamiento
        self.fields['tipoTratamiento'] = forms.ModelChoiceField(
            queryset=tipoTratamiento.objects.all(),
            empty_label="Seleccione un Tratamiento",
            widget=forms.Select(attrs={'class':'form-control','id':'nombreTratamiento'})
        )
        self.fields['tipoTratamiento'].label = "Tipo de tratamiento"

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

        self.fields['inicio'] = forms.ChoiceField(  #
            label="Hora de inicio:",
            choices=[(inicioB[i], str(inicioB[i])) for i in range(1, len(inicioB))],
            widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_HorIni'}),
            required=False
        )


# forms.py

from django import forms
from .models import Cita

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

        self.fields['inicio'] = forms.ChoiceField(  #
            label="Hora de inicio:",
            choices=[(inicioB[i], str(inicioB[i])) for i in range(1, len(inicioB))],
            widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_HorIni'}),
            required=False
        )
        self.fields['estudiante'].widget.attrs.update({'placeholder': 'Estudiante', 'hidden':True})
        self.fields['paciente'].widget.attrs.update({'placeholder': 'Paciente', 'hidden':True})