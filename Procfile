release: python manage.py makemigrations && python manage.py migrate
web: gunicorn snaps_api.wsgi