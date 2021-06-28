from django.shortcuts import render
from .models import *
# Create your views here.


def productos(request):
     productos = producto.objects.all()

     item_name = request.GET.get('item_name')
     if item_name != '' and item_name is not None:
          productos = productos.filter(nombre_producto=item_name)
     return render(request, 'productos.html', {'productos':productos})