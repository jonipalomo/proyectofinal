from django.db import models

# Create your models here.
from django.db import models

# Create your models here.





class Categoria(models.Model):
    description_categoria = models.CharField("Ingrese la categoria del producto", max_length=255)

    def __str__(self):
        return self.description_categoria

class Producto(models.Model):
    titulo = models.CharField("Ingrese el nombre del producto", max_length=255)
    imagen = models.ImageField("Suba la imagen del producto", null=True, max_length=255)
    descripcion = models.CharField(max_length=20)
    precio =  models.IntegerField(blank=True, null=True)
    categoria= models.ForeignKey(Categoria,on_delete=models.CASCADE, related_name="categorias")
    def __str__(self):
        return self.titulo
    
    def __str__(self):
        return f" #{self.titulo} categoria de producto: {self.categoria}"

class Usuario(models.Model):
    usuario1 = models.CharField("Ingrese el nombre del usuario", max_length=255)
    lista_productos = models.ManyToManyField(Producto, help_text="Seleccione lista de productos")
    total_carrito = models.CharField(max_length=20)
 

    def __str__(self):
        return f" #{self.usuario1}  {self.total_carrito}"