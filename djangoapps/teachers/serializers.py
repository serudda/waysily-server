from django.contrib.auth.models import User, Group
from rest_framework import serializers

from djangoapps.teachers.models import Profile, Teacher, Language, Immersion, Experience, Education, Certificate, Price, \
    PrivatePriceDetail, GroupPriceDetail, Rating
from djangoapps.locations.models import Location, Position
from djangoapps.locations.serializers import LocationSerializer
from djangoapps.early.serializers import EarlySerializer


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('name', )


class UserSerializer(serializers.ModelSerializer):

    groups = GroupSerializer(many=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'groups')


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


class LanguageSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Language model """

    class Meta:
        model = Language
        fields = ('id',
                  'uid',
                  'native',
                  'teach',
                  'learn',)

        read_only_fields = ('id',)


class ProfileSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Profile model """

    user_id = serializers.CharField(source='user.id', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.CharField(source='user.email')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')

    class Meta:
        model = Profile
        fields = ('user_id',
                  'username',
                  'email',
                  'first_name',
                  'last_name',
                  'phone_number',
                  'gender',
                  'birth_date',
                  'born',
                  'about',
                  'avatar',
                  'created_at',
                  'updated_at',)

        read_only_fields = ('created_at', 'updated_at',)

    def update(self, instance, validated_data):

        user_data = validated_data.pop('user', None)

        user = instance.user

        # Update User model
        if user_data:
            for attr, value in user_data.items():
                setattr(user, attr, value)

        # Update Profile model
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

    def create(self, validated_data):

        # Save User object
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)

        profile = Profile.objects.create(user=user, **validated_data)
        return profile


class TeacherSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Teacher model """

    """
        Profile information
    """
    profile_id = serializers.CharField(source='profile.user_id')
    # username = serializers.CharField(source='profile.user.username', read_only=True)
    # email = serializers.CharField(source='profile.user.email')
    # first_name = serializers.CharField(source='profile.user.first_name')
    # last_name = serializers.CharField(source='profile.user.last_name')
    # phone_number = serializers.CharField(source='profile.phone_number')
    # gender = serializers.CharField(source='profile.gender')
    # birth_date = serializers.DateField(source='profile.birth_date')
    # born = serializers.CharField(source='profile.born')
    # about = serializers.CharField(source='profile.about')
    # avatar = serializers.CharField(source='profile.avatar', allow_blank=True)

    """
        Teacher information
    """
    location = LocationSerializer()
    languages = LanguageSerializer()
    experiences = ExperienceSerializer(many=True, read_only=True, source='experience_set')
    educations = EducationSerializer(many=True, read_only=True, source='education_set')
    certificates = CertificateSerializer(many=True, read_only=True, source='certificate_set')
    ratings = RatingSerializer(many=True, read_only=True, source='rating_set')
    immersion = ImmersionSerializer()
    price = PriceSerializer()

    class Meta:
        model = Teacher
        fields = ('id',
                  'profile_id',
                  'location',
                  'languages',
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

        # Save profileId
        profile_data = validated_data.pop('profile')
        if profile_data:
            profile = Profile.objects.get(**profile_data)
            validated_data['profile'] = profile

        # Save Location object
        location_data = validated_data.pop('location', None)
        if location_data:

            # Save Position object
            position_data = location_data.pop('position', None)

            if position_data:
                position = Position.objects.create(**position_data)
                location_data['position'] = position

            location = Location.objects.create(**location_data)
            validated_data['location'] = location

        # Save Language object
        languages_data = validated_data.pop('languages', None)
        if languages_data:
            languages = Language.objects.create(**languages_data)
            validated_data['languages'] = languages

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

        # teacher = Teacher.objects.create(user=user, **validated_data)
        teacher = Teacher.objects.create(**validated_data)
        return teacher

    # def create(self, validated_data):
    #     # Get location object in order to save on DB
    #     location_data = validated_data.pop('location', None)
    #
    #     if location_data:
    #         # Get position object in order to save on DB
    #         position_data = location_data.pop('position', None)
    #
    #         if position_data:
    #             position = Position.objects.get_or_create(**position_data)[0]
    #             # This part is important to avoid error (Cannot assign "": "" must be a instance)
    #             location_data['position'] = position
    #         location = Location.objects.get_or_create(**location_data)[0]
    #         # This part is important to avoid error (Cannot assign "": "" must be a instance)
    #         validated_data['location'] = location
    #
    #     languages_data = validated_data.pop('languages', None)
    #
    #     if languages_data:
    #         languages = Language.objects.get_or_create(**languages_data)[0]
    #         validated_data['languages'] = languages
    #
    #     immersion_data = validated_data.pop('immersion', None)
    #
    #     if immersion_data:
    #         immersion = Immersion.objects.get_or_create(**immersion_data)[0]
    #         validated_data['immersion'] = immersion
    #
    #     price_data = validated_data.pop('price', None)
    #
    #     if price_data:
    #         # Get private class and group class object in order to save on DB
    #         private_class_data = price_data.pop('private_class', None)
    #         group_class_data = price_data.pop('group_class', None)
    #
    #         if private_class_data:
    #             private_class = PrivatePriceDetail.objects.get_or_create(**private_class_data)[0]
    #             # This part is important to avoid error (Cannot assign "": "" must be a instance)
    #             price_data['private_class'] = private_class
    #
    #         if group_class_data:
    #             group_class = GroupPriceDetail.objects.get_or_create(**group_class_data)[0]
    #             # This part is important to avoid error (Cannot assign "": "" must be a instance)
    #             price_data['group_class'] = group_class
    #
    #         price = Price.objects.get_or_create(**price_data)[0]
    #         # This part is important to avoid error (Cannot assign "": "" must be a instance)
    #         validated_data['price'] = price
    #
    #     return Teacher.objects.create(**validated_data)

    def update(self, instance, validated_data):

        # user_data = validated_data.pop('user')
        profile_data = validated_data.pop('profile')
        location_data = validated_data.pop('location')
        position_data = location_data.pop('position')
        languages_data = validated_data.pop('languages')
        immersion_data = validated_data.pop('immersion')
        price_data = validated_data.pop('price')
        private_class_data = price_data.pop('private_class')
        group_class_data = price_data.pop('group_class')

        profile = instance.profile
        location = instance.location
        position = instance.location.position
        languages = instance.languages
        immersion = instance.immersion
        price = instance.price
        private_class = instance.price.private_class
        group_class = instance.price.group_class

        # Update Profile model
        if profile_data:
            for attr, value in profile_data.items():
                setattr(profile, attr, value)

        # Update Location model
        if location_data:
            for attr, value in location_data.items():
                setattr(location, attr, value)
            location.save()

        # Update Position model
        if position_data:
            for attr, value in position_data.items():
                setattr(position, attr, value)
            position.save()

        # Update Languages model
        if languages_data:
            for attr, value in languages_data.items():
                setattr(languages, attr, value)
            languages.save()

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

    # def update(self, instance, validated_data):
    #     location_data = validated_data.pop('location')
    #     position_data = location_data.pop('position')
    #     languages_data = validated_data.pop('languages')
    #     immersion_data = validated_data.pop('immersion')
    #     price_data = validated_data.pop('price')
    #     private_class_data = price_data.pop('private_class')
    #     group_class_data = price_data.pop('group_class')
    #
    #     languages = instance.languages
    #     immersion = instance.immersion
    #     private_class = instance.price.private_class
    #     group_class = instance.price.group_class
    #     location = instance.location
    #     position = instance.location.position
    #
    #     # Create teacher instance in order to save on DB
    #     instance.uid = validated_data.get('uid', instance.uid)
    #     instance.first_name = validated_data.get('first_name', instance.first_name)
    #     instance.last_name = validated_data.get('last_name', instance.last_name)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.phone_number = validated_data.get('phone_number', instance.phone_number)
    #     instance.sex = validated_data.get('sex', instance.sex)
    #     instance.birth_date = validated_data.get('birth_date', instance.birth_date)
    #     instance.born = validated_data.get('born', instance.born)
    #     instance.about = validated_data.get('about', instance.about)
    #     instance.avatar = validated_data.get('avatar', instance.avatar)
    #     instance.type = validated_data.get('type', instance.type)
    #     instance.teacher_since = validated_data.get('teacher_since', instance.teacher_since)
    #     instance.methodology = validated_data.get('methodology', instance.methodology)
    #     instance.status = validated_data.get('status', instance.status)
    #     instance.recommended = validated_data.get('recommended', instance.recommended)
    #     instance.save()
    #
    #     if location_data:
    #         # Create location instance in order to save on DB
    #         location.uid = location_data.get('uid', location.uid)
    #         location.country = location_data.get('country', location.country)
    #         location.address = location_data.get('address', location.address)
    #         location.city = location_data.get('city', location.city)
    #         location.state = location_data.get('state', location.state)
    #         location.zip_code = location_data.get('zip_code', location.zip_code)
    #         location.save()
    #
    #     if position_data:
    #         # Create position instance in order to save on DB
    #         position.uid = position_data.get('uid', position.uid)
    #         position.lng = position_data.get('lng', position.lng)
    #         position.lat = position_data.get('lat', position.lat)
    #         position.save()
    #
    #     if languages_data:
    #         # Create languages instance in order to save on DB
    #         languages.uid = languages_data.get('uid', languages.uid)
    #         languages.native = languages_data.get('native', languages.native)
    #         languages.teach = languages_data.get('teach', languages.teach)
    #         languages.learn = languages_data.get('learn', languages.learn)
    #         languages.save()
    #
    #     if immersion_data:
    #         # Create immersion instance in order to save on DB
    #         immersion.uid = immersion_data.get('uid', immersion.uid)
    #         immersion.active = immersion_data.get('active', immersion.active)
    #         immersion.other_category = immersion_data.get('other_category', immersion.other_category)
    #         immersion.category = immersion_data.get('category', immersion.category)
    #         immersion.save()
    #
    #     if private_class_data:
    #         # Create private class instance in order to save on DB
    #         private_class.uid = private_class_data.get('uid', private_class.uid)
    #         private_class.active = private_class_data.get('active', private_class.active)
    #         private_class.hour_price = private_class_data.get('hour_price', private_class.hour_price)
    #         private_class.save()
    #
    #     if group_class_data:
    #         # Create private class instance in order to save on DB
    #         group_class.uid = group_class_data.get('uid', group_class.uid)
    #         group_class.active = group_class_data.get('active', group_class.active)
    #         group_class.hour_price = group_class_data.get('hour_price', group_class.hour_price)
    #         group_class.save()
    #
    #     return instance