"""
WSGI config for project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import ddtrace


ddtrace.tracer.configure(
    hostname=os.environ['DD_AGENT_SERVICE_HOST'],
    port=os.environ['DD_AGENT_SERVICE_PORT'],
)

ddtrace.patch_all()

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

application = get_wsgi_application()
