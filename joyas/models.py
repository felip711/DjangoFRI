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
    cantidad_producto = models.IntegerField(default=0)
    precio = MoneyField(decimal_places=0, verbose_name='Precio Unitario', default=0, default_currency='CLP', max_digits=11)

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

class venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    fecha_venta = models.DateField(auto_now=False)
    id_cliente = models.ForeignKey(cliente, null=False, default='-', on_delete=models.CASCADE)
    id_producto = models.ForeignKey(producto, null=False, default='-', on_delete=models.CASCADE)
    cantidad_venta = models.IntegerField(default=0)
    precio_venta = MoneyField(decimal_places=0, verbose_name='Monto Venta', default=0, default_currency='CLP', max_digits=11)

    def __str__(self):
        txt = "{0} - {1} - {2}"
        return txt.format(self.fecha_venta, self.cantidad_venta, self.precio_venta)