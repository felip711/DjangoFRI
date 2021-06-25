from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse('<h1>Página Principal</h1>')

def productos(request):

     context = {}
     return render(request, 'joyas/productos.html', context)