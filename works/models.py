from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save



class Companies(models.Model):
    company_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField(verbose_name='date published')

    def __str__(self):
        return f'Company name "{self.company_name}". ({self.id})'


class Manager(models.Model):
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return f'Manager "{self.name}". ({self.id})'


class Work(models.Model):
    description = models.CharField(max_length=200)
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'Work name "{self.description}". ({self.id})'


class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Name: {self.user.last_name}. ({self.id})'


class WorkPlace(models.Model):
    FINISHED = "F"
    NEW = "N"
    APPROVED = "A"
    CANCELLED = "C"

    STATUS_CHOITHES = (
        ("F", "Finished"),
        ("N", "New"),
        ("A", "Approved"),
        ("C", "Cancelled"),
    )

    work = models.ForeignKey(Work, on_delete=models.PROTECT)
    worker = models.OneToOneField(Worker, models.PROTECT, blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOITHES, default=NEW)
    is_copy = models.BooleanField(default=False)
    limit_hours = models.PositiveIntegerField()

    def __str__(self):
        return f'Work place {self.work} - {self.worker}. ({self.id})'


class WorkTime(models.Model):
    NEW = "N"
    APPROVED = "A"
    CANCELLED = "C"

    STATUS_CHOITHES = (
        ("N", "New"),
        ("A", "Approved"),
        ("C", "Cancelled"),
    )

    date_start = models.DateTimeField()
    date_end = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOITHES, default="NEW")
    work_place = models.ForeignKey(WorkPlace, on_delete=models.CASCADE)



    def set_date_end(self):
        from django.utils import timezone
        self.date_end = timezone.now()
        self.save()

    def __str__(self):
        return f'Work time {self.date_start} ({self.id})'

class Statistics(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.PROTECT)
    number_weak = models.PositiveIntegerField()
    work_time_in_weak = models.PositiveIntegerField()

    def timedelta_to_sec(time):
        return time.total_seconds()

    def __str__(self):
        return f'Statistics for {self.worker} ({self.id})'

