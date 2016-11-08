from rest_framework import viewsets
from early.models import Early
from early.serializers import EarlySerializer

class EarlyViewSet (viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Early Adopter objects """
    queryset = Early.objects.all()
    serializer_class = EarlySerializer