# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-14 04:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teachers', '0020_auto_20170212_2316'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(blank=True, default='', max_length=10000)),
                ('phone_number', models.CharField(blank=True, default='', max_length=30)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('born', models.CharField(blank=True, default='', max_length=200)),
                ('avatar', models.TextField(blank=True, default='', max_length=5000)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='about',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='born',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='sex',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='uid',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='user',
        ),
        migrations.AddField(
            model_name='teacher',
            name='profile',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='teachers.Profile'),
        ),
    ]
