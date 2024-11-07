from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import customuser

@receiver(post_save, sender=customuser)
def enviar_correo_estado_cuenta(sender, instance, **kwargs):
    if instance.estado_aprobacion == 'aprobado':
        subject = 'Tu cuenta en IODONT ha sido aprobada'
        html_message = f"""
        <div style="font-family: Arial, sans-serif; color: #333; max-width: 600px; margin: auto; padding: 20px; border: 1px solid #e0e0e0; border-radius: 8px;">
            <h2 style="color: #007BFF; text-align: center;">¡Felicidades {instance.first_name}! :D </h2>
            <p style="font-size: 1.1em;">
                Tu cuenta ha sido <strong>aprobada</strong> y ahora puedes acceder a todas las funcionalidades de IODONT.
            </p>
            <p>Para ingresar, utiliza tu correo registrado: <strong>{instance.email}</strong>.</p>
            <p style="font-size: 0.9em; color: #666;">
                Si tienes alguna pregunta o necesitas asistencia, no dudes en contactarnos.
            </p>
            <footer style="font-size: 0.8em; color: #aaa; text-align: center;">
                &copy; 2024 IODONT. Todos los derechos reservados.
            </footer>
        </div>
        """
        send_mail(
            subject=subject,
            message="",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[instance.email],
            fail_silently=False,
            html_message=html_message
        )
        
    elif instance.estado_aprobacion == 'rechazado':
        subject = 'Tu solicitud de cuenta en IODONT ha sido rechazada'
        html_message = f"""
        <div style="font-family: Arial, sans-serif; color: #333; max-width: 600px; margin: auto; padding: 20px; border: 1px solid #e0e0e0; border-radius: 8px;">
            <h2 style="color: #dc3545; text-align: center;">Lamentamos informarte :( </h2>
            <p style="font-size: 1.1em;">
                Tu solicitud de cuenta en IODONT ha sido <strong>rechazada</strong> debido a inconsistencias en los datos proporcionados.
            </p>
            <p>Para más detalles o para realizar otra solicitud, por favor contáctanos.</p>
            <footer style="font-size: 0.8em; color: #aaa; text-align: center;">
                &copy; 2024 IODONT. Todos los derechos reservados.
            </footer>
        </div>
        """
        send_mail(
            subject=subject,
            message="",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[instance.email],
            fail_silently=False,
            html_message=html_message
        )