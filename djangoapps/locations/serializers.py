from rest_framework import serializers
from locations.models import Location, Position


class PositionSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Position model """
    class Meta:
        model = Position
        field = ('id',
                 'lng',
                 'lat',)

        read_only_fields = ('id',)


class LocationSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Location model """
    position = PositionSerializer()

    class Meta:
        model = Location
        fields = ('id',
                  'country',
                  'address',
                  'city',
                  'state',
                  'position',
                  'zip_code',
                  'created_at',
                  'updated_at',)

        read_only_fields = ('id', 'created_at',)


