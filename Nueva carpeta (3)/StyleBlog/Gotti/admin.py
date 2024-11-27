from django.contrib import admin
from .models import Cliente, Barbero, BarberoPendiente

# Registramos los modelos para que se muestren en el admin
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'contraseña', 'correoElectronico')
    search_fields = ('nombre', 'apellido', 'contraseña', 'correoElectronico')

@admin.register(Barbero)
class BarberoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'especialidad', 'horario', 'correoElectronico')
    search_fields = ('nombre', 'apellido', 'especialidad', 'correoElectronico')

@admin.register(BarberoPendiente)
class BarberoPendienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'correoElectronico', 'direccion', 'telefono', 'especialidad', 'aprobado')
    actions = ['aprobar_barberos']

    @admin.action(description='Aprobar barberos seleccionados')
    def aprobar_barberos(self, request, queryset):
        for barbero_pendiente in queryset.filter(aprobado=False):
            # Crear el registro en el modelo Barbero
            Barbero.objects.create(
                nombre=barbero_pendiente.nombre,
                apellido=barbero_pendiente.apellido,
                contraseña=barbero_pendiente.contraseña,  # Ya encriptada
                direccion=barbero_pendiente.direccion,
                correoElectronico=barbero_pendiente.correoElectronico,
                telefono=barbero_pendiente.telefono,
                especialidad=barbero_pendiente.especialidad,
                horario=barbero_pendiente.horario,
            )
            # Marcar como aprobado
            barbero_pendiente.aprobado = True
            barbero_pendiente.save()
