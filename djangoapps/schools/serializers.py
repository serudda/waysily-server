from django.contrib.auth.models import User
from rest_framework import serializers

from djangoapps.schools.models import School, Immersion, Tour, Amenities, Accommodation, AccommodationOption, \
    Volunteering, WorkExchange, WorkExchangeOption, Price, PrivateClass, GroupClass, PrivateGeneralType, \
    PrivateIntensiveType, GroupGeneralType, GroupIntensiveType, Discount, Package, PackageOption, BookingFee, \
    PaymentMethod


class ImmersionSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Immersion model """

    class Meta:
        model = Immersion
        fields = ('id',
                  'active',
                  'option',
                  'other_option',
                  'rating',)
        read_only_fields = ('id',)


class TourSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Tour model """

    class Meta:
        model = Tour
        fields = ('id',
                  'active',
                  'option',
                  'city_tour',)
        read_only_fields = ('id',)


class AmenitiesSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Amenities model """

    class Meta:
        model = Amenities
        fields = ('id',
                  'active',
                  'option',
                  'other_option',
                  'rating',)
        read_only_fields = ('id',)


class AccommodationSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Accommodation model """

    class Meta:
        model = Accommodation
        fields = ('id',
                  'active',
                  'option',
                  'rating',)
        read_only_fields = ('id',)


class AccommodationOptionSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Accommodation Options model """

    class Meta:
        model = AccommodationOption
        fields = ('id',
                  'active',
                  'category',
                  'price',
                  'amenities',
                  'other_amenities',)
        read_only_fields = ('id',)


class VolunteeringSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Accommodation Options model """

    class Meta:
        model = Volunteering
        fields = ('id',
                  'active',
                  'option',
                  'rating',)
        read_only_fields = ('id',)


class WorkExchangeSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Work Exchange model """

    class Meta:
        model = WorkExchange
        fields = ('id',
                  'active',
                  'option',)
        read_only_fields = ('id',)


class WorkExchangeOptionSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Work Exchange Option model """

    class Meta:
        model = WorkExchangeOption
        fields = ('id',
                  'active',
                  'category',
                  'terms',)
        read_only_fields = ('id',)


class PriceSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Price model """

    class Meta:
        model = Price
        fields = ('id',
                  'active',
                  'private',
                  'group',)
        read_only_fields = ('id',)


class PrivateClassSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Private Class model """

    class Meta:
        model = PrivateClass
        fields = ('id',
                  'active',
                  'general_type',
                  'intensive_type',)
        read_only_fields = ('id',)


class GroupClassSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Group Class model """

    class Meta:
        model = GroupClass
        fields = ('id',
                  'active',
                  'general_type',
                  'intensive_type',)
        read_only_fields = ('id',)


class PrivateGeneralTypeSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Private general type classes model """

    class Meta:
        model = PrivateGeneralType
        fields = ('id',
                  'active',
                  'value',
                  'hour',
                  'terms',)
        read_only_fields = ('id',)


class PrivateIntensiveTypeSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Private intensive type classes model """

    class Meta:
        model = PrivateIntensiveType
        fields = ('id',
                  'active',
                  'value',
                  'hour',
                  'terms',)
        read_only_fields = ('id',)


class GroupGeneralTypeSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Group general type classes model """

    class Meta:
        model = GroupGeneralType
        fields = ('id',
                  'active',
                  'value',
                  'hour',
                  'terms',
                  'student',)
        read_only_fields = ('id',)


class GroupIntensiveTypeSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Group intensive type classes model """

    class Meta:
        model = GroupIntensiveType
        fields = ('id',
                  'active',
                  'value',
                  'hour',
                  'terms',
                  'student',)
        read_only_fields = ('id',)


class DiscountSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Discount model """

    class Meta:
        model = Discount
        fields = ('id',
                  'active',
                  'option',)
        read_only_fields = ('id',)


class PackageSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Package model """

    class Meta:
        model = Package
        fields = ('id',
                  'active',
                  'option',)
        read_only_fields = ('id',)


class PackageOptionSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Package Option model """

    class Meta:
        model = PackageOption
        fields = ('id',
                  'active',
                  'name',
                  'description',
                  'price',)
        read_only_fields = ('id',)


class BookingFeeSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Booking Fee model """

    class Meta:
        model = BookingFee
        fields = ('id',
                  'active',
                  'price',
                  'terms',)
        read_only_fields = ('id',)


class PaymentMethodSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Payment Method model """

    class Meta:
        model = PaymentMethod
        fields = ('id',
                  'active',
                  'methods',
                  'other',)
        read_only_fields = ('id',)


class SchoolSerializer(serializers.ModelSerializer):
    """ Serializer to represent the School model """

    immersion = ImmersionSerializer()
    tour = TourSerializer()
    amenities = AmenitiesSerializer()
    accommodation = AccommodationSerializer()
    volunteering = VolunteeringSerializer()
    work_exchange = WorkExchangeSerializer()
    price = PriceSerializer()
    discount = DiscountSerializer()
    package = PackageSerializer()
    booking_fee = BookingFeeSerializer()
    payment_method = PaymentMethodSerializer()

    class Meta:
        model = School
        fields = ('id',
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

        read_only_fields = ('id', 'created_at', 'updated_at',)
