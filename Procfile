web: gunicorn shielded-mountain-93739.wsgi
worker: python manage.py celery worker --app=otree.celery.app:app --loglevel=INFO

