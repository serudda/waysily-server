from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from djangoapps.profiles.views import ProfileViewSet


user_list = ProfileViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

user_detail = ProfileViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


router = DefaultRouter(trailing_slash=False)

urlpatterns = [
    url(r'users/(?P<pk>[0-9]+)$', user_detail, name='user_detail'),
    url(r'users$', user_list, name='user_list'),
]
