# Generated by Django 2.2.7 on 2019-11-25 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0005_auto_20191125_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work_place',
            name='work_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='works.Work'),
        ),
        migrations.AlterField(
            model_name='work_place',
            name='worker',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='works.Worker'),
        ),
    ]
