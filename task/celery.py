import os
from celery import Celery

# setting the Django settings module.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task.settings')
app = Celery('task')
app.config_from_object('django.conf:settings', namespace='CELERY')
# app.conf.broker_transport_options = {'visibility_timeout': 3600}  # 1 hour.
# Looks up for task modules in Django applications and loads them
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
