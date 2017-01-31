from rest_framework import serializers
from early.models import Early


class EarlySerializer(serializers.ModelSerializer):
    """ Serializer to represent the Early Adopter model """
    class Meta:
        model = Early
        fields = ('id', 'uid', 'first_name', 'last_name', 'email', 'comment', 'created_at')
        read_only_fields = ('id', 'created_at')