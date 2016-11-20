from rest_framework import viewsets
from teachers.models import Teacher
from teachers.serializers import TeacherSerializer

class TeacherViewSet (viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Teacher objects """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer