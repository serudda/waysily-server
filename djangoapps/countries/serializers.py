from rest_framework import serializers
from djangoapps.countries.models import Country


class CountrySerializer(serializers.ModelSerializer):
    """ Serializer to represent the Country model """

    class Meta:
        model = Country
        fields = ('id',
                  'code',
                  'created_at',
                  'updated_at',)

        read_only_fields = ('id', 'created_at',)


