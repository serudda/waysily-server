from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import detail_route

from djangoapps.countries.models import Country
from djangoapps.countries.serializers import CountrySerializer


class CountryViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Country objects """
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        """ allow rest api to filter by validated """
        queryset = Country.objects.all()

        return queryset

    @detail_route(methods=['get'])
    def get_by_alias(self, request, alias_country=None):
        queryset = Country.objects.all()
        country = get_object_or_404(queryset, alias_country=alias_country)
        serializer = CountrySerializer(country)

        return Response(serializer.data, status=status.HTTP_200_OK)


