## USER CREATION FORM
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm, PasswordResetForm #importa autenticacion de forms
from .models import * #importa modelos
from django import forms #importa formularios
from typing import Any #Te entrega todo (preguntarle a chatgpt)
from django.utils import timezone
from datetime import datetime, timedelta, time

# Set default values to use:
inicioB = ["",time(9,0),time(9,30), time(10,0), time(10,30), time(11,0), time(11,30), time(12,0), time(12,30), time(13,0), time(13,30), time(14,0), time(14,30), time(15,0), time(15,30), time(16,0), time(16,30)]

class CustomUserCreationForm(UserCreationForm):

    # Define id_tipo_user correctamente

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        # Add Email field
        self.fields['email'] = forms.EmailField()
        self.fields['email'].label = "Direccion de Email: "
        self.fields['email'].widget.attrs.update({'class': 'form-control'})

        # Add Username field
        self.fields['username'] = forms.CharField()
        self.fields['username'].label = "Nombre de usuario: "
        self.fields['username'].widget.attrs.update({'class': 'form-control'})

        # Add first_name field
        self.fields['first_name'] = forms.CharField()
        self.fields['first_name'].label = "Nombre: "
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})

        # Add last_name field
        self.fields['last_name'] = forms.CharField()
        self.fields['last_name'].label = "Apellido: "
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})

        # Add id_tipo_user field
        self.fields['id_tipo_user'] = forms.ModelChoiceField(
            queryset=TipoUsuario.objects.all(),
            empty_label=None,
            widget=forms.Select(attrs={'class': 'form-control'})  # Establece atributos del widget
        )
        self.fields['id_tipo_user'].label = "Tipo de usuario"

        # Add password1 field
        self.fields['password1'] = forms.CharField(widget=forms.PasswordInput)
        self.fields['password1'].label = "Contraseña: "
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})

        # Add password2 field
        self.fields['password2']   = forms.CharField(widget=forms.PasswordInput)
        self.fields['password2'].label = "Repita la contraseña: "
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})


    class Meta(UserCreationForm.Meta):
            model=customuser
            fields=('email',
            'username', 
            'first_name', 
            'last_name', 
            'id_tipo_user',
            'password1', 
            'password2',
            'rut')



class UserLoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username or Email'}),
        label="Username or Email")

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))
    
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
            empty_label=None,
            widget=forms.Select(attrs={'class':'form-control', 'hidden':True})
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