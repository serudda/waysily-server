from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from teachers.views import TeacherViewSet, ExperienceViewSet, EducationViewSet, CertificateViewSet, RatingViewSet


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

education_detail = EducationViewSet.as_view({
    'get': 'retrieve',
    'put': 'update'
})

education_list = TeacherViewSet.as_view({
    'get': 'get_education_list',
    'post': 'set_education'
})

certificate_detail = CertificateViewSet.as_view({
    'get': 'retrieve',
    'put': 'update'
})

certificate_list = TeacherViewSet.as_view({
    'get': 'get_certificate_list',
    'post': 'set_certificate'
})

rating_detail = RatingViewSet.as_view({
    'get': 'retrieve',
    'put': 'update'
})

rating_list = TeacherViewSet.as_view({
    'get': 'get_rating_list',
    'post': 'set_rating'
})

router = DefaultRouter(trailing_slash=False)

urlpatterns = [
    url(r'teachers$', teacher_list, name='teacher_list'),
    url(r'teachers/(?P<pk>[0-9]+)$', teacher_detail, name='teacher_detail'),
    url(r'teachers/(?P<pk>[0-9]+)/experiences$', experience_list, name='experience_list'),
    url(r'experiences/(?P<pk>[0-9]+)$', experience_detail, name='experience_detail'),
    url(r'teachers/(?P<pk>[0-9]+)/educations$', education_list, name='education_list'),
    url(r'educations/(?P<pk>[0-9]+)$', education_detail, name='education_detail'),
    url(r'teachers/(?P<pk>[0-9]+)/certificates$', certificate_list, name='certificate_list'),
    url(r'certificates/(?P<pk>[0-9]+)$', certificate_detail, name='certificate_detail'),
    url(r'teachers/(?P<pk>[0-9]+)/ratings$', rating_list, name='rating_list'),
    url(r'ratings/(?P<pk>[0-9]+)$', rating_detail, name='rating_detail'),
]
