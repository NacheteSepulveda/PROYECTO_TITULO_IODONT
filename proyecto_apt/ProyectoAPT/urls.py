"""
URL configuration for proyecto_apt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # Setup include to allow other app's urls to 
from . import views # COMO QUE NO EXISTE? XD

from django.conf import settings
from django.conf.urls.static import static
from .views import *
from ProyectoAPT.views import filtrar_estudiantes
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('', views.index, name='index'),
    # Horarios
    path('horarios/', views.registroHoras, name='horarios'),
    path('Horarios/<int:estudianteID>', views.tratamientosForm, name='tratamientosEstudiante'),
    # There we will enable the horario LIST
    path('obtener-horarios-disponibles/', views.obtener_horarios_disponibles, name='obtener_horarios_disponibles'),
    

    # Eliminar horario
    path('eliminar-horario/<int:horario_id>/', views.eliminar_horario, name='eliminar_horario'),



    # AUTH
    path('login/', views.loginUser, name='login'),
    path('registro/', views.register, name='registro'),
    path('logout/', views.custom_logout, name='logout'),
    path('obtener-direccion-universidad/', views.obtener_direccion_universidad, name='obtener_direccion_universidad'),
    path('revisar_estudiantes/', views.revisar_estudiantes, name='revisar_estudiantes'),
    #aptcha
    path('captcha/', include('captcha.urls')),
    #Servicios
    path('servicios/', views.servicios, name='servicios'),

    

    #Citas Paciente
    path('citas/', views.citas_pac, name='citas'),
    path('cita/anular/<int:cita_id>/', views.anular_cita, name='anular_cita'),

    # Añadir a subPage de Estudiante....
    path('estudiante/infopersonal/', views.infoestudiante, name="infoestudiante"),
    path('estudiante/notificaciones_estudiante/', views.notifiaciones_est, name="notificaciones"),
    path('estudiante/pacientes_estudiante/', views.pacientes_est, name="pacientes_est"),
    path('estudiante/calendario_est/',  views.calendar_est, name="calendario"), 
    path('crear_historial_medico/<int:paciente_id>/', views.crear_historial_medico, name='crear_historial_medico'),
    path('filtrar-estudiantes/', views.filtrar_estudiantes, name='filtrar_estudiantes'),


    #crear ficha paciente
    path('crear-ficha/<int:user_id>/', views.crear_ficha_paciente, name='crear_ficha_paciente'),
    path('lista_fichas_clinicas/', views.ver_ficha_clinica, name='lista_fichas_clinicas'),
    path('fichaExportar/<int:user_id>', views.exportar_ficha_paciente, name='fichaExportar'),
    #eliminar paciente
    path('eliminar-paciente/<int:paciente_id>/', views.eliminar_paciente, name='eliminar_paciente'),
    path('horarios/', filtrar_estudiantes, name='horarios'),  
    path('ver_ficha_clinica/<int:paciente_id>/', views.ver_ficha_clinica, name='ver_ficha_clinica'),
    

    # contraseña olvidada
    path('olvide-password/', 
        auth_views.PasswordResetView.as_view(
            template_name='login/olvide-pass.html',
            email_template_name='login/pass_email_reset.html',
            subject_template_name='login/password_reset_subject.txt',
        ),
        name='password_reset'
    ),
    path('reset-password-enviado/', 
        auth_views.PasswordResetDoneView.as_view(
            template_name='login/pass_confirm_email.html'
        ),
        name='password_reset_done'
    ),
    path('reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(
            template_name='login/reset-pass.html'
        ),
        name='password_reset_confirm'
    ),
    path('reset-password-completado/', 
        auth_views.PasswordResetCompleteView.as_view(
            template_name='login/pass_complete.html'
        ),
        name='password_reset_complete'
    ),
    ]
# Solo en modo de desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)