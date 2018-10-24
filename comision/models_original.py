from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# Create your models here.

class datos_personales1(models.Model):
        GENERO = (
                ('H', 'Hombre'),
                ('M', 'Mujer'),
                )
        cc = models.IntegerField(primary_key=True)
        nombres = models.CharField(max_length=30)
        apellidos = models.CharField(max_length=30)
        genero = models.CharField(max_length=1, choices=GENERO)
        fecha_nac = models.DateField()
        edad = models.IntegerField()

class datos_personales1Admin(admin.ModelAdmin):
        list_display = ('cc', 'nombres', 'apellidos', 'genero', 'fecha_nac','edad')

class datos_docente1(models.Model):
        FACULTAD1 = (
                ('FA', 'Facultad de Artes - ASAB'),
                ('FC', 'Facultad de Ciencias y Educacion'),
                ('FM', 'Facultad de Medio Ambiente y Recursos Naturales'),
                ('FI', 'Facultad de Ingenieria'),
                ('FT', 'Facultad Tecnologica'),
                )
        facultad = models.CharField(max_length=2, choices=FACULTAD1)
        proy_curricular = models.CharField(max_length=40)
        CATEGORIA_DOC = (
                ('A', 'Asistente'),
                ('B', 'Asociado'),
                ('C', 'Auxiliar'),
                ('D', 'Titular'),
                )
        cat_docente = models.CharField(max_length=1, choices= CATEGORIA_DOC)
        gr_inves_vinc = models.CharField(max_length=100)
        CATEGORIA_GR = (
                ('A', 'A'),
                ('A1', 'A1'),
                ('B', 'B'),
                ('C', 'C'),
                ('D', 'D'),
                ('RC', 'RC'),
                ('SC', 'SC'),
                 )
        clas_colciencia = models.CharField(max_length=2, choices= CATEGORIA_GR)
        fecha_vinc = models.DateField()
        REGIMEN = (
                ('A', ' Acuerdo 003/1973'),
                ('B', ' Decreto 1279/2002'),
                 )
	regimen = models.CharField(max_length=1, choices= REGIMEN)
        datos_personales = models.ForeignKey(datos_personales1, on_delete=models.CASCADE)

class datos_docente1Admin(admin.ModelAdmin):
        list_display = ('facultad', 'proy_curricular', 'cat_docente', 'gr_inves_vinc','clas_colciencia','fecha_vinc', 'regimen','datos_personales')



class comision1(models.Model):
        TIP_ESTUDIO = (
                ('A', ' Maestria'),
                ('B', ' Doctorado'),
                ('C', ' Posdoctorado'),
                 )
        tipo_estudio = models.CharField(max_length=1, choices= TIP_ESTUDIO)
        TIP_APOYO = (
                ('A', ' Apoyo economico'),
                ('B', ' Apoyo economico y comision de estudio'),
                ('C', ' Comision de estudios'),
                ('D', ' Descarga academica'),
                ('E', ' Descarga academica y apoyo economico'),
                )
        tipo_apoyo_form_pos = models.CharField(max_length=1, choices= TIP_APOYO)
        MOD_COMISION = (
                ('A', 'Presencial'),
                ('B', 'Semipresencial'),
                ('C', 'Virtual'),
                )
        modalidad_comision = models.CharField(max_length=1, choices= MOD_COMISION)
        prog_carg_adelanta = models.CharField(max_length=100)
        area_conocimiento_OCDE = models.CharField(max_length=40)
        entidad = models.CharField(max_length=100)
        pais = models.CharField(max_length=30)
        ciudad = models.CharField(max_length=30)
        BECA = (
                ('S', 'Si'),
                ('N', 'No'),
                )
        becado = models.CharField(max_length=1, choices= BECA)
        fecha_inicio_estudios = models.DateField()
        REG = (
                ('A', ' Acuerdo 09/2007 '),
                )
	regimen = models. CharField (max_length=1, choices= REG)
        duracion_estudios_meses = models.IntegerField()
        datos_personales = models.ForeignKey(datos_personales1, on_delete=models.CASCADE)

class comision1Admin(admin.ModelAdmin):
        list_display = ('tipo_estudio', 'tipo_apoyo_form_pos', 'modalidad_comision', 'prog_carg_adelanta','area_conocimiento_OCDE','entidad','pais','ciudad','becado','fecha_inicio_estudios','regimen','duracion_estudios_meses','datos_personales')


