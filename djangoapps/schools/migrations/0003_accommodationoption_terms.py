# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-21 01:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0002_auto_20170320_0641'),
    ]

    operations = [
        migrations.AddField(
            model_name='accommodationoption',
            name='terms',
            field=models.TextField(blank=True, max_length=5000, verbose_name='Terms, Details or more information'),
        ),
    ]
