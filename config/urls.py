"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.contrib import admin

urlpatterns = [
    # admin site urls
    url(r'^admin/', admin.site.urls),
    url(r'^grappelli/', include('grappelli.urls')),

    # api urls
    url(r'^api/v1/', include('early.urls')),
    url(r'^api/v1/', include('teachers.urls')),
    url(r'^api/v1/', include('locations.urls')),
    url(r'^api/v1/', include('feedbacks.urls')),

    # user account and auth urls
    url(r'^', include('usersystem.urls')),

    # user password reset urls
    url(r'^password-reset/confirm/$',
        TemplateView.as_view(template_name="password_reset_confirm.html"),
        name='password-reset-confirm'),
    url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        TemplateView.as_view(template_name="password_reset_confirm.html"),
        name='password_reset_confirm'),
    url(r'^rest-auth/', include('rest_auth.urls')),
]
