from subprocess import call
import os

command = '/opt/app-root/bin/ddtrace-run gunicorn wsgi --bind=0.0.0.0:8080 --access-logfile=-' 
call(command.split(' '), shell=True)
