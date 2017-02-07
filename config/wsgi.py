"""
WSGI config for waysily-server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.dev")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

#application = get_wsgi_application()

application = Cling(get_wsgi_application())

# from django.core.wsgi import get_wsgi_application
# from whitenoise.django import DjangoWhiteNoise
# from dj_static import Cling

# application = Cling(get_wsgi_application())
# application = get_wsgi_application()
# application = DjangoWhiteNoise(application)
