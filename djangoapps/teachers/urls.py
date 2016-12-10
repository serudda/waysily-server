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

experience_detail = ExperienceViewSet.as_view({
    'get': 'retrieve',
    'put': 'update'
})

experience_list = TeacherViewSet.as_view({
    'get': 'get_experience_list',
    'post': 'set_experience'
})

router = DefaultRouter(trailing_slash=False)

urlpatterns = [
    url(r'teachers$', teacher_list, name='teacher_list'),
    url(r'teachers/(?P<pk>[0-9]+)$', teacher_detail, name='teacher_detail'),
    url(r'teachers/(?P<pk>[0-9]+)/experiences$', experience_list, name='experience_list'),
    url(r'experiences/(?P<pk>[0-9]+)$', experience_detail, name='experience_detail')
]
