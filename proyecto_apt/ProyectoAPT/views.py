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
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import Http404
from django.db.models import Q
from django.core.mail import send_mail
from django.http import HttpResponseForbidden
from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os
from django.conf import settings
from reportlab.lib.utils import ImageReader



def index(request):
    return render(request, 'APT/index.html')

def register_user(request):
        # Configurar los detalles del correo
        subject = "Bienvenido a IODONT" #USAR

        # Mensaje en HTML con estilos inline #USAR
        html_message = """
        <div style="font-family: Arial, sans-serif; color: #333;">
                <h3 style="color: #007BFF;">Bienvenido a IODONT</h3>
                <p>
                    IODONT es una plataforma orientada a los estudiantes de odontología de diversas instituciones, 
                    con la finalidad de que estos puedan acercarse a sus pacientes sin la necesidad de recurrir a un 
                    método externo. Una buena oportunidad para estos jóvenes!
                </p>
                <h6 style="color: #dc3545;">Si has recibido este enlace por error o te han llegado múltiples notificaciones no deseadas,
                    por favor ignora este mensaje o bloquea al remitente. Gracias.</h6>
            </div>
            """

        from_email = settings.EMAIL_HOST_USER
        recipient_list = [request.user.email] #USAR

        # Enviar el correo con el mensaje HTML #USAR
        send_mail(
                subject,
                "",
                from_email,
                recipient_list,
                fail_silently=False,
                html_message=html_message  # Aquí se incluye el mensaje HTML
            )


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            rut = form.cleaned_data.get('rut')
            
            # Obtener dominio del correo para asociar la universidad
            dominio = email.split('@')[1]
            universidad = None

            # Verificar si el correo o el RUT ya están registrados
            if customuser.objects.filter(email=email).exists():
                messages.error(request, 'El correo ya está registrado. Por favor, utiliza otro.')
            elif customuser.objects.filter(rut=rut).exists():
                messages.error(request, 'El RUT ya está registrado. Por favor, utiliza otro.')
            else:
                # Asignar la universidad automáticamente en función del dominio
                if "uch.cl" in dominio:
                    universidad = get_object_or_404(Universidad, nombre="Universidad de Chile")
                user = form.save(commit=False)
                user.universidad = universidad  # Asignar el objeto de universidad antes de guardar el usuario
                user.estado_aprobacion = 'pendiente'  # Asignar el estado inicial como "pendiente"
                
                # Si es estudiante, verificar que se haya subido el certificado
                tipo_usuario = TipoUsuario.objects.get(id=form.cleaned_data['id_tipo_user'].id)
                if tipo_usuario.nombre_tipo_usuario == 'Estudiante':
                    if 'Certificado' not in request.FILES:
                        messages.error(request, 'Debe subir un certificado PDF para registrarse como estudiante.')
                        return render(request, "autorizacion/registro.html", {"form": form})
                    user.Certificado = request.FILES['Certificado']
                
                user.save()  # Guardar el usuario sin iniciar sesión

                # Informar al usuario que la cuenta está pendiente de aprobación
                messages.success(request, 'Tu cuenta ha sido creada y está pendiente de aprobación. Recibirás una notificación cuando sea revisada.')
                return redirect('index')  # Redirigir al usuario a la página principal
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    else:
        form = CustomUserCreationForm()

    return render(request, "autorizacion/registro.html", {"form": form})


# Vista para el administrador: lista de estudiantes pendientes
def revisar_estudiantes(request):
    estudiantes_pendientes = customuser.objects.filter(estado_aprobacion='pendiente', id_tipo_user__nombre_tipo_usuario='Estudiante')
    return render(request, 'autorizacion/revisar_estudiantes.html', {'estudiantes_pendientes': estudiantes_pendientes})


def vista_para_estudiantes_aprobados(request):
    if request.user.estado_aprobacion != 'aprobado':
        return HttpResponseForbidden("Su cuenta aún no ha sido aprobada.")
    # Lógica para estudiantes aprobados



