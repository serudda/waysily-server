from __future__ import unicode_literals
from django.contrib import admin

from djangoapps.profiles.models import Profile
from djangoapps.profiles.models import Language


class ProfileAdmin(admin.ModelAdmin):

    list_display = ('user_id',
                    'phone_number',
                    'gender',
                    'birth_date',
                    'born_country',
                    'born_city',
                    'about',
                    'avatar',
                    'languages',
                    'location',
                    'created_at',
                    'updated_at',)

    search_fields = ('id',)

    ordering = ('-created_at',)


class LanguageAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'native',
                    'teach',
                    'learn',)

    search_fields = ('id',)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Language, LanguageAdmin)
