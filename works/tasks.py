from __future__ import absolute_import, unicode_literals

from django.contrib.auth.models import User
from django.core.mail import send_mail

from workers_management.celery import app
from works.models import Worker, Statistics


import requests
import datetime
import pytz


@app.task(name="works.tasks.read_api")
def read_api():

    def create_workers_from_json(json):
        password = '12345678qwe'
        all_users = User.objects.all() 

        for user in json:
            if not all_users.filter(email=user['email']):
                user_name = user['name'].split()
                user_users = User.objects.create_user(
                    username=user['username'],
                    email=user['email'],
                    password=password,
                    first_name=user_name[0],
                    last_name=user_name[1],

                )

                Worker.objects.create(
                    user=user_users
                )

    url = 'https://jsonplaceholder.typicode.com/users'
    r = requests.get(url)

    if r.status_code==200:
        return create_workers_from_json(r.json())
    
    return False

@app.task(name="works.tasks.one_user_limit_time_in_project")
def one_user_limit_time_in_project():

    def list_emails(list_obj):
        return [email[0] for email in list_obj]

    users = Worker.objects.all()

    curdate = datetime.datetime.now()-datetime.timedelta(days=7)
    curdate = pytz.UTC.localize(curdate)

    for user in users:

        try:
            times = user.workplace.worktime_set.filter(date_start__gte=curdate)
        except Worker.workplace.RelatedObjectDoesNotExist:
            continue
        res = datetime.timedelta(hours=0)
        for time in times:
            res += time.date_end-time.date_start
        limit = datetime.timedelta(hours=user.workplace.limit_hours)
        if limit < res:
            print(user)
            lists = user.workplace.work.company.manager_set.all().values_list('user__email', flat=True)
            send_mail.apply_async(args=('Limit time',
                                        f'Limit error: {user}. ',
                                        lists
                                        )
                                  )

        Statistics.objects.create(
            worker=user,
            number_weak=len(user.statistics_set.all())+1,
            work_time_in_weak=Statistics.timedelta_to_sec(res),
        )


@app.task(name="works.tasks.send_mail")
def send_mail(subject, text, list_email):
    send_mail(
        subject,
        text,
        list_email,
    )
