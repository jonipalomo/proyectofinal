from app.models import Producto
from django.http import request
from django.shortcuts import get_object_or_404, redirect, render
from .models import Producto, Categoria
from .forms import ProductoForm, CustomerCreationForm
from django.contrib.auth import  authenticate, login
from django.contrib import messages


# Create your views here.



def home(request):
    productos13 = Producto.objects.all()[:3]
    productos410 = Producto.objects.all()[3:10]
    categorias = Categoria.objects.all()
    context = {
        'primeros_productos': productos13,
        'segundos_productos': productos410,
        'categorias': categorias,
    }
    return render(request, "app/home.html", context)

def acerca(request):
    return render(request,'app/acerca.html')



def agregar_producto(request):
    data = {
      'form': ProductoForm()
    }
    
    if request.method == "POST":
      formulario = ProductoForm(data=request.POST, files=request.FILES)
      if formulario.is_valid():
        formulario.save()
        data["mensaje"] = "guardado correctamente"
      else:
        data["form"]= formulario
    return render(request, 'app/producto/agregar.html',data)

def listar_productos(request):
  productos = Producto.objects.all()
  data= {
    'productos' : productos
  }
  return render(request, 'app/producto/listar.html',data)

def registro(request):
  data = {
    'form': CustomerCreationForm()
  }
  if request.method =='POST':
    formulario = CustomerCreationForm(data=request.POST)
    if formulario.is_valid():
      formulario.save()
      user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
      login(request, user)
      messages.success(request, "Te has registrado correctamente")
      # redirigir al home
      return redirect(to="home")
      data["form"] = formulario
      
  return render(request, 'registration/registro.html', data)

def modificar_producto(request, id):
  producto = get_object_or_404(Producto, id=id)
  data = {
    'form': ProductoForm(instance=producto)
  }
  if request.method =='POST':
      formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
      if formulario.is_valid():
        formulario.save()
        return redirect(to="listar_producto")
      data ["form"] = formulario
  return render(request, 'app/producto/modificar.html', data)


def eliminar_producto(request, id):
  producto = get_object_or_404(Producto, id=id)
  producto.delete()
  return redirect(to="listar_producto")

def categorias(request, categoria_id):
    categoria_id = get_object_or_404(Categoria, id=categoria_id)
    categorias = Categoria.objects.all()
    context = {
        'categorias': categorias,
        'id_cat': categoria_id,
    }
    return render(request, 'app/producto/categoria.html', context)