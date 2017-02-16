# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-14 06:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0021_auto_20170214_0424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='location',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='location', to='locations.Location'),
        ),
    ]
