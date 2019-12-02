from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


class Companies(models.Model):
    company_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField(verbose_name='date published')

    def __str__(self):
        return f'Company name "{self.company_name   }". ({self.id})'


class Manager(models.Model):
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'Manager "{self.name}". ({self.id})'


class Work(models.Model):
    description = models.CharField(max_length=200)
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)

    def __str__(self):
        return f'Work name "{self.description}". ({self.id})'


class Worker(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'Worker. Name: {self.last_name} . ({self.id})'


class WorkTime(models.Model):

    STATUS_CHOITHES = (
        (1, "New"),
        (2, "Approved"),
        (3, "Cancelled"),
    )

    date_start = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(
        max_length=1, choices=STATUS_CHOITHES, default=1)

    def set_date_end(self):
        import datetime
        self.date_end = datetime.datetime.today()
        self.save()

    def __str__(self):
        return f'{self.date_start} ({self.id})'


class Work_place(models.Model):

    STATUS_CHOITHES = (
        (0, "Finished"),
        (1, "New"),
        (2, "Approved"),
        (3, "Cancelled"),
    )

    COPY = (
        (0, False),
        (1, True),
    )

    work_name = models.ForeignKey(
        Work, on_delete=models.PROTECT)
    worker = models.OneToOneField(
        Worker, models.SET_NULL, blank=True, null=True)
    status = models.PositiveSmallIntegerField(
        max_length=1, choices=STATUS_CHOITHES, default=1)
    work_time = models.ForeignKey(WorkTime,
                                  on_delete=models.SET_NULL, blank=True, null=True)
    is_copy = models.PositiveSmallIntegerField(
        default=0, max_length=1, choices=COPY)

    def save(self, *args, **kwargs):
        if self.status == 0:
            if self.is_copy == 0:
                f = Fineshed_work(
                    worker=self.worker,
                    work_name=self.work_name,
                    work_time=self.work_time
                )
                self.is_copy = 1
                self.save()
                f.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Work place {self.work_name} - {self.worker}. ({self.id})'


class Fineshed_work(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.PROTECT)
    work_name = models.ForeignKey(Work, on_delete=models.DO_NOTHING)
    work_time = models.ForeignKey(WorkTime, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'Worker {self.worker}. ({self.id})'


@receiver(post_save, sender=Work_place)
def my_callback(sender, created, instance, **kwargs):

    if created:
        obj = WorkTime()
        obj.save()

        instance.work_time = obj
        instance.save()
