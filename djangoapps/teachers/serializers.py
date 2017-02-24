from django.contrib.auth.models import User
from rest_framework import serializers

from djangoapps.teachers.models import Teacher, Immersion, Experience, Education, Certificate, Price, \
    PrivatePriceDetail, GroupPriceDetail, Rating
from djangoapps.profiles.models import Profile
from djangoapps.profiles.serializers import ProfileSerializer
from djangoapps.early.serializers import EarlySerializer


class PrivatePriceDetailSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Private Classes PriceDetail model """

    class Meta:
        model = PrivatePriceDetail
        fields = ('id',
                  'uid',
                  'active',
                  'hour_price',)
        read_only_fields = ('id',)


class GroupPriceDetailSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Group Classes PriceDetail model """

    class Meta:
        model = GroupPriceDetail
        fields = ('id',
                  'uid',
                  'active',
                  'hour_price',)
        read_only_fields = ('id',)


class PriceSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Price model """
    private_class = PrivatePriceDetailSerializer()
    group_class = GroupPriceDetailSerializer()

    class Meta:
        model = Price
        fields = ('id',
                  'uid',
                  'private_class',
                  'group_class',)
        read_only_fields = ('id',)


class ImmersionSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Immersion model """

    class Meta:
        model = Immersion
        fields = ('id',
                  'uid',
                  'active',
                  'category',
                  'other_category',)
        read_only_fields = ('id',)


class CertificateSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Certificate model """

    class Meta:
        model = Certificate
        fields = ('id',
                  'uid',
                  'name',
                  'institution',
                  'date_received',
                  'description',)

        read_only_fields = ('id',)


class EducationSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Education model """

    class Meta:
        model = Education
        fields = ('id',
                  'uid',
                  'school',
                  'degree',
                  'field_study',
                  'date_start',
                  'date_finish',
                  'description',)

        read_only_fields = ('id',)


class RatingSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Rating model """
    author = EarlySerializer()

    class Meta:
        model = Rating
        fields = ('id',
                  'uid',
                  'author',
                  'methodology_value',
                  'teaching_value',
                  'communication_value',
                  'review',
                  'created_at',
                  'updated_at',)

        read_only_fields = ('id',)


class ExperienceSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Experience model """

    class Meta:
        model = Experience
        fields = ('id',
                  'uid',
                  'position',
                  'company',
                  'city',
                  'country',
                  'date_start',
                  'date_finish',
                  'description',)

        read_only_fields = ('id',)


class TeacherSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Teacher model """

    """
        Profile information
    """
    profile = ProfileSerializer()

    """
        Teacher information
    """
    experiences = ExperienceSerializer(many=True, read_only=True, source='experience_set')
    educations = EducationSerializer(many=True, read_only=True, source='education_set')
    certificates = CertificateSerializer(many=True, read_only=True, source='certificate_set')
    ratings = RatingSerializer(many=True, read_only=True, source='rating_set')
    immersion = ImmersionSerializer()
    price = PriceSerializer()

    class Meta:
        model = Teacher
        fields = ('id',
                  'profile',
                  'type',
                  'teacher_since',
                  'methodology',
                  'experiences',
                  'educations',
                  'certificates',
                  'immersion',
                  'price',
                  'status',
                  'recommended',
                  'ratings',
                  'created_at',
                  'updated_at',)

        read_only_fields = ('created_at', 'updated_at',)

    def create(self, validated_data):

        # Save Profile
        profile_data = validated_data.pop('profile')
        if profile_data:
            user_data = profile_data.pop('user')
            user = User.objects.get(**user_data)
            profile = Profile.objects.get(user_id=user.id)
            validated_data['profile'] = profile

        # Save Immersion object
        immersion_data = validated_data.pop('immersion', None)
        if immersion_data:
            immersion = Immersion.objects.create(**immersion_data)
            validated_data['immersion'] = immersion

        # Save Price object
        price_data = validated_data.pop('price', None)
        if price_data:

            # Save Private Class Price object
            private_class_data = price_data.pop('private_class', None)

            if private_class_data:
                private_class = PrivatePriceDetail.objects.create(**private_class_data)
                price_data['private_class'] = private_class

            # Save Group Class Price object
            group_class_data = price_data.pop('group_class', None)

            if group_class_data:
                group_class = GroupPriceDetail.objects.create(**group_class_data)
                price_data['group_class'] = group_class

            price = Price.objects.create(**price_data)
            validated_data['price'] = price

        teacher = Teacher.objects.create(**validated_data)
        return teacher

    def update(self, instance, validated_data):

        # Remove profile information in order to manage it in Profile serializer
        profile_data = validated_data.pop('profile')
        profile_data.pop('user')

        immersion_data = validated_data.pop('immersion')
        price_data = validated_data.pop('price')
        private_class_data = price_data.pop('private_class')
        group_class_data = price_data.pop('group_class')

        immersion = instance.immersion
        price = instance.price
        private_class = instance.price.private_class
        group_class = instance.price.group_class

        # Update Immersion model
        if immersion_data:
            for attr, value in immersion_data.items():
                setattr(immersion, attr, value)
            immersion.save()

        # Update Price model
        if price_data:
            for attr, value in price_data.items():
                setattr(price, attr, value)
            price.save()

        # Update Private Classes Price model
        if private_class_data:
            for attr, value in private_class_data.items():
                setattr(private_class, attr, value)
            private_class.save()

        # Update Group Classes Price model
        if group_class_data:
            for attr, value in group_class_data.items():
                setattr(group_class, attr, value)
            group_class.save()

        # Update Teacher model
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