@login_required
def actualizar_estado_estudiante(request, estudiante_id, estado):
    estudiante = get_object_or_404(customuser, id=estudiante_id)
    
    if estado == 'aprobado':
        estudiante.estado_aprobacion = 'aprobado'
        mensaje = 'Tu cuenta ha sido aprobada. Utiliza tu correo registrado para iniciar sesión y configura tu contraseña.'

        # Enviar correo de aprobación
        send_mail(
            'Tu cuenta ha sido aprobada',
            mensaje,
            settings.EMAIL_HOST_USER,
            [estudiante.email],
            fail_silently=False,
        )
        messages.success(request, f"El estudiante {estudiante.email} ha sido aprobado y se ha enviado un correo.")
    elif estado == 'rechazado':
        estudiante.estado_aprobacion = 'rechazado'
        mensaje = 'Tu solicitud ha sido rechazada debido a inconsistencias en los datos.'

        # Enviar correo de rechazo
        send_mail(
            'Tu solicitud ha sido rechazada',
            mensaje,
            settings.EMAIL_HOST_USER,
            [estudiante.email],
            fail_silently=False,
        )
        messages.warning(request, f"El estudiante {estudiante.email} ha sido rechazado y se ha enviado un correo.")
    
    estudiante.save()
    return redirect('revisar_estudiantes')




def obtener_direccion_universidad(request):
    universidad_id = request.GET.get('universidad_id')
    if universidad_id:
        universidad = Universidad.objects.filter(id=universidad_id).first()
        if universidad:
            return JsonResponse({'direccion': universidad.direccion})
    return JsonResponse({'direccion': ''})  # Devuelve vacío si no se encuentra la universidad


def filtrar_estudiantes(request):
    estudiantes = customuser.objects.filter(id_tipo_user__nombre_tipo_usuario='Estudiante')
    
    query = request.GET.get('q')
    universidad_id = request.GET.get('universidad')
    tratamiento_id = request.GET.get('tratamiento')
    
    print(f"Tratamiento seleccionado: {tratamiento_id}")
    
    if query:
        estudiantes = estudiantes.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query)
        )
    
    if universidad_id:
        estudiantes = estudiantes.filter(universidad_id=universidad_id)
    
    if tratamiento_id:
        estudiantes = estudiantes.filter(
            horarios_estudiante__tipoTratamiento_id=tratamiento_id,
            horarios_estudiante__fecha_seleccionada__gte=datetime.now().date()
        ).distinct()
    
    universidades = Universidad.objects.all()
    tratamientos = tipoTratamiento.objects.all()
    

    context = {
        'estudiantes': estudiantes,
        'universidades': universidades,
        'tratamientos': tratamientos,

    }
    return render(request, 'APT/horarios.html', context)

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

    context = {
        'paciente': paciente,
        'form': form,
        'fecha_nacimiento': spanish_date(paciente.fecha_nac),
    }
    return render(request, 'estudiante/crear_ficha_clinica.html', context)




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
                # Verificar el estado de aprobación
                if user.estado_aprobacion == 'aprobado':
                    login(request, user)
                    messages.success(request, f"Bienvenido {user.email}. Has iniciado sesión")

                    # Redirigir según el tipo de usuario
                    if user.id_tipo_user and user.id_tipo_user.nombre_tipo_usuario == "Estudiante":
                        return redirect('infoestudiante')  # Vista de estudiante
                    elif user.id_tipo_user and user.id_tipo_user.nombre_tipo_usuario == "Paciente":
                        return redirect('index')  # Vista de paciente
                    else:
                        return redirect('/')  # Vista por defecto
                elif user.estado_aprobacion == 'pendiente':
                    messages.error(request, "Tu cuenta está pendiente de aprobación. Esto se realizará dentro de 24 horas.")
                else:
                    messages.error(request, "Tu solicitud fue rechazada. Contacta con soporte para más detalles.")
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



