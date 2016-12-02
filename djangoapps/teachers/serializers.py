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
        # Get location object in order to save on DB
        location_data = validated_data.pop('location', None)

        if location_data:
            # Get position object in order to save on DB
            position_data = location_data.pop('position', None)
            if position_data:
                position = Position.objects.get_or_create(**position_data)[0]
                # This part is important to avoid error (Cannot assign "": "" must be a instance)
                location_data['position'] = position
            location = Location.objects.get_or_create(**location_data)[0]
            # This part is important to avoid error (Cannot assign "": "" must be a instance)
            validated_data['location'] = location
        return Teacher.objects.create(**validated_data)

    def update(self, instance, validated_data):
        location_data = validated_data.pop('location')
        position_data = location_data.pop('position')

        location = instance.location
        position = instance.location.position

        # Create teacher instance in order to save on DB
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.sex = validated_data.get('sex', instance.sex)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.born = validated_data.get('born', instance.born)
        instance.about = validated_data.get('about', instance.about)
        instance.save()

        if location_data:
            # Create location instance in order to save on DB
            location.country = location_data.get('country', location.country)
            location.address = location_data.get('address', location.address)
            location.city = location_data.get('city', location.city)
            location.state = location_data.get('state', location.state)
            location.zip_code = location_data.get('zip_code', location.zip_code)
            location.save()

        if position_data:
            # Create position instance in order to save on DB
            position.lng = position_data.get('lng', position.lng)
            position.lat = position_data.get('lat', position.lat)
            position.save()

        return instance
