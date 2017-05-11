from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from djangoapps.features.models import Feature
from djangoapps.features.serializers import FeatureSerializer


class FeatureViewSet (viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Feature objects """
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        """ allow rest api to filter by validated """
        queryset = Feature.objects.all()
        min_id = self.request.query_params.get('minId', None)
        queryset = queryset.filter(active=True)

        if min_id is not None:
            queryset = queryset.filter(pk__gt=min_id)

        return queryset
