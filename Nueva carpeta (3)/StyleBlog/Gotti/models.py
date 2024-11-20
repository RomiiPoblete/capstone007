from django.db import models
from django.contrib.auth.hashers import make_password

class DatosPersonales(models.Model):
    idDatoPersonal = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=100)  # Guardar usando make_password en el registro
    direccion = models.CharField(max_length=255)
    correoElectronico = models.EmailField(unique=True)  # Asegura que no haya correos duplicados

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Cliente(DatosPersonales):
    idCliente = models.AutoField(primary_key=True)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.telefono}"

class Barbero(DatosPersonales):
    idBarbero = models.AutoField(primary_key=True)
    especialidad = models.CharField(max_length=100)
    horario = models.DateField()
    telefono = models.CharField(max_length=15)

    def save(self, *args, **kwargs):
        # Encriptar la contraseña solo si no está encriptada
        if not self.contraseña.startswith('pbkdf2_'):
            self.contraseña = make_password(self.contraseña)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.especialidad} {self.horario}"

class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    nombreProducto = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    precio = models.FloatField(max_length=10)
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)  # Campo para la imagen

    def __str__(self):
        return f"{self.nombreProducto} - {self.descripcion} - ${self.precio} - Stock: {self.stock}"

    



class Servicio(models.Model):
    idServicio = models.AutoField(primary_key=True)
    nombreServicio = models.CharField(max_length=100)  # Cambié a nombreServicio para evitar confusión
    descripcion = models.CharField(max_length=255)  # Corregí max_length
    precio = models.FloatField(max_length=10)
    imagen = models.ImageField(upload_to='servicios/', null=True, blank=True)

    def __str__(self):
        return f"{self.nombreServicio} - ${self.precio}"

class BloqueHorario(models.Model):
    idbloque = models.AutoField(primary_key=True)
    horarioinicio = models.TimeField()
    horariofin = models.TimeField()
    fecha = models.DateField()
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    disponibilidad = models.CharField(max_length=20, default='DISPONIBLE')
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.fecha} {self.horarioinicio} - {self.horariofin} ({self.disponibilidad})"

    
class ContactInfo(models.Model):

    sucursal = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    numero = models.CharField(max_length=20)

    def __str__(self):
        return self.sucursal




class CarritoProducto(models.Model):
    carrito = models.ForeignKey('Carrito', related_name='carrito_productos', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def str(self):
        return f"{self.carrito} - {self.producto} x {self.cantidad}"

class Carrito(models.Model):
    idCarrito = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    productos = models.ManyToManyField(Producto, related_name='carritos')
    reservado = models.BooleanField(default=False)
    confirmado = models.BooleanField(default=False)  # Nuevo campo

    def str(self):
        return f"Carrito {self.idCarrito} de {self.cliente}"
    

class BarberoPendiente(models.Model):
    idBarberoPendiente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    correoElectronico = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    especialidad = models.CharField(max_length=100)
    horario = models.DateField()
    aprobado = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.contraseña.startswith('pbkdf2_'):
            self.contraseña = make_password(self.contraseña)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.correoElectronico}"

