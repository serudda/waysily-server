from __future__ import unicode_literals
from django.contrib import admin
from django import forms

from djangoapps.countries.models import Country


class CountryAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'alias_country',
                    'name_en',
                    'name_es',
                    'description_en',
                    'description_es',
                    'recommend',
                    'currency_code',
                    'currency_name',
                    'code',
                    'capital',
                    'zone',
                    'photo',
                    'thumbnail',
                    'active',
                    'created_at',
                    'updated_at',)

    fieldsets = (
        ('Basic Information', {
            'fields': ('name_en', 'name_es', 'description_en', 'description_es', 'alias_country', 'code', 'capital',
                       'zone', 'currency_code', 'currency_name', 'photo', 'thumbnail', 'recommend', 'active')
        }),
    )

    search_fields = ('id',)

    ordering = ('-created_at',)

admin.site.register(Country, CountryAdmin)
