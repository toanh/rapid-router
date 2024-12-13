release: ./example_project/manage.py collectstatic --noinput --clear
release: ./example_project/manage.py migrate --no-input

web: gunicorn --config gunicorn.conf.py example_project.wsgi