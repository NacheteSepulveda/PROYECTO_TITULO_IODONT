from django.shortcuts import redirect
from functools import wraps

def user_not_authenticated(function=None, redirect_url='/'):
    """
    Decorador para vistas que verifica que el usuario NO esté autenticado,
    redirigiendo a la página principal si es necesario por defecto.
    """
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):  # Cambia 'args' a '*args'
            if request.user.is_authenticated:
                return redirect(redirect_url)

            return view_func(request, *args, **kwargs)  # Pasa '*args' aquí

        return _wrapped_view

    if function:
        return decorator(function)

    return decorator

def estudiante_aprobado_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.estado_aprobacion == 'aprobado':
            return view_func(request, *args, **kwargs)
        return redirect('inicio')  # Redirige si no está aprobado
    return _wrapped_view


