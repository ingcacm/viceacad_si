# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 17:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puntos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puntos',
            name='facultad',
            field=models.CharField(choices=[('FA', 'Facultad de Artes - ASAB'), ('FC', 'Facultad de Ciencias y Educacion'), ('FM', 'Facultad de Medio Ambiente y Recursos Naturales'), ('FI', 'Facultad de Ingenieria'), ('FT', 'Facultad Tecnologica')], max_length=2),
        ),
    ]
