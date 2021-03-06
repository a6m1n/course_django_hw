# Generated by Django 2.2.7 on 2019-12-06 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0005_auto_20191205_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workplace',
            name='is_copy',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='workplace',
            name='status',
            field=models.CharField(choices=[('F', 'Finished'), ('N', 'New'), ('A', 'Approved'), ('C', 'Cancelled')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='workplace',
            name='worker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='works.Worker'),
        ),
        migrations.AlterField(
            model_name='worktime',
            name='status',
            field=models.CharField(choices=[(1, 'New'), (2, 'Approved'), (3, 'Cancelled')], default='NEW', max_length=1),
        ),
    ]
