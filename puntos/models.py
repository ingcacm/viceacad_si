from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# Create your models here.

class puntos(models.Model):
        cc = models.IntegerField()
        FACULTAD1 = (
                ('Facultad de Artes - ASAB', 'Facultad de Artes - ASAB'),
                ('Facultad de Ciencias y Educacion', 'Facultad de Ciencias y Educacion'),
                ('Facultad de Medio Ambiente y Recursos Naturales', 'Facultad de Medio Ambiente y Recursos Naturales'),
                ('Facultad de Ingenieria', 'Facultad de Ingenieria'),
                ('Facultad Tecnologica', 'Facultad Tecnologica'),
                )
        facultad = models.CharField(max_length=70, choices=FACULTAD1)
        concepto = models.CharField(max_length=30)
        descripcion = models.TextField(null=True, blank=True)
        resolucion = models.IntegerField(null=True, blank=True)
        fecha_res = models.DateField(null=True, blank=True)
	enlace_res = models.CharField(max_length=150)
	acta = models.IntegerField(null=True, blank=True)
	fecha_acta = models.DateField(null=True, blank=True)
	enlace_acta = models.CharField(max_length=150)
	puntos_salariales = models.IntegerField(null=True, blank=True)
	puntos_bonificacion = models.IntegerField(null=True, blank=True)


class puntosAdmin(admin.ModelAdmin):
        list_display = ('cc', 'facultad', 'concepto', 'descripcion', 'resolucion','fecha_res','enlace_res', 'acta', 'fecha_acta','enlace_acta','puntos_salariales','puntos_bonificacion')
