from __future__ import unicode_literals
from django.contrib import admin

from djangoapps.locations.models import Location, Position


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


class PositionAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'uid',
                    'lng',
                    'lat',)

    search_fields = ('id',)

admin.site.register(Location, LocationAdmin)
admin.site.register(Position, PositionAdmin)
