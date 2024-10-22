from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .decorators import user_not_authenticated
from django.contrib import messages
from .forms import CustomUserCreationForm, UserLoginForm # USERS LOGIN FORMS
from .forms import *
from .models import *
from django.http import JsonResponse
from datetime import time, timedelta, datetime
from .models import FichaClinica 
from .models import customuser, Universidad, Tratamiento



def index(request):
    return render(request, 'APT/index.html')


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            rut = form.cleaned_data.get('rut')

            # Verificar si el correo o el RUT ya están registrados
            if customuser.objects.filter(email=email).exists():
                messages.error(request, 'El correo ya está registrado. Por favor, utiliza otro.')
            elif customuser.objects.filter(rut=rut).exists():
                messages.error(request, 'El RUT ya está registrado. Por favor, utiliza otro.')
            else:
                user = form.save()
                login(request, user)
                messages.success(request, '¡Registro Exitoso!')

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

def filtrar_estudiantes(request):
    estudiantes = customuser.objects.filter(id_tipo_user__nombre_tipo_usuario='Estudiante')
    
    query = request.GET.get('q')
    universidad_id = request.GET.get('universidad')
    tratamiento_id = request.GET.get('tratamiento')
    
    if query:
        estudiantes = estudiantes.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query)
        )
    
    if universidad_id:
        estudiantes = estudiantes.filter(universidad_id=universidad_id)
    
    if tratamiento_id:
        estudiantes = estudiantes.filter(tratamientos__id=tratamiento_id)
    
    universidades = Universidad.objects.all()
    tratamientos = Tratamiento.objects.all()

    context = {
        'estudiantes': estudiantes,
        'universidades': universidades,
        'tratamientos': tratamientos,
    }

    return render(request, 'APT/debug_template.html', context)

@login_required
def crear_ficha_paciente(request, user_id):
    try:
        paciente = customuser.objects.get(id=user_id, id_tipo_user__nombre_tipo_usuario='Paciente')
    except customuser.DoesNotExist:
        return redirect('pacientes_est')

    # Verifica si ya existe una ficha clínica para el paciente
    ficha_existente = FichaClinica.objects.filter(paciente=paciente).exists()

    if request.method == 'POST':
        form = FichaClinicaForm(request.POST)
        if form.is_valid():
            if ficha_existente:
                messages.error(request, 'Este paciente ya tiene una ficha clínica registrada.')
            else:
                ficha = form.save(commit=False)
                ficha.paciente = paciente
                ficha.save()
                messages.success(request, '¡Ficha clínica creada con éxito!')
                return redirect('pacientes_est')  # Redirige a la vista de la ficha clínica
        else:
            # Mostrar los errores del formulario si no es válido
            print(form.errors)
            messages.error(request, 'Error en los datos ingresados. Verifica los campos.')
    else:
        form = FichaClinicaForm()

    return render(request, 'estudiante/crear_ficha_clinica.html', {
        'paciente': paciente,
        'form': form,
    })




def ver_ficha_clinica(request):
    # Lógica de la vista aquí
    return render(request, 'estudiante/lista_fichas_clinicas.html')



