from subprocess import call
import os

module = os.environ['APP_MODULE']
app_config = os.environ['APP_CONFIG']
command = 'gunicorn %s --bind=0.0.0.0:8080 --access-logfile=- --config %s' % (module, app_config)
call(command.split(' '), shell=True)
