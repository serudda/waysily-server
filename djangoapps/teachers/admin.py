from __future__ import unicode_literals
from django.contrib import admin

from djangoapps.teachers.models import Profile, Teacher, Language, Experience, Education, Certificate, Immersion, Price, \
    PrivatePriceDetail, GroupPriceDetail, Rating


class ProfileAdmin(admin.ModelAdmin):

    list_display = ('phone_number',
                    'gender',
                    'birth_date',
                    'born',
                    'about',
                    'avatar',
                    'created_at',
                    'updated_at',)

    search_fields = ('id',)

    ordering = ('-created_at',)


class TeacherAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'location',
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

    search_fields = ('id',)

    ordering = ('-created_at',)


class LanguageAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'uid',
                    'native',
                    'teach',
                    'learn',)

    search_fields = ('id',)


class RatingAdmin(admin.ModelAdmin):

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


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Immersion, ImmersionAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(PrivatePriceDetail, PrivatePriceDetailAdmin)
admin.site.register(GroupPriceDetail, GroupPriceDetailAdmin)
