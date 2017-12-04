# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-10-18 20:06
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0006_remove_perfil_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='user',
            field=models.OneToOneField(default=datetime.datetime(2017, 10, 18, 20, 6, 52, 933000, tzinfo=utc), on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]