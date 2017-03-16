from __future__ import unicode_literals
from django.contrib import admin

from djangoapps.schools.models import School, Immersion, Tour, Amenities, Accommodation, AccommodationOption,\
    Volunteering, WorkExchange, WorkExchangeOption, Price, PrivateClass, PrivateGeneralType, PrivateIntensiveType,  \
    GroupClass, GroupGeneralType, GroupIntensiveType, Discount, Package, PackageOption, BookingFee, PaymentMethod


# INLINE BLOCKS
class ImmersionInline(admin.StackedInline):
    model = Immersion


class AmenitiesInline(admin.StackedInline):
    model = Amenities

#########################################################


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


class VolunteeringAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'active',
                    'option',
                    'rating',)

    search_fields = ('id',)


class WorkExchangeAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'active',
                    'option',)

    search_fields = ('id',)


class WorkExchangeOptionAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'active',
                    'category',
                    'terms',)

    search_fields = ('id',)


class PriceAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'active',
                    'private',
                    'group',)

    search_fields = ('id',)


class PrivateClassAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'active',
                    'general_type',
                    'intensive_type',)

    search_fields = ('id',)


class PrivateGeneralTypeAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'active',
                    'value',
                    'hour',
                    'terms',)

    search_fields = ('id',)


class PrivateIntensiveTypeAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'active',
                    'value',
                    'hour',
                    'terms',)

    search_fields = ('id',)


class GroupClassAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'active',
                    'general_type',
                    'intensive_type',)

    search_fields = ('id',)


class GroupGeneralTypeAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'active',
                    'value',
                    'hour',
                    'terms',
                    'student',)

    search_fields = ('id',)


class GroupIntensiveTypeAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'active',
                    'value',
                    'hour',
                    'terms',
                    'student',)

    search_fields = ('id',)


class DiscountAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'active',
                    'option',)

    search_fields = ('id',)


class PackageAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'active',
                    'option',)

    search_fields = ('id',)


class PackageOptionAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'active',
                    'name',
                    'description',
                    'price',)

    search_fields = ('id',)


class BookingFeeAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'active',
                    'price',
                    'terms',)

    search_fields = ('id',)


class PaymentMethodAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'active',
                    'methods',
                    'other',)

    search_fields = ('id',)


admin.site.register(School, SchoolAdmin)
admin.site.register(Immersion, ImmersionAdmin)
admin.site.register(Tour, TourAdmin)
admin.site.register(Amenities, AmenitiesAdmin)
admin.site.register(Accommodation, AccommodationAdmin)
admin.site.register(AccommodationOption, AccommodationOptionAdmin)
admin.site.register(Volunteering, VolunteeringAdmin)
admin.site.register(WorkExchange, WorkExchangeAdmin)
admin.site.register(WorkExchangeOption, WorkExchangeOptionAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(PrivateClass, PrivateClassAdmin)
admin.site.register(PrivateGeneralType, PrivateGeneralTypeAdmin)
admin.site.register(PrivateIntensiveType, PrivateIntensiveTypeAdmin)
admin.site.register(GroupClass, GroupClassAdmin)
admin.site.register(GroupGeneralType, GroupGeneralTypeAdmin)
admin.site.register(GroupIntensiveType, GroupIntensiveTypeAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(Package, PackageAdmin)
admin.site.register(PackageOption, PackageOptionAdmin)
admin.site.register(BookingFee, BookingFeeAdmin)
admin.site.register(PaymentMethod, PaymentMethodAdmin)
