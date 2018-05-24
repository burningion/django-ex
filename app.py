from subprocess import call
import os

command = 'DATADOG_TRACE_DEBUG=true /opt/app-root/bin/ddtrace-run gunicorn wsgi:application --bind=0.0.0.0:8080 --access-logfile=-' 
call(command.split(' '))
