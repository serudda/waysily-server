from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter


from djangoapps.features.views import FeatureViewSet


router = DefaultRouter(trailing_slash=False)
router.register(r'features', FeatureViewSet, base_name='features')


urlpatterns = [
    url(r'^', include(router.urls)),
]