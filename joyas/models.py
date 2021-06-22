from django.db import models
from djmoney.models.fields import MoneyField

# Create your models here.

class tipo_producto(models.Model):
    id_tipo_producto = models.AutoField(primary_key=True)
    nombre_tipo_producto = models.CharField(max_length=100)

    def __str__(self):
        txt = "{0}"
        return txt.format(self.nombre_tipo_producto)

class producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=100)
    id_tipo_producto = models.ForeignKey(tipo_producto, null=False, default='-', on_delete=models.CASCADE)

    def __str__(self):
        txt = "{0}"
        return txt.format(self.nombre_producto)

class cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre_cliente = models.CharField(max_length=100)
    rut_cliente = models.CharField(max_length=100)
    email_cliente = models.EmailField(max_length=200)

    def __str__(self):
        txt = "{0} - {1}"
        return txt.format(self.nombre_cliente, self.email_cliente)