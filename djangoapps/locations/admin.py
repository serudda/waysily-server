from __future__ import unicode_literals
from django.contrib import admin

from djangoapps.locations.models import Location


class LocationAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'uid',
                    'country',
                    'address',
                    'city',
                    'state',
                    'position',
                    'zip_code',
                    'created_at',
                    'updated_at',)

    search_fields = ('address',)

    ordering = ('-created_at',)


admin.site.register(Location, LocationAdmin)
