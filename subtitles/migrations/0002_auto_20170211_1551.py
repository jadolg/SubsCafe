# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 15:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('subtitles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subtitulo',
            name='ruta',
        ),
        migrations.AddField(
            model_name='subtitulo',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
