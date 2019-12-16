# from __future__ import absolute_import, unicode_literals
# import os
# from celery import Celery

# # set the default Django settings module for the 'celery' program.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'workers_management.settings')

# app = Celery('workers_management')

# # Using a string here means the worker doesn't have to serialize
# # the configuration object to child processes.
# # - namespace='CELERY' means all celery-related configuration keys
# #   should have a `CELERY_` prefix.
# app.config_from_object('django.conf:settings', namespace='CELERY')

# # Load task modules from all registered Django app configs.
# app.autodiscover_tasks()


# @app.task(bind=True)
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))


import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'workers_management.settings')
app = Celery(
   'tasks',
   broker='redis://127.0.0.1:6379/0',
   backend='redis://127.0.0.1:6379/1'
)
# Загрузка конфигурации из Django settings.py
# namespace='CELERY' обозначает что все celery конфиги будут называться с частицы 'CELERY_'
app.config_from_object('django.conf:settings', namespace='CELERY')
# автоматически искать файлы tasks.py в каждом приложении Django
app.autodiscover_tasks()

