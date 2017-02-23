# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-23 05:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0027_auto_20170223_0053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='languages',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AlterField(
            model_name='teacher',
            name='profile',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='profiles.Profile'),
        ),
        migrations.DeleteModel(
            name='Language',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
