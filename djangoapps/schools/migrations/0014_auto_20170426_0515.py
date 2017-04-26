# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-26 05:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    
    dependencies = [
        ('schools', '0011_auto_20170425_1847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='username',
        ),
        migrations.AddField(
            model_name='school',
            name='alias_school',
            field=models.CharField(default='', help_text='Example: "colombia-immersion-school-2" (name splitted by - and id)', max_length=250, unique=True, verbose_name='Alias School'),
        ),
    ]
