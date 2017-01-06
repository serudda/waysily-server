from rest_framework import viewsets
from countries.models import Country
from countries.serializers import CountrySerializer


class CountryViewSet (viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Location objects """
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
