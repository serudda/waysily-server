from rest_framework import viewsets

from djangoapps.locations.models import Location
from djangoapps.locations.serializers import LocationSerializer


class LocationViewSet (viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Location objects """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
