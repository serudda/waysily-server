from __future__ import unicode_literals
from django.contrib import admin
from django.utils.translation import ugettext, ugettext_lazy as _

from teachers.models import Teacher, Rating


# Register your models here.
class TeacherAdmin(admin.ModelAdmin):

    # The fields to be used in displaying the Teacher model.
    list_display = ('id',
                    'uid',
                    'location',
                    'email',
                    'phone_number',
                    'first_name',
                    'last_name',
                    'sex',
                    'birth_date',
                    'born',
                    'about',
                    'avatar',
                    'languages',
                    'type',
                    'teacher_since',
                    'methodology',
                    'immersion',
                    'price',
                    'status',
                    'recommended',
                    'created_at',
                    'updated_at',)

    search_fields = ('email',)

    # fieldsets = (
    #     (None, {'fields': ('title', 'link')}),
    #     (_('Writer'), {'fields': ('author')}),
    # )
    ordering = ('-created_at',)


class RatingAdmin(admin.ModelAdmin):

    # The fields to be used in displaying the Teacher model.
    list_display = ('id',
                    'uid',
                    'teacher',
                    'author',
                    'methodology_value',
                    'teaching_value',
                    'communication_value',
                    'review',
                    'created_at',
                    'updated_at',)

    search_fields = ('review',)

    # fieldsets = (
    #     (None, {'fields': ('title', 'link')}),
    #     (_('Writer'), {'fields': ('author')}),
    # )
    ordering = ('-created_at',)


# Now register the new Admin...
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Rating, RatingAdmin)
