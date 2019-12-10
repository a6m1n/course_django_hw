# Generated by Django 3.0 on 2019-12-09 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0009_auto_20191206_1307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workplace',
            name='work_time',
        ),
        migrations.AddField(
            model_name='worktime',
            name='work_place',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='works.WorkPlace'),
            preserve_default=False,
        ),
    ]