# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-10-18 20:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20171018_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='user',
        ),
    ]
