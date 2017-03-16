from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from djangoapps.schools.models import School
from djangoapps.schools.serializers import SchoolSerializer


class SchoolViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing School objects """
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