def custom_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Si el usuario es estudiante y no está aprobado, impedir el inicio de sesión y mostrar mensaje
                if user.id_tipo_user.nombre_tipo_usuario == 'Estudiante' and user.estado_aprobacion != 'aprobado':
                    if user.estado_aprobacion == 'pendiente':
                        messages.error(request, 'Tu cuenta está pendiente de aprobación. No puedes iniciar sesión hasta que sea aprobada.')
                    elif user.estado_aprobacion == 'rechazado':
                        messages.error(request, 'Tu solicitud ha sido rechazada. No puedes acceder a la plataforma.')
                    return redirect('login')  # Redirigir de vuelta al inicio de sesión
                login(request, user)  # Permitir el inicio de sesión si es aprobado o es un tipo de usuario diferente
                return redirect('index')  # Redirigir al inicio
            else:
                messages.error(request, 'Usuario o contraseña incorrectos')
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})



@login_required
def registroHoras(request):
    form = horariosForm(request.POST or None, user=request.user)  # Aquí se pasa el usuario actual
    horarios_disponibles = [] 
    query = request.GET.get('q')
    universidad_id = request.GET.get('universidad')
    tratamiento_id = request.GET.get('tratamiento')
    estudiantes = customuser.objects.filter(id_tipo_user__nombre_tipo_usuario='Estudiante')
    
    if query:
        estudiantes = estudiantes.filter(
            Q(first_name_icontains=query) | Q(last_name_icontains=query)
        )
    
    if universidad_id:
        estudiantes = estudiantes.filter(universidad_id=universidad_id)
    
    if tratamiento_id:
        estudiantes = estudiantes.filter(horarios_estudiante__tipoTratamiento_id=tratamiento_id).distinct()
    
    universidades = Universidad.objects.all()
    tratamientos = tipoTratamiento.objects.all()

    if request.method == 'POST' and form.is_valid():
        horarios_disponibles = obtener_horarios_disponibles(request)

    context = {
        'form': form,
        'horarios_disponibles': horarios_disponibles,
        'universidades': universidades,
        'tratamientos': tratamientos,
        'universidad_seleccionada': universidad_id,
        'tratamiento_seleccionado': tratamiento_id,
        'estudiantes': estudiantes,
    }
    
    return render(request, 'APT/horarios.html', context)
#eliminar paciente
@login_required
def eliminar_paciente(request, paciente_id):
    # Obtener el paciente y todas sus citas asociadas con el estudiante actual
    paciente = get_object_or_404(customuser, id=paciente_id)
    citas = Cita.objects.filter(paciente=paciente, estudiante=request.user)
    
    if request.method == 'POST':
        # Eliminar todas las citas asociadas
        citas.delete()
        messages.success(request, f'El paciente {paciente.first_name} {paciente.last_name} ha sido eliminado de tu lista.')
        return redirect('pacientes_est')
        
    return render(request, 'estudiante/eliminar_paciente.html', {
        'paciente': paciente
    })

# Vista para obtener los horarios disponibles para un tratamiento en una fecha específica
def obtener_horarios_disponibles(request):
    if request.method == 'GET':
        tratamiento_id = request.GET.get('tratamiento_id')
        fecha_seleccionada = request.GET.get('fecha_seleccionada')
        estudiante_id = request.GET.get('estudiante_id')

        idEstudianteTipo = TipoUsuario.objects.filter(nombre_tipo_usuario='Estudiante').first()

        # Consulta base para horarios disponibles
        query = horarios.objects.filter(
            tipoTratamiento_id=tratamiento_id,
            estudiante__id_tipo_user_id=idEstudianteTipo,
            estudiante_id=estudiante_id
        )

        # Obtener las citas ya reservadas para esta fecha y estudiante
        citas_reservadas = Cita.objects.filter(
            estudiante_id=estudiante_id,
            fecha_seleccionada=fecha_seleccionada
        ).values_list('inicio', flat=True)

        # Si se proporciona una fecha específica
        if fecha_seleccionada:
            query = query.filter(fecha_seleccionada=fecha_seleccionada)
            horarios_disponibles = query.values('inicio')
            
            # Crear lista con información de disponibilidad
            horarios_list = []
            for horario in horarios_disponibles:
                horarios_list.append({
                    'inicio': horario['inicio'],
                    'reservado': horario['inicio'] in citas_reservadas
                })
        else:
            # Si no hay fecha específica, obtener todas las fechas
            horarios_disponibles = query.values('fecha_seleccionada', 'inicio').distinct()
            horarios_list = list(horarios_disponibles)

        print('Horarios disponibles:', horarios_list)
        return JsonResponse(horarios_list, safe=False)
    
