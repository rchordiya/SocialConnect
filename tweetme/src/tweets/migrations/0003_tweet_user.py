# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-11 20:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tweets', '0002_auto_20170411_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
