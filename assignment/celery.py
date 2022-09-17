import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'assignment.settings')
app = Celery('assignment',include=['performance.slowIterationCelery'])
app.config_from_object('django.conf:settings')
from django.apps import apps
app.autodiscover_tasks(lambda: [n.name for n in apps.get_app_configs()])
