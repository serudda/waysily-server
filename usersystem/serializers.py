from django.contrib.auth.models import User, Group
from rest_framework import serializers
from usersystem import settings


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('name', )


class UserSerializer(serializers.ModelSerializer):

    groups = GroupSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'groups', 'date_joined')


class UserRegisterSerializer(serializers.ModelSerializer):
    """
    A serializer for registering users
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {
            'username': {'required': True, 'max_length': settings.USERNAME_MAX_LENGTH,
                         'min_length': settings.USERNAME_MIN_LENGTH},
            'email': {'required': True},
            'password': {'required': True, 'max_length': settings.PASSWORD_MAX_LENGTH,
                         'min_length': settings.PASSWORD_MIN_LENGTH},
            'first_name': {'required': True},
            'last_name': {'required': True},
        }
