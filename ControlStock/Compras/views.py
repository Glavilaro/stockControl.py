from django.shortcuts import render, redirect
from Compras.models import Productos
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,"principal.html"),

def consultas(request):
    Productos = Productos.objects.all()
    return render(request,"Productos.html",{
        'productos' : Productos
    })

def guardar(request):
    nombre = request.POST["nombre"]
    precio = request.POST["precio"]
    descripcion = request.POST["descripcion"]
    p = Productos(name=nombre,precio=precio,descripcion=descripcion)
    p.save()
    messages.success(request, 'Producto agregado')
    return redirect('consultar')

def eliminar(request, id):
    Productos = Productos.objects.filter(pk=id)
    Productos.delete()
    messages.success(request,'Producto eliminado')
    return redirect('Consultar')

def detalle(request, id):
    Productos = Productos.objects.get(pk=id)
    return render(request, "productoEditar.html",{
        'producto':Productos
    })

def editar(request):
    nombre = request.POST["nombre"]
    precio = request.POST["precio"]
    descripcion = request.POST["descripcion"]
    id = request.POST["id"]
    Productos.objects.filter(pk=id).update(id=id,name=nombre,precio=precio,descripcion=descripcion)
    messages.success(request,'producto actualizado')
    return redirect('consultar')
