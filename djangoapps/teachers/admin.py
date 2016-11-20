from __future__ import unicode_literals
from django.contrib import admin
from django.utils.translation import ugettext, ugettext_lazy as _

from teachers.models import Teacher


# Register your models here.
class TeacherAdmin(admin.ModelAdmin):

    # The fields to be used in displaying the Post model.
    list_display = ('first_name',
                    'last_name',
                    'email',
                    'phone',
                    'country_birth',
                    'city_birth',
                    'state_birth',
                    'country_live_in',
                    'city_live_in',
                    'state_live_in',
                    'address_live_in',
                    'native_languages',
                    'languages_speak',
                    'created_at',)

    search_fields = ('email',)

    # fieldsets = (
    #     (None, {'fields': ('title', 'link')}),
    #     (_('Writer'), {'fields': ('author')}),
    # )
    ordering = ('-created_at',)


# Now register the new Admin...
admin.site.register(Teacher, TeacherAdmin)
