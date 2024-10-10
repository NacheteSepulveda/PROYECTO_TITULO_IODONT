from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .decorators import user_not_authenticated
from django.contrib import messages
from .forms import CustomUserCreationForm, UserLoginForm # USERS LOGIN FORMS
from .forms import horariosForm # HORARIOS CHECK
from .models import *
from django.http import JsonResponse
from datetime import time, timedelta, datetime


def index(request):
    return render(request, 'APT/index.html')


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # messages.success(request, f"New account created: {user.username}")
            return redirect('/')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = CustomUserCreationForm()

    return render(
        request=request,
        template_name="autorizacion/registro.html",
        context={"form": form}
        )

@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('/')

@user_not_authenticated
def loginUser(request):
    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            
            user = authenticate(
                email=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Bienvenido <b>{user.username}</b>! Has iniciado sesiÃ³n")
                return redirect('/')
            else:
                pass
        else:
            for key, error in list(form.errors.items()):          
                messages.error(request, error) 

    form = UserLoginForm()
    return render(
        request=request,
        template_name="autorizacion/login.html",
        context={"form": form}
        )
@login_required
def registroHoras(request):
    form = horariosForm(request.POST or None)
    horarios_disponibles = []  # Inicializa la lista para almacenar los horarios

    if request.method == 'POST' and form.is_valid():
        # Aquí puedes obtener el tratamiento y la fecha seleccionada
        horarios_disponibles = obtener_horarios_disponibles(request)

    context = {
        'form': form,
        'horarios_disponibles': horarios_disponibles,  # Agregamos los horarios disponibles al contexto
    }
    return render(request, 'APT/horarios.html', context)

# Vista para obtener los horarios disponibles para un tratamiento en una fecha específica
def obtener_horarios_disponibles(request):
    if request.method == 'GET':
        tratamiento_id = request.GET.get('tratamiento_id')
        fecha_seleccionada = request.GET.get('fecha_seleccionada')

        # Obtenemos los horarios disponibles para el tratamiento y la fecha seleccionada
        horarios_disponibles = horarios.objects.filter(
            tipoTratamiento_id=tratamiento_id,
            fecha_seleccionada=fecha_seleccionada
        ).values('HoraInicial')

        # Convertimos los horarios en una lista para enviarlos en formato JSON
        horarios_list = list(horarios_disponibles)

        # Devolvemos la respuesta como JSON
        return JsonResponse(horarios_list, safe=False)
@login_required
def tratamientosForm(request, estudianteID):
    form = horariosForm(request.POST or None)

    context = {'form':form,'estudianteID':estudianteID}
    if request.method=='POST':
        form = horariosForm(request.POST)

        if form.is_valid():
            
            form.save()
        else:
            print(form.errors)
    return render(request, 'APT/horariosEstudianteTratamiento.html', context)

def servicios(request):
    return render(request, 'APT/servicios.html')

def calendar_est(request):
    return render(request, 'estudiante/calendario_est.html')

def infoestudiante(request):
    return render(request, 'estudiante/infopersonal.html')

def notifiaciones_est(request):
    return render(request, 'estudiante/notificaciones_estudiante.html')

def pacientes_est(request):
    return render(request, 'estudiante/pacientes_estudiante.html')

def publicacion_est(request):
    return render(request, 'estudiante/publicacion_estudiante.html')