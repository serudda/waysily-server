from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from djangoapps.schools.views import SchoolViewSet

school_list = SchoolViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

school_detail = SchoolViewSet.as_view({
    'get': 'get_by_username',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

router = DefaultRouter(trailing_slash=False)
# router.register(r'schools', SchoolViewSet, base_name='schools')

urlpatterns = [
    url(r'schools$', school_list, name='school_list'),
    url(r'schools/(?P<alias_school>.*)$', school_detail, name='school_detail'),
]
