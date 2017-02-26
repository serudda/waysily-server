from django.contrib.auth.models import User, Group
from rest_framework import serializers

from djangoapps.teachers.models import Profile
from djangoapps.profiles.models import Language
from djangoapps.locations.models import Location, Position

from djangoapps.locations.serializers import LocationSerializer


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('name', )


class UserSerializer(serializers.ModelSerializer):

    groups = GroupSerializer(many=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'groups')


class LanguageSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Language model """

    class Meta:
        model = Language
        fields = ('id',
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
    languages = LanguageSerializer()
    location = LocationSerializer()

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
                  'born_country',
                  'born_city',
                  'about',
                  'avatar',
                  'languages',
                  'location',
                  'created_at',
                  'updated_at',)

        read_only_fields = ('created_at', 'updated_at',)

    def create(self, validated_data):

        # Save User object
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)

        # Save Language object
        languages_data = validated_data.pop('languages', None)
        if languages_data:
            languages = Language.objects.create(**languages_data)
            validated_data['languages'] = languages

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

        profile = Profile.objects.create(user=user, **validated_data)
        return profile

    def update(self, instance, validated_data):

        user_data = validated_data.pop('user')
        languages_data = validated_data.pop('languages')
        location_data = validated_data.pop('location')
        position_data = location_data.pop('position')

        user = instance.user
        languages = instance.languages
        location = instance.location
        if location is not None:
            position = instance.location.position
        else:
            position = None

        # Update User model
        if user_data:
            for attr, value in user_data.items():
                setattr(user, attr, value)
            user.save()

        # Update Languages model
        if languages_data:
            if languages is not None:
                for attr, value in languages_data.items():
                    setattr(languages, attr, value)
                languages.save()
            else:
                languages = Language.objects.create(**languages_data)
                validated_data['languages'] = languages

        # Update Position model
        if position_data:
            if position is not None:
                for attr, value in position_data.items():
                    setattr(position, attr, value)
                position.save()
            else:
                position = Position.objects.create(**position_data)
                location_data['position'] = position

        # Update Location model
        if location_data:
            if location is not None:
                for attr, value in location_data.items():
                    setattr(location, attr, value)
                location.save()
            else:
                location = Location.objects.create(**location_data)
                validated_data['location'] = location

        # Update Profile model
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
