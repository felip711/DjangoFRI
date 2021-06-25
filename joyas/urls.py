from django.conf.urls import url
from . import views

urlpatterns = [
    path('productos/',views.productos,name='Productos'),
]