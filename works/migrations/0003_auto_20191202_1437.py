# Generated by Django 2.2.7 on 2019-12-02 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0002_auto_20191202_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worktime',
            name='date_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='worktime',
            name='date_start',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
