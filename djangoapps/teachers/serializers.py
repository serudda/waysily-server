from rest_framework import serializers
from teachers.models import Teacher
from locations.models import Location, Position
from locations.serializers import LocationSerializer


class TeacherSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Teacher model """
    location = LocationSerializer()

    class Meta:
        model = Teacher
        fields = ('id',
                  'location',
                  'email',
                  'phone_number',
                  'first_name',
                  'last_name',
                  'sex',
                  'birth_date',
                  'born',
                  'about',
                  'created_at',
                  'updated_at',)

        read_only_fields = ('id', 'created_at',)

    def create(self, validated_data):
        """Create and return a new `Teacher` instance, given the validated data."""
        """Get location object in order to save on DB"""
        location_data = validated_data.pop('location', None)

        if location_data:
            """Get position object in order to save on DB"""
            position_data = location_data.pop('position', None)
            if position_data:
                position = Position.objects.get_or_create(**position_data)[0]
                """This part is important to avoid error (Cannot assign "": "" must be a instance)"""
                location_data['position'] = position
            location = Location.objects.get_or_create(**location_data)[0]
            """This part is important to avoid error (Cannot assign "": "" must be a instance)"""
            validated_data['location'] = location
        return Teacher.objects.create(**validated_data)

