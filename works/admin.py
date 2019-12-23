from django.contrib import admin
from .models import (
    Companies, Manager, Work, Worker, WorkPlace, WorkTime, Statistics
)

# Register your models here.

admin.site.register(Companies)
admin.site.register(Manager)
admin.site.register(Work)
admin.site.register(Worker)
admin.site.register(WorkPlace)
admin.site.register(WorkTime)
admin.site.register(Statistics)