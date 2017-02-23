from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from djangoapps.teachers.models import Profile
from djangoapps.teachers.serializers import ProfileSerializer

from djangoapps.profiles.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # TODO: Remover esto cuando termine de probar
    permission_classes = (IsAuthenticatedOrReadOnly,)


