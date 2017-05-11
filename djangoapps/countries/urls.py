from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from djangoapps.countries.views import CountryViewSet

country_list = CountryViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

country_detail = CountryViewSet.as_view({
    'get': 'get_by_alias',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

country_id_detail = CountryViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

router = DefaultRouter(trailing_slash=False)

urlpatterns = [
    url(r'countries$', country_list, name='country_list'),
    url(r'countries/(?P<alias_country>[a-zA-Z]+)$', country_detail, name='country_detail'),
    url(r'countries/(?P<pk>[0-9]+)$', country_id_detail, name='country_id_detail'),
]