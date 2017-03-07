from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from djangoapps.locations.views import LocationViewSet


router = DefaultRouter(trailing_slash=False)
router.register(r'locations', LocationViewSet, base_name='locations')


urlpatterns = [
    url(r'^', include(router.urls)),
]
