from rest_framework import serializers
from djangoapps.countries.models import Country


class CountrySerializer(serializers.ModelSerializer):
    """ Serializer to represent the Country model """

    class Meta:
        model = Country
        fields = ('id',
                  'alias_country',
                  'name_en',
                  'name_es',
                  'description_en',
                  'description_es',
                  'recommend',
                  'currency_code',
                  'currency_name',
                  'code',
                  'capital',
                  'zone',
                  'photo',
                  'thumbnail',
                  'active',
                  'created_at',
                  'updated_at',)

        read_only_fields = ('id', 'created_at',)


