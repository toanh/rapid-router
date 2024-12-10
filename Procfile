# Uncomment this `release` process if you are using a database, so that Django's model
# migrations are run as part of app deployment, using Heroku's Release Phase feature:
# https://docs.djangoproject.com/en/5.1/topics/migrations/
# https://devcenter.heroku.com/articles/release-phase
release: ./example_project/manage.py migrate --no-input
release: ./example_project/manage.py collectstatic --noinput --clear

web: gunicorn --config gunicorn.conf.py example_project.wsgi