@login_required
def tratamientosForm(request, estudianteID):
    form = CitaForm(request.POST or None)
    estudiante = get_object_or_404(customuser, id=estudianteID)
    actualUser = request.user.id

    # Horarios ocupados
    horarios_ocupados = Cita.objects.filter(
        estudiante=estudiante,
        fecha_seleccionada__gte=timezone.now().date()
    ).values('fecha_seleccionada', 'inicio')

    context = {
        'form': form,
        'estudianteID': estudianteID,
        'actualUser': actualUser,
        'estudiante': estudiante,
        'horarios_ocupados': list(horarios_ocupados)  # Convertimos la QuerySet en una lista para JSON
    }

    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            tipo_tratamiento = form.cleaned_data['tipotratamiento']
            fecha_seleccionada = form.cleaned_data['fecha_seleccionada']
            hora_inicio = form.cleaned_data['inicio']

            # Verificar si ya existe una cita en el mismo horario y fecha
            cita_misma = Cita.objects.filter(
                estudiante=estudiante,
                paciente=request.user,
                tipotratamiento=tipo_tratamiento,
                fecha_seleccionada=fecha_seleccionada,
                inicio=hora_inicio
            ).exists()

            horario_ocupado = Cita.objects.filter(
                estudiante=estudiante,
                fecha_seleccionada=fecha_seleccionada,
                inicio=hora_inicio
            ).exclude(paciente=request.user).exists()

            if cita_misma:
                messages.error(request, 'Ya tienes una cita agendada en esta fecha y hora. Por favor, selecciona otro horario.')
            elif horario_ocupado:
                messages.error(request, 'Este horario no está disponible. Por favor, selecciona otro horario.')

            else:
                horario = form.save(commit=False)
                horario.paciente = request.user
                horario.estudiante = estudiante
                horario.save()

                subject = "Bienvenido a IODONT"
                html_message = f"""
                <div>Confirmación de cita...</div>
                """
                from_email = settings.EMAIL_HOST_USER
                recipient_list = [request.user.email, estudiante.email]
                send_mail(subject, "", from_email, recipient_list, fail_silently=False, html_message=html_message)

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
    # Obtener los horarios disponibles del estudiante actual
    horarios_disponibles = horarios.objects.filter(
        estudiante=request.user,
        fecha_seleccionada__gte=timezone.now().date()
    ).order_by('fecha_seleccionada', 'inicio')

    # Verificar si el método es POST para procesar la creación de horarios
    if request.method == 'POST':
        form = horariosForm(request.POST, user=request.user)  # Pasar el usuario al formulario
        if form.is_valid():
            try:
                # Obtener las fechas seleccionadas del formulario
                fechas_str = request.POST.get('fecha_seleccionada', '').split(',')
                
                if not fechas_str[0]:  # Si no hay fechas seleccionadas
                    messages.error(request, 'Por favor, selecciona al menos una fecha.')
                else:
                    horarios_creados = 0
                    tipo_tratamiento = form.cleaned_data['tipoTratamiento']
                    hora_inicio = form.cleaned_data['inicio']
                    hora_fin = form.cleaned_data['fin']
                    
                    # Crear un horario para cada fecha seleccionada
                    for fecha_str in fechas_str:
                        fecha = datetime.strptime(fecha_str.strip(), '%Y-%m-%d').date()
                        
                        # Comprobar si ya existe un horario con el mismo tratamiento, fecha y hora para evitar duplicados
                        if not horarios.objects.filter(
                            estudiante=request.user,
                            tipoTratamiento=tipo_tratamiento,
                            fecha_seleccionada=fecha,
                            inicio=hora_inicio
                        ).exists():
                            # Crear y guardar el horario
                            horarios.objects.create(
                                estudiante=request.user,
                                tipoTratamiento=tipo_tratamiento,
                                inicio=hora_inicio,
                                fin=hora_fin,
                                fecha_seleccionada=fecha
                            )
                            horarios_creados += 1
                    
                    # Mostrar mensaje de éxito si se crearon horarios
                    if horarios_creados > 0:
                        messages.success(request, f'¡Se han creado {horarios_creados} horarios exitosamente!')
                    else:
                        messages.info(request, 'No se crearon horarios nuevos, ya existen horarios en las fechas seleccionadas.')
                    
                    # Redirigir al calendario
                    return redirect('calendario')  # Aseguramos que el nombre de la URL sea correcto
                
            except Exception as e:
                print(f"Error al guardar: {e}")
                messages.error(request, f'Error al guardar los horarios: {str(e)}')
        else:
            # Imprimir y mostrar errores de formulario
            print("Errores del formulario:", form.errors)
            messages.error(request, 'Por favor, verifica los datos del formulario.')
    else:
        form = horariosForm(user=request.user)  # Pasar el usuario al formulario

    context = {
        'form': form,
        'horarios_disponibles': horarios_disponibles,
    }

    return render(request, 'estudiante/calendario_est.html', context)



