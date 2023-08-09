import os
from celery import Celery, shared_task
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', "core.settings")

application = Celery()
application.config_from_object("django.conf:settings", namespace="CELERY")
application.autodiscover_tasks()


application.conf.beat_schedule = {
    'clear-activation-codes': {
        'task': 'clear_activation_codes',
        'schedule': 60*30,
        'args': ()
    },

}
