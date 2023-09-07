from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from .models import User


# Create your views here.
def login(request):
    if (request.method == 'POST'):
        user_name = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username = user_name).exists():
            user = get_object_or_404(User, username = user_name)
            user_password = user.password
            if check_password(password, user_password):
                return HttpResponse('Ingresa')
            else:
                return HttpResponse('Contraseña incorrecta')
        else:
            return HttpResponse('Usuario no existe')
        
    return render(request, 'login.html')

def register(request):
    if(request.method == 'POST'):
        user_name = request.POST['username']

        if User.objects.filter(username=user_name).exists():
            messages.error(request, 'El nombre de usuario ya está en uso.')
            return render(request, 'register.html')
        
        full_name = request.POST['full_name']
        password = request.POST['password']
        password_hashed = make_password(password)
        try:
            User.objects.create(username=user_name, full_name=full_name, password=password_hashed)
        except Exception as e:
            messages.error(request, f'Error al registrar el usuario: {str(e)}')
            return render(request, 'register.html')


    return render(request, 'register.html')
        