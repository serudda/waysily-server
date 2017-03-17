from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from djangoapps.schools.views import SchoolViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'schools', SchoolViewSet, base_name='school')


urlpatterns = [
    url(r'^', include(router.urls)),
]