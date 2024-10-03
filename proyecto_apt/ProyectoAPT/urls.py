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


urlpatterns = [
    path('', views.index, name='index'),
    path('Horarios', views.registroHoras, name='horarios'),
    path('servicios/', views.servicios, name='servicios'),
    # AUTH
    path('login/', views.loginUser, name='login'),
    path('registro/', views.register, name='registro'),
    path('logout/', views.custom_logout, name='logout')
]
# Solo en modo de desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)