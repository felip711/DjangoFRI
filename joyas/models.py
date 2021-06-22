from django.db import models
from djmoney.models.fields import MoneyField

# Create your models here.

class tipo_producto(models.Model):
    id_tipo_producto = models.AutoField(primary_key=True)
    nombre_tipo_producto = models.CharField(max_length=100)

    def __str__(self):
        txt = "{0}"
        return txt.format(self.nombre_tipo_producto)

