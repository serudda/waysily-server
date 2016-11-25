# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-20 00:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_auto_20161120_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='address_details_live_in',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='address_live_in',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='city_birth',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='city_live_in',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='country_live_in',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='state_birth',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='state_live_in',
            field=models.CharField(max_length=100),
        ),
    ]