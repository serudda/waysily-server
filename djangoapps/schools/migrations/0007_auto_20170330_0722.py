# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-30 07:22
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0006_auto_20170330_0720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='immersion',
            name='option',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Games and activities with local'), (2, 'Coffee tasting experience'), (3, 'Beer tasting experience'), (4, 'Chocolate tasting experience'), (5, 'Pub crawl'), (6, 'Local food tasting'), (7, 'Local dance class'), (8, 'Cooking Local Food'), (9, 'Local Movies Night'), (10, 'Practice local sports')], max_length=20, verbose_name='Immersion options'),
        ),
    ]
