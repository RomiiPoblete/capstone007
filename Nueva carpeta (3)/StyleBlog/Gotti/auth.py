from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import redirect
from .models import Cliente,Barbero
from functools import wraps

def authenticate_user(correoElectronico, contraseña):
    try:
        user = Cliente.objects.get(correoElectronico=correoElectronico)
    except Cliente.DoesNotExist:
        return None  # Usuario no encontrado

    if check_password(contraseña, user.contraseña):
        return user  # Usuario autenticado
    else:
        return None  # Contraseña incorrecta

def create_user( correoElectronico, contraseña):
    user = Cliente(correoElectronico=correoElectronico, contraseña=make_password(contraseña))
    user.save()
    return user

def is_authenticated(request):
    # Obtén el ID del usuario desde la sesión (si la hay)
    user_id = request.session.get('user_id')
    if user_id:
        try:
            user = Cliente.objects.get(pk=user_id)
            return True
        except Cliente.DoesNotExist:
            request.session.flush()  # cierra sesion
    return False

def login_user(request, user):
    request.session['user_id'] = user.pk

def logout_user(request):
    request.session.flush()

def custom_login_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if is_authenticated(request):
            return view_func(request, *args, **kwargs)
        else:
            return redirect('iniciarCliente')
    return wrapper