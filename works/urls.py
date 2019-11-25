#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
from django.urls import path
from . import views

urlpatterns = [
    #ex: /works/
    path('', views.index, name='index'),
    #ex: /works/1
    path('<int:work_id>/', views.info_work, name='info_work'),

]