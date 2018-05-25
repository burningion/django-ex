"""
WSGI config for project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import ddtrace


ddtrace.tracer.configure(
    hostname=os.environ['KUBERNETES_SERVICE_HOST'],
)

ddtrace.tracer.set_level('debug')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
ddtrace.patch_all()

application = get_wsgi_application()
