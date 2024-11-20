from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import redirect
from .models import Barbero
from functools import wraps

# Autenticar al barbero
def authenticate_barbero(correoElectronico, contraseña):
    try:
        user = Barbero.objects.get(correoElectronico=correoElectronico)
    except Barbero.DoesNotExist:
        return None  # Usuario no encontrado

    # Verificar si la contraseña es correcta
    if check_password(contraseña, user.contraseña):
        return user  # Usuario autenticado
    else:
        return None  # Contraseña incorrecta

# Crear un nuevo barbero con contraseña encriptada
def create_barbero(correoElectronico, contraseña):
    user = Barbero(correoElectronico=correoElectronico, contraseña=make_password(contraseña))
    user.save()
    return user

# Verificar si el barbero está autenticado
def is2_authenticated(request):
    user_id = request.session.get('user_id')
    if user_id:
        try:
            user = Barbero.objects.get(pk=user_id)
            return True
        except Barbero.DoesNotExist:
            request.session.flush()  # Cierra la sesión si el usuario no existe
    return False

# Iniciar sesión y guardar el user_id en la sesión
def login_barbero(request, user):
    request.session['user_id'] = user.pk
    print("User ID set in session:", request.session['user_id'])  # Depuración

# Cerrar la sesión del barbero
def logout_barbero(request):
    request.session.flush()

# Decorador personalizado para proteger las vistas
def custom2_login_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if is2_authenticated(request):
            return view_func(request, *args, **kwargs)
        else:
            return redirect('iniciarColaborador')  # Redirige si no está autenticado
    return wrapper
