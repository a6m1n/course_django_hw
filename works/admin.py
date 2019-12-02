from django.contrib import admin
from .models import (
    Companies, Manager, Work, Worker, Work_place, Fineshed_work, WorkTime
)

# Register your models here.

admin.site.register(Companies)
admin.site.register(Manager)
admin.site.register(Work)
admin.site.register(Worker)
admin.site.register(Work_place)
admin.site.register(WorkTime)
admin.site.register(Fineshed_work)
