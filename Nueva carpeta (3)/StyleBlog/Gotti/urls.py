from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    ##Principal
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('iniciarCliente/', views.iniciarCliente, name='iniciarCliente'),
    path('iniciarColaborador/', views.iniciarColaborador, name='iniciarColaborador'),
    path('iniciarSesion/', views.iniciarSesion, name='iniciarSesion'),
    path('inicioCliente/', views.inicioCliente, name='inicioCliente'),
    path('inicioColaborador/', views.inicioColaborador, name='inicioColaborador'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('perfilCliente/', views.perfilCliente, name='perfilCliente'),
    path('perfilCliente/<int:id>/', views.perfilCliente, name='perfil_Cliente'),
    path('perfilColaborador/', views.perfilColaborador, name='perfilColaborador'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('cerrar_sesion2/', views.cerrar_sesion2, name='cerrar_sesion2'),
    path('registro_barbero/', views.registro_barbero, name='registro_barbero'),
    path('aprobar_barberos/', views.aprobar_barberos, name='aprobar_barberos'),
    path('registrarse_como',views.registrarse_como, name='registrarse_como'),


    ###barbero
    path('indexbarbero/', views.indexbarbero, name='indexbarbero'),
    path('carritobarbero/', views.carritobarbero, name='carritobarbero'),
    path('confirmar_pedido/<int:carrito_id>/', views.confirmar_pedido, name='confirmar_pedido'),
    path('cancelar_pedido/<int:carrito_id>/', views.cancelar_pedido, name='cancelar_pedido'),
    path('contactoact/', views.contactoact, name='contactoact'),
    path('contactobarbero/', views.contactobarbero, name='contactobarbero'),
    path('productosbarbero/', views.productosbarbero, name='productosbarbero'),
    path('serviciosbarbero/', views.serviciosbarbero, name='serviciosbarbero'),
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('editar_producto/<int:id>/', views.editar_producto, name='editar_producto'),
    path('eliminar_producto/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
    path('serviciosbarbero/', views.serviciosbarbero, name='serviciosbarbero'),
    path('agregar_servicio/', views.agregar_servicio, name='agregar_servicio'),
    path('editar_servicio/<int:id>/', views.editar_servicio, name='editar_servicio'),
    path('eliminar_servicio/<int:id>/', views.eliminar_servicio, name='eliminar_servicio'),
    #######
    path('crear_horarios/<int:idServicio>/', views.crear_horarios, name='crear_horarios'),
    path('ver_todos_horarios/<int:idServicio>/', views.ver_todos_horarios, name='ver_todos_horarios'),
    path('eliminar_horario/<int:idbloque>/', views.eliminar_horario, name='eliminar_horario'),  # Nueva URL para eliminar horarios
    path('horas_reservadas/', views.horas_reservadas, name='horas_reservadas'),
    path('confirmar_pedido/<int:carrito_id>/', views.confirmar_pedido, name='confirmar_pedido'),
    path('cancelar_pedido/<int:carrito_id>/', views.cancelar_pedido, name='cancelar_pedido'),
    path('aceptar_hora/<int:bloque_id>/', views.aceptar_hora, name='aceptar_hora'),
    path('cancelar_hora/<int:bloque_id>/', views.cancelar_hora, name='cancelar_hora'),

    ###cliente
    path('indexCliente/', views.indexCliente, name='indexCliente'),
    path('carritoCliente/', views.carritoCliente, name='carritoCliente'),
    path('contactoCliente/', views.contactoCliente, name='contactoCliente'),
    path('nosotrosCliente/', views.nosotrosCliente, name='nosotrosCliente'),
    path('productosCliente/', views.productosCliente, name='productosCliente'),
    path('servicio/', views.servicio, name='servicio'),
    path('reservar_carrito/', views.reservar_carrito, name='reservar_carrito'),
    path('horarios_disponibles/<int:idServicio>/', views.horarios_disponibles_cliente, name='horarios_disponibles_cliente'),
    path('agendar_horario/<int:bloque_id>/', views.agendar_horario, name='agendar_horario'),
    path('agregar_al_carrito/<int:id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar_del_carrito/<int:id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('agendar_horario/<int:bloque_id>/', views.agendar_horario, name='agendar_horario'),
    path('carrito/actualizar/<int:id>/', views.actualizar_cantidad, name='actualizar_cantidad'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
