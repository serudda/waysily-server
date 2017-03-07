from rest_framework import viewsets
from djangoapps.countries import models
from djangoapps.countries import serializers


class CountryViewSet (viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Location objects """
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer
