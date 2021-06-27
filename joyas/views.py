from django.shortcuts import render

# Create your views here.


def productos(request):
     producto = producto.objects.all()
     return render(request, 'productos.html', {'producto':producto})