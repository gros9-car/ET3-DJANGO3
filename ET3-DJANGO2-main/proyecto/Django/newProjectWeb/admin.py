from django.contrib import admin
from .models import Usuario,tipoUsuario, Cliente, Producto
# Register your models here.
admin.site.register(tipoUsuario)
admin.site.register(Usuario)
admin.site.register(Cliente)
admin.site.register(Producto)