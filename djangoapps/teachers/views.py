from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import detail_route

from teachers.models import Teacher, Experience
from teachers.serializers import TeacherSerializer, ExperienceSerializer


class ExperienceViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Experience objects """
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class TeacherViewSet (viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Teacher objects """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    @detail_route(methods=['post'])
    def set_experience(self, request, pk=None):

        # get teacher object
        teacher = self.get_object()
        serializer = ExperienceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(teacher=teacher)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
