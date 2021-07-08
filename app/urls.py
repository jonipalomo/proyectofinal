from django.urls import path
from .views import home , categorias,  acerca , agregar_producto, listar_productos, modificar_producto, eliminar_producto,  registro

urlpatterns = [
    path('', home, name="home"),     
    path('acerca/', acerca, name="acerca"), 
    path('agregar-producto/', agregar_producto, name="agregar-producto"), 
    path('listar-producto/', listar_productos, name="listar_producto"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"), 
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"), 
    path('registro/', registro, name="registro"), 
    path('categoria/<id>', categorias, name="categoria"), 

]
