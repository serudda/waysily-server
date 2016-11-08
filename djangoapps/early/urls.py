from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter


from early.views import EarlyViewSet


router = DefaultRouter()
router.register(r'early', EarlyViewSet, base_name='early')


urlpatterns = [
    url(r'^', include(router.urls)),
]