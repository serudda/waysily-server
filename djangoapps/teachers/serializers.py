from rest_framework import serializers
from teachers.models import Teacher

class TeacherSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Teacher model """
    class Meta:
        model = Teacher
        fields = ('email',
                  'phone_number',
                  'first_name',
                  'last_name',
                  'sex',
                  'birth_date',
                  'born',
                  'about',
                  'created_at',)

        read_only_fields = ('id', 'created_at')