from subprocess import call
command = 'gunicorn "$APP_MODULE" --bind=0.0.0.0:8080 --access-logfile=- --config "$APP_CONFIG"'
call(command.split(' '), shell=True)
