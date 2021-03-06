from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


class Company(models.Model):
    company_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField(verbose_name='date published')

    def __str__(self):
        return f'Company name "{self.company_name   }". ({self.id})'


class Manager(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'Manager "{self.name}". ({self.id})'


class Work(models.Model):

    description = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'Work name "{self.description}". ({self.id})'


class Worker(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'Worker. Name: {self.last_name} . ({self.id})'


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

    work = models.ForeignKey(
        Work, on_delete=models.PROTECT)

    worker = models.OneToOneField(
        Worker, models.SET_NULL, blank=True, null=True)

    status = models.CharField(
        max_length=1, choices=STATUS_CHOITHES, default=NEW)

    is_copy = models.BooleanField(default=False)

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
    status = models.CharField(
        max_length=1, choices=STATUS_CHOITHES, default="NEW")
    work_place = models.ForeignKey(WorkPlace,
                                   on_delete=models.CASCADE)

    def set_date_end(self):
        from django.utils import timezone
        self.date_end = timezone.now()
        self.save()

    def __str__(self):
        return f'Work time {self.date_start} ({self.id})'
