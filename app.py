from subprocess import call
import os

# Set this to be the name of the Agent service defined in your Agent YAML
os.environ['DATADOG_TRACE_AGENT_HOSTNAME'] = 'dd-agent'

# Run gunicorn wrapped in ddtrace-run
command = '/opt/app-root/bin/ddtrace-run gunicorn wsgi:application --bind=0.0.0.0:8080 --access-logfile=-' 

call(command.split(' '))
