from django.contrib import admin
from .models import (
    Company, Manager, Work, Worker, WorkPlace, WorkTime
)

# Register your models here.

admin.site.register(Company)
admin.site.register(Manager)
admin.site.register(Work)
admin.site.register(Worker)
admin.site.register(WorkPlace)
admin.site.register(WorkTime)
