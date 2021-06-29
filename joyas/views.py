from django.shortcuts import render
from .models import *
# Create your views here.


def productos(request):
     productos = producto.objects.all()

     nombre_producto = request.GET.get('nombre_producto')
     if nombre_producto != '' and nombre_producto is not None:
          productos = productos.filter(nombre_producto__contains=nombre_producto)
          print productos
     return render(request, 'productos.html', {'productos':productos})