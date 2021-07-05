from django.contrib import admin
from joyas.models import *

# Register your models here.

admin.site.register(tipo_producto)
admin.site.register(producto)
admin.site.register(cliente)
admin.site.register(venta)
admin.site.register(detalle_venta)
admin.site.register(pedido)
admin.site.register(detalle_pedido)