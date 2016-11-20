from rest_framework import serializers
from teachers.models import Teacher

class TeacherSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Teacher model """
    class Meta:
        model = Teacher
        fields = ('first_name',
                  'last_name',
                  'email',
                  'phone',
                  'country_birth',
                  'city_birth',
                  'state_birth',
                  'country_live_in',
                  'city_live_in',
                  'state_live_in',
                  'address_live_in',
                  'native_languages',
                  'languages_speak',
                  'created_at',)

        read_only_fields = ('id', 'created_at')