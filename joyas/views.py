from django.shortcuts import render

# Create your views here.


def productos(request):
     productos = producto.objects.all()
     return render(request, 'productos.html', {'productos':productos})