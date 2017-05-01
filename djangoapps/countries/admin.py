from __future__ import unicode_literals
from django.contrib import admin
from django import forms

from djangoapps.countries.models import Country


class CountryAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'name_en',
                    'name_es',
                    'alias_country',
                    'code',
                    'photo',
                    'thumbnail',
                    'active',
                    'created_at',
                    'updated_at',)

    fieldsets = (
        ('Basic Information', {
            'fields': ('name_en', 'name_es', 'alias_country', 'code', 'photo', 'thumbnail', 'active')
        }),
    )

    search_fields = ('id',)

    ordering = ('-created_at',)

admin.site.register(Country, CountryAdmin)
