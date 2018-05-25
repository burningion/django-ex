"""
WSGI config for project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
from ddtrace import tracer
from ddtrace.contrib.django.conf import settings


# ddtrace.tracer.hostname = os.environ['KUBERNETES_SERVICE_HOST']

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
tracer = settings.TRACER
tracer.configure(hostname=os.environ['KUBERNETES_SERVICE_HOST'])


application = get_wsgi_application()
