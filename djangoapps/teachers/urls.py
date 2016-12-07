from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from teachers.views import TeacherViewSet, ExperienceViewSet


teacher_list = TeacherViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

teacher_detail = TeacherViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

experience_creation = TeacherViewSet.as_view({
    'post': 'set_experience'
})

router = DefaultRouter(trailing_slash=False)

urlpatterns = [
    url(r'teachers/$', teacher_list, name='teacher_list'),
    url(r'teachers/(?P<pk>[0-9]+)/$', teacher_detail, name='teacher_detail'),
    url(r'teachers/(?P<pk>[0-9]+)/experiences/$', experience_creation, name='experience_creation')
]
