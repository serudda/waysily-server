from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import detail_route

from djangoapps.schools.models import School
from djangoapps.schools.serializers import SchoolSerializer


class SchoolViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing School objects """
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        """ allow rest api to filter by validated """
        queryset = School.objects.all()
        status_school = self.request.query_params.get('status', None)
        country = self.request.query_params.get('country', None)

        if country is not None:
            queryset = queryset.filter(country=country)

        if status_school is not None:
            queryset = queryset.filter(status=status_school)

        return queryset

    # TODO: Cambiar por get_by_alias cuando se pueda
    @detail_route(methods=['get'])
    def get_by_username(self, request, alias_school=None):
        queryset = School.objects.all()
        school = get_object_or_404(queryset, alias_school=alias_school)
        serializer = SchoolSerializer(school)

        return Response(serializer.data, status=status.HTTP_200_OK)

