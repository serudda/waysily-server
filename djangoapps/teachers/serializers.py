from rest_framework import serializers
from teachers.models import Teacher
from locations.models import Location, Position
from locations.serializers import LocationSerializer


class TeacherSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Teacher model """
    location = LocationSerializer()
    #created_at = serializers.ModelField(model_field=Teacher()._meta.get_field('created_at'))

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

    """def update(self, instance, validated_data):
        # Update teacher instance
        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.email = validated_data['email']
        instance.phone_number = validated_data['phone_number']
        instance.sex = validated_data['sex']
        instance.birth_date = validated_data['birth_date']
        instance.born = validated_data['born']
        instance.about = validated_data['about']

        location = validated_data['location']
        country = location['country']
        address = location['address']
        city = location['city']
        state = location['state']
        zip_code = location['zip_code']
        location_instance = Location(country=country,
                                     address=address,
                                     city=city,
                                     state=state,
                                     zip_code=zip_code,)

        position = location['position']
        lng = position['lng']
        lat = position['lat']
        position_instance = Position(lng=lng,
                                     lat=lat)

        position_instance.save()

        location_instance.save()

        instance.save()

        return instance"""

    def update(self, instance, validated_data):
        location_data = validated_data.pop('location')
        position_data = location_data.pop('position')

        location = instance.location
        position = instance.location.position

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
            location.country = location_data.get('country', location.country)
            location.address = location_data.get('address', location.address)
            location.city = location_data.get('city', location.city)
            location.state = location_data.get('state', location.state)
            location.zip_code = location_data.get('zip_code', location.zip_code)
            location.save()

        if position_data:
            position.lng = position_data.get('lng', position.lng)
            position.lat = position_data.get('lat', position.lat)
            position.save()

        return instance
