from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'start_celery.settings')

app = Celery('start_celery')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Dhaka')

app.config_from_object(settings, namespace='CELERY')

app.autodiscover_tasks()

# DJANGO BEAT SETTING 

app.conf.beat_schedule ={
    
}

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")