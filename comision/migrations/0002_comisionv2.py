# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 14:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comision', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='comisionv2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cc', models.IntegerField()),
                ('nombres', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('genero', models.CharField(choices=[('H', 'Hombre'), ('M', 'Mujer')], max_length=1)),
                ('fecha_nac', models.DateField()),
                ('edad', models.IntegerField()),
                ('facultad', models.CharField(choices=[('FA', 'Facultad de Artes - ASAB'), ('FC', 'Facultad de Ciencias y Educacion'), ('FM', 'Facultad de Medio Ambiente y Recursos Naturales'), ('FI', 'Facultad de Ingenieria'), ('FT', 'Facultad Tecnologica')], max_length=2)),
                ('proy_curricular', models.CharField(max_length=40)),
                ('cat_docente', models.CharField(choices=[('A', 'Asistente'), ('B', 'Asociado'), ('C', 'Auxiliar'), ('D', 'Titular')], max_length=1)),
                ('gr_inves_vinc', models.CharField(max_length=100)),
                ('clas_colciencia', models.CharField(choices=[('A', 'A'), ('A1', 'A1'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('RC', 'RC'), ('SC', 'SC')], max_length=2)),
                ('fecha_vinc', models.DateField()),
                ('tipo_estudio', models.CharField(choices=[('A', ' Maestria'), ('B', ' Doctorado'), ('C', ' Posdoctorado')], max_length=1)),
                ('tipo_apoyo_form_pos', models.CharField(choices=[('A', ' Apoyo economico'), ('B', ' Apoyo economico y comision de estudio'), ('C', ' Comision de estudios'), ('D', ' Descarga academica'), ('E', ' Descarga academica y apoyo economico')], max_length=1)),
                ('modalidad_comision', models.CharField(choices=[('A', 'Presencial'), ('B', 'Semipresencial'), ('C', 'Virtual')], max_length=1)),
                ('prog_carg_adelanta', models.CharField(max_length=100)),
                ('area_conocimiento_OCDE', models.CharField(max_length=40)),
                ('entidad', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=30)),
                ('ciudad', models.CharField(max_length=30)),
                ('becado', models.CharField(choices=[('S', 'Si'), ('N', 'No')], max_length=1)),
                ('fecha_inicio_estudios', models.DateField()),
                ('regimen', models.CharField(choices=[('A', ' Acuerdo 09/2007 ')], max_length=1)),
                ('duracion_estudios_meses', models.IntegerField()),
                ('csu_ca_res', models.CharField(max_length=15)),
                ('fecha_res_CSU_CA', models.DateField()),
                ('num_res_aprobacion_CSU', models.CharField(max_length=15)),
                ('num_contrato', models.CharField(max_length=10)),
                ('fecha_contrato', models.DateField()),
                ('duracion_contrato_meses', models.IntegerField()),
                ('obj_contrato', models.TextField(max_length=2000)),
                ('num_pagare_poliza', models.CharField(max_length=10)),
                ('remunerada', models.CharField(choices=[('S', 'Si'), ('N', 'No')], max_length=1)),
                ('salario_RRHH', models.IntegerField()),
                ('salario_reemplazo', models.IntegerField()),
                ('tiquetes', models.IntegerField()),
                ('matricula', models.IntegerField()),
                ('seguro_medico', models.IntegerField()),
                ('apoyo_bibliografico', models.IntegerField()),
                ('gastos_instalacion', models.IntegerField()),
                ('costo_inicial', models.IntegerField()),
                ('otrosi', models.CharField(choices=[('S', 'Si'), ('N', 'No')], max_length=1)),
                ('fecha_otrosi', models.DateField()),
                ('obj_otrosi', models.TextField(max_length=2000)),
                ('valor_otrosi', models.IntegerField()),
                ('salario_RRHH_otrosi', models.IntegerField()),
                ('salario_reemplazo_otrosi', models.IntegerField()),
                ('tiquetes_otrosi', models.IntegerField()),
                ('matricula_otrosi', models.IntegerField()),
                ('seguro_medico_otrosi', models.IntegerField()),
                ('apoyo_bibliografico_otrosi', models.IntegerField()),
                ('costo_total_programa', models.IntegerField()),
                ('estado_agosto_2016', models.CharField(choices=[('A', 'Con incumplimiento'), ('B', 'En curso'), ('C', 'Fallecido'), ('D', 'Liquidado'), ('E', 'Liquidado sin titulo'), ('F', 'Renuncia a la Comision'), ('G', 'Renuncia a la Universidad'), ('H', 'Sin Informacion'), ('I', 'Terminado'), ('J', 'Titulado con Contrato Vigente'), ('K', 'Estudios Terminados sin Titulacion')], max_length=1)),
                ('responsable_cierre', models.CharField(max_length=30)),
                ('titulo_otorgado', models.CharField(max_length=50)),
                ('fecha_titulacion', models.DateField()),
                ('observaciones', models.CharField(max_length=255)),
                ('soporte_base', models.FileField(upload_to=b'', verbose_name='opt/si/comisiones/%Y/%m/%d/')),
                ('soportes_finales', models.FileField(upload_to=b'', verbose_name='opt/si/comisiones/%Y/%m/%d/')),
            ],
        ),
    ]