@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, "Haz Cerrado Sesión!")
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
                messages.success(request, f"Bienvenido {user.email} Has iniciado sesión")

                # Redirige según el tipo de usuario
                if user.id_tipo_user and user.id_tipo_user.nombre_tipo_usuario == "Estudiante":
                    return redirect('infoestudiante')  # Redirige a la vista de estudiante
                elif user.id_tipo_user and user.id_tipo_user.nombre_tipo_usuario == "Paciente":
                    return redirect('index')  # Redirige a la vista de paciente
                else:
                    return redirect('/')  # Redirige a una vista por defecto si no se encuentra el tipo de usuario

            else:
                messages.error(request, "Credenciales inválidas.")
                return redirect('login')
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
    horarios_disponibles = [] 
    query = request.GET.get('q')
    universidad_id = request.GET.get('universidad')
    tratamiento_id = request.GET.get('tratamiento')
    estudiantes = customuser.objects.filter(id_tipo_user__nombre_tipo_usuario='Estudiante')
    if query:
        estudiantes = estudiantes.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query)
        )
    
    if universidad_id:
        estudiantes = estudiantes.filter(universidad_id=universidad_id)
    
    if tratamiento_id:
        estudiantes = estudiantes.filter(tratamientos__id=tratamiento_id)
    
    universidades = Universidad.objects.all()
    tratamientos = tipoTratamiento.objects.all() # Inicializa la lista para almacenar los horarios

    if request.method == 'POST' and form.is_valid():
        # Aquí puedes obtener el tratamiento y la fecha seleccionada
        horarios_disponibles = obtener_horarios_disponibles(request)

    context = {
        'form': form,
        'horarios_disponibles': horarios_disponibles,  # Agregamos los horarios disponibles al contexto
        'universidades': universidades,
        'tratamientos': tratamientos,
        'estudiantes': estudiantes,
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
    form = CitaForm(request.POST or None)

    # Obtiene el estudiante usando el ID proporcionado
    estudiante = get_object_or_404(customuser, id=estudianteID)
    actualUser = request.user.id
    
    context = {'form': form, 'estudianteID': estudianteID, 'actualUser': actualUser, 'estudiante': estudiante,}

    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            # Obtén los datos del formulario
            tipo_tratamiento = form.cleaned_data['tipotratamiento']
            fecha_seleccionada = form.cleaned_data['fecha_seleccionada']
            hora_inicio = form.cleaned_data['inicio']

            # Verifica si ya existe una cita con el mismo estudiante, paciente, tipo de tratamiento, fecha y hora
            cita_existente = Cita.objects.filter(
                estudiante=estudiante,
                paciente=request.user,
                tipotratamiento=tipo_tratamiento,
                fecha_seleccionada=fecha_seleccionada,
                inicio=hora_inicio
            ).exists()

            if cita_existente:
                messages.error(request, 'Ya tienes una cita agendada con este estudiante.')
            else:
                horario = form.save(commit=False)

                # Asigna el paciente actual y el estudiante al horario
                horario.paciente = request.user
                horario.estudiante = estudiante
                horario.save()
                
                messages.success(request, '¡Cita agendada con éxito!')
                return redirect('index')
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
    # Filtramos las citas en las que el estudiante logueado está involucrado
    citas = Cita.objects.filter(estudiante=request.user)
    
    context = {
        'citas': citas,
    }
    return render(request, 'estudiante/notificaciones_estudiante.html', context)

@login_required
def pacientes_est(request):
    estudiante = request.user
    # Filtramos las citas donde el estudiante actual está involucrado
    citas_agendadas = Cita.objects.filter(estudiante=estudiante).values_list('paciente', flat=True)
    # Filtramos los pacientes utilizando los IDs de las citas agendadas
    pacientes = customuser.objects.filter(id__in=citas_agendadas, id_tipo_user__nombre_tipo_usuario='Paciente')
    
    return render(request, 'estudiante/pacientes_estudiante.html', {
        'pacientes': pacientes,
    })


@login_required
def publicacion_est(request):
    return render(request, 'estudiante/publicacion_estudiante.html')


@login_required
def citas_pac(request):
    paciente_id = request.user  # Obtener el usuario logueado
    citas = Cita.objects.filter(paciente=paciente_id)  # Filtrar las citas para el paciente logueado

    return render(request, 'APT/citas.html', {
        'citas': citas  # Pasar las citas al contexto
    })

@login_required
def crear_historial_medico(request, paciente_id):
    paciente = get_object_or_404(customuser, id=paciente_id, id_tipo_user__nombre_tipo_usuario='Paciente')
    
    try:
        # Obtener la cita más reciente del paciente
        cita = Cita.objects.filter(paciente=paciente).latest('fecha_seleccionada')
    except Cita.DoesNotExist:
        messages.error(request, 'No se encontró ninguna cita para este paciente.')
        return redirect('pacientes_est')  # Cambia a la vista que corresponda

    if request.method == 'POST':
        form = HistorialForm(request.POST)
        if form.is_valid():
            historial = form.save(commit=False)
            historial.fecha_seleccionada = cita
            historial.paciente = paciente
            historial.save()
            messages.success(request, '¡Historial médico creado con éxito!')
            return redirect('pacientes_est')  # Redirige a donde desees
    else:
        form = HistorialForm()

    return render(request, 'estudiante/historial_medico.html', {
        'form': form,
        'cita': cita,
        'paciente': paciente,
    })

@login_required
def ver_ficha_clinica(request, paciente_id):
    paciente = get_object_or_404(customuser, id=paciente_id)
    try:
        ficha_clinica = FichaClinica.objects.get(paciente=paciente)
    except FichaClinica.DoesNotExist:
        messages.error(request, 'Este paciente no tiene ficha clínica.')
        return redirect('pacientes_est')

    return render(request, 'estudiante/ver_ficha_clinica.html', {
        'paciente': paciente,
        'ficha_clinica': ficha_clinica,
    })