@login_required
def eliminar_horario(request, id):
    horario = get_object_or_404(horarios, id=id)

    if request.method == 'POST':
        horario.delete()  # Elimina el horario de la base de datos
        return redirect('calendario')  # Redirige a la vista de calendario o donde desees

    return render(request, 'estudiante/eliminar_horario.html', {'horario': horario})

@login_required
def infoestudiante(request):
    estudiante = request.user
    
    # Crear el formulario con la instancia del usuario actual
    form = ModificarPerfil(instance=estudiante)
    
    # Inicializar los valores de universidad y comuna en el formulario para mostrarlos como solo lectura
    if estudiante.universidad:
        form.fields['universidad'].initial = estudiante.universidad.nombre
    if estudiante.comuna:
        form.fields['comuna'].initial = estudiante.comuna.nombreComuna

    context = {'form': form, 'user': estudiante}

    if request.method == 'POST':
        form = ModificarPerfil(request.POST, request.FILES, instance=estudiante)
        
        if form.is_valid():
            usuario = form.save(commit=False)
            
            # Conservar el certificado existente si no se sube uno nuevo
            if hasattr(estudiante, 'Certificado') and estudiante.Certificado:
                usuario.Certificado = estudiante.Certificado
            if 'Certificado' in request.FILES:
                usuario.Certificado = request.FILES['Certificado']
            
            usuario.save()
            form.save_m2m()  # Guardar relaciones many-to-many (tratamientos)

            messages.success(request, 'Perfil actualizado exitosamente')
            return HttpResponseRedirect(reverse('infoestudiante'))
        
        else:
            messages.error(request, 'Error al actualizar el perfil')
            print(form.errors)  # Mostrar errores en la consola para depuración

    # Actualizar los campos no editables en el formulario después de la actualización
    if estudiante.universidad:
        form.fields['universidad'].initial = estudiante.universidad.nombre
    if estudiante.comuna:
        form.fields['comuna'].initial = estudiante.comuna.nombreComuna

    return render(request, 'estudiante/infopersonal.html', context)



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
    
    # Obtiene la lista de pacientes asociados con el estudiante actual
    citas_agendadas = Cita.objects.filter(estudiante=estudiante).values_list('paciente', flat=True).distinct()
    pacientes = customuser.objects.filter(id__in=citas_agendadas, id_tipo_user__nombre_tipo_usuario='Paciente')

    print(citas_agendadas)
    print(pacientes)
    # Diccionario para almacenar el último tratamiento para cada paciente
    tratamientos_por_paciente = {}

    for paciente in pacientes:
        ultima_cita = (Cita.objects
                       .filter(paciente=paciente, estudiante=estudiante)
                       .order_by('-fecha_seleccionada', '-inicio')
                       .first())  # Obtenemos la última cita de cada paciente
        print(ultima_cita)
        if ultima_cita:
            tratamientos_por_paciente[paciente.id] = {
                'tratamiento': ultima_cita.tipotratamiento.nombreTratamiento,
                'fecha': ultima_cita.fecha_seleccionada,
                'hora': ultima_cita.inicio,
            }
    print(tratamientos_por_paciente)
    # Enviar los datos al contexto
    return render(request, 'estudiante/pacientes_estudiante.html', {
        'pacientes': pacientes,
        'tratamientos_por_paciente': tratamientos_por_paciente,
    })


