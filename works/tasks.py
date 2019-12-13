
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from math import sqrt
from workers_management.celery import app

@app.task(name="works.tasks.square_root")
def square_root(value):
    return sqrt(value)


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)