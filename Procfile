release: ./example_project/manage.py migrate --no-input
release: ./example_project/manage.py collectstatic --noinput --clear

web: gunicorn --config gunicorn.conf.py example_project.wsgi