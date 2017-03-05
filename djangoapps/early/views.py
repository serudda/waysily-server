from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from djangoapps.early.models import Early
from djangoapps.early.serializers import EarlySerializer


class EarlyViewSet (viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Early Adopter objects """
    queryset = Early.objects.all()
    serializer_class = EarlySerializer
    permission_classes = (AllowAny,)
