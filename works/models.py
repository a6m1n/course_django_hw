from django.db import models


# Create your models here.

def get_name():
    return 'name'


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
        return f'Worker. Name: {self.first_name} - {self.last_name}. ({self.id})'


class Work_place(models.Model):
    work_name = models.ForeignKey(Work, on_delete=models.PROTECT)
    worker = models.OneToOneField(Worker, on_delete=models.PROTECT)

    def name(self):
        return self.work_name.description

    def __str__(self):
        return f'Work place {self.work_name} - {self.worker}. ({self.id})'
