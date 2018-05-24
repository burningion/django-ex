from subprocess import call
import os

command = 'gunicorn wsgi --bind=0.0.0.0:8080 --access-logfile=- --config' 
call(command.split(' '), shell=True)
