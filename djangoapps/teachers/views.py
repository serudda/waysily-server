from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import detail_route, list_route

from teachers.models import Teacher, Experience
from teachers.serializers import TeacherSerializer, ExperienceSerializer


class ExperienceViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Experience objects """
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

    """ SIRVE PARA SOBREESCRIBIR EL METODO GET (UN SOLO ELEMENTO)
    @detail_route(methods=['get'])
    def get_experience(self, request, pk=None):
        queryset = Experience.objects.all()
        experience = get_object_or_404(queryset, pk=pk)
        serializer = ExperienceSerializer(experience)
        return Response(serializer.data, status=status.HTTP_200_OK)"""


class TeacherViewSet (viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Teacher objects """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    @list_route(methods=['get'])
    def get_experience_list(self, request, pk=None):

        # get experiences list
        queryset = Experience.objects.all()
        serializer = ExperienceSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @detail_route(methods=['post'])
    def set_experience(self, request, pk=None):

        # get teacher object
        teacher = self.get_object()
        serializer = ExperienceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(teacher=teacher)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