class info_comision1(models.Model):
        csu_ca_res = models.CharField(max_length=15)
        fecha_res_CSU_CA = models.DateField()
        num_res_aprobacion_CSU = models.CharField(max_length=15)
        num_contrato = models.CharField(max_length=10)
        fecha_contrato = models.DateField()
        duracion_contrato_meses = models.IntegerField()
        obj_contrato= models.TextField(max_length=2000)
        num_pagare_poliza  = models.CharField(max_length=10)
        REMU = (
                ('S', 'Si'),
                ('N', 'No'),
                )
	remunerada = models.CharField(max_length=1, choices= REMU)
	salario_RRHH  = models.IntegerField()
        salario_reemplazo = models.IntegerField()
        tiquetes = models.IntegerField()
        matricula = models.IntegerField()
        seguro_medico = models.IntegerField()
        apoyo_bibliografico = models.IntegerField()
        gastos_instalacion = models.IntegerField()
        costo_inicial = models.IntegerField()
        comision = models.ForeignKey(comision1, on_delete=models.CASCADE)

class info_comision1Admin(admin.ModelAdmin):
        list_display = ('csu_ca_res', 'fecha_res_CSU_CA', 'num_res_aprobacion_CSU', 'num_contrato', 'fecha_contrato','duracion_contrato_meses','obj_contrato','num_pagare_poliza','remunerada','salario_RRHH','salario_reemplazo','tiquetes','matricula','seguro_medico','apoyo_bibliografico','gastos_instalacion','costo_inicial','comision')


class info_otrosi1(models.Model):
        OTRO_SI = (
                ('S', 'Si'),
                ('N', 'No'),
                )
	otrosi = models.CharField(max_length=1, choices= OTRO_SI)
        fecha_otrosi = models.DateField()
        obj_otrosi = models.TextField(max_length=2000)
        valor_otrosi = models.IntegerField()
        salario_RRHH_otrosi = models.IntegerField()
        salario_reemplazo_otrosi = models.IntegerField()
        tiquetes_otrosi = models.IntegerField()
        matricula_otrosi = models.IntegerField()
        seguro_medico_otrosi = models.IntegerField()
        apoyo_bibliografico_otrosi = models.IntegerField()
        comision = models.ForeignKey(comision1, on_delete=models.CASCADE)

class info_otrosi1Admin(admin.ModelAdmin):
        list_display = ('otrosi', 'fecha_otrosi', 'obj_otrosi', 'valor_otrosi', 'salario_RRHH_otrosi','salario_reemplazo_otrosi','tiquetes_otrosi','matricula_otrosi', 'seguro_medico_otrosi', 'apoyo_bibliografico_otrosi', 'comision')


class programa1(models.Model):
        costo_total_programa = models.IntegerField()
        ESTADO = (
                ('A', 'Con incumplimiento'),
                ('B', 'En curso'),
                ('C', 'Fallecido'),
                ('D', 'Liquidado'),
                ('E', 'Liquidado sin titulo'),
                ('F', 'Renuncia a la Comision'),
                ('G', 'Renuncia a la Universidad'),
                ('H', 'Sin Informacion'),
                ('I', 'Terminado'),
                ('J', 'Titulado con Contrato Vigente'),
                ('K', 'Estudios Terminados sin Titulacion'),
        )
        estado_agosto_2016= models.CharField(max_length=1, choices= ESTADO)
        responsable_cierre = models.CharField(max_length=30)
        titulo_otorgado = models.CharField(max_length=50)
        fecha_titulacion = models.DateField()
        observaciones = models.CharField(max_length=255)
        soporte_base = models.FileField('opt/si/comisiones/%Y/%m/%d/')
        soportes_finales = models.FileField('opt/si/comisiones/%Y/%m/%d/')
        comision = models.ForeignKey(comision1, on_delete=models.CASCADE)

class programa1Admin(admin.ModelAdmin):
        list_display = ('costo_total_programa', 'estado_agosto_2016', 'responsable_cierre', 'titulo_otorgado', 'fecha_titulacion','observaciones', 'soporte_base', 'soportes_finales', 'comision')


