from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
# Create your views here.


def productos(request):
     productos = producto.objects.all()

     #Buscador
     nombre_producto = request.GET.get('nombre_producto')
     if nombre_producto != '' and nombre_producto is not None:
          productos = productos.filter(nombre_producto__contains=nombre_producto)
     
     #Paginador
     paginador = Paginator(productos,10)
     pagina = request.GET.get('page')
     productos = paginador.get_page(pagina)

     return render(request, 'productos.html', {'productos':productos})