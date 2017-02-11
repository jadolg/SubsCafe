# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subtitulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=500)),
                ('ruta', models.CharField(max_length=5000)),
                ('descargas', models.IntegerField(default=0)),
                ('ahash', models.CharField(max_length=64, unique=True)),
            ],
        ),
    ]
