from __future__ import unicode_literals
from django.contrib import admin

from djangoapps.features.models import Feature


class FeatureAdmin(admin.ModelAdmin):

    list_display = ('id', 'active', 'feature_en', 'feature_es', 'description_en', 'description_es', 'created_at')
    search_fields = ('feature_es',)
    
    ordering = ('-created_at',)

admin.site.register(Feature, FeatureAdmin)
