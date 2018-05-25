from subprocess import call
import os

# Set this to be the name of the Agent service defined in your Agent YAML
myenv = os.environ.copy()
myenv['DATADOG_TRACE_AGENT_HOSTNAME'] = os.environ['KUBERNETES_SERVICE_HOST']

# Run gunicorn wrapped in ddtrace-run
command = '/opt/app-root/bin/ddtrace-run gunicorn wsgi:application --bind=0.0.0.0:8080 --access-logfile=-' 
print(myenv['KUBERNETES_SERVICE_HOST'])
call(command.split(' '), env=myenv)
