from rest_framework import serializers
from djangoapps.countries.models import Country


class CountrySerializer(serializers.ModelSerializer):
    """ Serializer to represent the Country model """

    class Meta:
        model = Country
        fields = ('id',
                  'name_en',
                  'name_es',
                  'alias_country',
                  'code',
                  'photo',
                  'thumbnail',
                  'active',
                  'created_at',
                  'updated_at',)

        read_only_fields = ('id', 'created_at',)


