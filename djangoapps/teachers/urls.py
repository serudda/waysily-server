from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter


from teachers.views import TeacherViewSet


router = DefaultRouter()
router.register(r'teachers', TeacherViewSet, base_name='teacher')


urlpatterns = [
    url(r'^', include(router.urls)),
]