# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 15:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20161028_1513'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pelicula',
            old_name='cienes',
            new_name='cines',
        ),
    ]
