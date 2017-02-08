from __future__ import unicode_literals
from django.contrib import admin

from teachers.models import Teacher, Rating, Immersion, Experience, Education, Certificate, Price, PrivatePriceDetail, GroupPriceDetail


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


class ImmersionAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'uid',
                    'active',
                    'other_category',
                    'category',)

    search_fields = ('id',)


class ExperienceAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'uid',
                    'position',
                    'company',
                    'city',
                    'country',
                    'date_start',
                    'date_finish',
                    'description',)

    search_fields = ('id',)


class EducationAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'uid',
                    'school',
                    'degree',
                    'field_study',
                    'date_start',
                    'date_finish',
                    'description',)

    search_fields = ('id',)


class CertificateAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'uid',
                    'name',
                    'institution',
                    'date_received',
                    'description',)

    search_fields = ('id',)


class PriceAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'uid',
                    'private_class',
                    'group_class',)

    search_fields = ('id',)


class PrivatePriceDetailAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'uid',
                    'active',
                    'hour_price',)

    search_fields = ('id',)


class GroupPriceDetailAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'uid',
                    'active',
                    'hour_price',)

    search_fields = ('id',)


# Now register the new Admin...
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Immersion, ImmersionAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(PrivatePriceDetail, PrivatePriceDetailAdmin)
admin.site.register(GroupPriceDetail, GroupPriceDetailAdmin)
