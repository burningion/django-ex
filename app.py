from subprocess import call

# Run gunicorn wrapped in ddtrace-run
command = 'python manage.py migrate'
call(command.split(' '))
command = '/opt/app-root/bin/ddtrace-run gunicorn wsgi:application --bind=0.0.0.0:8080 --access-logfile=-' 
call(command.split(' '))
