from django.contrib import admin
from .models import datos_personales1, datos_docente1, comision1, info_comision1, info_otrosi1, programa1, datos_personales1Admin, datos_docente1Admin, comision1Admin, info_comision1Admin, info_otrosi1Admin, programa1Admin
# Register your models here.

admin.site.register(datos_personales1,datos_personales1Admin)
admin.site.register(datos_docente1,datos_docente1Admin)
admin.site.register(comision1,comision1Admin)
admin.site.register(info_comision1,info_comision1Admin)
admin.site.register(info_otrosi1,info_otrosi1Admin)
admin.site.register(programa1,programa1Admin)
