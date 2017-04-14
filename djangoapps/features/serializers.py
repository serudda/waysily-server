from rest_framework import serializers
from djangoapps.features.models import Feature


class FeatureSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Feature model """

    class Meta:
        model = Feature
        fields = ('id',
                  'feature_en',
                  'feature_es',
                  'description_en',
                  'description_es',
                  'active',
                  'created_at',
                  'updated_at',)

        read_only_fields = ('id', 'created_at',)