@login_required
def citas_pac(request):
    paciente_id = request.user  # Obtener el usuario logueado
    citas = Cita.objects.filter(paciente=paciente_id).select_related('estudiante__universidad')  # Filtrar las citas para el paciente logueado

    return render(request, 'APT/citas.html', {
        'citas': citas  # Pasar las citas al contexto
    })


@login_required
def anular_cita(request, cita_id):
    # Obtiene la cita o muestra un 404 si no existe
    cita = get_object_or_404(Cita, id=cita_id, paciente=request.user)
    
    # Borra la cita y muestra un mensaje de éxito
    cita.delete()
    messages.success(request, "La cita ha sido anulada exitosamente.")
    
    # Redirige a la página de citas
    return redirect('citas')

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

    context = {
        'paciente': paciente,
        'cita': cita,
        'form': form,
        'fecha_nacimiento': spanish_date(paciente.fecha_nac),
        'fecha_cita': spanish_date(cita.fecha_seleccionada),
    }

    return render(request, 'estudiante/historial_medico.html', context)

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


from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def exportar_ficha_paciente(request, user_id=None):
    # Obtener los datos
    actualFicha = FichaClinica.objects.filter(paciente=user_id).values()
    paciente = customuser.objects.get(id=user_id)
    nombre_completo = f"{paciente.first_name} {paciente.last_name}"

    # Configurar el PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=fichaClinica_{nombre_completo}.pdf'
    
    # Crear el PDF
    pdf = canvas.Canvas(response, pagesize=A4)
    ancho, alto = A4
    
    # Modificar esta parte para usar BASE_DIR
    logo_path = os.path.join(settings.BASE_DIR, 'ProyectoAPT', 'static', 'img', 'LogoOdont.png')
    
    try:
        logo = ImageReader(logo_path)
        pdf.drawImage(logo, 50, alto - 100, width=100, height=100, preserveAspectRatio=True)
        # Si la imagen se carga correctamente, ajustar la posición del título
        pdf.setFont("Helvetica-Bold", 20)
        pdf.setFont("Helvetica", 12)
        pdf.drawString(160, alto - 70, f"Ficha Clínica Odontológica - Paciente: {nombre_completo}")
    except Exception as e:
        print(f"Error al cargar la imagen: {e}")
        print(f"Ruta intentada: {logo_path}")
        # Si hay error, poner el título en la posición original
        pdf.setFont("Helvetica-Bold", 20)
        pdf.setFont("Helvetica", 12)
        pdf.drawString(50, alto - 70, "Ficha Clínica Odontológica")
    
    # Línea separadora
    pdf.line(50, alto - 120, ancho - 50, alto - 120)
    
    # Información del paciente
    y = alto - 160  # Ajustar la posición inicial del contenido para dar espacio al logo
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, y, "Datos del Paciente")
    
    # Datos personales
    y -= 30
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(50, y, f"Nombre completo: {nombre_completo}")
    y -= 20
    pdf.drawString(50, y, f"RUT: {paciente.rut}")
    y -= 20
    pdf.drawString(50, y, f"Fecha de nacimiento: {paciente.fecha_nac}")
    y -= 20
    pdf.drawString(50, y, f"Teléfono: {paciente.num_tel}")
    y -= 20
    pdf.drawString(50, y, f"Email: {paciente.email}")
    
    # Línea separadora
    y -= 20
    pdf.line(50, y, ancho - 50, y)
    
    # Información clínica
    y -= 30
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, y, "Información Clínica")
    
    for ficha in actualFicha:
        y -= 30
        # Contacto de emergencia
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(50, y, "Contacto de Emergencia")
        y -= 20
        pdf.setFont("Helvetica", 11)
        pdf.drawString(70, y, f"Nombre: {ficha.get('nombre_contacto_emergencia', 'No especificado')}")
        y -= 20
        pdf.drawString(70, y, f"Teléfono: {ficha.get('telefono_contacto_emergencia', 'No especificado')}")
        
        # Motivo de consulta
        y -= 30
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(50, y, "Motivo de Consulta")
        y -= 20
        pdf.setFont("Helvetica", 11)
        pdf.drawString(70, y, f"{ficha.get('motivo_consulta', 'No especificado')}")
        
        # Síntomas
        y -= 30
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(50, y, "Síntomas Actuales")
        y -= 20
        pdf.setFont("Helvetica", 11)
        pdf.drawString(70, y, f"{ficha.get('sintomas_actuales', 'No especificado')}")
        
        # Diagnóstico
        y -= 30
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(50, y, "Diagnóstico")
        y -= 20
        pdf.setFont("Helvetica", 11)
        pdf.drawString(70, y, f"{ficha.get('diagnostico', 'No especificado')}")
        
        # Tratamiento
        y -= 30
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(50, y, "Tratamiento Actual")
        y -= 20
        pdf.setFont("Helvetica", 11)
        pdf.drawString(70, y, f"{ficha.get('tratamiento_actual', 'No especificado')}")

    # Pie de página
    pdf.line(50, 50, ancho - 50, 50)
    pdf.setFont("Helvetica", 8)
    pdf.drawString(50, 35, f"Documento generado el {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    pdf.drawString(ancho - 200, 35, "IODONT - Sistema de Gestión Odontológica")

    # Finalizar el PDF
    pdf.showPage()
    pdf.save()
    return response


def spanish_date(date):
    months = {
        'January': 'Enero',
        'February': 'Febrero',
        'March': 'Marzo',
        'April': 'Abril',
        'May': 'Mayo',
        'June': 'Junio',
        'July': 'Julio',
        'August': 'Agosto',
        'September': 'Septiembre',
        'October': 'Octubre',
        'November': 'Noviembre',
        'December': 'Diciembre'
    }
    
    days = {
        'Monday': 'Lunes',
        'Tuesday': 'Martes',
        'Wednesday': 'Miércoles',
        'Thursday': 'Jueves',
        'Friday': 'Viernes',
        'Saturday': 'Sábado',
        'Sunday': 'Domingo'
    }
    
    english_date = date.strftime('%A %d de %B de %Y')
    
    for eng, esp in months.items():
        english_date = english_date.replace(eng, esp)
    for eng, esp in days.items():
        english_date = english_date.replace(eng, esp)
    
    return english_date

def test_email(request):
    try:
        send_mail(
            'Prueba de correo',  # asunto
            'Este es un correo de prueba desde Django',  # mensaje
            os.getenv('EMAIL_HOST_USER'),  # remitente
            [os.getenv('EMAIL_HOST_USER')],  # destinatario (enviamos al mismo correo)
            fail_silently=False,
        )
        return HttpResponse('Correo enviado correctamente!')
    except Exception as e:
        return HttpResponse(f'Error al enviar el correo: {str(e)}')