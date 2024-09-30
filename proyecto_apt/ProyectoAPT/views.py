from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .decorators import user_not_authenticated
from django.contrib import messages
from .forms import CustomUserCreationForm, UserLoginForm
from .models import *

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
        def get_username_by_mail(email):
                try:
                    username = customuser.objects.get(email=email).username
                    return username
                except:
                    username= email
                    return email 
        mutable_data = form.data.copy()
        mutable_data['username'] = get_username_by_mail(form.data["username"])
        form.data = mutable_data
        if form.is_valid():
            
            user = authenticate(
                username=form.cleaned_data["username"],
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
