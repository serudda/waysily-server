from rest_framework import serializers
from locations.models import Location, Position


class PositionSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Position model """
    #id = serializers.ModelField(model_field=Position()._meta.get_field('id'))

    class Meta:
        model = Position
        field = ('id',
                 'lng',
                 'lat',)

        read_only_fields = ('id',)


class LocationSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Location model """
    position = PositionSerializer()
    #id = serializers.ModelField(model_field=Location()._meta.get_field('id'))
    #created_at = serializers.ModelField(model_field=Location()._meta.get_field('created_at'))

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


