from rest_framework import viewsets
from locations.models import Location
from locations.serializers import LocationSerializer


class LocationViewSet (viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Location objects """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
