from __future__ import unicode_literals
from django.contrib import admin

from locations.models import Location


# Register your models here.
class LocationAdmin(admin.ModelAdmin):

    # The fields to be used in displaying the Teacher model.
    list_display = ('id',
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


# Now register the new Admin...
admin.site.register(Location, LocationAdmin)
