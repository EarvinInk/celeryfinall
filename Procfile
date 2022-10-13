web: gunicorn celerytask.wsgi
celery: celery -A celerytask worker --loglevel=info -P eventlet