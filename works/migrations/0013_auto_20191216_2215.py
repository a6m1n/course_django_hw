# Generated by Django 3.0 on 2019-12-16 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0012_auto_20191216_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistics',
            name='work_time_in_weak',
            field=models.PositiveIntegerField(),
        ),
    ]
