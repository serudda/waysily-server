from __future__ import unicode_literals
from django.contrib import admin

from djangoapps.schools.models import School, Immersion, Tour, Amenities, Accommodation, AccommodationOption,\
    Volunteering, WorkExchange, Price, Discount, Package, PaymentMethod


class SchoolAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'user',
                    'name',
                    'photo',
                    'about',
                    'language_teach',
                    'website',
                    'facebook',
                    'twitter',
                    'instagram',
                    'email',
                    'facebook_group',
                    'meetup_group',
                    'immersion',
                    'language_exchange',
                    'tour',
                    'amenities',
                    'atmosphere',
                    'accommodation',
                    'volunteering',
                    'work_exchange',
                    'price',
                    'discount',
                    'package',
                    'booking_fee',
                    'classes_begin',
                    'payment_method',
                    'created_at',
                    'updated_at',)

    search_fields = ('id',)

    ordering = ('-created_at',)


class ImmersionAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'active',
                    'option',
                    'other_option',
                    'rating',)

    search_fields = ('id',)


class TourAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'active',
                    'option',
                    'city_tour',)

    search_fields = ('id',)


class AmenitiesAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'active',
                    'option',
                    'other_option',
                    'rating',)

    search_fields = ('id',)


class AccommodationOptionAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'active',
                    'category',
                    'price',
                    'amenities',
                    'other_amenities',)

    search_fields = ('id',)


class AccommodationAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'active',
                    'option',
                    'rating',)

    search_fields = ('id',)


admin.site.register(School, SchoolAdmin)
admin.site.register(Immersion, ImmersionAdmin)
admin.site.register(Tour, TourAdmin)
admin.site.register(Amenities, AmenitiesAdmin)
admin.site.register(Accommodation, AccommodationAdmin)
admin.site.register(AccommodationOption, AccommodationOptionAdmin)
