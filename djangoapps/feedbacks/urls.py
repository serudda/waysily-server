from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter


from djangoapps.feedbacks.views import FeedbackViewSet


router = DefaultRouter(trailing_slash=False)
router.register(r'feedbacks', FeedbackViewSet, base_name='feedbacks')


urlpatterns = [
    url(r'^', include(router.urls)),
]