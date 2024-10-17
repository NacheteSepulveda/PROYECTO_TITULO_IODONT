from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .decorators import user_not_authenticated
from django.contrib import messages
from .forms import CustomUserCreationForm, UserLoginForm # USERS LOGIN FORMS
from .forms import horariosForm, CitaForm # HORARIOS CHECK
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
            messages.success(request, "Tu cuenta ha sido creada con éxito.")

            tipo_usuario = TipoUsuario.objects.get(id=user.id_tipo_user_id)


             # Redirigimos según el tipo de usuario
            if tipo_usuario.nombre_tipo_usuario == 'Estudiante':
                return redirect('infoestudiante')  # Redirige a la vista de infoestudiante
            
            elif tipo_usuario.nombre_tipo_usuario == 'Paciente':
                return redirect('index')  # Redirige a la página principal o cualquier otra página
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = CustomUserCreationForm()

    return render(request, "autorizacion/registro.html", {"form": form})


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
                email=form.cleaned_data["username"],  # El campo 'username' se utiliza como email
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Bienvenido <b>{user.email}</b>! Has iniciado sesión")

                # Redirige según el tipo de usuario
                if user.id_tipo_user and user.id_tipo_user.nombre_tipo_usuario == "Estudiante":
                    return redirect('infoestudiante')  # Redirige a la vista de estudiante
                elif user.id_tipo_user and user.id_tipo_user.nombre_tipo_usuario == "Paciente":
                    return redirect('index')  # Redirige a la vista de paciente
                else:
                    return redirect('/')  # Redirige a una vista por defecto si no se encuentra el tipo de usuario

            else:
                messages.error(request, "Credenciales inválidas.")
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
        
        # Obtener solo los horarios del estudiante con id_tipo_user = 2
        estudiante_id = 2  # ID del estudiante

        # Obtenemos los horarios disponibles para el tratamiento, la fecha seleccionada y el estudiante
        horarios_disponibles = horarios.objects.filter(
            tipoTratamiento_id=tratamiento_id,
            fecha_seleccionada=fecha_seleccionada,
            estudiante__id_tipo_user_id=estudiante_id  # Filtrar solo por el estudiante
        ).values('inicio')  # Cambia 'HoraInicial' a 'inicio' según tu modelo

        # Convertimos los horarios en una lista para enviarlos en formato JSON
        horarios_list = list(horarios_disponibles)

        # Devolvemos la respuesta como JSON
        return JsonResponse(horarios_list, safe=False)
    
@login_required 
def tratamientosForm(request, estudianteID):
    # Inicializa el formulario
    form = horariosForm(request.POST or None)
    
    # Obtiene el estudiante usando el ID proporcionado
    estudiante = get_object_or_404(customuser, id=estudianteID)
    
    # Prepara el contexto
    context = {'form': form, 'estudianteID': estudianteID}

    if request.method == 'POST':
        form = horariosForm(request.POST)
        if form.is_valid():
            print("flag 1")
            
            horario = form.save(commit=False)
            print(horario)

            # Asigna el paciente actual y el estudiante
            horario.paciente = request.user
            print(horario.paciente)
            print(request.user)

            horario.estudiante = estudiante  # Asigna el estudiante al horario
            print(horario.estudiante)

            
            horario.save()
            return redirect('index')  # Cambia 'nombre_de_la_vista' a la vista a la que deseas redirigir después de guardar
            
        else:
            print(form.errors)


    return render(request, 'APT/horariosEstudianteTratamiento.html', context)



def publicar_horario(request):
    if request.method == 'POST':
        form = (request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendario')
    else:
        form = horariosForm()
    return render(request, 'publicar_horario.html', {'form': form})


def servicios(request):
    return render(request, 'APT/servicios.html')

@login_required
def calendar_est(request):
    estudiante = request.user  # El estudiante que está logueado
    horarios_disponibles = horarios.objects.filter(estudiante=estudiante)

    if request.method == 'POST':
        form = horariosForm(request.POST)
        if form.is_valid():
            nuevo_horario = form.save(commit=False)
            nuevo_horario.estudiante = estudiante
            nuevo_horario.save()
            return redirect('calendario')  # Redirige para actualizar la página y mostrar el nuevo horario
    else:
        form = horariosForm()

    return render(request, 'estudiante/calendario_est.html', {
        'horarios_disponibles': horarios_disponibles,
        'form': form,
    })

@login_required
def eliminar_horario(request, id):
    horario = get_object_or_404(horarios, id=id)

    if request.method == 'POST':
        horario.delete()  # Elimina el horario de la base de datos
        return redirect('calendario')  # Redirige a la vista de calendario o donde desees

    return render(request, 'estudiante/eliminar_horario.html', {'horario': horario})

@login_required
def infoestudiante(request):
    return render(request, 'estudiante/infopersonal.html', {'user': request.user})

@login_required
def notifiaciones_est(request):
    notificaciones = horarios.objects.filter(estudiante=request.user)
    context ={
        'notificaciones':notificaciones
    }
    return render(request, 'estudiante/notificaciones_estudiante.html', context)

@login_required
def pacientes_est(request):
    return render(request, 'estudiante/pacientes_estudiante.html')


@login_required
def publicacion_est(request):
    return render(request, 'estudiante/publicacion_estudiante.html')


@login_required
def citas_pac(request):
    paciente_id = request.user  # Obtener el usuario logueado
    citas = horarios.objects.filter(paciente=paciente_id)  # Filtrar las citas para el paciente logueado

    return render(request, 'APT/citas.html', {
        'citas': citas  # Pasar las citas al contexto
    })



