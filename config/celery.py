import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.django.dev')

celery = Celery('config')
celery.config_from_object('django.conf:django', namespace='CELERY')
celery.conf.broker_connection_retry_on_startup=True
celery.autodiscover_tasks()