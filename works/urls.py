#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
from django.urls import path
from . import views

urlpatterns = [
    # ex: /works/ - all companies
    path('', views.index, name='index'),
    # ex: /works/1 - company info
    path('<int:work_id>/', views.info_work, name='info_work'),
    # ex: /works/workers/ - list workers all
    path('workers/', views.info_workers, name='info_workers'),
    # ex: /works/workers/1 - details info for one worker
    path('workers/<int:worker_id>/', views.info_worker, name='info_worker'),
    # ex: /works/1 - company info
    path('<int:work_id>/managers', views.info_managers, name='info_managers'),
    # ex: /works/work/create - Create work
    path('work/create', views.WorkCreate.as_view(), name='work_create'),
]
