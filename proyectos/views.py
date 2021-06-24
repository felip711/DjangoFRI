from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Página Principal</h1>')

